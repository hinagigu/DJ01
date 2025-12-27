#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UE 命令监控脚本 - 在 UE 编辑器中运行
使用 Windows 原生文件监听 API，零轮询开销

使用方法：
1. 在 UE 编辑器的 Output Log 中执行:
   ExecutePythonScript D:/UnrealProjects/DJ01/Tools/DataAssetManager/ue_scripts/command_monitor.py

2. 或添加到启动脚本 (Content/Python/init_unreal.py)
"""

import unreal
import os
import json
import threading
import ctypes
from ctypes import wintypes
from datetime import datetime

# 路径配置
PROJECT_ROOT = unreal.Paths.project_dir().rstrip('/')
INTERMEDIATE_DIR = os.path.join(PROJECT_ROOT, "Intermediate", "DataAssetManager")
CMD_FILE = os.path.join(INTERMEDIATE_DIR, "pending_command.json")
RESULT_FILE = os.path.join(INTERMEDIATE_DIR, "command_result.json")
HEARTBEAT_FILE = os.path.join(INTERMEDIATE_DIR, "ue_heartbeat.txt")

# 确保目录存在
os.makedirs(INTERMEDIATE_DIR, exist_ok=True)


def write_result(success: bool, message: str):
    """写入执行结果"""
    result = {
        "success": success,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    with open(RESULT_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def update_heartbeat():
    """更新心跳文件"""
    with open(HEARTBEAT_FILE, 'w') as f:
        f.write(datetime.now().isoformat())


def execute_command(cmd: dict) -> tuple:
    """执行命令"""
    cmd_type = cmd.get("type", "")
    
    if cmd_type == "execute_file":
        script_path = cmd.get("script_path", "")
        if not os.path.exists(script_path):
            return False, f"脚本文件不存在: {script_path}"
        
        try:
            with open(script_path, 'r', encoding='utf-8') as f:
                code = f.read()
            # 提供 __file__ 变量给脚本使用
            exec(code, {
                "__name__": "__main__",
                "__file__": script_path
            })
            return True, f"脚本执行成功: {os.path.basename(script_path)}"
        except Exception as e:
            import traceback
            return False, f"执行失败: {str(e)}\n{traceback.format_exc()}"
    
    elif cmd_type == "execute_code":
        code = cmd.get("code", "")
        try:
            exec(code)
            return True, "代码执行成功"
        except Exception as e:
            return False, f"执行失败: {str(e)}"
    
    else:
        return False, f"未知命令类型: {cmd_type}"


def process_pending_command():
    """处理待执行的命令文件"""
    if not os.path.exists(CMD_FILE):
        return
    
    try:
        with open(CMD_FILE, 'r', encoding='utf-8') as f:
            cmd = json.load(f)
        
        # 删除命令文件（表示已接收）
        os.remove(CMD_FILE)
        
        unreal.log(f"[DataAssetManager] 收到命令: {cmd.get('type', 'unknown')}")
        
        # 执行命令
        success, message = execute_command(cmd)
        
        # 写入结果
        write_result(success, message)
        
        if success:
            unreal.log(f"[DataAssetManager] ✅ {message}")
        else:
            unreal.log_warning(f"[DataAssetManager] ❌ {message}")
            
    except Exception as e:
        unreal.log_error(f"[DataAssetManager] 处理命令失败: {e}")
        write_result(False, str(e))


# ===== Windows 文件监听器 =====

class FileWatcher:
    """
    Windows 原生文件监听器
    使用 ReadDirectoryChangesW API，在后台线程监听文件变化
    """
    
    # Windows API 常量
    FILE_NOTIFY_CHANGE_FILE_NAME = 0x00000001
    FILE_NOTIFY_CHANGE_LAST_WRITE = 0x00000010
    FILE_LIST_DIRECTORY = 0x0001
    FILE_SHARE_READ = 0x00000001
    FILE_SHARE_WRITE = 0x00000002
    FILE_SHARE_DELETE = 0x00000004
    OPEN_EXISTING = 3
    FILE_FLAG_BACKUP_SEMANTICS = 0x02000000
    INVALID_HANDLE_VALUE = -1
    
    FILE_ACTION_ADDED = 1
    FILE_ACTION_MODIFIED = 3
    
    def __init__(self, watch_dir: str, target_filename: str, on_detected):
        """
        初始化文件监听器
        
        Args:
            watch_dir: 要监听的目录
            target_filename: 目标文件名（如 "pending_command.json"）
            on_detected: 检测到文件时的回调（设置标志）
        """
        self.watch_dir = watch_dir
        self.target_filename = target_filename
        self.on_detected = on_detected
        self._stop_event = threading.Event()
        self._thread = None
    
    def start(self):
        """启动监听线程"""
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._watch_loop, daemon=True)
        self._thread.start()
    
    def stop(self):
        """停止监听"""
        self._stop_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=2.0)
    
    def _watch_loop(self):
        """监听循环 - 在后台线程运行"""
        kernel32 = ctypes.windll.kernel32
        
        # 获取目录句柄
        handle = kernel32.CreateFileW(
            self.watch_dir,
            self.FILE_LIST_DIRECTORY,
            self.FILE_SHARE_READ | self.FILE_SHARE_WRITE | self.FILE_SHARE_DELETE,
            None,
            self.OPEN_EXISTING,
            self.FILE_FLAG_BACKUP_SEMANTICS,
            None
        )
        
        if handle == self.INVALID_HANDLE_VALUE:
            unreal.log_error(f"[FileWatcher] 无法打开目录: {self.watch_dir}")
            return
        
        try:
            buffer = ctypes.create_string_buffer(4096)
            bytes_returned = wintypes.DWORD()
            
            while not self._stop_event.is_set():
                # 等待目录变化（阻塞调用）
                result = kernel32.ReadDirectoryChangesW(
                    handle,
                    buffer,
                    len(buffer),
                    False,  # 不监听子目录
                    self.FILE_NOTIFY_CHANGE_FILE_NAME | self.FILE_NOTIFY_CHANGE_LAST_WRITE,
                    ctypes.byref(bytes_returned),
                    None,
                    None
                )
                
                if not result or bytes_returned.value == 0:
                    continue
                
                # 解析变化信息
                self._parse_notifications(buffer, bytes_returned.value)
                
        finally:
            kernel32.CloseHandle(handle)
    
    def _parse_notifications(self, buffer, size):
        """解析文件变化通知"""
        offset = 0
        while offset < size:
            # FILE_NOTIFY_INFORMATION 结构
            next_offset = ctypes.cast(
                ctypes.byref(buffer, offset),
                ctypes.POINTER(wintypes.DWORD)
            ).contents.value
            
            action = ctypes.cast(
                ctypes.byref(buffer, offset + 4),
                ctypes.POINTER(wintypes.DWORD)
            ).contents.value
            
            name_length = ctypes.cast(
                ctypes.byref(buffer, offset + 8),
                ctypes.POINTER(wintypes.DWORD)
            ).contents.value
            
            # 获取文件名 (Unicode, name_length 是字节数)
            if name_length > 0:
                filename = ctypes.wstring_at(
                    ctypes.addressof(buffer) + offset + 12,
                    name_length // 2
                )
                
                # 检查是否是目标文件
                if action in (self.FILE_ACTION_ADDED, self.FILE_ACTION_MODIFIED):
                    if self.target_filename in filename:
                        self.on_detected()
            
            if next_offset == 0:
                break
            offset += next_offset


# ===== 命令监控器 =====

class CommandMonitor:
    """
    命令监控器 - 事件驱动模式
    
    架构说明：
    - FileWatcher 在后台线程监听文件变化
    - 检测到 pending_command.json 后设置 _command_pending 标志
    - 主线程的 tick() 检查标志并执行命令
    
    为什么需要标志？
    - UE 的资产操作必须在主线程执行
    - 后台线程不能直接调用 unreal.* API
    - 标志是线程间通信的安全方式
    """
    
    def __init__(self):
        # 命令待处理标志（线程安全）
        self._command_pending = False
        self._lock = threading.Lock()
        
        # 心跳计时
        self._heartbeat_counter = 0.0
        
        # 运行状态
        self.running = True
        
        # 启动文件监听器
        self._watcher = FileWatcher(
            watch_dir=INTERMEDIATE_DIR,
            target_filename="pending_command.json",
            on_detected=self._on_command_detected
        )
        self._watcher.start()
    
    def _on_command_detected(self):
        """文件监听回调 - 在后台线程中调用"""
        with self._lock:
            self._command_pending = True
    
    def tick(self, delta_time):
        """
        主线程 Tick - 开销极低
        
        每帧只做两件事：
        1. 累加心跳计时器（简单加法）
        2. 检查布尔标志（几乎零开销）
        """
        if not self.running:
            return
        
        # 心跳更新（每秒一次）
        self._heartbeat_counter += delta_time
        if self._heartbeat_counter >= 1.0:
            self._heartbeat_counter = 0.0
            update_heartbeat()
        
        # 检查是否有待处理命令
        should_process = False
        with self._lock:
            if self._command_pending:
                should_process = True
                self._command_pending = False
        
        # 在主线程处理命令
        if should_process:
            process_pending_command()
    
    def stop(self):
        """停止监控"""
        self.running = False
        self._watcher.stop()
        unreal.log("[DataAssetManager] 命令监控已停止")


# ===== 全局实例管理 =====

_monitor = None
_tick_handle = None


def start_monitor():
    """启动命令监控"""
    global _monitor, _tick_handle
    
    if _monitor is not None:
        unreal.log_warning("[DataAssetManager] 监控已在运行")
        return
    
    _monitor = CommandMonitor()
    _tick_handle = unreal.register_slate_post_tick_callback(_monitor.tick)
    
    # 初始心跳
    update_heartbeat()
    
    unreal.log("=" * 50)
    unreal.log("[DataAssetManager] 命令监控已启动")
    unreal.log("  模式: 文件系统事件监听（零轮询）")
    unreal.log(f"  监听目录: {INTERMEDIATE_DIR}")
    unreal.log(f"  目标文件: pending_command.json")
    unreal.log("=" * 50)


def stop_monitor():
    """停止命令监控"""
    global _monitor, _tick_handle
    
    if _tick_handle:
        unreal.unregister_slate_post_tick_callback(_tick_handle)
        _tick_handle = None
    
    if _monitor:
        _monitor.stop()
        _monitor = None


# 自动启动
if __name__ == "__main__" or True:
    start_monitor()
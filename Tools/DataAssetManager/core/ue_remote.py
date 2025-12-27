#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UE 远程执行模块 - 通过文件监控方式与 UE 通信
"""

import os
import json
import time
from typing import Tuple
from datetime import datetime


class UERemoteExecutor:
    """UE 远程执行器 - 基于文件监控"""
    
    def __init__(self, project_root: str = None):
        if project_root is None:
            # 默认项目根目录
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        
        self.project_root = project_root
        
        # 命令文件路径（工具写入）
        self.cmd_file = os.path.join(project_root, "Intermediate", "DataAssetManager", "pending_command.json")
        # 结果文件路径（UE 写入）
        self.result_file = os.path.join(project_root, "Intermediate", "DataAssetManager", "command_result.json")
        # 状态文件（UE 心跳）
        self.heartbeat_file = os.path.join(project_root, "Intermediate", "DataAssetManager", "ue_heartbeat.txt")
        
        # 确保目录存在
        os.makedirs(os.path.dirname(self.cmd_file), exist_ok=True)
    
    def is_ue_running(self) -> bool:
        """检查 UE 是否在运行（通过心跳文件）"""
        if not os.path.exists(self.heartbeat_file):
            return False
        
        try:
            # 检查心跳文件是否在 10 秒内更新
            mtime = os.path.getmtime(self.heartbeat_file)
            age = time.time() - mtime
            return age < 10
        except:
            return False
    
    def connect(self) -> bool:
        """检查连接（文件监控模式下总是成功）"""
        return True
    
    def disconnect(self):
        """断开连接（文件监控模式下无需操作）"""
        pass
    
    def execute_file(self, script_path: str, timeout: float = 30.0) -> Tuple[bool, str]:
        """请求 UE 执行脚本文件"""
        command = {
            "type": "execute_file",
            "script_path": script_path,
            "timestamp": datetime.now().isoformat(),
        }
        return self._send_command(command, timeout)
    
    def execute_code(self, code: str, timeout: float = 10.0) -> Tuple[bool, str]:
        """请求 UE 执行代码"""
        command = {
            "type": "execute_code",
            "code": code,
            "timestamp": datetime.now().isoformat(),
        }
        return self._send_command(command, timeout)
    
    def _send_command(self, command: dict, timeout: float) -> Tuple[bool, str]:
        """发送命令并等待结果"""
        # 清除旧的结果文件
        if os.path.exists(self.result_file):
            os.remove(self.result_file)
        
        # 写入命令文件
        try:
            with open(self.cmd_file, 'w', encoding='utf-8') as f:
                json.dump(command, f, indent=2, ensure_ascii=False)
        except Exception as e:
            return False, f"写入命令文件失败: {e}"
        
        # 等待结果
        start_time = time.time()
        while time.time() - start_time < timeout:
            if os.path.exists(self.result_file):
                try:
                    with open(self.result_file, 'r', encoding='utf-8') as f:
                        result = json.load(f)
                    
                    # 删除结果文件
                    os.remove(self.result_file)
                    
                    success = result.get("success", False)
                    message = result.get("message", "")
                    return success, message
                    
                except Exception as e:
                    return False, f"读取结果失败: {e}"
            
            time.sleep(0.2)
        
        return False, "执行超时，UE 可能未运行监控脚本"
    
    def get_setup_info(self) -> str:
        """获取设置说明"""
        monitor_script = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 
            "ue_scripts", "command_monitor.py"
        )
        
        return f"""文件监控模式设置说明：

1. 在 UE 编辑器中运行监控脚本:
   py "{monitor_script}"

2. 或添加到项目启动脚本自动运行

监控脚本会：
- 每秒检查命令文件
- 执行命令并写入结果
- 发送心跳表示 UE 在线

命令文件: {self.cmd_file}
结果文件: {self.result_file}
心跳文件: {self.heartbeat_file}
"""
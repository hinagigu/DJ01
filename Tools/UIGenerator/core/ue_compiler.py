"""
Unreal Engine 编译器集成
"""
import os
import json
import subprocess
import threading
from typing import Optional, Dict, Callable, List

try:
    import winreg
except ImportError:
    winreg = None

from utils.paths import paths


class UECompiler:
    """UE 项目编译器"""
    
    def __init__(self):
        self.engine_dir: Optional[str] = None
        self.build_bat: Optional[str] = None
        self.is_compiling = False
        
        # 回调
        self.on_output: Optional[Callable[[str], None]] = None
        self.on_success: Optional[Callable[[], None]] = None
        self.on_failed: Optional[Callable[[List[str]], None]] = None
        self.on_error: Optional[Callable[[str], None]] = None
    
    def detect_engine_paths(self) -> Dict[str, Optional[str]]:
        """检测 UE 引擎路径"""
        result = {
            'engine_dir': None,
            'build_bat': None,
            'uat_bat': None
        }
        
        # 方法1: 从 uproject 的 EngineAssociation 查找
        engine_id = paths.get_engine_association()
        
        if engine_id and winreg:
            if engine_id.startswith('{'):
                # GUID 格式 - 源码版本
                result['engine_dir'] = self._find_engine_by_guid(engine_id)
            else:
                # 版本号格式 - 安装版本
                result['engine_dir'] = self._find_engine_by_version(engine_id)
        
        # 方法2: 常见路径扫描
        if not result['engine_dir']:
            result['engine_dir'] = self._scan_common_paths()
        
        # 查找编译脚本
        if result['engine_dir']:
            build_bat = os.path.join(
                result['engine_dir'], "Engine", "Build", "BatchFiles", "Build.bat"
            )
            uat_bat = os.path.join(
                result['engine_dir'], "Engine", "Build", "BatchFiles", "RunUAT.bat"
            )
            
            if os.path.exists(build_bat):
                result['build_bat'] = build_bat
            if os.path.exists(uat_bat):
                result['uat_bat'] = uat_bat
        
        self.engine_dir = result['engine_dir']
        self.build_bat = result['build_bat']
        
        return result
    
    def _find_engine_by_guid(self, guid: str) -> Optional[str]:
        """通过 GUID 从注册表查找引擎路径"""
        if not winreg:
            return None
        
        try:
            key_path = r"SOFTWARE\Epic Games\Unreal Engine\Builds"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                engine_path, _ = winreg.QueryValueEx(key, guid)
                if os.path.exists(engine_path):
                    return engine_path
        except WindowsError:
            pass
        
        return None
    
    def _find_engine_by_version(self, version: str) -> Optional[str]:
        """通过版本号从注册表查找引擎路径"""
        if not winreg:
            return None
        
        try:
            key_path = rf"SOFTWARE\EpicGames\Unreal Engine\{version}"
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
                install_dir, _ = winreg.QueryValueEx(key, "InstalledDirectory")
                if os.path.exists(install_dir):
                    return install_dir
        except WindowsError:
            pass
        
        return None
    
    def _scan_common_paths(self) -> Optional[str]:
        """扫描常见安装路径"""
        common_paths = [
            r"C:\Program Files\Epic Games\UE_5.5",
            r"C:\Program Files\Epic Games\UE_5.4",
            r"C:\Program Files\Epic Games\UE_5.3",
            r"D:\Epic Games\UE_5.5",
            r"D:\Epic Games\UE_5.4",
            r"D:\Epic Games\UE_5.3",
            r"E:\UnrealEngine",
            r"D:\UnrealEngine",
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                return path
        
        return None
    
    def set_engine_dir(self, engine_dir: str):
        """手动设置引擎目录"""
        self.engine_dir = engine_dir
        self.build_bat = os.path.join(
            engine_dir, "Engine", "Build", "BatchFiles", "Build.bat"
        )
    
    def can_compile(self) -> bool:
        """检查是否可以编译"""
        return self.build_bat is not None and os.path.exists(self.build_bat)
    
    def compile_async(self, target: str = "DJ01Editor", 
                      platform: str = "Win64",
                      configuration: str = "Development"):
        """异步编译项目"""
        if self.is_compiling:
            return False
        
        if not self.can_compile():
            if self.on_error:
                self.on_error("未找到编译工具")
            return False
        
        self.is_compiling = True
        
        # 构建命令
        cmd = [
            self.build_bat,
            target,
            platform,
            configuration,
            f"-Project={paths.uproject_file}",
            "-WaitMutex",
            "-FromMsBuild"
        ]
        
        def run():
            try:
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    cwd=paths.project_root,
                    creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
                )
                
                output_lines = []
                for line in process.stdout:
                    line = line.strip()
                    if line:
                        output_lines.append(line)
                        if self.on_output:
                            # 过滤关键信息
                            keywords = ['error', 'warning', 'success', 'complete', 'failed', 'building']
                            if any(kw in line.lower() for kw in keywords):
                                self.on_output(line)
                
                process.wait()
                self.is_compiling = False
                
                if process.returncode == 0:
                    if self.on_success:
                        self.on_success()
                else:
                    if self.on_failed:
                        self.on_failed(output_lines)
                        
            except Exception as e:
                self.is_compiling = False
                if self.on_error:
                    self.on_error(str(e))
        
        thread = threading.Thread(target=run, daemon=True)
        thread.start()
        return True
    
    def get_compile_command(self) -> List[str]:
        """获取编译命令（用于显示）"""
        if not self.build_bat:
            return []
        
        return [
            self.build_bat,
            "DJ01Editor",
            "Win64", 
            "Development",
            f"-Project={paths.uproject_file}"
        ]


class UECommandSender:
    """向 UE 发送 Python 命令"""
    
    @staticmethod
    def send(code: str) -> bool:
        """发送命令到 UE"""
        cmd_dir = os.path.dirname(paths.command_file)
        os.makedirs(cmd_dir, exist_ok=True)
        
        cmd = {
            "type": "execute_code",
            "code": code
        }
        
        try:
            with open(paths.command_file, 'w', encoding='utf-8') as f:
                json.dump(cmd, f, indent=2)
            return True
        except:
            return False
    
    @staticmethod
    def send_blueprint_generation(schemas_dir: str) -> bool:
        """发送蓝图生成命令"""
        code = f"""
import sys
sys.path.insert(0, r'{paths.ue_scripts_dir}')
from generate_widget_bp import generate_all_from_directory
result = generate_all_from_directory(r'{schemas_dir}')
print(f"生成结果: 成功 {{len(result['success'])}}, 失败 {{len(result['failed'])}}")
"""
        return UECommandSender.send(code)
"""
路径配置管理
"""
import os
import json
from typing import Optional, Dict


class Paths:
    """集中管理所有路径配置"""
    
    _instance: Optional['Paths'] = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        
        # 工具根目录
        self.tool_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # 项目根目录 (DJ01)
        self.project_root = os.path.dirname(os.path.dirname(self.tool_root))
        
        # 配置文件
        self.widget_types_config = os.path.join(self.tool_root, "configs", "widget_types.json")
        self.bindingset_config = os.path.join(
            self.project_root, 
            "Source", "DJ01", "AbilitySystem", "Config", 
            "BindingSetDefinitions.json"
        )
        
        # Schema 目录
        self.schemas_dir = os.path.join(self.tool_root, "schemas", "widgets")
        self.examples_dir = os.path.join(self.tool_root, "schemas", "examples")
        self.schema_definition = os.path.join(self.tool_root, "schemas", "ui_schema_v1.json")
        
        # UE 脚本目录
        self.ue_scripts_dir = os.path.join(self.tool_root, "ue_scripts")
        
        # 中间文件目录
        self.intermediate_dir = os.path.join(self.project_root, "Intermediate", "UIGenerator")
        self.state_file = os.path.join(self.intermediate_dir, "state.json")
        self.command_file = os.path.join(
            self.project_root, "Intermediate", "DataAssetManager", "pending_command.json"
        )
        
        # uproject 文件
        self.uproject_file = os.path.join(self.project_root, "DJ01.uproject")
        
        # 确保必要目录存在
        self._ensure_directories()
    
    def _ensure_directories(self):
        """确保必要的目录存在"""
        dirs = [
            os.path.join(self.tool_root, "configs"),
            self.schemas_dir,
            self.examples_dir,
            self.intermediate_dir,
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
    
    def get_output_dir(self, schema: dict) -> str:
        """获取 Schema 的输出目录（绝对路径）"""
        relative_path = schema.get('output_path', 'Source/DJ01/UI/Generated')
        return os.path.join(self.project_root, relative_path)
    
    def get_engine_association(self) -> Optional[str]:
        """从 uproject 获取引擎关联"""
        if not os.path.exists(self.uproject_file):
            return None
        
        try:
            with open(self.uproject_file, 'r') as f:
                data = json.load(f)
            return data.get('EngineAssociation')
        except:
            return None


# 全局单例
paths = Paths()
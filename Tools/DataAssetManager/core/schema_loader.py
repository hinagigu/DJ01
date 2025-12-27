#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - Schema 加载器
职责：从 JSON 文件或目录加载 Schema 定义（支持多文件）
"""

import json
import os
from typing import Dict, List, Optional

from .schema import PropertyDef, StructDef, DataAssetDef


class SchemaLoader:
    """Schema 加载器（单例，支持多文件）"""
    
    _instance: Optional['SchemaLoader'] = None
    _schema: Optional[dict] = None
    
    def __new__(cls, schema_path: str = None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, schema_path: str = None):
        if self._initialized:
            return
        
        self._schema_path = schema_path
        self._data_assets: Dict[str, DataAssetDef] = {}
        self._structs: Dict[str, StructDef] = {}
        self._game_feature_actions: Dict[str, dict] = {}
        
        if schema_path:
            self.load(schema_path)
        
        self._initialized = True
    
    def load(self, schema_path: str) -> bool:
        """加载 Schema（支持文件或目录）"""
        if os.path.isdir(schema_path):
            return self._load_from_directory(schema_path)
        elif os.path.exists(schema_path):
            return self._load_from_file(schema_path)
        else:
            print(f"警告: Schema 路径不存在: {schema_path}")
            return False
    
    def _load_from_directory(self, dir_path: str) -> bool:
        """从目录加载多个 Schema 文件"""
        SchemaLoader._schema = {}
        
        try:
            # 先加载 _common.json（如果存在）
            common_file = os.path.join(dir_path, "_common.json")
            if os.path.exists(common_file):
                self._load_and_merge(common_file)
            
            # 加载其他 json 文件（按字母顺序）
            for filename in sorted(os.listdir(dir_path)):
                if filename.endswith('.json') and not filename.startswith('_'):
                    file_path = os.path.join(dir_path, filename)
                    self._load_and_merge(file_path)
            
            self._parse_schema()
            return True
        except Exception as e:
            print(f"加载 Schema 目录失败: {e}")
            return False
    
    def _load_and_merge(self, file_path: str):
        """加载并合并单个文件到 _schema"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 合并 structs
            if "structs" in data:
                if "structs" not in SchemaLoader._schema:
                    SchemaLoader._schema["structs"] = {}
                SchemaLoader._schema["structs"].update(data["structs"])
            
            # 合并 data_assets
            if "data_assets" in data:
                if "data_assets" not in SchemaLoader._schema:
                    SchemaLoader._schema["data_assets"] = {}
                SchemaLoader._schema["data_assets"].update(data["data_assets"])
            
            # 合并 gamefeature_actions
            if "gamefeature_actions" in data:
                if "gamefeature_actions" not in SchemaLoader._schema:
                    SchemaLoader._schema["gamefeature_actions"] = {}
                SchemaLoader._schema["gamefeature_actions"].update(data["gamefeature_actions"])
            
            # 合并 widget_types
            if "widget_types" in data:
                if "widget_types" not in SchemaLoader._schema:
                    SchemaLoader._schema["widget_types"] = {}
                SchemaLoader._schema["widget_types"].update(data["widget_types"])
            
            # 处理顶层的 DataAsset 定义（非嵌套格式）
            for key, value in data.items():
                if key.startswith('_') or key in ('structs', 'data_assets', 
                        'gamefeature_actions', 'widget_types', 'common_types'):
                    continue
                if isinstance(value, dict) and 'class_name' in value:
                    if "data_assets" not in SchemaLoader._schema:
                        SchemaLoader._schema["data_assets"] = {}
                    SchemaLoader._schema["data_assets"][key] = value
                    
        except Exception as e:
            print(f"加载文件 {file_path} 失败: {e}")
    
    def _load_from_file(self, file_path: str) -> bool:
        """从单个文件加载"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                SchemaLoader._schema = json.load(f)
            self._parse_schema()
            return True
        except Exception as e:
            print(f"加载 Schema 失败: {e}")
            return False
    
    def _parse_schema(self):
        """解析 Schema"""
        if not self._schema:
            return
        
        # 解析结构体定义
        for name, data in self._schema.get("structs", {}).items():
            self._structs[name] = StructDef.from_dict(name, data)
        
        # 解析 DataAsset 定义
        for name, data in self._schema.get("data_assets", {}).items():
            self._data_assets[name] = DataAssetDef.from_dict(name, data)
        
        # 解析 GameFeatureAction 定义
        self._game_feature_actions = self._schema.get("gamefeature_actions", {})
    
    @property
    def schema(self) -> dict:
        """获取原始 Schema"""
        return SchemaLoader._schema or {}
    
    def get_data_asset_def(self, asset_type: str) -> Optional[DataAssetDef]:
        """获取 DataAsset 定义"""
        return self._data_assets.get(asset_type)
    
    def get_struct_def(self, struct_name: str) -> Optional[StructDef]:
        """获取结构体定义"""
        return self._structs.get(struct_name)
    
    def get_all_asset_types(self) -> List[str]:
        """获取所有 DataAsset 类型"""
        return list(self._data_assets.keys())
    
    def get_all_struct_types(self) -> List[str]:
        """获取所有结构体类型"""
        return list(self._structs.keys())
    
    def get_game_feature_actions(self) -> Dict[str, dict]:
        """获取所有 GameFeatureAction 定义"""
        return self._game_feature_actions
    
    def get_gamefeature_actions(self) -> Dict[str, dict]:
        """获取所有 GameFeatureAction 定义（别名）"""
        return self._game_feature_actions
    
    def get_widget_types(self) -> Dict[str, str]:
        """获取所有控件类型"""
        return self.schema.get("widget_types", {})
    
    @classmethod
    def reset(cls):
        """重置单例（用于测试）"""
        cls._instance = None
        cls._schema = None
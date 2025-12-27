#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - Schema 加载器
从 asset_schema.json 加载配置，驱动编辑器 UI 生成
"""

import json
import os
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class PropertyDef:
    """属性定义"""
    name: str
    type: str
    display_name: str
    description: str = ""
    widget: str = "text_input"
    category: str = "Default"
    required: bool = False
    default: Any = None
    
    # 特定控件的参数
    item_type: str = ""           # 数组项类型
    struct_type: str = ""         # 结构体类型
    asset_class: str = ""         # 资产类型
    base_class: str = ""          # 基类
    content_path: str = ""        # 内容路径
    categories: str = ""          # Tag 类别
    min_value: float = None
    max_value: float = None
    
    @classmethod
    def from_dict(cls, name: str, data: dict) -> 'PropertyDef':
        return cls(
            name=name,
            type=data.get("type", "string"),
            display_name=data.get("display_name", name),
            description=data.get("description", ""),
            widget=data.get("widget", "text_input"),
            category=data.get("category", "Default"),
            required=data.get("required", False),
            default=data.get("default"),
            item_type=data.get("item_type", ""),
            struct_type=data.get("struct_type", ""),
            asset_class=data.get("asset_class", ""),
            base_class=data.get("base_class", ""),
            content_path=data.get("content_path", ""),
            categories=data.get("categories", ""),
            min_value=data.get("min"),
            max_value=data.get("max"),
        )


@dataclass
class StructDef:
    """结构体定义"""
    name: str
    description: str
    properties: Dict[str, PropertyDef] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, name: str, data: dict) -> 'StructDef':
        props = {}
        for prop_name, prop_data in data.get("properties", {}).items():
            props[prop_name] = PropertyDef.from_dict(prop_name, prop_data)
        return cls(
            name=name,
            description=data.get("description", ""),
            properties=props
        )


@dataclass
class DataAssetDef:
    """DataAsset 定义"""
    name: str
    class_name: str
    parent_class: str
    asset_type: str  # "Blueprint" 或 "DataAsset"
    display_name: str
    description: str
    content_path: str
    icon: str
    properties: Dict[str, PropertyDef] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, name: str, data: dict) -> 'DataAssetDef':
        props = {}
        for prop_name, prop_data in data.get("properties", {}).items():
            props[prop_name] = PropertyDef.from_dict(prop_name, prop_data)
        return cls(
            name=name,
            class_name=data.get("class_name", ""),
            parent_class=data.get("parent_class", ""),
            asset_type=data.get("asset_type", "DataAsset"),
            display_name=data.get("display_name", name),
            description=data.get("description", ""),
            content_path=data.get("content_path", ""),
            icon=data.get("icon", "📄"),
            properties=props
        )
    
    def get_properties_by_category(self) -> Dict[str, List[PropertyDef]]:
        """按类别分组属性"""
        categories = {}
        for prop in self.properties.values():
            cat = prop.category
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(prop)
        return categories


class SchemaLoader:
    """Schema 加载器"""
    
    _instance = None
    _schema = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if SchemaLoader._schema is None:
            self._load_schema()
    
    def _load_schema(self):
        """加载 schema 文件"""
        schema_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "configs",
            "asset_schema.json"
        )
        
        if os.path.exists(schema_path):
            with open(schema_path, 'r', encoding='utf-8') as f:
                SchemaLoader._schema = json.load(f)
        else:
            SchemaLoader._schema = {}
            print(f"警告: Schema 文件不存在: {schema_path}")
    
    @property
    def schema(self) -> dict:
        return SchemaLoader._schema or {}
    
    def get_data_asset_def(self, asset_type: str) -> Optional[DataAssetDef]:
        """获取 DataAsset 定义"""
        data_assets = self.schema.get("data_assets", {})
        if asset_type in data_assets:
            return DataAssetDef.from_dict(asset_type, data_assets[asset_type])
        return None
    
    def get_struct_def(self, struct_name: str) -> Optional[StructDef]:
        """获取结构体定义"""
        structs = self.schema.get("structs", {})
        if struct_name in structs:
            return StructDef.from_dict(struct_name, structs[struct_name])
        return None
    
    def get_all_asset_types(self) -> List[str]:
        """获取所有 DataAsset 类型"""
        return list(self.schema.get("data_assets", {}).keys())
    
    def get_game_feature_actions(self) -> Dict[str, dict]:
        """获取所有 GameFeatureAction 定义"""
        return self.schema.get("game_feature_actions", {})
    
    def get_widget_types(self) -> Dict[str, str]:
        """获取所有控件类型"""
        return self.schema.get("widget_types", {})
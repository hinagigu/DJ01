#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - Schema 数据类定义
职责：定义 Schema 相关的数据结构
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional


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
    item_type: str = ""
    struct_type: str = ""
    asset_class: str = ""
    base_class: str = ""
    content_path: str = ""
    categories: str = ""
    min_value: float = None
    max_value: float = None
    
    # 选项相关
    options_source: str = ""  # 选项数据源（game_features, pawn_data 等）
    allow_empty: bool = True  # 是否允许空值
    
    # 多态类型相关（用于 instanced_array_editor）
    available_types: List[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, name: str, data: dict) -> 'PropertyDef':
        """从字典创建"""
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
            options_source=data.get("options_source", ""),
            allow_empty=data.get("allow_empty", True),
            available_types=data.get("available_types", []),
        )
    
    def to_dict(self) -> dict:
        """转换为字典"""
        return {
            "type": self.type,
            "display_name": self.display_name,
            "description": self.description,
            "widget": self.widget,
            "category": self.category,
            "required": self.required,
            "default": self.default,
        }


@dataclass
class StructDef:
    """结构体定义"""
    name: str
    description: str
    properties: Dict[str, PropertyDef] = field(default_factory=dict)
    
    @classmethod
    def from_dict(cls, name: str, data: dict) -> 'StructDef':
        """从字典创建"""
        props = {}
        for prop_name, prop_data in data.get("properties", {}).items():
            props[prop_name] = PropertyDef.from_dict(prop_name, prop_data)
        return cls(
            name=name,
            description=data.get("description", ""),
            properties=props
        )
    
    def get_property_names(self) -> List[str]:
        """获取属性名列表"""
        return list(self.properties.keys())


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
        """从字典创建"""
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
        categories: Dict[str, List[PropertyDef]] = {}
        for prop in self.properties.values():
            cat = prop.category
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(prop)
        return categories
    
    def get_required_properties(self) -> List[PropertyDef]:
        """获取必填属性"""
        return [p for p in self.properties.values() if p.required]
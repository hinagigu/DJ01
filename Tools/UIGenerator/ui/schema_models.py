#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - Schema 数据模型
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class ComponentData:
    """UI 组件数据"""
    name: str = "NewComponent"
    type: str = "TextBlock"
    comment: str = ""
    optional: bool = False
    bind_percent: str = ""
    bind_text: str = ""
    bind_image: str = ""
    width_override: Optional[float] = None
    height_override: Optional[float] = None
    children: List['ComponentData'] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        result = {"name": self.name, "type": self.type}
        if self.comment:
            result["comment"] = self.comment
        if self.optional:
            result["optional"] = True
        if self.bind_percent:
            result["bind_percent"] = self.bind_percent
        if self.bind_text:
            result["bind_text"] = self.bind_text
        if self.bind_image:
            result["bind_image"] = self.bind_image
        if self.width_override is not None:
            result["width_override"] = self.width_override
        if self.height_override is not None:
            result["height_override"] = self.height_override
        if self.children:
            result["children"] = [c.to_dict() for c in self.children]
        return result
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ComponentData':
        children = [cls.from_dict(c) for c in data.get('children', [])]
        return cls(
            name=data.get('name', 'Component'),
            type=data.get('type', 'TextBlock'),
            comment=data.get('comment', ''),
            optional=data.get('optional', False),
            bind_percent=data.get('bind_percent', ''),
            bind_text=data.get('bind_text', ''),
            bind_image=data.get('bind_image', ''),
            width_override=data.get('width_override'),
            height_override=data.get('height_override'),
            children=children
        )


@dataclass
class PropertyData:
    """自定义属性数据"""
    name: str = "NewProperty"
    type: str = "float"
    category: str = ""
    default: Any = None
    description: str = ""
    blueprint_read_only: bool = False
    
    def to_dict(self) -> dict:
        result = {"name": self.name, "type": self.type}
        if self.category:
            result["category"] = self.category
        if self.default is not None:
            result["default"] = self.default
        if self.description:
            result["description"] = self.description
        if self.blueprint_read_only:
            result["blueprint_read_only"] = True
        return result
    
    @classmethod
    def from_dict(cls, data: dict) -> 'PropertyData':
        return cls(
            name=data.get('name', 'Property'),
            type=data.get('type', 'float'),
            category=data.get('category', ''),
            default=data.get('default'),
            description=data.get('description', ''),
            blueprint_read_only=data.get('blueprint_read_only', False)
        )


@dataclass 
class WidgetSchema:
    """Widget Schema 数据"""
    name: str = "MyWidget"
    description: str = ""
    parent_class: str = "CommonUserWidget"
    output_path: str = "Source/DJ01/UI/Generated"
    blueprint_path: str = "/Game/UI/Generated"
    layer: str = ""
    input_config: Dict = field(default_factory=dict)
    activation: Dict = field(default_factory=dict)
    components: List[ComponentData] = field(default_factory=list)
    properties: List[PropertyData] = field(default_factory=list)
    binding_set: Dict = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        result = {
            "$schema": "../ui_schema_v1.json",
            "name": self.name,
            "description": self.description,
            "parent_class": self.parent_class,
            "output_path": self.output_path,
            "blueprint_path": self.blueprint_path,
            "components": [c.to_dict() for c in self.components]
        }
        if self.layer:
            result["layer"] = self.layer
        if self.input_config:
            result["input_config"] = self.input_config
        if self.activation:
            result["activation"] = self.activation
        if self.properties:
            result["properties"] = [p.to_dict() for p in self.properties]
        if self.binding_set:
            result["binding_set"] = self.binding_set
        return result
    
    @classmethod
    def from_dict(cls, data: dict) -> 'WidgetSchema':
        components = [ComponentData.from_dict(c) for c in data.get('components', [])]
        properties = [PropertyData.from_dict(p) for p in data.get('properties', [])]
        return cls(
            name=data.get('name', 'MyWidget'),
            description=data.get('description', ''),
            parent_class=data.get('parent_class', 'CommonUserWidget'),
            output_path=data.get('output_path', 'Source/DJ01/UI/Generated'),
            blueprint_path=data.get('blueprint_path', '/Game/UI/Generated'),
            layer=data.get('layer', ''),
            input_config=data.get('input_config', {}),
            activation=data.get('activation', {}),
            components=components,
            properties=properties,
            binding_set=data.get('binding_set', {})
        )
    
    @classmethod
    def create_template(cls) -> 'WidgetSchema':
        """创建默认模板"""
        return cls(
            name="MyWidget",
            description="",
            parent_class="CommonUserWidget",
            components=[ComponentData(name="RootCanvas", type="CanvasPanel", children=[])]
        )
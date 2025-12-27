#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 验证引擎
职责：验证资产配置的有效性
"""

from typing import List, Dict, Any
from dataclasses import dataclass

from .schema import DataAssetDef, PropertyDef
from .registry import AssetRegistry


@dataclass
class ValidationResult:
    """验证结果"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    
    def __bool__(self):
        return self.is_valid
    
    @classmethod
    def success(cls) -> 'ValidationResult':
        return cls(True, [], [])
    
    @classmethod
    def failure(cls, errors: List[str]) -> 'ValidationResult':
        return cls(False, errors, [])


class ValidationEngine:
    """验证引擎"""
    
    @staticmethod
    def validate_name(name: str, existing_names: List[str] = None) -> ValidationResult:
        """验证资产名称"""
        errors = []
        warnings = []
        
        if not name:
            errors.append("名称不能为空")
        elif not name[0].isalpha():
            errors.append("名称必须以字母开头")
        elif not name.replace('_', '').isalnum():
            errors.append("名称只能包含字母、数字和下划线")
        
        if existing_names and name in existing_names:
            errors.append(f"名称 '{name}' 已存在")
        
        if name and name[0].islower():
            warnings.append("建议使用大驼峰命名")
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    @staticmethod
    def validate_asset(asset_def: DataAssetDef, data: Dict[str, Any], 
                       registry: AssetRegistry = None) -> ValidationResult:
        """验证资产数据"""
        errors = []
        warnings = []
        
        # 检查必填属性
        for prop in asset_def.get_required_properties():
            value = data.get(prop.name)
            if not value:
                errors.append(f"必填属性 '{prop.display_name}' 未填写")
        
        # 检查资产引用
        if registry:
            for prop_name, prop in asset_def.properties.items():
                if prop.widget in ["asset_picker", "asset_picker_list"]:
                    value = data.get(prop_name)
                    if value:
                        # 验证引用的资产是否存在
                        pass  # TODO: 实现引用验证
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    @staticmethod
    def validate_registry(registry: AssetRegistry) -> List[str]:
        """验证注册表的依赖关系"""
        errors = []
        for key, asset in registry.assets.items():
            for dep_key in asset.dependencies:
                if dep_key not in registry.assets:
                    errors.append(f"{key} 依赖的 {dep_key} 不存在")
        return errors
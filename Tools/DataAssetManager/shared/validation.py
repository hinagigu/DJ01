#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 验证引擎
"""

from typing import List, Dict, Any, Tuple
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """验证结果"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    
    def __bool__(self):
        return self.is_valid


class ValidationEngine:
    """验证引擎 - 用于验证 DataAsset 配置"""
    
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
            warnings.append("建议使用大驼峰命名 (PascalCase)")
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    @staticmethod
    def validate_experience(config: Dict[str, Any], registry) -> ValidationResult:
        """验证 Experience 配置"""
        errors = []
        warnings = []
        
        # 检查必需字段
        if not config.get("name"):
            errors.append("Experience 必须有名称")
        
        # 检查 PawnData 引用
        pawn_data = config.get("default_pawn_data")
        if pawn_data:
            if not registry.get("PawnData", pawn_data):
                warnings.append(f"PawnData '{pawn_data}' 未在注册表中找到")
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    @staticmethod
    def validate_pawn_data(config: Dict[str, Any], registry) -> ValidationResult:
        """验证 PawnData 配置"""
        errors = []
        warnings = []
        
        if not config.get("name"):
            errors.append("PawnData 必须有名称")
        
        if not config.get("pawn_class"):
            warnings.append("未指定 PawnClass，将使用默认值")
        
        # 检查 AbilitySet 引用
        ability_sets = config.get("ability_sets", [])
        for ability_set in ability_sets:
            if not registry.get("AbilitySet", ability_set):
                warnings.append(f"AbilitySet '{ability_set}' 未在注册表中找到")
        
        # 检查 InputConfig 引用
        input_config = config.get("input_config")
        if input_config and not registry.get("InputConfig", input_config):
            warnings.append(f"InputConfig '{input_config}' 未在注册表中找到")
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    @staticmethod
    def validate_input_config(config: Dict[str, Any], registry) -> ValidationResult:
        """验证 InputConfig 配置"""
        errors = []
        warnings = []
        
        if not config.get("name"):
            errors.append("InputConfig 必须有名称")
        
        # 检查输入动作
        native_actions = config.get("native_input_actions", [])
        ability_actions = config.get("ability_input_actions", [])
        
        if not native_actions and not ability_actions:
            warnings.append("InputConfig 没有配置任何输入动作")
        
        # 检查重复的输入标签
        all_tags = []
        for action in native_actions + ability_actions:
            tag = action.get("input_tag")
            if tag in all_tags:
                errors.append(f"输入标签 '{tag}' 重复")
            all_tags.append(tag)
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    @staticmethod
    def validate_ability_set(config: Dict[str, Any], registry) -> ValidationResult:
        """验证 AbilitySet 配置"""
        errors = []
        warnings = []
        
        if not config.get("name"):
            errors.append("AbilitySet 必须有名称")
        
        abilities = config.get("abilities", [])
        effects = config.get("effects", [])
        attributes = config.get("attributes", [])
        
        if not abilities and not effects and not attributes:
            warnings.append("AbilitySet 没有配置任何内容")
        
        return ValidationResult(len(errors) == 0, errors, warnings)
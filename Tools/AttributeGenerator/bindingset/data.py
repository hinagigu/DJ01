#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BindingSet 数据模型
支持 Tag 绑定和 Attribute 绑定，可用于 AnimInstance、UI Widget 等任意部件
"""

from dataclasses import dataclass, field
from typing import List, Literal


# ============================================================
# 绑定类型常量
# ============================================================

BINDING_TYPE_TAG = "Tag"
BINDING_TYPE_ATTRIBUTE = "Attribute"


# ============================================================
# Tag 绑定
# ============================================================

@dataclass
class TagBinding:
    """单个 Tag 到变量的绑定"""
    tag: str = ""                    # 完整的 Tag 名称（如 Status.Condition.Stunned）
    variable_name: str = ""          # 变量名（如 bStunned）
    event_type: str = "NewOrRemoved" # NewOrRemoved 或 AnyCountChange
    description: str = ""            # 描述
    
    @property
    def binding_type(self) -> str:
        return BINDING_TYPE_TAG
    
    @property
    def var_type(self) -> str:
        """根据事件类型返回变量类型"""
        return "bool" if self.event_type == "NewOrRemoved" else "int32"
    
    @property
    def callback_name(self) -> str:
        """生成回调函数名"""
        # 移除 b 前缀（如果有）来生成回调名
        base_name = self.variable_name
        if base_name.startswith('b') and len(base_name) > 1 and base_name[1].isupper():
            base_name = base_name[1:]
        return f"On{base_name}TagChanged"
    
    @property
    def tag_cpp_name(self) -> str:
        """生成 Tag 的 C++ 变量名（用于引用 DJ01GameplayTags::XXX）"""
        return self.tag.replace('.', '_').replace('-', '_')
    
    def to_dict(self) -> dict:
        return {
            'Type': BINDING_TYPE_TAG,
            'Tag': self.tag,
            'VariableName': self.variable_name,
            'EventType': self.event_type,
            'Description': self.description
        }
    
    @staticmethod
    def from_dict(d: dict) -> 'TagBinding':
        return TagBinding(
            tag=d.get('Tag', ''),
            variable_name=d.get('VariableName', ''),
            event_type=d.get('EventType', 'NewOrRemoved'),
            description=d.get('Description', '')
        )


# ============================================================
# Attribute 绑定
# ============================================================

# ============================================================
# 属性值类型枚举
# ============================================================

# 三层属性值类型
VALUE_TYPE_CURRENT = "Current"       # 当前值（资源型属性，如 Health）
VALUE_TYPE_BASE = "Base"             # 基础层值（BaseAttackPower）
VALUE_TYPE_FLAT = "Flat"             # 固定加成层（FlatAttackPower）
VALUE_TYPE_PERCENT = "Percent"       # 百分比加成层（PercentAttackPower）
VALUE_TYPE_TOTAL = "Total"           # 计算后总值（GetTotalAttackPower）
VALUE_TYPE_EXTRA = "Extra"           # 额外值：Total - Base
VALUE_TYPE_MAX = "Max"               # 最大值（资源型，GetTotalMaxHealth）

# 所有有效的值类型
VALID_VALUE_TYPES = [
    VALUE_TYPE_CURRENT,
    VALUE_TYPE_BASE,
    VALUE_TYPE_FLAT,
    VALUE_TYPE_PERCENT,
    VALUE_TYPE_TOTAL,
    VALUE_TYPE_EXTRA,
    VALUE_TYPE_MAX,
]


@dataclass
class AttributeBinding:
    """单个 Attribute 到变量的绑定"""
    attribute_set: str = ""          # AttributeSet 名称（如 DJ01ResourceSet）
    attribute_name: str = ""         # 属性名（如 Health, AttackPower）
    variable_name: str = ""          # 变量名（如 CurrentHealth, TotalAttackPower）
    var_type: str = "float"          # 变量类型: float, int32, FGameplayAttributeData
    value_type: str = "Current"      # 值类型: Current/Base/Flat/Percent/Total/Extra/Max
    description: str = ""            # 描述
    
    # 兼容旧版本（deprecated，建议使用 value_type）
    listen_current: bool = True      # 是否监听 CurrentValue 变化（废弃）
    listen_base: bool = False        # 是否监听 BaseValue 变化（废弃）
    
    @property
    def binding_type(self) -> str:
        return BINDING_TYPE_ATTRIBUTE
    
    @property
    def full_attribute_name(self) -> str:
        """完整属性名: SetName.AttributeName"""
        return f"{self.attribute_set}.{self.attribute_name}"
    
    @property
    def callback_name(self) -> str:
        """生成回调函数名"""
        return f"On{self.attribute_name}Changed"
    
    @property
    def attribute_getter_name(self) -> str:
        """生成属性 Getter 宏名（如 UCharacterAttributeSet::GetHealthAttribute）"""
        # 对于层属性，返回实际的层属性 Getter
        return f"U{self.attribute_set}::Get{self.actual_attribute_name}Attribute"
    
    def to_dict(self) -> dict:
        return {
            'Type': BINDING_TYPE_ATTRIBUTE,
            'AttributeSet': self.attribute_set,
            'AttributeName': self.attribute_name,
            'VariableName': self.variable_name,
            'VarType': self.var_type,
            'ValueType': self.value_type,
            'Description': self.description
        }
    
    @staticmethod
    def from_dict(d: dict) -> 'AttributeBinding':
        # 兼容旧数据格式
        value_type = d.get('ValueType', '')
        if not value_type:
            # 旧格式兼容：根据 ListenBase/ListenCurrent 推断
            if d.get('ListenBase', False):
                value_type = VALUE_TYPE_BASE
            else:
                value_type = VALUE_TYPE_CURRENT
        
        return AttributeBinding(
            attribute_set=d.get('AttributeSet', ''),
            attribute_name=d.get('AttributeName', ''),
            variable_name=d.get('VariableName', ''),
            var_type=d.get('VarType', 'float'),
            value_type=value_type,
            description=d.get('Description', ''),
            listen_current=d.get('ListenCurrent', True),
            listen_base=d.get('ListenBase', False)
        )
    
    @property
    def is_layered_attribute(self) -> bool:
        """是否是三层属性（需要监听 Base/Flat/Percent 中的某一层）"""
        return self.value_type in [VALUE_TYPE_BASE, VALUE_TYPE_FLAT, VALUE_TYPE_PERCENT]
    
    @property
    def is_computed_value(self) -> bool:
        """是否是计算值（Total/Extra/Max，不直接监听，需要在任意层变化时重算）"""
        return self.value_type in [VALUE_TYPE_TOTAL, VALUE_TYPE_EXTRA, VALUE_TYPE_MAX]
    
    @property
    def actual_attribute_name(self) -> str:
        """
        获取实际的 GAS 属性名（考虑三层属性前缀）
        
        例如：
        - value_type=Current, attribute_name=Health -> Health
        - value_type=Base, attribute_name=AttackPower -> BaseAttackPower
        - value_type=Total, attribute_name=AttackPower -> 需要监听 BaseAttackPower
        """
        if self.value_type == VALUE_TYPE_CURRENT:
            return self.attribute_name
        elif self.value_type in [VALUE_TYPE_BASE, VALUE_TYPE_TOTAL, VALUE_TYPE_EXTRA]:
            return f"Base{self.attribute_name}"
        elif self.value_type == VALUE_TYPE_FLAT:
            return f"Flat{self.attribute_name}"
        elif self.value_type == VALUE_TYPE_PERCENT:
            return f"Percent{self.attribute_name}"
        elif self.value_type == VALUE_TYPE_MAX:
            return f"BaseMax{self.attribute_name}"
        return self.attribute_name


# ============================================================
# BindingSet - 绑定集
# ============================================================

@dataclass 
class BindingSetData:
    """BindingSet 数据模型 - 一组相关的绑定，可包含 Tag 和 Attribute"""
    name: str = ""                   # Set 名称（如 CommonStatus, PlayerHUD）
    description: str = ""            # Set 描述
    tag_bindings: List[TagBinding] = field(default_factory=list)
    attribute_bindings: List[AttributeBinding] = field(default_factory=list)
    
    @property
    def macro_prefix(self) -> str:
        """生成宏名前缀（大写下划线格式）"""
        # CommonStatus -> COMMON_STATUS
        result = []
        for i, c in enumerate(self.name):
            if c.isupper() and i > 0:
                result.append('_')
            result.append(c.upper())
        return ''.join(result)
    
    @property
    def header_filename(self) -> str:
        """生成头文件名"""
        return f"BindingSet_{self.name}.h"
    
    @property
    def total_bindings(self) -> int:
        """总绑定数"""
        return len(self.tag_bindings) + len(self.attribute_bindings)
    
    @property
    def has_tag_bindings(self) -> bool:
        return len(self.tag_bindings) > 0
    
    @property
    def has_attribute_bindings(self) -> bool:
        return len(self.attribute_bindings) > 0
    
    def to_dict(self) -> dict:
        return {
            'Name': self.name,
            'Description': self.description,
            'TagBindings': [b.to_dict() for b in self.tag_bindings],
            'AttributeBindings': [b.to_dict() for b in self.attribute_bindings]
        }
    
    @staticmethod
    def from_dict(d: dict) -> 'BindingSetData':
        # 兼容旧格式（只有 Bindings 字段的 AnimTagSet）
        tag_bindings = []
        attribute_bindings = []
        
        # 新格式
        if 'TagBindings' in d:
            tag_bindings = [TagBinding.from_dict(b) for b in d.get('TagBindings', [])]
        if 'AttributeBindings' in d:
            attribute_bindings = [AttributeBinding.from_dict(b) for b in d.get('AttributeBindings', [])]
        
        # 旧格式兼容（AnimTagSet 的 Bindings 字段）
        if 'Bindings' in d and not tag_bindings:
            for b in d.get('Bindings', []):
                if b.get('Type') == BINDING_TYPE_ATTRIBUTE:
                    attribute_bindings.append(AttributeBinding.from_dict(b))
                else:
                    # 默认为 Tag 绑定（兼容旧数据）
                    tag_bindings.append(TagBinding.from_dict(b))
        
        return BindingSetData(
            name=d.get('Name', ''),
            description=d.get('Description', ''),
            tag_bindings=tag_bindings,
            attribute_bindings=attribute_bindings
        )


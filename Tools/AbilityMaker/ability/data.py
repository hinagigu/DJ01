#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
技能数据模型
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from pathlib import Path


@dataclass
class AttributeCapture:
    """属性捕获定义"""
    source: str  # "Source" 或 "Target"
    set: str     # 属性集名称
    attr: str    # 属性名称
    layer: str   # "Base", "Current", "Total"
    
    @classmethod
    def from_dict(cls, data: dict) -> 'AttributeCapture':
        return cls(
            source=data.get('source', 'Target'),
            set=data.get('set', ''),
            attr=data.get('attr', ''),
            layer=data.get('layer', 'Total')
        )


@dataclass
class TagCondition:
    """Tag 条件定义"""
    source: str  # "Source" 或 "Target"
    tag: str     # 完整 Tag 路径
    
    @classmethod
    def from_dict(cls, data: dict) -> 'TagCondition':
        return cls(
            source=data.get('source', 'Target'),
            tag=data.get('tag', '')
        )


@dataclass
class ConditionDefinition:
    """效果条件定义"""
    captures: List[AttributeCapture] = field(default_factory=list)
    tag_conditions: List[TagCondition] = field(default_factory=list)
    code: str = ""
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ConditionDefinition':
        if not data:
            return cls()
        return cls(
            captures=[AttributeCapture.from_dict(c) for c in data.get('Captures', [])],
            tag_conditions=[TagCondition.from_dict(t) for t in data.get('TagConditions', [])],
            code=data.get('Code', '')
        )


@dataclass
class ScalingRatio:
    """属性缩放比例"""
    attr: str
    ratio: float
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ScalingRatio':
        return cls(
            attr=data.get('attr', ''),
            ratio=data.get('ratio', 0.0)
        )


@dataclass
class DamageConfig:
    """伤害配置"""
    base_damage: float = 0.0
    damage_type: str = "Physical"  # Physical, Magical, Pure
    scaling_ratios: List[ScalingRatio] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'DamageConfig':
        if not data:
            return cls()
        return cls(
            base_damage=data.get('BaseDamage', 0.0),
            damage_type=data.get('DamageType', 'Physical'),
            scaling_ratios=[ScalingRatio.from_dict(s) for s in data.get('ScalingRatios', [])]
        )


@dataclass
class HealConfig:
    """治疗配置"""
    base_heal: float = 0.0
    scaling_ratios: List[ScalingRatio] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'HealConfig':
        if not data:
            return cls()
        return cls(
            base_heal=data.get('BaseHeal', 0.0),
            scaling_ratios=[ScalingRatio.from_dict(s) for s in data.get('ScalingRatios', [])]
        )


@dataclass
class ApplyEffectConfig:
    """应用效果配置"""
    effect_class: str = ""
    duration: float = 0.0
    stacks: int = 1
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ApplyEffectConfig':
        if not data:
            return cls()
        return cls(
            effect_class=data.get('EffectClass', ''),
            duration=data.get('Duration', 0.0),
            stacks=data.get('Stacks', 1)
        )


@dataclass
class EffectDefinition:
    """技能效果定义"""
    name: str
    phase: str  # OnActivate, OnCommit, OnAnimEvent, OnEnd
    event_tag: str = ""
    effect_type: str = "Damage"  # Damage, Heal, ApplyEffect, SpawnActor
    condition: ConditionDefinition = field(default_factory=ConditionDefinition)
    damage_config: Optional[DamageConfig] = None
    heal_config: Optional[HealConfig] = None
    apply_effect_config: Optional[ApplyEffectConfig] = None
    
    @classmethod
    def from_dict(cls, data: dict) -> 'EffectDefinition':
        return cls(
            name=data.get('Name', 'UnnamedEffect'),
            phase=data.get('Phase', 'OnCommit'),
            event_tag=data.get('EventTag', ''),
            effect_type=data.get('Type', 'Damage'),
            condition=ConditionDefinition.from_dict(data.get('Condition', {})),
            damage_config=DamageConfig.from_dict(data.get('DamageConfig')) if data.get('DamageConfig') else None,
            heal_config=HealConfig.from_dict(data.get('HealConfig')) if data.get('HealConfig') else None,
            apply_effect_config=ApplyEffectConfig.from_dict(data.get('ApplyEffectConfig')) if data.get('ApplyEffectConfig') else None
        )


@dataclass
class AbilityDefinition:
    """技能定义"""
    name: str
    display_name: str = ""
    description: str = ""
    effects: List[EffectDefinition] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'AbilityDefinition':
        return cls(
            name=data.get('Name', 'UnnamedAbility'),
            display_name=data.get('DisplayName', ''),
            description=data.get('Description', ''),
            effects=[EffectDefinition.from_dict(e) for e in data.get('Effects', [])]
        )


def load_ability_definitions(file_path: Path) -> List[AbilityDefinition]:
    """从 JSON 文件加载技能定义"""
    if not file_path.exists():
        return []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    return [AbilityDefinition.from_dict(a) for a in data.get('Abilities', [])]


def save_ability_definitions(file_path: Path, abilities: List[AbilityDefinition]):
    """保存技能定义到 JSON 文件"""
    data = {
        "Version": "1.0.0",
        "Description": "技能效果配置 - 由 AbilityMaker 生成",
        "Abilities": [ability_to_dict(a) for a in abilities]
    }
    
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def ability_to_dict(ability: AbilityDefinition) -> dict:
    """将技能定义转换为字典"""
    return {
        "Name": ability.name,
        "DisplayName": ability.display_name,
        "Description": ability.description,
        "Effects": [effect_to_dict(e) for e in ability.effects]
    }


def effect_to_dict(effect: EffectDefinition) -> dict:
    """将效果定义转换为字典"""
    result = {
        "Name": effect.name,
        "Phase": effect.phase,
        "EventTag": effect.event_tag,
        "Type": effect.effect_type,
        "Condition": {
            "Captures": [{"source": c.source, "set": c.set, "attr": c.attr, "layer": c.layer} 
                        for c in effect.condition.captures],
            "TagConditions": [{"source": t.source, "tag": t.tag} 
                             for t in effect.condition.tag_conditions],
            "Code": effect.condition.code
        }
    }
    
    if effect.damage_config:
        result["DamageConfig"] = {
            "BaseDamage": effect.damage_config.base_damage,
            "DamageType": effect.damage_config.damage_type,
            "ScalingRatios": [{"attr": s.attr, "ratio": s.ratio} 
                            for s in effect.damage_config.scaling_ratios]
        }
    
    if effect.heal_config:
        result["HealConfig"] = {
            "BaseHeal": effect.heal_config.base_heal,
            "ScalingRatios": [{"attr": s.attr, "ratio": s.ratio} 
                            for s in effect.heal_config.scaling_ratios]
        }
    
    if effect.apply_effect_config:
        result["ApplyEffectConfig"] = {
            "EffectClass": effect.apply_effect_config.effect_class,
            "Duration": effect.apply_effect_config.duration,
            "Stacks": effect.apply_effect_config.stacks
        }
    
    return result
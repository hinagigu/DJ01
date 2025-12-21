#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
属性数据模型 - 扩展版本
支持 Clamp、委托、事件触发、GameplayCue 配置
"""

import json


class ClampConfig:
    """Clamp 配置"""
    
    def __init__(self, enabled=False, min_value=None, max_value=None, max_attribute=None):
        self.enabled = enabled
        self.min_value = min_value           # 最小值 (float 或 None)
        self.max_value = max_value           # 最大值固定值 (float 或 None)
        self.max_attribute = max_attribute   # 最大值属性名 (str 或 None)
    
    def to_dict(self):
        return {
            'Enabled': self.enabled,
            'MinValue': self.min_value,
            'MaxValue': self.max_value,
            'MaxAttribute': self.max_attribute
        }
    
    @staticmethod
    def from_dict(d):
        if not d:
            return ClampConfig()
        return ClampConfig(
            enabled=d.get('Enabled', False),
            min_value=d.get('MinValue'),
            max_value=d.get('MaxValue'),
            max_attribute=d.get('MaxAttribute')
        )


class DelegateConfig:
    """委托配置"""
    
    def __init__(self, on_change=False, on_increase=False, on_decrease=False,
                 decrease_alias=""):
        self.on_change = on_change           # 任何变化时广播
        self.on_increase = on_increase       # 值增加时广播
        self.on_decrease = on_decrease       # 值减少时广播
        self.decrease_alias = decrease_alias # 减少委托别名 (如 OnDamageReceived)
    
    def to_dict(self):
        return {
            'OnChange': self.on_change,
            'OnIncrease': self.on_increase,
            'OnDecrease': self.on_decrease,
            'DecreaseAlias': self.decrease_alias
        }
    
    @staticmethod
    def from_dict(d):
        if not d:
            return DelegateConfig()
        return DelegateConfig(
            on_change=d.get('OnChange', False),
            on_increase=d.get('OnIncrease', False),
            on_decrease=d.get('OnDecrease', False),
            decrease_alias=d.get('DecreaseAlias', '')
        )


class EventConfig:
    """事件触发配置"""
    
    def __init__(self, on_zero_tag="", on_full_tag="", 
                 threshold_low=None, threshold_low_tag="",
                 threshold_high=None, threshold_high_tag=""):
        self.on_zero_tag = on_zero_tag           # 归零时添加的 Tag
        self.on_full_tag = on_full_tag           # 满值时添加的 Tag
        self.threshold_low = threshold_low       # 低阈值百分比 (0.3 = 30%)
        self.threshold_low_tag = threshold_low_tag
        self.threshold_high = threshold_high     # 高阈值百分比
        self.threshold_high_tag = threshold_high_tag
    
    def to_dict(self):
        return {
            'OnZeroTag': self.on_zero_tag,
            'OnFullTag': self.on_full_tag,
            'ThresholdLow': self.threshold_low,
            'ThresholdLowTag': self.threshold_low_tag,
            'ThresholdHigh': self.threshold_high,
            'ThresholdHighTag': self.threshold_high_tag
        }
    
    @staticmethod
    def from_dict(d):
        if not d:
            return EventConfig()
        return EventConfig(
            on_zero_tag=d.get('OnZeroTag', ''),
            on_full_tag=d.get('OnFullTag', ''),
            threshold_low=d.get('ThresholdLow'),
            threshold_low_tag=d.get('ThresholdLowTag', ''),
            threshold_high=d.get('ThresholdHigh'),
            threshold_high_tag=d.get('ThresholdHighTag', '')
        )


class CueConfig:
    """GameplayCue 配置"""
    
    def __init__(self, on_decrease_cue="", on_zero_cue="", on_increase_cue=""):
        self.on_decrease_cue = on_decrease_cue  # 减少时触发的 Cue
        self.on_zero_cue = on_zero_cue          # 归零时触发的 Cue
        self.on_increase_cue = on_increase_cue  # 增加时触发的 Cue
    
    def to_dict(self):
        return {
            'OnDecreaseCue': self.on_decrease_cue,
            'OnZeroCue': self.on_zero_cue,
            'OnIncreaseCue': self.on_increase_cue
        }
    
    @staticmethod
    def from_dict(d):
        if not d:
            return CueConfig()
        return CueConfig(
            on_decrease_cue=d.get('OnDecreaseCue', ''),
            on_zero_cue=d.get('OnZeroCue', ''),
            on_increase_cue=d.get('OnIncreaseCue', '')
        )


class ResourceConfig:
    """Resource 属性配置 - MaxXxx 变化时 Xxx 的联动模式"""
    
    # 联动模式常量
    MODE_KEEP_CURRENT = "KeepCurrent"    # 保持当前值不变（超出上限时 Clamp）
    MODE_KEEP_RATIO = "KeepRatio"        # 保持百分比（80% → 80%）
    MODE_ADD_DIFFERENCE = "AddDifference" # 增加差值（MaxHealth +100 → Health +100）
    
    MODES = [MODE_KEEP_CURRENT, MODE_KEEP_RATIO, MODE_ADD_DIFFERENCE]
    MODE_DESCRIPTIONS = {
        MODE_KEEP_CURRENT: "保持当前值（超限时Clamp）",
        MODE_KEEP_RATIO: "保持百分比（如 80%→80%）",
        MODE_ADD_DIFFERENCE: "同步增减差值"
    }
    
    def __init__(self, max_change_mode="KeepCurrent"):
        self.max_change_mode = max_change_mode  # MaxXxx 变化时的联动模式
    
    def to_dict(self):
        return {
            'MaxChangeMode': self.max_change_mode
        }
    
    @staticmethod
    def from_dict(d):
        if not d:
            return ResourceConfig()
        return ResourceConfig(
            max_change_mode=d.get('MaxChangeMode', 'KeepCurrent')
        )


class MetaConfig:
    """Meta 属性配置 - 用于临时中转值的处理"""
    
    def __init__(self, target_attribute="", apply_mode="Add", 
                 broadcast_event=False, event_tag=""):
        self.target_attribute = target_attribute    # 转发到的目标属性（如 Health）
        self.apply_mode = apply_mode                # 应用模式: Add, Set, Multiply
        self.broadcast_event = broadcast_event      # 是否广播事件
        self.event_tag = event_tag                  # 广播的事件 Tag
    
    def to_dict(self):
        return {
            'TargetAttribute': self.target_attribute,
            'ApplyMode': self.apply_mode,
            'BroadcastEvent': self.broadcast_event,
            'EventTag': self.event_tag
        }
    
    @staticmethod
    def from_dict(d):
        if not d:
            return MetaConfig()
        return MetaConfig(
            target_attribute=d.get('TargetAttribute', ''),
            apply_mode=d.get('ApplyMode', 'Add'),
            broadcast_event=d.get('BroadcastEvent', False),
            event_tag=d.get('EventTag', '')
        )


class AttributeData:
    """属性数据模型 - 扩展版本"""
    
    def __init__(self, set_name="", name="", attr_type="Layered", category="Combat",
                 default_base=0.0, default_flat=0.0, default_percent=0.0, 
                 default_current=0.0, description="",
                 clamp=None, delegate=None, event=None, cue=None, 
                 meta_config=None, resource_config=None):
        # 基础信息
        self.set_name = set_name
        self.name = name
        self.type = attr_type
        self.category = category
        self.description = description
        
        # 默认值
        self.default_base = default_base
        self.default_flat = default_flat
        self.default_percent = default_percent
        self.default_current = default_current
        
        # 行为配置
        self.clamp = clamp if clamp else ClampConfig()
        self.delegate = delegate if delegate else DelegateConfig()
        self.event = event if event else EventConfig()
        self.cue = cue if cue else CueConfig()
        self.meta_config = meta_config if meta_config else MetaConfig()
        self.resource_config = resource_config if resource_config else ResourceConfig()
    
    def to_dict(self):
        """转换为字典（用于 JSON 保存）"""
        return {
            'SetName': self.set_name,
            'AttributeName': self.name,
            'Type': self.type,
            'Category': self.category,
            'DefaultBase': self.default_base,
            'DefaultFlat': self.default_flat,
            'DefaultPercent': self.default_percent,
            'DefaultCurrent': self.default_current,
            'Description': self.description,
            # 行为配置
            'Clamp': self.clamp.to_dict(),
            'Delegate': self.delegate.to_dict(),
            'Event': self.event.to_dict(),
            'Cue': self.cue.to_dict(),
            'MetaConfig': self.meta_config.to_dict(),
            'ResourceConfig': self.resource_config.to_dict()
        }
    
    def to_csv_dict(self):
        """转换为 CSV 格式字典（向后兼容）"""
        return {
            'SetName': self.set_name,
            'AttributeName': self.name,
            'Type': self.type,
            'Category': self.category,
            'DefaultBase': str(self.default_base) if self.default_base else '',
            'DefaultFlat': str(self.default_flat) if self.default_flat else '',
            'DefaultPercent': str(self.default_percent) if self.default_percent else '',
            'DefaultCurrent': str(self.default_current) if self.default_current else '',
            'Description': self.description,
            # 行为配置序列化为 JSON 字符串
            'BehaviorConfig': json.dumps({
                'Clamp': self.clamp.to_dict(),
                'Delegate': self.delegate.to_dict(),
                'Event': self.event.to_dict(),
                'Cue': self.cue.to_dict(),
                'MetaConfig': self.meta_config.to_dict(),
                'ResourceConfig': self.resource_config.to_dict()
            }, ensure_ascii=False)
        }

    @staticmethod
    def from_dict(d):
        """从字典创建（支持 CSV 和 JSON 两种格式）"""
        # 解析行为配置
        clamp = None
        delegate = None
        event = None
        cue = None
        meta_config = None
        resource_config = None
        
        # 方式1: 直接嵌套对象 (JSON 格式)
        if 'Clamp' in d and isinstance(d['Clamp'], dict):
            clamp = ClampConfig.from_dict(d.get('Clamp'))
            delegate = DelegateConfig.from_dict(d.get('Delegate'))
            event = EventConfig.from_dict(d.get('Event'))
            cue = CueConfig.from_dict(d.get('Cue'))
            meta_config = MetaConfig.from_dict(d.get('MetaConfig'))
            resource_config = ResourceConfig.from_dict(d.get('ResourceConfig'))
        # 方式2: JSON 字符串 (CSV 格式)
        elif 'BehaviorConfig' in d and d['BehaviorConfig']:
            try:
                behavior = json.loads(d['BehaviorConfig'])
                clamp = ClampConfig.from_dict(behavior.get('Clamp'))
                delegate = DelegateConfig.from_dict(behavior.get('Delegate'))
                event = EventConfig.from_dict(behavior.get('Event'))
                cue = CueConfig.from_dict(behavior.get('Cue'))
                meta_config = MetaConfig.from_dict(behavior.get('MetaConfig'))
                resource_config = ResourceConfig.from_dict(behavior.get('ResourceConfig'))
            except json.JSONDecodeError:
                pass
        
        # 解析默认值
        def parse_float(val):
            if val is None or val == '':
                return 0.0
            try:
                return float(val)
            except (ValueError, TypeError):
                return 0.0
        
        return AttributeData(
            set_name=d.get('SetName', ''),
            name=d.get('AttributeName', ''),
            attr_type=d.get('Type', 'Layered'),
            category=d.get('Category', 'Combat'),
            default_base=parse_float(d.get('DefaultBase')),
            default_flat=parse_float(d.get('DefaultFlat')),
            default_percent=parse_float(d.get('DefaultPercent')),
            default_current=parse_float(d.get('DefaultCurrent')),
            description=d.get('Description', ''),
            clamp=clamp,
            delegate=delegate,
            event=event,
            cue=cue,
            meta_config=meta_config,
            resource_config=resource_config
        )
    
    def has_behavior_config(self):
        """检查是否有行为配置"""
        return (self.clamp.enabled or 
                self.delegate.on_change or self.delegate.on_increase or self.delegate.on_decrease or
                self.event.on_zero_tag or self.event.on_full_tag or 
                self.event.threshold_low is not None or
                self.cue.on_decrease_cue or self.cue.on_zero_cue or self.cue.on_increase_cue)
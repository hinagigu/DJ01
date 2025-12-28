#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 配置文件
"""

from pathlib import Path
import sys


def get_project_root():
    """获取项目根目录（兼容 exe 和 py 运行）"""
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent.resolve()
    else:
        return Path(__file__).parent.parent.parent.resolve()


PROJECT_ROOT = get_project_root()

# 模块名
MODULE_NAME = "DJ01"

# ========== 属性配置 ==========
ATTRIBUTES_CONFIG = PROJECT_ROOT / "Source/DJ01/AbilitySystem/Attributes/Config/AttributeDefinitions.csv"
ATTRIBUTES_BEHAVIORS = PROJECT_ROOT / "Source/DJ01/AbilitySystem/Attributes/Config/AttributeBehaviors.json"
ATTRIBUTES_HEADER = PROJECT_ROOT / "Source/DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"
ATTRIBUTES_SOURCE = PROJECT_ROOT / "Source/DJ01/AbilitySystem/Attributes/Private/DJ01GeneratedAttributes.cpp"

# 属性 CSV 字段头（不再包含 BehaviorConfig）
ATTRIBUTES_CSV_FIELDS = [
    'SetName', 'AttributeName', 'Type', 'Category',
    'DefaultBase', 'DefaultFlat', 'DefaultPercent', 'DefaultCurrent',
    'Description'
]

# 旧版 CSV 字段头（用于向后兼容读取）
ATTRIBUTES_CSV_FIELDS_LEGACY = [
    'SetName', 'AttributeName', 'Type', 'Category',
    'DefaultBase', 'DefaultFlat', 'DefaultPercent', 'DefaultCurrent',
    'Description', 'BehaviorConfig'
]

# ========== Execution 配置 ==========
EXECUTIONS_CONFIG = PROJECT_ROOT / "Source/DJ01/AbilitySystem/Executions/Config/ExecutionDefinitions.json"
EXECUTIONS_OUTPUT = PROJECT_ROOT / "Source/DJ01/AbilitySystem/Executions/Generated"

# ========== GameplayTags 配置 ==========
TAGS_CONFIG_CSV = PROJECT_ROOT / "Source/DJ01/System/Config/GameplayTagDefinitions.csv"
TAGS_CONFIG_JSON = PROJECT_ROOT / "Source/DJ01/System/Config/GameplayTagDefinitions.json"  # 旧版后备
TAGS_CONFIG = TAGS_CONFIG_CSV  # 默认使用 CSV
TAGS_HEADER = PROJECT_ROOT / "Source/DJ01/System/Public/DJ01GameplayTags.h"
TAGS_SOURCE = PROJECT_ROOT / "Source/DJ01/System/Private/DJ01GameplayTags.cpp"

# Tag CSV 字段
TAGS_CSV_FIELDS = ['Category', 'Tag', 'VariableName', 'Description']

# BindingSet 配置
BINDINGSET_CONFIG = PROJECT_ROOT / "Source/DJ01/GAS/Config/BindingSetDefinitions.json"
BINDINGSET_OUTPUT = PROJECT_ROOT / "Source/DJ01/GAS/Generated/BindingSets"

# ========== MMC 配置 ==========
MMC_CONFIG = PROJECT_ROOT / "Source/DJ01/AbilitySystem/MMC/Config/MMCDefinitions.json"
MMC_HEADER = PROJECT_ROOT / "Source/DJ01/AbilitySystem/MMC/Public/DJ01GeneratedMMC.h"
MMC_SOURCE = PROJECT_ROOT / "Source/DJ01/AbilitySystem/MMC/Private/DJ01GeneratedMMC.cpp"

# ========== 选项 ==========
ATTRIBUTE_TYPES = ["Layered", "Simple", "Meta", "Resource"]
ATTRIBUTE_CATEGORIES = ["Combat", "Resource", "Element", "Utility"]
CAPTURE_LAYERS = ["Base", "Flat", "Percent", "Total", "Value"]
OUTPUT_OPS = ["Additive", "Multiply", "Override"]

# Tag 条件效果类型
TAG_EFFECTS = ["Skip", "Multiply", "Add"]
TAG_SOURCES = ["Source", "Target"]

# Tag 分类（基于现有项目结构）
TAG_CATEGORIES = [
    "InitState",        # 初始化状态
    "InputTag",         # 输入标签
    "AttributeSet",     # 属性集标签
    "Ability",          # 技能系统
    "Event",            # 事件标签
    "Status",           # 状态标签
    "Damage",           # 伤害相关
    "Weakness",         # 弱点标签
    "GameplayCue",      # 游戏提示
    "Cheat",            # 作弊标签
    "Custom",           # 自定义
]
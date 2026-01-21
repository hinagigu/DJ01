#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AbilityMaker 配置文件
"""

from pathlib import Path

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent.parent

# 配置文件路径
CONFIG_DIR = PROJECT_ROOT / "Source" / "DJ01" / "AbilitySystem" / "Abilities" / "Config"
ABILITY_DEFINITIONS_FILE = CONFIG_DIR / "AbilityDefinitions.json"

# AngelScript 输出目录
SCRIPT_OUTPUT_DIR = PROJECT_ROOT / "Script" / "GeneratedAbilities"

# 模块名
MODULE_NAME = "DJ01"

# 默认 GameplayEffect 类
DEFAULT_DAMAGE_GE = "GE_GenericDamage"
DEFAULT_HEAL_GE = "GE_GenericHeal"

# GameplayTag 前缀
TAG_PREFIX = "DJ01GameplayTags"
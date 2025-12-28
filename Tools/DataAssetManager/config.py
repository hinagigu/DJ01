#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 配置常量
职责：定义全局路径和常量
"""

import os

# ===== 路径配置 =====

TOOL_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(TOOL_DIR))

# 导出项目根目录
__all__ = ['PROJECT_ROOT', 'TOOL_DIR', 'CONFIG_DIR', 'CONFIG_FILES', 
           'PROJECT_PREFIX', 'APP_TITLE', 'APP_VERSION', 'ASSET_TYPES', 
           'ASSET_TYPE_TO_CONFIG']

# 配置文件目录
CONFIG_DIR = os.path.join(TOOL_DIR, "configs")

# UE 项目路径
UE_CONTENT_DIR = os.path.join(PROJECT_ROOT, "Content")
UE_SOURCE_DIR = os.path.join(PROJECT_ROOT, "Source", "DJ01")
UE_SCRIPTS_DIR = os.path.join(TOOL_DIR, "ue_scripts")

# ===== 配置文件路径 =====

# Schema 目录（拆分的 schema 文件）
SCHEMA_DIR = os.path.join(CONFIG_DIR, "schema")
os.makedirs(SCHEMA_DIR, exist_ok=True)

# Options 目录（拆分的可选项文件）
OPTIONS_DIR = os.path.join(CONFIG_DIR, "options")
os.makedirs(OPTIONS_DIR, exist_ok=True)

CONFIG_FILES = {
    # Schema 文件
    "schema_dir": SCHEMA_DIR,
    "schema_common": os.path.join(SCHEMA_DIR, "common.json"),
    
    # Options 目录
    "options_dir": OPTIONS_DIR,
    
    # 扫描路径配置
    "scan_paths": os.path.join(CONFIG_DIR, "scan_paths.json"),
    
    # 其他配置
    "registry": os.path.join(CONFIG_DIR, "asset_registry.json"),
    
    # 资产数据文件
    "experiences": os.path.join(CONFIG_DIR, "experiences.json"),
    "pawn_data": os.path.join(CONFIG_DIR, "pawn_data.json"),
    "input_configs": os.path.join(CONFIG_DIR, "input_configs.json"),
    "ability_sets": os.path.join(CONFIG_DIR, "ability_sets.json"),
    "action_sets": os.path.join(CONFIG_DIR, "action_sets.json"),
}

# ===== 项目常量 =====

PROJECT_PREFIX = "DJ01"
APP_TITLE = f"{PROJECT_PREFIX} DataAsset 配置管理器"
APP_VERSION = "1.0.0"

# ===== 资产类型映射 =====

ASSET_TYPES = [
    "Experience",
    "PawnData", 
    "InputConfig",
    "AbilitySet",
    "ActionSet",
]

# 资产类型到配置文件的映射
ASSET_TYPE_TO_CONFIG = {
    "Experience": "experiences",
    "PawnData": "pawn_data",
    "InputConfig": "input_configs",
    "AbilitySet": "ability_sets",
    "ActionSet": "action_sets",
}

# ===== 确保目录存在 =====

os.makedirs(CONFIG_DIR, exist_ok=True)
os.makedirs(UE_SCRIPTS_DIR, exist_ok=True)
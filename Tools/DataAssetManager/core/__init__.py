#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 核心模块
"""

import os
import sys

# 确保父目录在路径中
_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

from core.schema import PropertyDef, StructDef, DataAssetDef
from core.schema_loader import SchemaLoader
from core.registry import AssetRegistry, AssetReference
from core.validation import ValidationEngine
from core.data_manager import DataManager
from core.options_scanner import OptionsScanner, OptionItem
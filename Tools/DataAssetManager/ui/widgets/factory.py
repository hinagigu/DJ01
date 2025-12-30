#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 控件工厂
职责：根据属性定义创建对应的控件
"""

import tkinter as tk
from typing import Any, Callable, List, Dict, Optional
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from ui.widgets.base import PropertyWidget
from ui.widgets.text import TextInputWidget
from ui.widgets.number import SpinBoxWidget, CheckboxWidget
from ui.widgets.list import StringListWidget, AssetPickerListWidget
from ui.widgets.picker import ComboBoxWidget, TagSelectorWidget, AssetPickerWidget
from ui.widgets.struct_array import StructArrayEditorWidget
from ui.widgets.checkbox_list import CheckboxListWidget
from ui.widgets.instanced_array import InstancedArrayEditorWidget
from ui_base.property_widgets import MultiSelectDropdownWidget

from core.schema import PropertyDef, StructDef
from core.schema_loader import SchemaLoader
from core.options_scanner import OptionsScanner


class WidgetFactory:
    """控件工厂"""
    
    def __init__(self, schema_loader: SchemaLoader = None, 
                 options_scanner: OptionsScanner = None):
        self.schema_loader = schema_loader
        self.options_scanner = options_scanner
        self._tag_provider: Callable[[], List[str]] = None
        self._asset_provider: Callable[[str, str], List[str]] = None
    
    def set_options_scanner(self, scanner: OptionsScanner):
        """设置选项扫描器"""
        self.options_scanner = scanner
    
    def set_tag_provider(self, provider: Callable[[], List[str]]):
        """设置标签提供器"""
        self._tag_provider = provider
    
    def set_asset_provider(self, provider: Callable[[str, str], List[str]]):
        """设置资产提供器"""
        self._asset_provider = provider
    
    def create(self, parent: tk.Widget, prop: PropertyDef,
               on_change: Callable[[str, Any], None] = None) -> Optional[PropertyWidget]:
        """根据属性定义创建控件"""
        
        widget_type = prop.widget
        
        if widget_type == "text_input":
            return TextInputWidget(parent, prop, on_change)
        
        elif widget_type == "spin_box":
            return SpinBoxWidget(parent, prop, on_change)
        
        elif widget_type == "checkbox":
            return CheckboxWidget(parent, prop, on_change)
        
        elif widget_type == "combobox":
            # 获取选项
            options = self._get_options_from_source(prop.options_source)
            return ComboBoxWidget(parent, prop, options, on_change)
        
        elif widget_type == "checkbox_list":
            # 多选列表控件
            options = self._get_options_for_checkbox_list(prop.options_source)
            return CheckboxListWidget(parent, prop, on_change, options)
        
        elif widget_type == "multi_select_dropdown":
            # 多选下拉控件（支持 JSON 同步）
            options = self._get_options_from_source(prop.options_source)
            return MultiSelectDropdownWidget(
                parent, prop,
                options=options,
                on_change=on_change,
                json_source=prop.options_source
            )
        
        elif widget_type == "tag_selector":
            tags = self._get_tags(prop.categories)
            return TagSelectorWidget(parent, prop, tags, on_change)
        
        elif widget_type == "asset_picker":
            assets = self._get_assets(prop.asset_class, prop.content_path)
            return AssetPickerWidget(parent, prop, assets, on_change)
        
        elif widget_type == "asset_picker_list":
            assets = self._get_assets(prop.asset_class, prop.content_path)
            return AssetPickerListWidget(parent, prop, assets, on_change)
        
        elif widget_type == "string_list":
            return StringListWidget(parent, prop, on_change)
        
        elif widget_type == "struct_array_editor":
            struct_def = None
            if self.schema_loader and prop.struct_type:
                struct_def = self.schema_loader.get_struct_def(prop.struct_type)
            return StructArrayEditorWidget(parent, prop, struct_def, on_change, self.options_scanner)
        
        elif widget_type == "instanced_array_editor":
            # 获取可用类型定义
            available_types = self._get_available_types(prop.available_types)
            return InstancedArrayEditorWidget(
                parent, prop, available_types, 
                self.schema_loader, self, on_change
            )
        
        elif widget_type == "class_picker":
            # 类选择器暂用文本输入
            return TextInputWidget(parent, prop, on_change)
        
        else:
            # 默认文本输入
            return TextInputWidget(parent, prop, on_change)
    
    def _get_options_from_source(self, source: str) -> List[Dict[str, str]]:
        """
        从选项源获取下拉选项
        
        返回字典列表，包含 name 和 display_name
        ComboBoxWidget 会使用 display_name 显示，但返回 name 作为值
        """
        if not self.options_scanner or not source:
            return []
        
        options_map = {
            "game_features": self.options_scanner.get_game_features,
            "pawn_data": self.options_scanner.get_pawn_data_options,
            "ability_sets": self.options_scanner.get_ability_set_options,
            "action_sets": self.options_scanner.get_action_set_options,
            "input_configs": self.options_scanner.get_input_config_options,
            "input_actions": self.options_scanner.get_input_action_options,
            "pawn_classes": self.options_scanner.get_pawn_class_options,
            "camera_modes": self.options_scanner.get_camera_mode_options,
            "gamefeature_actions": self.options_scanner.get_gamefeature_action_options,
            # GameFeature Actions 相关
            "input_mapping_contexts": self.options_scanner.get_input_mapping_context_options,
            "gameplay_abilities": self.options_scanner.get_gameplay_ability_options,
            "attribute_sets": self.options_scanner.get_attribute_set_options,
            "widget_classes": self.options_scanner.get_widget_class_options,
            "activatable_widgets": self.options_scanner.get_activatable_widget_options,
            "ui_layer_tags": self.options_scanner.get_ui_layer_tag_options,
            "ui_slot_tags": self.options_scanner.get_ui_slot_tag_options,
        }
        
        getter = options_map.get(source)
        if getter:
            return getter()  # 直接返回字典列表
        return []
    
    def _get_options_for_checkbox_list(self, source: str) -> List[Dict[str, str]]:
        """获取多选列表的完整选项信息"""
        if not self.options_scanner or not source:
            return []
        
        options_map = {
            "game_features": self.options_scanner.get_game_features,
            "pawn_data": self.options_scanner.get_pawn_data_options,
            "ability_sets": self.options_scanner.get_ability_set_options,
            "action_sets": self.options_scanner.get_action_set_options,
            "input_configs": self.options_scanner.get_input_config_options,
            "input_actions": self.options_scanner.get_input_action_options,
            "gamefeature_actions": self.options_scanner.get_gamefeature_action_options,
            # GameFeature Actions 相关
            "input_mapping_contexts": self.options_scanner.get_input_mapping_context_options,
            "gameplay_abilities": self.options_scanner.get_gameplay_ability_options,
            "attribute_sets": self.options_scanner.get_attribute_set_options,
            "widget_classes": self.options_scanner.get_widget_class_options,
            "activatable_widgets": self.options_scanner.get_activatable_widget_options,
            "ui_layer_tags": self.options_scanner.get_ui_layer_tag_options,
            "ui_slot_tags": self.options_scanner.get_ui_slot_tag_options,
        }
        
        getter = options_map.get(source)
        if getter:
            return getter()
        return []
    
    def _get_tags(self, categories: str = "") -> List[str]:
        """获取可用标签"""
        if self._tag_provider:
            all_tags = self._tag_provider()
            if categories:
                return [t for t in all_tags if t.startswith(categories)]
            return all_tags
        
        # 也从 options_scanner 获取
        if self.options_scanner:
            return self.options_scanner.get_gameplay_tags(categories)
        
        return []
    
    def _get_assets(self, asset_class: str, content_path: str) -> List[str]:
        """获取可用资产"""
        if self._asset_provider:
            return self._asset_provider(asset_class, content_path)
        return []
    
    def _get_available_types(self, type_names: List[str]) -> Dict[str, Dict]:
        """获取可用的多态类型定义"""
        if not self.schema_loader or not type_names:
            return {}
        
        result = {}
        # 从 schema_loader 获取 gamefeature_actions 定义
        gamefeature_actions = self.schema_loader.get_gamefeature_actions()
        
        for type_name in type_names:
            if type_name in gamefeature_actions:
                result[type_name] = gamefeature_actions[type_name]
        
        return result
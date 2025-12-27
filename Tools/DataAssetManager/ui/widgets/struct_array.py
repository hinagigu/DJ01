#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 结构体数组控件
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, List, Dict, Callable, Optional
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from ui.widgets.base import PropertyWidget
from ui.widgets.text import TextInputWidget
from ui.widgets.picker import ComboBoxWidget
from core.schema import PropertyDef, StructDef


class StructArrayEditorWidget(PropertyWidget):
    """结构体数组编辑器"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 struct_def: StructDef = None, on_change: Callable = None,
                 options_scanner = None):
        self.struct_def = struct_def
        self.items: List[Dict[str, Any]] = []
        self.options_scanner = options_scanner  # 用于获取下拉选项
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        # 标题栏
        header = ttk.Frame(self.frame)
        header.pack(fill=tk.X, pady=2)
        
        self.count_label = ttk.Label(header, text=f"{self.prop_def.display_name} (0)")
        self.count_label.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(header, text="➕ 添加", 
                   command=self._add_item).pack(side=tk.RIGHT, padx=5)
        
        # 列表容器
        self.list_frame = ttk.Frame(self.frame)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=5)
    
    def _update_count(self):
        self.count_label.config(text=f"{self.prop_def.display_name} ({len(self.items)})")
    
    def _get_root_window(self) -> tk.Tk:
        """获取根窗口"""
        widget = self.frame
        while widget.master:
            widget = widget.master
        return widget
    
    def _center_dialog(self, dialog: tk.Toplevel, width: int = 500, height: int = 400):
        """将对话框居中到父窗口"""
        root = self._get_root_window()
        
        # 更新对话框以获取其实际尺寸
        dialog.update_idletasks()
        
        # 获取父窗口的位置和尺寸
        root_x = root.winfo_x()
        root_y = root.winfo_y()
        root_width = root.winfo_width()
        root_height = root.winfo_height()
        
        # 计算居中位置
        x = root_x + (root_width - width) // 2
        y = root_y + (root_height - height) // 2
        
        dialog.geometry(f"{width}x{height}+{x}+{y}")
    
    def _get_options_for_source(self, source: str) -> List[str]:
        """从选项源获取选项列表"""
        if not self.options_scanner or not source:
            return []
        
        options_map = {
            "input_actions": self.options_scanner.get_input_action_options,
            "input_tags": self.options_scanner.get_input_tags,
            "input_mapping_contexts": self.options_scanner.get_input_mapping_context_options,
            "gameplay_abilities": self.options_scanner.get_gameplay_ability_options,
            "attribute_sets": self.options_scanner.get_attribute_set_options,
            "widget_classes": self.options_scanner.get_widget_class_options,
            "activatable_widgets": self.options_scanner.get_activatable_widget_options,
            "ui_layer_tags": self.options_scanner.get_ui_layer_tag_options,
            "ui_slot_tags": self.options_scanner.get_ui_slot_tag_options,
            "pawn_classes": self.options_scanner.get_pawn_class_options,
            "ability_sets": self.options_scanner.get_ability_set_options,
        }
        
        getter = options_map.get(source)
        if getter:
            items = getter()
            # 返回 name（用于存储）和 display_name（用于显示）的映射
            if isinstance(items, list) and len(items) > 0:
                if isinstance(items[0], dict):
                    return [item.get("name", item.get("display_name", "")) for item in items]
                return items
        return []
    
    def _create_property_widget(self, parent: tk.Widget, prop: PropertyDef) -> PropertyWidget:
        """根据属性定义创建合适的控件"""
        # 如果属性有 options_source 且需要选择框
        if hasattr(prop, 'options_source') and prop.options_source:
            options = self._get_options_for_source(prop.options_source)
            if options:
                return ComboBoxWidget(parent, prop, options)
        
        # 默认使用文本输入
        return TextInputWidget(parent, prop)
    
    def _add_item(self):
        if not self.struct_def:
            return
        
        dialog = tk.Toplevel(self.frame)
        dialog.title(f"添加 {self.struct_def.name}")
        dialog.transient(self._get_root_window())
        dialog.grab_set()
        
        # 居中显示
        self._center_dialog(dialog, 500, 400)
        
        widgets = {}
        for prop_name, prop in self.struct_def.properties.items():
            frame = ttk.Frame(dialog)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            # 根据属性类型创建合适的控件
            widget = self._create_property_widget(frame, prop)
            widget.pack(fill=tk.X)
            widgets[prop_name] = widget
        
        def on_save():
            values = {name: w.get_value() for name, w in widgets.items()}
            self.items.append(values)
            self._refresh_list()
            self._update_count()
            self._notify_change()
            dialog.destroy()
        
        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(fill=tk.X, pady=20)
        ttk.Button(btn_frame, text="保存", command=on_save).pack(side=tk.RIGHT, padx=20)
        ttk.Button(btn_frame, text="取消", 
                   command=dialog.destroy).pack(side=tk.RIGHT, padx=5)
    
    def _edit_item(self, index: int):
        if not self.struct_def or index >= len(self.items):
            return
        
        item_data = self.items[index]
        
        dialog = tk.Toplevel(self.frame)
        dialog.title(f"编辑 {self.struct_def.name}")
        dialog.transient(self._get_root_window())
        dialog.grab_set()
        
        # 居中显示
        self._center_dialog(dialog, 500, 400)
        
        widgets = {}
        for prop_name, prop in self.struct_def.properties.items():
            frame = ttk.Frame(dialog)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            # 根据属性类型创建合适的控件
            widget = self._create_property_widget(frame, prop)
            widget.set_value(item_data.get(prop_name, ""))
            widget.pack(fill=tk.X)
            widgets[prop_name] = widget
        
        def on_save():
            values = {name: w.get_value() for name, w in widgets.items()}
            self.items[index] = values
            self._refresh_list()
            self._notify_change()
            dialog.destroy()
        
        btn_frame = ttk.Frame(dialog)
        btn_frame.pack(fill=tk.X, pady=20)
        ttk.Button(btn_frame, text="保存", command=on_save).pack(side=tk.RIGHT, padx=20)
        ttk.Button(btn_frame, text="取消", 
                   command=dialog.destroy).pack(side=tk.RIGHT, padx=5)
    
    def _remove_item(self, index: int):
        if index < len(self.items):
            self.items.pop(index)
            self._refresh_list()
            self._update_count()
            self._notify_change()
    
    def _refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        for i, item in enumerate(self.items):
            row = ttk.Frame(self.list_frame)
            row.pack(fill=tk.X, pady=1)
            
            # 摘要显示
            summary = ", ".join(f"{k}={v}" for k, v in list(item.items())[:2])
            if len(summary) > 50:
                summary = summary[:47] + "..."
            
            ttk.Label(row, text=f"[{i}] {summary}").pack(side=tk.LEFT, padx=5)
            
            ttk.Button(row, text="✏️", width=3,
                       command=lambda idx=i: self._edit_item(idx)).pack(side=tk.RIGHT, padx=2)
            ttk.Button(row, text="🗑️", width=3,
                       command=lambda idx=i: self._remove_item(idx)).pack(side=tk.RIGHT, padx=2)
    
    def get_value(self) -> List[Dict[str, Any]]:
        return self.items.copy()
    
    def set_value(self, value: Any):
        self.items = list(value) if value else []
        self._refresh_list()
        self._update_count()
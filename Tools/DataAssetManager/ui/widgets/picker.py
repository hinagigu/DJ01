#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 选择器控件
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, List, Dict, Callable
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from ui.widgets.base import PropertyWidget
from core.schema import PropertyDef


class ComboBoxWidget(PropertyWidget):
    """
    下拉选择控件
    
    支持两种选项格式:
    1. 简单字符串列表: ["option1", "option2"]
    2. 字典列表（带 name 和 display_name）: [{"name": "/Script/...", "display_name": "类名 (C++)"}]
    
    当使用字典列表时，显示 display_name，但 get_value() 返回 name
    """
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 options: List[Any] = None, on_change: Callable = None):
        """
        Args:
            options: 可以是字符串列表或字典列表
        """
        self._raw_options = options or []
        self._name_to_display: Dict[str, str] = {}  # name -> display_name
        self._display_to_name: Dict[str, str] = {}  # display_name -> name
        self.options: List[str] = []  # 用于显示的选项列表
        self._process_options()
        super().__init__(parent, prop_def, on_change)
    
    def _process_options(self):
        """处理选项，构建名称映射"""
        self._name_to_display.clear()
        self._display_to_name.clear()
        self.options = []
        
        for opt in self._raw_options:
            if isinstance(opt, dict):
                # 字典格式: {"name": "...", "display_name": "..."}
                name = opt.get("name", "")
                display_name = opt.get("display_name", name)
                if name:
                    self._name_to_display[name] = display_name
                    self._display_to_name[display_name] = name
                    self.options.append(display_name)
            else:
                # 简单字符串
                self.options.append(str(opt))
    
    def _create_widget(self):
        self._create_label().pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        
        # 如果允许空值，添加空选项
        display_options = self.options.copy()
        if self.prop_def.allow_empty and "(无)" not in display_options:
            display_options = ["(无)"] + display_options
        
        self.combo = ttk.Combobox(
            self.frame, 
            textvariable=self.var, 
            values=display_options,
            state='readonly', 
            width=35
        )
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # 设置默认值
        if self.prop_def.default:
            self.set_value(self.prop_def.default)
        elif self.options and not self.prop_def.allow_empty:
            self.var.set(self.options[0])
        elif self.prop_def.allow_empty:
            self.var.set("(无)")
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
        
        # 如果没有选项，显示提示
        if not self.options:
            ttk.Label(self.frame, text="(无可用选项)", 
                      foreground="gray", font=("", 8)).pack(side=tk.LEFT, padx=5)
    
    def set_options(self, options: List[Any]):
        """更新选项列表"""
        self._raw_options = options
        self._process_options()
        
        display_options = self.options.copy()
        if self.prop_def.allow_empty and "(无)" not in display_options:
            display_options = ["(无)"] + display_options
        self.combo['values'] = display_options
    
    def get_value(self) -> str:
        """获取选中的值（返回 name，而非 display_name）"""
        display_val = self.var.get()
        if display_val == "(无)" or not display_val:
            return ""
        # 如果有映射，返回 name；否则直接返回显示值
        return self._display_to_name.get(display_val, display_val)
    
    def set_value(self, value: Any):
        """设置值（可以传入 name 或 display_name）"""
        if not value:
            if self.prop_def.allow_empty:
                self.var.set("(无)")
            return
        
        value_str = str(value)
        
        # 检查是否是 name
        if value_str in self._name_to_display:
            self.var.set(self._name_to_display[value_str])
        # 检查是否已经是 display_name
        elif value_str in self.options:
            self.var.set(value_str)
        elif self.prop_def.allow_empty:
            self.var.set("(无)")


class TagSelectorWidget(PropertyWidget):
    """Gameplay 标签选择器"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_tags: List[str] = None, on_change: Callable = None):
        self.available_tags = available_tags or []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        self._create_label().pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        filtered = self._filter_tags()
        
        self.combo = ttk.Combobox(self.frame, textvariable=self.var, 
                                   values=filtered, width=40)
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
        self.combo.bind('<KeyRelease>', self._on_key_release)
    
    def _filter_tags(self) -> List[str]:
        if not self.prop_def.categories:
            return self.available_tags
        prefix = self.prop_def.categories
        return [t for t in self.available_tags if t.startswith(prefix)]
    
    def _on_key_release(self, event):
        typed = self.var.get().lower()
        if typed:
            filtered = [t for t in self._filter_tags() if typed in t.lower()]
            self.combo['values'] = filtered
        else:
            self.combo['values'] = self._filter_tags()
    
    def set_available_tags(self, tags: List[str]):
        self.available_tags = tags
        self.combo['values'] = self._filter_tags()
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(str(value) if value else "")


class AssetPickerWidget(PropertyWidget):
    """资产选择器"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_assets: List[str] = None, on_change: Callable = None):
        self.available_assets = available_assets or []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        self._create_label().pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        self.combo = ttk.Combobox(
            self.frame, 
            textvariable=self.var,
            values=self.available_assets, 
            width=40
        )
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        ttk.Button(self.frame, text="...", width=3, 
                   command=self._browse).pack(side=tk.LEFT, padx=2)
        ttk.Button(self.frame, text="✕", width=3,
                   command=self._clear).pack(side=tk.LEFT, padx=2)
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
    
    def _browse(self):
        """显示选择对话框"""
        if not self.available_assets:
            return
        
        dialog = tk.Toplevel(self.frame)
        dialog.title(f"选择 {self.prop_def.display_name}")
        dialog.geometry("400x300")
        dialog.transient(self.frame)
        dialog.grab_set()
        
        # 搜索
        search_var = tk.StringVar()
        ttk.Entry(dialog, textvariable=search_var).pack(fill=tk.X, padx=10, pady=5)
        
        # 列表
        listbox = tk.Listbox(dialog, selectmode=tk.SINGLE)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        for asset in self.available_assets:
            listbox.insert(tk.END, asset)
        
        def filter_list(*args):
            search = search_var.get().lower()
            listbox.delete(0, tk.END)
            for asset in self.available_assets:
                if search in asset.lower():
                    listbox.insert(tk.END, asset)
        
        search_var.trace_add('write', filter_list)
        
        def on_select():
            sel = listbox.curselection()
            if sel:
                self.var.set(listbox.get(sel[0]))
                self._notify_change()
            dialog.destroy()
        
        ttk.Button(dialog, text="选择", command=on_select).pack(pady=10)
    
    def _clear(self):
        self.var.set("")
        self._notify_change()
    
    def set_available_assets(self, assets: List[str]):
        self.available_assets = assets
        self.combo['values'] = assets
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(str(value) if value else "")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 选择器控件
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, List, Callable
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from ui.widgets.base import PropertyWidget
from core.schema import PropertyDef


class ComboBoxWidget(PropertyWidget):
    """下拉选择控件"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 options: List[str] = None, on_change: Callable = None):
        self.options = options or []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        self._create_label().pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        
        # 如果允许空值，添加空选项
        display_options = self.options.copy()
        if self.prop_def.allow_empty and "" not in display_options:
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
        if self.prop_def.default and self.prop_def.default in self.options:
            self.var.set(self.prop_def.default)
        elif self.options and not self.prop_def.allow_empty:
            self.var.set(self.options[0])
        elif self.prop_def.allow_empty:
            self.var.set("(无)")
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
        
        # 如果没有选项，显示提示
        if not self.options:
            ttk.Label(self.frame, text="(无可用选项)", 
                      foreground="gray", font=("", 8)).pack(side=tk.LEFT, padx=5)
    
    def set_options(self, options: List[str]):
        self.options = options
        display_options = options.copy()
        if self.prop_def.allow_empty and "(无)" not in display_options:
            display_options = ["(无)"] + display_options
        self.combo['values'] = display_options
    
    def get_value(self) -> str:
        val = self.var.get()
        return "" if val == "(无)" else val
    
    def set_value(self, value: Any):
        if value and str(value) in self.options:
            self.var.set(str(value))
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
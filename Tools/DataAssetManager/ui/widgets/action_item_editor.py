#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - Action 项编辑器辅助类
包含嵌套数组和字段的编辑逻辑
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, List, Dict, Callable, Optional

from ui.widgets.action_schema import ACTION_PROPERTIES


class ActionEditorMixin:
    """
    Action 编辑器混入类
    提供嵌套数组/字段编辑的共用方法
    """
    
    # === 嵌套数组编辑 ===
    
    def _create_nested_array_editor(self, parent: ttk.Widget, action_index: int,
                                    prop_name: str, arr_idx: int, arr_item: Dict,
                                    field_name: str, field_def: Dict):
        """创建嵌套数组编辑器"""
        nested_frame = ttk.Frame(parent)
        nested_frame.pack(fill=tk.X, expand=True)
        nested_frame.columnconfigure(0, weight=1)
        
        current_list = arr_item.get(field_name, [])
        nested_item_schema = field_def.get("item_schema", {})
        nested_options_source = field_def.get("options_source")
        
        # 头部
        header = ttk.Frame(nested_frame)
        header.pack(fill=tk.X)
        
        ttk.Label(header, text=f"共 {len(current_list)} 项", foreground="gray").pack(side=tk.LEFT)
        
        ttk.Button(header, text="➕", width=3,
                  command=lambda: self._add_nested_array_item(
                      action_index, prop_name, arr_idx, field_name, field_def
                  )).pack(side=tk.RIGHT)
        
        # 列表项容器
        list_frame = ttk.Frame(nested_frame)
        list_frame.pack(fill=tk.X, pady=2)
        
        if not current_list:
            ttk.Label(list_frame, text="(空列表，点击 ➕ 添加)", 
                     foreground="gray", font=("", 8)).pack(anchor=tk.W, padx=10)
            return
        
        # 确定嵌套项的类型
        if nested_item_schema and len(nested_item_schema) == 1:
            self._render_single_field_nested_items(
                list_frame, action_index, prop_name, arr_idx, 
                field_name, current_list, nested_item_schema
            )
        else:
            self._render_simple_nested_items(
                list_frame, action_index, prop_name, arr_idx,
                field_name, current_list, nested_options_source
            )
    
    def _render_single_field_nested_items(self, list_frame: ttk.Frame, action_index: int,
                                           prop_name: str, arr_idx: int, field_name: str,
                                           current_list: List, nested_item_schema: Dict):
        """渲染单字段结构体的嵌套列表"""
        field_key = list(nested_item_schema.keys())[0]
        field_opts = nested_item_schema[field_key].get("options_source")
        options = self._get_options(field_opts)
        
        for ni, nested_item in enumerate(current_list):
            item_row = ttk.Frame(list_frame)
            item_row.pack(fill=tk.X, pady=2)
            item_row.columnconfigure(1, weight=1)
            
            ttk.Label(item_row, text=f"[{ni}]", width=4).pack(side=tk.LEFT)
            
            combo = ttk.Combobox(item_row, values=options, width=40)
            val = nested_item.get(field_key, "") if isinstance(nested_item, dict) else str(nested_item)
            display_val = self._path_to_display(val, field_opts) if val else ""
            combo.set(display_val)
            combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
            combo.bind("<<ComboboxSelected>>",
                      lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, ni2=ni, fk=field_key, os=field_opts:
                      self._on_double_nested_change(ai, pn, ai2, fn, ni2, fk, e.widget.get(), os))
            combo.bind("<FocusOut>",
                      lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, ni2=ni, fk=field_key, os=field_opts:
                      self._on_double_nested_change(ai, pn, ai2, fn, ni2, fk, e.widget.get(), os))
            
            ttk.Button(item_row, text="✕", width=3,
                      command=lambda ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, ni2=ni:
                      self._remove_nested_array_item(ai, pn, ai2, fn, ni2)).pack(side=tk.RIGHT, padx=2)
    
    def _render_simple_nested_items(self, list_frame: ttk.Frame, action_index: int,
                                     prop_name: str, arr_idx: int, field_name: str,
                                     current_list: List, nested_options_source: Optional[str]):
        """渲染简单类型的嵌套列表"""
        options = self._get_options(nested_options_source)
        
        for ni, nested_item in enumerate(current_list):
            item_row = ttk.Frame(list_frame)
            item_row.pack(fill=tk.X, pady=2)
            item_row.columnconfigure(1, weight=1)
            
            ttk.Label(item_row, text=f"[{ni}]", width=4).pack(side=tk.LEFT)
            
            if options:
                combo = ttk.Combobox(item_row, values=options, width=40)
                display_val = self._path_to_display(str(nested_item), nested_options_source) if nested_item else ""
                combo.set(display_val)
                combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
                combo.bind("<<ComboboxSelected>>",
                          lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, ni2=ni, os=nested_options_source:
                          self._on_nested_list_item_change(ai, pn, ai2, fn, ni2, e.widget.get(), os))
                combo.bind("<FocusOut>",
                          lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, ni2=ni, os=nested_options_source:
                          self._on_nested_list_item_change(ai, pn, ai2, fn, ni2, e.widget.get(), os))
            else:
                entry = ttk.Entry(item_row, width=50)
                entry.insert(0, str(nested_item) if nested_item else "")
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
            
            ttk.Button(item_row, text="✕", width=3,
                      command=lambda ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, ni2=ni:
                      self._remove_nested_array_item(ai, pn, ai2, fn, ni2)).pack(side=tk.RIGHT, padx=2)
    
    # === 嵌套字段编辑 ===
    
    def _create_nested_field_editor_grid(self, parent: ttk.Widget, row: int, action_index: int,
                                          prop_name: str, arr_idx: int, arr_item: Dict,
                                          field_name: str, field_def: Dict):
        """创建嵌套字段编辑器（grid 布局）"""
        field_type = field_def.get("type", "string")
        display_name = field_def.get("display_name", field_name)
        options_source = field_def.get("options_source")
        current_value = arr_item.get(field_name, "")
        
        # 标签列
        ttk.Label(parent, text=f"{display_name}:", anchor=tk.W).grid(
            row=row, column=0, sticky="nw", padx=(0, 15), pady=5)
        
        # 值区域
        value_frame = ttk.Frame(parent)
        value_frame.grid(row=row, column=1, sticky="ew", pady=5)
        value_frame.columnconfigure(0, weight=1)
        
        if field_type == "array":
            self._create_nested_array_editor(
                value_frame, action_index, prop_name, arr_idx, arr_item, field_name, field_def
            )
        elif options_source or field_type in ("class", "asset", "tag"):
            options = self._get_options(options_source)
            combo = ttk.Combobox(value_frame, values=options, width=50)
            display_value = self._path_to_display(str(current_value), options_source) if current_value else ""
            combo.set(display_value)
            combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
            combo.bind("<<ComboboxSelected>>",
                      lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, os=options_source:
                      self._on_nested_field_change(ai, pn, ai2, fn, e.widget.get(), os))
            combo.bind("<FocusOut>",
                      lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name, os=options_source:
                      self._on_nested_field_change(ai, pn, ai2, fn, e.widget.get(), os))
        elif field_type == "integer":
            spin = ttk.Spinbox(value_frame, from_=-9999, to=9999, width=10)
            spin.set(current_value if current_value else 0)
            spin.pack(side=tk.LEFT)
            spin.bind("<FocusOut>",
                     lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name:
                     self._on_nested_field_change(ai, pn, ai2, fn, int(e.widget.get() or 0)))
        else:
            entry = ttk.Entry(value_frame, width=55)
            entry.insert(0, str(current_value) if current_value else "")
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            entry.bind("<FocusOut>",
                      lambda e, ai=action_index, pn=prop_name, ai2=arr_idx, fn=field_name:
                      self._on_nested_field_change(ai, pn, ai2, fn, e.widget.get()))
    
    # === 回调方法 ===
    
    def _on_nested_field_change(self, action_index: int, prop_name: str, 
                                arr_idx: int, field_name: str, value: Any,
                                options_source: Optional[str] = None):
        """嵌套字段变化回调"""
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_idx < len(arr):
                if not isinstance(arr[arr_idx], dict):
                    arr[arr_idx] = {}
                if options_source:
                    value = self._display_to_path(value, options_source)
                arr[arr_idx][field_name] = value
                self.items[action_index][prop_name] = arr
                self._notify_change()
    
    def _on_double_nested_change(self, action_index: int, prop_name: str,
                                 arr_idx: int, field_name: str, nested_idx: int,
                                 nested_field: str, value: Any,
                                 options_source: Optional[str] = None):
        """双重嵌套字段变化回调"""
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_idx < len(arr):
                if not isinstance(arr[arr_idx], dict):
                    arr[arr_idx] = {}
                nested_arr = arr[arr_idx].get(field_name, [])
                if nested_idx < len(nested_arr):
                    if not isinstance(nested_arr[nested_idx], dict):
                        nested_arr[nested_idx] = {}
                    if options_source:
                        value = self._display_to_path(value, options_source)
                    nested_arr[nested_idx][nested_field] = value
                    arr[arr_idx][field_name] = nested_arr
                    self.items[action_index][prop_name] = arr
                    self._notify_change()
    
    def _on_nested_list_item_change(self, action_index: int, prop_name: str,
                                    arr_idx: int, field_name: str, nested_idx: int, value: Any,
                                    options_source: Optional[str] = None):
        """嵌套列表项变化回调"""
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_idx < len(arr):
                if not isinstance(arr[arr_idx], dict):
                    arr[arr_idx] = {}
                nested_arr = arr[arr_idx].get(field_name, [])
                if nested_idx < len(nested_arr):
                    if options_source:
                        value = self._display_to_path(value, options_source)
                    nested_arr[nested_idx] = value
                    arr[arr_idx][field_name] = nested_arr
                    self.items[action_index][prop_name] = arr
                    self._notify_change()
    
    def _add_nested_array_item(self, action_index: int, prop_name: str,
                               arr_idx: int, field_name: str, field_def: Dict):
        """添加嵌套数组项"""
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_idx < len(arr):
                if not isinstance(arr[arr_idx], dict):
                    arr[arr_idx] = {}
                nested_arr = arr[arr_idx].get(field_name, [])
                
                nested_schema = field_def.get("item_schema", {})
                if nested_schema:
                    new_item = {k: "" for k in nested_schema.keys()}
                else:
                    new_item = ""
                
                nested_arr.append(new_item)
                arr[arr_idx][field_name] = nested_arr
                self.items[action_index][prop_name] = arr
                self._refresh_list()
                self._notify_change()
    
    def _remove_nested_array_item(self, action_index: int, prop_name: str,
                                  arr_idx: int, field_name: str, nested_idx: int):
        """删除嵌套数组项"""
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_idx < len(arr) and isinstance(arr[arr_idx], dict):
                nested_arr = arr[arr_idx].get(field_name, [])
                if nested_idx < len(nested_arr):
                    nested_arr.pop(nested_idx)
                    arr[arr_idx][field_name] = nested_arr
                    self.items[action_index][prop_name] = arr
                    self._refresh_list()
                    self._notify_change()
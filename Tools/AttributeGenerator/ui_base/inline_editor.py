#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 内联编辑器组件
可复用的 Treeview 内联编辑功能
"""

import tkinter as tk
from tkinter import ttk


class InlineEditorMixin:
    """内联编辑器 Mixin，为 UI 类提供内联编辑功能"""
    
    def _init_inline_editor(self):
        """初始化内联编辑器状态"""
        self._active_editor = None
    
    def _destroy_active_editor(self):
        """销毁当前活动的内联编辑器"""
        if self._active_editor is not None:
            try:
                self._active_editor.destroy()
            except:
                pass
            self._active_editor = None
    
    def _create_inline_combo(self, tree, item, column, x, y, w, h, 
                              data_dict, key, values, refresh_callback):
        """
        在表格单元格位置创建内联下拉框
        
        Args:
            tree: Treeview 组件
            item: 行 ID
            column: 列 ID
            x, y, w, h: 单元格位置和大小
            data_dict: 数据字典
            key: 要修改的键
            values: 下拉选项列表
            refresh_callback: 刷新回调函数 (tree, item, data_dict) -> None
        """
        self._destroy_active_editor()
        
        combo = ttk.Combobox(tree, values=values, width=max(10, w // 8))
        combo.set(data_dict.get(key, ''))
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        
        def do_save():
            if self._active_editor != combo:
                return
            data_dict[key] = combo.get()
            refresh_callback(tree, item, data_dict)
            self._destroy_active_editor()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        combo.bind('<<ComboboxSelected>>', lambda e: do_save())
        combo.bind('<Return>', lambda e: do_save())
        combo.bind('<Escape>', on_escape)
        
        # 聚焦并展开
        combo.focus_set()
        combo.after(50, lambda: combo.tk.call('ttk::combobox::Post', combo) if self._active_editor == combo else None)
    
    def _create_inline_combo_with_sync(self, tree, item, column, x, y, w, h,
                                        data_dict, key, values, sync_key, sync_values_func,
                                        refresh_callback):
        """
        创建内联下拉框，并在选择后同步更新另一个字段
        
        Args:
            sync_key: 要同步更新的键
            sync_values_func: 获取同步值列表的函数 (new_value) -> list
        """
        self._destroy_active_editor()
        
        combo = ttk.Combobox(tree, values=values, width=max(10, w // 8))
        combo.set(data_dict.get(key, ''))
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        
        def do_save():
            if self._active_editor != combo:
                return
            new_value = combo.get()
            old_value = data_dict.get(key, '')
            
            if new_value != old_value:
                data_dict[key] = new_value
                # 同步更新关联字段
                sync_values = sync_values_func(new_value)
                if sync_values:
                    data_dict[sync_key] = sync_values[0]
                else:
                    data_dict[sync_key] = ''
            
            refresh_callback(tree, item, data_dict)
            self._destroy_active_editor()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        combo.bind('<<ComboboxSelected>>', lambda e: do_save())
        combo.bind('<Return>', lambda e: do_save())
        combo.bind('<Escape>', on_escape)
        
        # 聚焦并展开
        combo.focus_set()
        combo.after(50, lambda: combo.tk.call('ttk::combobox::Post', combo) if self._active_editor == combo else None)
    
    def _create_inline_entry(self, tree, item, column, x, y, w, h,
                              data_dict, key, refresh_callback, value_type=str):
        """
        在表格单元格位置创建内联输入框
        
        Args:
            value_type: 值类型 (str, int, float)
        """
        self._destroy_active_editor()
        
        entry = ttk.Entry(tree, width=max(5, w // 8))
        current_val = data_dict.get(key, 0 if value_type in (int, float) else '')
        entry.insert(0, str(current_val))
        entry.place(x=x, y=y, width=w, height=h)
        entry.select_range(0, tk.END)
        self._active_editor = entry
        
        def on_confirm(event=None):
            if self._active_editor != entry:
                return
            try:
                new_value = value_type(entry.get())
            except ValueError:
                new_value = 0 if value_type in (int, float) else ''
            data_dict[key] = new_value
            refresh_callback(tree, item, data_dict)
            self._destroy_active_editor()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        entry.bind('<Return>', on_confirm)
        entry.bind('<Escape>', on_escape)
        
        entry.focus_set()
    
    def _get_cell_info(self, tree, event):
        """
        获取双击位置的单元格信息
        
        Returns:
            (item, column, col_idx, bbox) 或 None
        """
        region = tree.identify_region(event.x, event.y)
        if region != 'cell':
            return None
        
        item = tree.identify_row(event.y)
        column = tree.identify_column(event.x)
        if not item or not column:
            return None
        
        col_idx = int(column[1:]) - 1  # '#1' -> 0
        bbox = tree.bbox(item, column)
        if not bbox:
            return None
        
        return item, column, col_idx, bbox
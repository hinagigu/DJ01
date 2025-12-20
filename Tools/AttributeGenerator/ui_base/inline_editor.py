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
        self._editor_ready = False  # 编辑器就绪标志
        self._pending_click = None
        self._editor_ready = False  # 编辑器就绪标志
        self._pending_click = None
    
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
        获取点击位置的单元格信息
        
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

    def _setup_single_click_editing(self, tree, column_handlers, refresh_callback):
        """
        为 Treeview 设置单击编辑功能
        
        Args:
            tree: Treeview 组件
            column_handlers: 列处理器字典 {col_idx: handler_config}
                handler_config: {
                    'type': 'entry' | 'combo',
                    'key': 数据键名,
                    'values': 下拉选项列表 (仅 combo 类型),
                    'value_type': 值类型 (仅 entry 类型, 默认 str)
                }
            refresh_callback: 刷新回调函数 (idx, data) -> None
        """
        self._column_handlers = column_handlers
        self._click_refresh_callback = refresh_callback
        self._pending_click = None
        
        def on_single_click(event):
            # 取消之前的延迟点击
            if self._pending_click:
                tree.after_cancel(self._pending_click)
                self._pending_click = None
            
            # 延迟 150ms 区分单击和双击
            self._pending_click = tree.after(150, lambda: self._handle_single_click(tree, event))
        
        def on_double_click(event):
            # 取消单击处理
            if self._pending_click:
                tree.after_cancel(self._pending_click)
                self._pending_click = None
        
        tree.bind('<Button-1>', on_single_click)
        tree.bind('<Double-1>', on_double_click)
    
    def _handle_single_click(self, tree, event):
        """处理单击编辑事件"""
        self._pending_click = None
        
        cell_info = self._get_cell_info(tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        
        if col_idx not in self._column_handlers:
            return
        
        handler = self._column_handlers[col_idx]
        x, y, w, h = bbox
        
        # 获取当前行索引和数据
        try:
            idx = int(item)
        except ValueError:
            return
        
        # 先选中行
        tree.selection_set(item)
        tree.focus(item)
        
        # 创建编辑器
        if handler['type'] == 'entry':
            self._create_single_click_entry(tree, item, column, x, y, w, h,
                                            idx, handler['key'], 
                                            handler.get('value_type', str))
        elif handler['type'] == 'combo':
            self._create_single_click_combo(tree, item, column, x, y, w, h,
                                            idx, handler['key'], handler['values'])
    
    def _create_single_click_entry(self, tree, item, column, x, y, w, h,
                                    idx, key, value_type=str):
        """创建单击编辑的输入框"""
        self._destroy_active_editor()
        
        # 获取当前值
        current_val = self._get_attribute_value(idx, key)
        
        entry = ttk.Entry(tree, width=max(5, w // 8))
        entry.insert(0, str(current_val) if current_val is not None else '')
        entry.place(x=x, y=y, width=w, height=h)
        entry.select_range(0, tk.END)
        self._active_editor = entry
        self._editor_ready = False  # 标记编辑器尚未就绪
        
        def on_confirm(event=None):
            if self._active_editor != entry:
                return
            try:
                new_value = value_type(entry.get())
            except ValueError:
                new_value = 0 if value_type in (int, float) else ''
            
            self._set_attribute_value(idx, key, new_value)
            self._click_refresh_callback(idx)
            self._destroy_active_editor()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        def on_focus_out(event):
            # 只有就绪后才响应 FocusOut
            if self._editor_ready and self._active_editor == entry:
                tree.after(50, on_confirm)
        
        entry.bind('<Return>', on_confirm)
        entry.bind('<Escape>', on_escape)
        entry.bind('<FocusOut>', on_focus_out)
        
        entry.focus_set()
        # 延迟标记就绪
        entry.after(200, lambda: setattr(self, '_editor_ready', True))
    
    def _create_single_click_combo(self, tree, item, column, x, y, w, h,
                                    idx, key, values):
        """创建单击编辑的下拉框"""
        self._destroy_active_editor()
        
        # 获取当前值
        current_val = self._get_attribute_value(idx, key)
        
        combo = ttk.Combobox(tree, values=values, width=max(10, w // 8))
        combo.set(current_val if current_val else '')
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        self._editor_ready = False  # 标记编辑器尚未就绪
        
        def do_save():
            if self._active_editor != combo:
                return
            new_value = combo.get()
            self._set_attribute_value(idx, key, new_value)
            self._click_refresh_callback(idx)
            self._destroy_active_editor()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        def on_focus_out(event):
            # 只有就绪后才响应 FocusOut
            if self._editor_ready and self._active_editor == combo:
                tree.after(50, do_save)
        
        combo.bind('<<ComboboxSelected>>', lambda e: do_save())
        combo.bind('<Return>', lambda e: do_save())
        combo.bind('<Escape>', on_escape)
        combo.bind('<FocusOut>', on_focus_out)
        
        # 聚焦并展开
        combo.focus_set()
        
        def post_and_ready():
            if self._active_editor == combo:
                try:
                    combo.tk.call('ttk::combobox::Post', combo)
                except:
                    pass
                # 延迟标记就绪
                combo.after(150, lambda: setattr(self, '_editor_ready', True))
        
        combo.after(80, post_and_ready)
    
    def _get_attribute_value(self, idx, key):
        """获取属性值 - 子类需要覆写"""
        raise NotImplementedError("子类需要实现 _get_attribute_value")
    
    def _set_attribute_value(self, idx, key, value):
        """设置属性值 - 子类需要覆写"""
        raise NotImplementedError("子类需要实现 _set_attribute_value")
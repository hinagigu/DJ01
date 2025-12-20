#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 可复用 UI 组件
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Tuple, Optional, Any


class GroupListWidget:
    """
    左侧分组列表组件
    
    用于显示分组（如属性集、标签分类、Execution 列表）
    支持选择、添加、删除操作
    """
    
    def __init__(
        self,
        parent,
        title: str = "分组",
        on_select: Callable[[int, str], None] = None,
        on_add: Callable[[], None] = None,
        on_delete: Callable[[int, str], None] = None,
        show_count: bool = True,
        width: int = 150
    ):
        """
        初始化分组列表组件
        
        Args:
            parent: 父级容器
            title: 标题
            on_select: 选择回调 (index, value) -> None
            on_add: 添加按钮回调
            on_delete: 删除按钮回调 (index, value) -> None
            show_count: 是否在项目后显示数量
            width: 组件宽度
        """
        self.on_select = on_select
        self.on_add = on_add
        self.on_delete = on_delete
        self.show_count = show_count
        self._items = []  # 原始数据
        self._counts = {}  # 项目计数
        
        # 创建 UI
        self.frame = ttk.LabelFrame(parent, text=title, width=width)
        
        # 列表
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.listbox = tk.Listbox(list_frame, exportselection=False)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        self.listbox.bind('<<ListboxSelect>>', self._on_select)
        
        # 按钮栏
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        
        self.add_btn = ttk.Button(btn_frame, text="+ 新建", width=8, command=self._on_add)
        self.add_btn.pack(side=tk.LEFT, padx=(0, 5))
        
        self.delete_btn = ttk.Button(btn_frame, text="- 删除", width=8, command=self._on_delete)
        self.delete_btn.pack(side=tk.LEFT)
    
    def _on_select(self, event):
        """内部选择事件"""
        if self.on_select:
            selection = self.listbox.curselection()
            if selection:
                idx = selection[0]
                value = self._items[idx] if idx < len(self._items) else None
                self.on_select(idx, value)
    
    def _on_add(self):
        """内部添加事件"""
        if self.on_add:
            self.on_add()
    
    def _on_delete(self):
        """内部删除事件"""
        if self.on_delete:
            selection = self.listbox.curselection()
            if selection:
                idx = selection[0]
                value = self._items[idx] if idx < len(self._items) else None
                self.on_delete(idx, value)
    
    def refresh(self, items: List[str], counts: dict = None):
        """
        刷新列表
        
        Args:
            items: 项目列表
            counts: 项目计数字典 {name: count}
        """
        self._items = list(items)
        self._counts = counts or {}
        
        self.listbox.delete(0, tk.END)
        for item in self._items:
            display = item
            if self.show_count and item in self._counts:
                display = f"{item} ({self._counts[item]})"
            self.listbox.insert(tk.END, display)
    
    def get_selection(self) -> Tuple[Optional[int], Optional[str]]:
        """
        获取当前选中项
        
        Returns:
            (index, value) 或 (None, None)
        """
        selection = self.listbox.curselection()
        if selection:
            idx = selection[0]
            return idx, self._items[idx] if idx < len(self._items) else None
        return None, None
    
    def select(self, index: int):
        """选中指定索引"""
        self.listbox.selection_clear(0, tk.END)
        if 0 <= index < self.listbox.size():
            self.listbox.selection_set(index)
            self.listbox.see(index)
            self.listbox.event_generate('<<ListboxSelect>>')
    
    def select_by_value(self, value: str):
        """根据值选中"""
        if value in self._items:
            self.select(self._items.index(value))
    
    def pack(self, **kwargs):
        """pack 布局"""
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        """grid 布局"""
        self.frame.grid(**kwargs)


class ItemTreeWidget:
    """
    中间项目表格组件
    
    基于 Treeview 的表格，支持多列显示和双击编辑
    """
    
    def __init__(
        self,
        parent,
        columns: List[Tuple[str, int]],
        title: str = "项目",
        on_select: Callable[[str, dict], None] = None,
        on_double_click: Callable[[str, str, Any], None] = None,
        show_buttons: bool = True,
        on_add: Callable[[], None] = None,
        on_delete: Callable[[str], None] = None
    ):
        """
        初始化项目表格组件
        
        Args:
            parent: 父级容器
            columns: 列配置 [(列名, 宽度), ...]
            title: 标题
            on_select: 选择回调 (item_id, values_dict) -> None
            on_double_click: 双击回调 (item_id, column, current_value) -> None
            show_buttons: 是否显示添加/删除按钮
            on_add: 添加回调
            on_delete: 删除回调 (item_id) -> None
        """
        self.on_select = on_select
        self.on_double_click = on_double_click
        self.on_add = on_add
        self.on_delete = on_delete
        self._columns = [col[0] for col in columns]
        
        # 创建 UI
        self.frame = ttk.LabelFrame(parent, text=title)
        
        # 表格
        tree_frame = ttk.Frame(self.frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.tree = ttk.Treeview(tree_frame, columns=self._columns, show='headings')
        
        for col_name, col_width in columns:
            self.tree.heading(col_name, text=col_name)
            self.tree.column(col_name, width=col_width, minwidth=50)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)
        
        self.tree.bind('<<TreeviewSelect>>', self._on_select)
        self.tree.bind('<Double-1>', self._on_double_click)
        
        # 按钮栏
        if show_buttons:
            btn_frame = ttk.Frame(self.frame)
            btn_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
            
            self.add_btn = ttk.Button(btn_frame, text="+ 添加", width=8, command=self._on_add)
            self.add_btn.pack(side=tk.LEFT, padx=(0, 5))
            
            self.delete_btn = ttk.Button(btn_frame, text="- 删除", width=8, command=self._on_delete)
            self.delete_btn.pack(side=tk.LEFT)
    
    def _on_select(self, event):
        """内部选择事件"""
        if self.on_select:
            selection = self.tree.selection()
            if selection:
                item = selection[0]
                values = {col: self.tree.set(item, col) for col in self._columns}
                self.on_select(item, values)
    
    def _on_double_click(self, event):
        """内部双击事件"""
        if self.on_double_click:
            region = self.tree.identify('region', event.x, event.y)
            if region == 'cell':
                item = self.tree.identify_row(event.y)
                column = self.tree.identify_column(event.x)
                col_idx = int(column[1:]) - 1
                if 0 <= col_idx < len(self._columns):
                    col_name = self._columns[col_idx]
                    current_value = self.tree.set(item, col_name)
                    self.on_double_click(item, col_name, current_value)
    
    def _on_add(self):
        if self.on_add:
            self.on_add()
    
    def _on_delete(self):
        if self.on_delete:
            selection = self.tree.selection()
            if selection:
                self.on_delete(selection[0])
    
    def refresh(self, items: List[dict]):
        """
        刷新表格
        
        Args:
            items: 数据列表 [{"col1": val1, "col2": val2, ...}, ...]
        """
        self.tree.delete(*self.tree.get_children())
        for item_data in items:
            values = [item_data.get(col, "") for col in self._columns]
            self.tree.insert('', tk.END, values=values)
    
    def add_item(self, item_data: dict) -> str:
        """
        添加单个项目
        
        Returns:
            新项目的 ID
        """
        values = [item_data.get(col, "") for col in self._columns]
        return self.tree.insert('', tk.END, values=values)
    
    def update_item(self, item_id: str, item_data: dict):
        """更新指定项目"""
        for col, val in item_data.items():
            if col in self._columns:
                self.tree.set(item_id, col, val)
    
    def delete_item(self, item_id: str):
        """删除指定项目"""
        self.tree.delete(item_id)
    
    def get_selection(self) -> Tuple[Optional[str], Optional[dict]]:
        """获取当前选中项"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            values = {col: self.tree.set(item, col) for col in self._columns}
            return item, values
        return None, None
    
    def select(self, item_id: str):
        """选中指定项目"""
        self.tree.selection_set(item_id)
        self.tree.see(item_id)
    
    def get_all_items(self) -> List[Tuple[str, dict]]:
        """获取所有项目"""
        result = []
        for item in self.tree.get_children():
            values = {col: self.tree.set(item, col) for col in self._columns}
            result.append((item, values))
        return result
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)


class BottomButtonBar:
    """
    底部按钮栏组件
    
    用于放置保存、生成代码等操作按钮
    """
    
    def __init__(
        self,
        parent,
        buttons: List[Tuple[str, Callable, Optional[str]]] = None
    ):
        """
        初始化底部按钮栏
        
        Args:
            parent: 父级容器
            buttons: 按钮配置 [(文字, 回调, 样式), ...]
                     样式可选: None(默认), "primary", "danger"
        """
        self.frame = ttk.Frame(parent)
        self.buttons = {}
        
        if buttons:
            for btn_config in buttons:
                text = btn_config[0]
                command = btn_config[1]
                style = btn_config[2] if len(btn_config) > 2 else None
                
                btn = ttk.Button(self.frame, text=text, command=command)
                btn.pack(side=tk.LEFT, padx=5)
                self.buttons[text] = btn
    
    def add_button(self, text: str, command: Callable, side: str = tk.LEFT):
        """动态添加按钮"""
        btn = ttk.Button(self.frame, text=text, command=command)
        btn.pack(side=side, padx=5)
        self.buttons[text] = btn
        return btn
    
    def set_button_state(self, text: str, state: str):
        """设置按钮状态"""
        if text in self.buttons:
            self.buttons[text].config(state=state)
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
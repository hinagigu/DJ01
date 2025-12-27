#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 列表控件
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Any, List, Callable
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from ui.widgets.base import PropertyWidget
from core.schema import PropertyDef


class StringListWidget(PropertyWidget):
    """字符串列表编辑器"""
    
    def _create_widget(self):
        self.items: List[str] = []
        
        self._create_label().pack(anchor=tk.W, padx=5)
        
        # 列表框
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        self.listbox = tk.Listbox(list_frame, height=4)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, 
                                  command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # 输入和按钮
        input_frame = ttk.Frame(self.frame)
        input_frame.pack(fill=tk.X, padx=5, pady=2)
        
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_var)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        ttk.Button(input_frame, text="➕", width=3, 
                   command=self._add_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(input_frame, text="➖", width=3, 
                   command=self._remove_item).pack(side=tk.LEFT, padx=2)
        
        self.input_entry.bind('<Return>', lambda e: self._add_item())
    
    def _add_item(self):
        item = self.input_var.get().strip()
        if item and item not in self.items:
            self.items.append(item)
            self.listbox.insert(tk.END, item)
            self.input_var.set("")
            self._notify_change()
    
    def _remove_item(self):
        sel = self.listbox.curselection()
        if sel:
            self.items.pop(sel[0])
            self.listbox.delete(sel[0])
            self._notify_change()
    
    def get_value(self) -> List[str]:
        return self.items.copy()
    
    def set_value(self, value: Any):
        self.items = list(value) if value else []
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)


class AssetPickerListWidget(PropertyWidget):
    """资产列表选择器（多选）"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_assets: List[str] = None, on_change: Callable = None):
        self.available_assets = available_assets or []
        self.selected_assets: List[str] = []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        self._create_label().pack(anchor=tk.W, padx=5)
        
        # 列表
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        self.listbox = tk.Listbox(list_frame, height=4, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, 
                                  command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # 按钮
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=2)
        
        ttk.Button(btn_frame, text="➕ 添加", 
                   command=self._add_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="➖ 移除", 
                   command=self._remove_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="⬆", width=3, 
                   command=self._move_up).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="⬇", width=3, 
                   command=self._move_down).pack(side=tk.LEFT, padx=2)
    
    def _add_item(self):
        available = [a for a in self.available_assets if a not in self.selected_assets]
        if not available:
            messagebox.showinfo("提示", "没有更多可添加的资产")
            return
        
        dialog = tk.Toplevel(self.frame)
        dialog.title("添加资产")
        dialog.geometry("400x300")
        dialog.transient(self.frame)
        dialog.grab_set()
        
        listbox = tk.Listbox(dialog, selectmode=tk.EXTENDED)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for asset in available:
            listbox.insert(tk.END, asset)
        
        def on_add():
            for idx in listbox.curselection():
                asset = listbox.get(idx)
                if asset not in self.selected_assets:
                    self.selected_assets.append(asset)
                    self.listbox.insert(tk.END, asset)
            self._notify_change()
            dialog.destroy()
        
        ttk.Button(dialog, text="添加", command=on_add).pack(pady=10)
    
    def _remove_item(self):
        sel = self.listbox.curselection()
        if sel:
            self.selected_assets.pop(sel[0])
            self.listbox.delete(sel[0])
            self._notify_change()
    
    def _move_up(self):
        sel = self.listbox.curselection()
        if sel and sel[0] > 0:
            idx = sel[0]
            self.selected_assets[idx-1], self.selected_assets[idx] = \
                self.selected_assets[idx], self.selected_assets[idx-1]
            self._refresh_list()
            self.listbox.selection_set(idx-1)
            self._notify_change()
    
    def _move_down(self):
        sel = self.listbox.curselection()
        if sel and sel[0] < len(self.selected_assets) - 1:
            idx = sel[0]
            self.selected_assets[idx], self.selected_assets[idx+1] = \
                self.selected_assets[idx+1], self.selected_assets[idx]
            self._refresh_list()
            self.listbox.selection_set(idx+1)
            self._notify_change()
    
    def _refresh_list(self):
        self.listbox.delete(0, tk.END)
        for asset in self.selected_assets:
            self.listbox.insert(tk.END, asset)
    
    def set_available_assets(self, assets: List[str]):
        self.available_assets = assets
    
    def get_value(self) -> List[str]:
        return self.selected_assets.copy()
    
    def set_value(self, value: Any):
        self.selected_assets = list(value) if value else []
        self._refresh_list()
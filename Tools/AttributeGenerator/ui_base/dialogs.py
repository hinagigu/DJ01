#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
通用对话框组件
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Callable, Optional, Tuple, Any


class DialogBase(tk.Toplevel):
    """对话框基类 - 提供居中显示、模态等通用功能"""
    
    def __init__(self, parent, title: str, width: int = 400, height: int = 300):
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.transient(parent)
        self.grab_set()
        
        # 居中显示
        self.update_idletasks()
        x = parent.winfo_rootx() + (parent.winfo_width() - width) // 2
        y = parent.winfo_rooty() + (parent.winfo_height() - height) // 2
        self.geometry(f"+{x}+{y}")
        
        self.result = None
        
        # 绑定 Escape 关闭
        self.bind('<Escape>', lambda e: self.destroy())
    
    def show(self) -> Any:
        """显示对话框并等待结果"""
        self.wait_window()
        return self.result


class SelectionDialog(DialogBase):
    """选择对话框 - 从下拉框选择或手动输入"""
    
    def __init__(self, parent, title: str, label: str, 
                 options: List[str], allow_custom: bool = True,
                 custom_label: str = "或手动输入名称:"):
        super().__init__(parent, title, width=400, height=240 if allow_custom else 160)
        
        self.options = options
        self.allow_custom = allow_custom
        
        self._create_ui(label, custom_label)
    
    def _create_ui(self, label: str, custom_label: str):
        # 选择标签
        ttk.Label(self, text=label).pack(pady=(20, 10))
        
        # 下拉选择框
        self.selected_var = tk.StringVar()
        self.combo = ttk.Combobox(self, textvariable=self.selected_var, 
                                   values=self.options, state='readonly', width=30)
        self.combo.pack(pady=5)
        if self.options:
            self.combo.current(0)
        
        # 自定义输入（可选）
        self.custom_var = tk.StringVar()
        if self.allow_custom:
            ttk.Label(self, text=custom_label).pack(pady=(15, 5))
            self.custom_entry = ttk.Entry(self, textvariable=self.custom_var, width=33)
            self.custom_entry.pack(pady=5)
        
        # 按钮
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="确定", command=self._on_confirm).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self.destroy).pack(side=tk.LEFT, padx=10)
    
    def _on_confirm(self):
        # 优先使用手动输入
        if self.allow_custom:
            self.result = self.custom_var.get().strip() or self.selected_var.get()
        else:
            self.result = self.selected_var.get()
        self.destroy()


class SearchListDialog(DialogBase):
    """搜索列表对话框 - 带搜索框的多选列表"""
    
    def __init__(self, parent, title: str, label: str,
                 items: List[str], select_mode: str = tk.MULTIPLE,
                 extra_widgets: Optional[Callable[['SearchListDialog'], None]] = None):
        super().__init__(parent, title, width=500, height=420)
        
        self.items = items
        self.select_mode = select_mode
        self.extra_widgets_callback = extra_widgets
        
        self._create_ui(label)
    
    def _create_ui(self, label: str):
        ttk.Label(self, text=label).pack(pady=(15, 5))
        
        # 搜索框
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=20, pady=5)
        ttk.Label(search_frame, text="搜索:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(search_frame, textvariable=self.search_var, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # 列表框
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(list_frame, selectmode=self.select_mode, 
                                   height=10, yscrollcommand=scrollbar.set)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # 填充列表
        self._refresh_list()
        
        # 搜索过滤
        self.search_var.trace('w', lambda *args: self._refresh_list())
        
        # 额外的组件（由调用者添加）
        if self.extra_widgets_callback:
            self.extra_widgets_callback(self)
        
        # 按钮
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="确定", command=self._on_confirm).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self.destroy).pack(side=tk.LEFT, padx=10)
        
        self.search_entry.focus_set()
    
    def _refresh_list(self):
        """刷新列表（应用搜索过滤）"""
        filter_text = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for item in self.items:
            if filter_text in item.lower():
                self.listbox.insert(tk.END, item)
    
    def _on_confirm(self):
        selected_indices = self.listbox.curselection()
        self.result = [self.listbox.get(i) for i in selected_indices]
        self.destroy()
    
    def get_selected_items(self) -> List[str]:
        """获取当前选中的项（供额外组件使用）"""
        return [self.listbox.get(i) for i in self.listbox.curselection()]


class ConfirmDialog(DialogBase):
    """确认对话框"""
    
    def __init__(self, parent, title: str, message: str):
        super().__init__(parent, title, width=350, height=150)
        
        ttk.Label(self, text=message, wraplength=300).pack(pady=30)
        
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="确定", command=self._on_yes).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self._on_no).pack(side=tk.LEFT, padx=10)
    
    def _on_yes(self):
        self.result = True
        self.destroy()
    
    def _on_no(self):
        self.result = False
        self.destroy()


def show_selection_dialog(parent, title: str, label: str, 
                          options: List[str], allow_custom: bool = True) -> Optional[str]:
    """显示选择对话框的便捷函数"""
    dialog = SelectionDialog(parent, title, label, options, allow_custom)
    return dialog.show()


def show_search_list_dialog(parent, title: str, label: str,
                            items: List[str], select_mode: str = tk.MULTIPLE,
                            extra_widgets: Optional[Callable] = None) -> List[str]:
    """显示搜索列表对话框的便捷函数"""
    dialog = SearchListDialog(parent, title, label, items, select_mode, extra_widgets)
    result = dialog.show()
    return result if result else []
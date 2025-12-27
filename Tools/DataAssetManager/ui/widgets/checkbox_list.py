#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 多选列表控件
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
from core.schema import PropertyDef


class CheckboxListWidget(PropertyWidget):
    """
    多选列表控件
    用于从预定义选项中选择多个值（如选择要启用的 GameFeature）
    """
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 on_change: Callable[[str, Any], None],
                 options: List[Dict[str, str]] = None):
        self.options = options or []
        self.checkbox_vars: Dict[str, tk.BooleanVar] = {}
        self.checkboxes: Dict[str, ttk.Checkbutton] = {}
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        """创建多选列表控件"""
        # 主容器
        self.main_frame = ttk.Frame(self.frame)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题和操作按钮
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(header_frame, text=self.prop_def.display_name).pack(side=tk.LEFT)
        
        # 全选/取消全选按钮
        btn_frame = ttk.Frame(header_frame)
        btn_frame.pack(side=tk.RIGHT)
        
        ttk.Button(btn_frame, text="全选", width=6,
                   command=self._select_all).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="清空", width=6,
                   command=self._clear_all).pack(side=tk.LEFT, padx=2)
        
        # 如果选项较多，使用滚动区域
        if len(self.options) > 6:
            # 创建滚动容器
            canvas_frame = ttk.Frame(self.main_frame)
            canvas_frame.pack(fill=tk.BOTH, expand=True)
            
            canvas = tk.Canvas(canvas_frame, height=150, highlightthickness=0)
            scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
            
            self.options_frame = ttk.Frame(canvas)
            
            canvas.configure(yscrollcommand=scrollbar.set)
            
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            canvas_window = canvas.create_window((0, 0), window=self.options_frame, anchor="nw")
            
            def on_configure(event):
                canvas.configure(scrollregion=canvas.bbox("all"))
                canvas.itemconfig(canvas_window, width=event.width)
            
            self.options_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.bind("<Configure>", on_configure)
            
            # 绑定鼠标滚轮
            def on_mousewheel(event):
                canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            canvas.bind_all("<MouseWheel>", on_mousewheel)
        else:
            self.options_frame = ttk.Frame(self.main_frame)
            self.options_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建选项复选框
        self._create_checkboxes()
        
        # 描述提示
        if self.prop_def.description:
            desc_label = ttk.Label(self.main_frame, text=self.prop_def.description,
                                   font=("", 8), foreground="gray")
            desc_label.pack(anchor=tk.W, pady=(5, 0))
    
    def _create_checkboxes(self):
        """创建所有选项的复选框"""
        for option in self.options:
            name = option.get("name", "")
            display_name = option.get("display_name", name)
            description = option.get("description", "")
            
            var = tk.BooleanVar(value=False)
            self.checkbox_vars[name] = var
            
            # 创建带提示的复选框
            cb_frame = ttk.Frame(self.options_frame)
            cb_frame.pack(fill=tk.X, pady=1)
            
            cb = ttk.Checkbutton(
                cb_frame,
                text=f"{display_name}",
                variable=var,
                command=lambda: self._on_checkbox_change()
            )
            cb.pack(side=tk.LEFT)
            self.checkboxes[name] = cb
            
            if description:
                ttk.Label(cb_frame, text=f"- {description}",
                          font=("", 8), foreground="gray").pack(side=tk.LEFT, padx=(5, 0))
        
        # 如果没有选项，显示提示
        if not self.options:
            ttk.Label(self.options_frame, text="(无可用选项)",
                      foreground="gray").pack(anchor=tk.W)
    
    def _on_checkbox_change(self):
        """复选框状态改变时触发"""
        self._notify_change()
    
    def _select_all(self):
        """全选"""
        for var in self.checkbox_vars.values():
            var.set(True)
        self._notify_change()
    
    def _clear_all(self):
        """取消全选"""
        for var in self.checkbox_vars.values():
            var.set(False)
        self._notify_change()
    
    def _notify_change(self):
        """通知值变化"""
        if self.on_change:
            self.on_change(self.prop_def.name, self.get_value())
    
    def get_value(self) -> List[str]:
        """获取选中的值列表"""
        selected = []
        for name, var in self.checkbox_vars.items():
            if var.get():
                selected.append(name)
        return selected
    
    def set_value(self, value: Any):
        """设置选中的值"""
        if not isinstance(value, list):
            value = [value] if value else []
        
        # 重置所有复选框
        for var in self.checkbox_vars.values():
            var.set(False)
        
        # 设置选中项
        for item in value:
            if item in self.checkbox_vars:
                self.checkbox_vars[item].set(True)
    
    def update_options(self, options: List[Dict[str, str]]):
        """更新可选项"""
        # 保存当前选中的值
        current_value = self.get_value()
        
        # 清除旧的复选框
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        self.checkbox_vars.clear()
        self.checkboxes.clear()
        
        # 重新创建
        self.options = options
        self._create_checkboxes()
        
        # 恢复选中状态
        self.set_value(current_value)
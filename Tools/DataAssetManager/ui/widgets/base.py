#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 控件基类
职责：定义属性控件的基类接口
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, Optional
from abc import ABC, abstractmethod
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from core.schema import PropertyDef


class PropertyWidget(ABC):
    """属性控件基类"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 on_change: Callable[[str, Any], None] = None):
        self.parent = parent
        self.prop_def = prop_def
        self.on_change = on_change
        self.frame = ttk.Frame(parent)
        self._create_widget()
    
    @abstractmethod
    def _create_widget(self):
        """创建控件（子类实现）"""
        pass
    
    @abstractmethod
    def get_value(self) -> Any:
        """获取值"""
        pass
    
    @abstractmethod
    def set_value(self, value: Any):
        """设置值"""
        pass
    
    def _notify_change(self):
        """通知值变化"""
        if self.on_change:
            self.on_change(self.prop_def.name, self.get_value())
    
    def _create_label(self) -> ttk.Label:
        """创建标签"""
        text = self.prop_def.display_name
        if self.prop_def.required:
            text += " *"
        label = ttk.Label(self.frame, text=text + ":")
        return label
    
    def _create_tooltip(self, widget: tk.Widget, text: str):
        """创建工具提示"""
        if not text:
            return
        
        def show(event):
            tooltip = tk.Toplevel(widget)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            ttk.Label(tooltip, text=text, background="#ffffe0", 
                     relief="solid", padding=5).pack()
            widget._tooltip = tooltip
            widget.after(2000, lambda: self._hide_tooltip(widget))
        
        def hide(event):
            self._hide_tooltip(widget)
        
        widget.bind('<Enter>', show)
        widget.bind('<Leave>', hide)
    
    def _hide_tooltip(self, widget: tk.Widget):
        """隐藏工具提示"""
        if hasattr(widget, '_tooltip'):
            try:
                widget._tooltip.destroy()
            except:
                pass
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)
    
    def destroy(self):
        self.frame.destroy()
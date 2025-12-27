#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 文本控件
"""

import tkinter as tk
from tkinter import ttk
from typing import Any

from .base import PropertyWidget


class TextInputWidget(PropertyWidget):
    """文本输入控件"""
    
    def _create_widget(self):
        self._create_label().pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        self.entry = ttk.Entry(self.frame, textvariable=self.var, width=40)
        self.entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        if self.prop_def.default:
            self.var.set(str(self.prop_def.default))
        
        self.var.trace_add('write', lambda *args: self._notify_change())
        self._create_tooltip(self.entry, self.prop_def.description)
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(str(value) if value else "")


class TextAreaWidget(PropertyWidget):
    """多行文本输入控件"""
    
    def _create_widget(self):
        self._create_label().pack(anchor=tk.W, padx=5)
        
        self.text = tk.Text(self.frame, height=4, width=40)
        self.text.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        if self.prop_def.default:
            self.text.insert('1.0', str(self.prop_def.default))
        
        self.text.bind('<KeyRelease>', lambda e: self._notify_change())
    
    def get_value(self) -> str:
        return self.text.get('1.0', tk.END).strip()
    
    def set_value(self, value: Any):
        self.text.delete('1.0', tk.END)
        if value:
            self.text.insert('1.0', str(value))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 数值控件
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Union

from .base import PropertyWidget


class SpinBoxWidget(PropertyWidget):
    """数值输入控件"""
    
    def _create_widget(self):
        self._create_label().pack(side=tk.LEFT, padx=5)
        
        from_val = self.prop_def.min_value if self.prop_def.min_value is not None else 0
        to_val = self.prop_def.max_value if self.prop_def.max_value is not None else 9999
        
        is_float = "float" in self.prop_def.type.lower()
        self.var = tk.DoubleVar() if is_float else tk.IntVar()
        
        if self.prop_def.default is not None:
            self.var.set(self.prop_def.default)
        
        increment = 0.1 if is_float else 1
        self.spinbox = ttk.Spinbox(
            self.frame, 
            from_=from_val, 
            to=to_val,
            increment=increment,
            textvariable=self.var, 
            width=10
        )
        self.spinbox.pack(side=tk.LEFT, padx=5)
        
        self.var.trace_add('write', lambda *args: self._notify_change())
    
    def get_value(self) -> Union[int, float]:
        return self.var.get()
    
    def set_value(self, value: Any):
        if value is not None:
            self.var.set(value)


class CheckboxWidget(PropertyWidget):
    """复选框控件"""
    
    def _create_widget(self):
        self.var = tk.BooleanVar()
        if self.prop_def.default:
            self.var.set(self.prop_def.default)
        
        self.check = ttk.Checkbutton(
            self.frame, 
            text=self.prop_def.display_name,
            variable=self.var, 
            command=self._notify_change
        )
        self.check.pack(side=tk.LEFT, padx=5)
    
    def get_value(self) -> bool:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(bool(value) if value else False)
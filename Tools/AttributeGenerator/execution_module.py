#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - Execution 模块
重构后的入口文件，统一导出所有组件
"""

# 数据模型
from execution_data import ExecutionData

# 代码生成器
from execution_generator import ExecutionCodeGenerator

# 内联编辑器 Mixin
from inline_editor import InlineEditorMixin

# UI 组件
from execution_ui import ExecutionEditorUI

# 为了向后兼容，保留旧的对话框类（如果其他地方仍在使用）
import tkinter as tk
from tkinter import ttk
from collections import OrderedDict
from config import CAPTURE_LAYERS, OUTPUT_OPS, TAG_EFFECTS, TAG_SOURCES


class CaptureDialog:
    """捕获属性选择对话框（保留以兼容旧代码）"""
    
    def __init__(self, parent, attributes):
        self.result = None
        self.attributes = attributes
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("添加捕获属性")
        self.dialog.geometry("350x180")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        ttk.Label(self.dialog, text="属性集:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.set_var = tk.StringVar()
        sets = list(OrderedDict.fromkeys(a.set_name for a in attributes))
        self.set_combo = ttk.Combobox(self.dialog, textvariable=self.set_var, values=sets, width=25)
        self.set_combo.grid(row=0, column=1, padx=10, pady=5)
        self.set_combo.bind('<<ComboboxSelected>>', self._on_set_change)
        
        ttk.Label(self.dialog, text="属性:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.attr_var = tk.StringVar()
        self.attr_combo = ttk.Combobox(self.dialog, textvariable=self.attr_var, width=25)
        self.attr_combo.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.dialog, text="层级:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.layer_var = tk.StringVar(value="Total")
        ttk.Combobox(self.dialog, textvariable=self.layer_var, values=CAPTURE_LAYERS, width=25).grid(row=2, column=1, padx=10, pady=5)
        
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)
        ttk.Button(btn_frame, text="确定", command=self._ok).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self._cancel).pack(side=tk.LEFT, padx=10)
        
        self.dialog.wait_window()
    
    def _on_set_change(self, event):
        set_name = self.set_var.get()
        attrs = [a.name for a in self.attributes if a.set_name == set_name]
        self.attr_combo['values'] = attrs
        if attrs:
            self.attr_var.set(attrs[0])
    
    def _ok(self):
        if self.set_var.get() and self.attr_var.get():
            self.result = {'set': self.set_var.get(), 'attr': self.attr_var.get(), 'layer': self.layer_var.get()}
        self.dialog.destroy()
    
    def _cancel(self):
        self.dialog.destroy()


class TagConditionDialog:
    """Tag 条件对话框（保留以兼容旧代码）"""
    
    def __init__(self, parent, tags):
        self.result = None
        self.tags = tags
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("添加 Tag 条件")
        self.dialog.geometry("400x220")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        ttk.Label(self.dialog, text="检查对象:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.source_var = tk.StringVar(value="Target")
        ttk.Combobox(self.dialog, textvariable=self.source_var, values=TAG_SOURCES, width=30).grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(self.dialog, text="Tag:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.tag_var = tk.StringVar()
        tag_values = [t.tag for t in tags] if tags else []
        self.tag_combo = ttk.Combobox(self.dialog, textvariable=self.tag_var, values=tag_values, width=30)
        self.tag_combo.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.dialog, text="效果:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.effect_var = tk.StringVar(value="Skip")
        effect_combo = ttk.Combobox(self.dialog, textvariable=self.effect_var, values=TAG_EFFECTS, width=30)
        effect_combo.grid(row=2, column=1, padx=10, pady=5)
        effect_combo.bind('<<ComboboxSelected>>', self._on_effect_change)
        
        ttk.Label(self.dialog, text="数值:").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.value_var = tk.StringVar(value="0")
        self.value_entry = ttk.Entry(self.dialog, textvariable=self.value_var, width=32)
        self.value_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.hint_label = ttk.Label(self.dialog, text="Skip: 免疫，直接跳过计算", foreground='gray')
        self.hint_label.grid(row=4, column=0, columnspan=2, pady=5)
        
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=15)
        ttk.Button(btn_frame, text="确定", command=self._ok).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self._cancel).pack(side=tk.LEFT, padx=10)
        
        self._on_effect_change(None)
        self.dialog.wait_window()
    
    def _on_effect_change(self, event):
        effect = self.effect_var.get()
        if effect == 'Skip':
            self.value_entry.config(state='disabled')
            self.hint_label.config(text="Skip: 免疫，直接跳过计算")
        elif effect == 'Multiply':
            self.value_entry.config(state='normal')
            self.value_var.set("1.5")
            self.hint_label.config(text="Multiply: 乘以倍率（如 1.5 = +50%，0.5 = -50%）")
        elif effect == 'Add':
            self.value_entry.config(state='normal')
            self.value_var.set("100")
            self.hint_label.config(text="Add: 增加固定值")
    
    def _ok(self):
        if self.tag_var.get():
            try:
                value = float(self.value_var.get()) if self.effect_var.get() != 'Skip' else 0
            except ValueError:
                value = 0
            self.result = {
                'source': self.source_var.get(),
                'tag': self.tag_var.get(),
                'effect': self.effect_var.get(),
                'value': value
            }
        self.dialog.destroy()
    
    def _cancel(self):
        self.dialog.destroy()


class OutputDialog:
    """输出属性选择对话框（保留以兼容旧代码）"""
    
    def __init__(self, parent, attributes):
        self.result = None
        self.attributes = attributes
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("添加输出属性")
        self.dialog.geometry("350x180")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        ttk.Label(self.dialog, text="属性集:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.set_var = tk.StringVar()
        sets = list(OrderedDict.fromkeys(a.set_name for a in attributes))
        self.set_combo = ttk.Combobox(self.dialog, textvariable=self.set_var, values=sets, width=25)
        self.set_combo.grid(row=0, column=1, padx=10, pady=5)
        self.set_combo.bind('<<ComboboxSelected>>', self._on_set_change)
        
        ttk.Label(self.dialog, text="属性:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.attr_var = tk.StringVar()
        self.attr_combo = ttk.Combobox(self.dialog, textvariable=self.attr_var, width=25)
        self.attr_combo.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.dialog, text="操作:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.op_var = tk.StringVar(value="Additive")
        ttk.Combobox(self.dialog, textvariable=self.op_var, values=OUTPUT_OPS, width=25).grid(row=2, column=1, padx=10, pady=5)
        
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)
        ttk.Button(btn_frame, text="确定", command=self._ok).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self._cancel).pack(side=tk.LEFT, padx=10)
        
        self.dialog.wait_window()
    
    def _on_set_change(self, event):
        set_name = self.set_var.get()
        attrs = [a.name for a in self.attributes if a.set_name == set_name]
        self.attr_combo['values'] = attrs
        if attrs:
            self.attr_var.set(attrs[0])
    
    def _ok(self):
        if self.set_var.get() and self.attr_var.get():
            self.result = {'set': self.set_var.get(), 'attr': self.attr_var.get(), 'op': self.op_var.get()}
        self.dialog.destroy()
    
    def _cancel(self):
        self.dialog.destroy()


# 导出所有公共接口
__all__ = [
    'ExecutionData',
    'ExecutionCodeGenerator',
    'ExecutionEditorUI',
    'InlineEditorMixin',
    'CaptureDialog',
    'TagConditionDialog',
    'OutputDialog',
]
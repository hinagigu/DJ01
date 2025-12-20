#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 通用辅助函数
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Optional


def create_labeled_entry(
    parent,
    label: str,
    variable: tk.StringVar = None,
    width: int = 20,
    readonly: bool = False
) -> tuple:
    """
    创建带标签的输入框
    
    Args:
        parent: 父级容器
        label: 标签文字
        variable: StringVar 变量
        width: 输入框宽度
        readonly: 是否只读
    
    Returns:
        (frame, entry) 元组
    """
    frame = ttk.Frame(parent)
    
    ttk.Label(frame, text=label).pack(side=tk.LEFT, padx=(0, 5))
    
    entry = ttk.Entry(frame, textvariable=variable, width=width)
    if readonly:
        entry.config(state='readonly')
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    return frame, entry


def create_labeled_combo(
    parent,
    label: str,
    values: List[str],
    variable: tk.StringVar = None,
    width: int = 18,
    on_change: Callable = None,
    readonly: bool = True
) -> tuple:
    """
    创建带标签的下拉框
    
    Args:
        parent: 父级容器
        label: 标签文字
        values: 选项列表
        variable: StringVar 变量
        width: 下拉框宽度
        on_change: 选择变化回调
        readonly: 是否只读
    
    Returns:
        (frame, combobox) 元组
    """
    frame = ttk.Frame(parent)
    
    ttk.Label(frame, text=label).pack(side=tk.LEFT, padx=(0, 5))
    
    state = 'readonly' if readonly else 'normal'
    combo = ttk.Combobox(frame, textvariable=variable, values=values, width=width, state=state)
    combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
    
    if on_change:
        combo.bind('<<ComboboxSelected>>', on_change)
    
    return frame, combo


def create_labeled_spinbox(
    parent,
    label: str,
    variable: tk.StringVar = None,
    from_: float = 0,
    to: float = 100,
    increment: float = 1,
    width: int = 10
) -> tuple:
    """
    创建带标签的数字输入框
    
    Args:
        parent: 父级容器
        label: 标签文字
        variable: StringVar 变量
        from_: 最小值
        to: 最大值
        increment: 步进值
        width: 宽度
    
    Returns:
        (frame, spinbox) 元组
    """
    frame = ttk.Frame(parent)
    
    ttk.Label(frame, text=label).pack(side=tk.LEFT, padx=(0, 5))
    
    spinbox = ttk.Spinbox(
        frame,
        textvariable=variable,
        from_=from_,
        to=to,
        increment=increment,
        width=width
    )
    spinbox.pack(side=tk.LEFT)
    
    return frame, spinbox


def create_scrolled_text(
    parent,
    height: int = 10,
    width: int = 40,
    readonly: bool = False
) -> tk.Text:
    """
    创建带滚动条的文本框
    
    Args:
        parent: 父级容器
        height: 高度（行数）
        width: 宽度（字符数）
        readonly: 是否只读
    
    Returns:
        Text 控件
    """
    frame = ttk.Frame(parent)
    frame.pack(fill=tk.BOTH, expand=True)
    
    text = tk.Text(frame, height=height, width=width, wrap=tk.WORD)
    text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.config(yscrollcommand=scrollbar.set)
    
    if readonly:
        text.config(state='disabled')
    
    return text


def create_button_group(
    parent,
    buttons: List[tuple],
    pack_side: str = tk.LEFT
) -> dict:
    """
    创建按钮组
    
    Args:
        parent: 父级容器
        buttons: [(文字, 回调, 宽度), ...]
        pack_side: 排列方向
    
    Returns:
        {文字: Button} 字典
    """
    result = {}
    for btn_config in buttons:
        text = btn_config[0]
        command = btn_config[1]
        width = btn_config[2] if len(btn_config) > 2 else None
        
        btn = ttk.Button(parent, text=text, command=command)
        if width:
            btn.config(width=width)
        btn.pack(side=pack_side, padx=2)
        result[text] = btn
    
    return result
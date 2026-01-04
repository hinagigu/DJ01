#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - 编辑器对话框
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, List

from .schema_models import PropertyData


class ComponentTypeDialog(tk.Toplevel):
    """组件类型选择对话框"""
    
    # 组件分类映射
    CATEGORY_MAP = {
        "容器": ["CanvasPanel", "HorizontalBox", "VerticalBox", "Overlay", 
                "WidgetSwitcher", "GridPanel", "UniformGridPanel", "ScrollBox", "WrapBox"],
        "文本": ["TextBlock", "RichTextBlock", "EditableText", "EditableTextBox", 
                "MultiLineEditableText"],
        "图像": ["Image", "Border", "BackgroundBlur"],
        "交互": ["Button", "CheckBox", "ComboBoxString", "Slider", "SpinBox"],
        "布局": ["SizeBox", "ScaleBox", "Spacer", "SafeZone"]
    }
    
    def __init__(self, parent, component_types: List[str], widget_types: dict):
        super().__init__(parent)
        
        self.result: Optional[str] = None
        self.component_types = component_types
        self.widget_types = widget_types
        
        self.title("选择组件类型")
        self.geometry("400x500")
        self.transient(parent)
        self.grab_set()
        
        self._create_ui()
        self._center_window(parent)
    
    def _center_window(self, parent):
        """居中显示"""
        self.update_idletasks()
        x = parent.winfo_rootx() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_rooty() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
    
    def _create_ui(self):
        # 搜索框
        search_frame = ttk.Frame(self)
        search_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(search_frame, text="搜索:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self._filter_list())
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        search_entry.focus_set()
        
        # 分类选择
        category_frame = ttk.Frame(self)
        category_frame.pack(fill=tk.X, padx=10)
        
        categories = ["全部", "容器", "文本", "图像", "交互", "布局"]
        self.category_var = tk.StringVar(value="全部")
        for cat in categories:
            ttk.Radiobutton(category_frame, text=cat, variable=self.category_var, 
                           value=cat, command=self._filter_list).pack(side=tk.LEFT, padx=5)
        
        # 列表
        list_frame = ttk.Frame(self)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.listbox = tk.Listbox(list_frame, font=("Consolas", 10))
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.listbox.bind('<Double-1>', lambda e: self._on_select())
        self.listbox.bind('<<ListboxSelect>>', self._on_selection_changed)
        
        # 描述
        self.desc_label = ttk.Label(self, text="", foreground="gray")
        self.desc_label.pack(fill=tk.X, padx=10)
        
        # 按钮
        btn_frame = ttk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(btn_frame, text="选择", command=self._on_select).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="取消", command=self.destroy).pack(side=tk.RIGHT)
        
        self._filter_list()
    
    def _filter_list(self):
        """过滤列表"""
        self.listbox.delete(0, tk.END)
        
        search = self.search_var.get().lower()
        category = self.category_var.get()
        
        for comp_type in self.component_types:
            # 搜索过滤
            if search and search not in comp_type.lower():
                continue
            
            # 分类过滤
            if category != "全部":
                type_category = None
                for cat, types in self.CATEGORY_MAP.items():
                    if comp_type in types:
                        type_category = cat
                        break
                if type_category != category:
                    continue
            
            self.listbox.insert(tk.END, comp_type)
    
    def _on_selection_changed(self, event):
        """选择变更"""
        selection = self.listbox.curselection()
        if selection:
            comp_type = self.listbox.get(selection[0])
            type_info = self.widget_types.get("types", {}).get(comp_type, {})
            desc = type_info.get("description", "")
            self.desc_label.config(text=desc)
    
    def _on_select(self):
        """确认选择"""
        selection = self.listbox.curselection()
        if selection:
            self.result = self.listbox.get(selection[0])
            self.destroy()


class PropertyEditDialog(tk.Toplevel):
    """属性编辑对话框"""
    
    PROPERTY_TYPES = ["float", "int32", "bool", "FText", "FString", "FLinearColor"]
    
    def __init__(self, parent, prop: Optional[PropertyData] = None):
        super().__init__(parent)
        
        self.result: Optional[dict] = None
        self.prop = prop
        
        self.title("编辑属性" if prop else "添加属性")
        self.geometry("400x300")
        self.transient(parent)
        self.grab_set()
        
        self._create_ui()
        self._center_window(parent)
    
    def _center_window(self, parent):
        """居中显示"""
        self.update_idletasks()
        x = parent.winfo_rootx() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_rooty() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
    
    def _create_ui(self):
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 名称
        row1 = ttk.Frame(main_frame)
        row1.pack(fill=tk.X, pady=5)
        ttk.Label(row1, text="名称:", width=10).pack(side=tk.LEFT)
        self.name_var = tk.StringVar(value=self.prop.name if self.prop else "NewProperty")
        ttk.Entry(row1, textvariable=self.name_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 类型
        row2 = ttk.Frame(main_frame)
        row2.pack(fill=tk.X, pady=5)
        ttk.Label(row2, text="类型:", width=10).pack(side=tk.LEFT)
        self.type_var = tk.StringVar(value=self.prop.type if self.prop else "float")
        ttk.Combobox(row2, textvariable=self.type_var, values=self.PROPERTY_TYPES, 
                    state='readonly').pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 默认值
        row3 = ttk.Frame(main_frame)
        row3.pack(fill=tk.X, pady=5)
        ttk.Label(row3, text="默认值:", width=10).pack(side=tk.LEFT)
        self.default_var = tk.StringVar(
            value=str(self.prop.default) if self.prop and self.prop.default is not None else ""
        )
        ttk.Entry(row3, textvariable=self.default_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 分类
        row4 = ttk.Frame(main_frame)
        row4.pack(fill=tk.X, pady=5)
        ttk.Label(row4, text="分类:", width=10).pack(side=tk.LEFT)
        self.category_var = tk.StringVar(value=self.prop.category if self.prop else "")
        ttk.Entry(row4, textvariable=self.category_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 描述
        row5 = ttk.Frame(main_frame)
        row5.pack(fill=tk.X, pady=5)
        ttk.Label(row5, text="描述:", width=10).pack(side=tk.LEFT)
        self.desc_var = tk.StringVar(value=self.prop.description if self.prop else "")
        ttk.Entry(row5, textvariable=self.desc_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 选项
        row6 = ttk.Frame(main_frame)
        row6.pack(fill=tk.X, pady=5)
        self.readonly_var = tk.BooleanVar(value=self.prop.blueprint_read_only if self.prop else False)
        ttk.Checkbutton(row6, text="蓝图只读 (BlueprintReadOnly)", variable=self.readonly_var).pack(side=tk.LEFT)
        
        # 按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)
        
        ttk.Button(btn_frame, text="确定", command=self._on_ok).pack(side=tk.RIGHT, padx=5)
        ttk.Button(btn_frame, text="取消", command=self.destroy).pack(side=tk.RIGHT)
    
    def _on_ok(self):
        """确定"""
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("警告", "属性名称不能为空")
            return
        
        # 解析默认值
        default_str = self.default_var.get().strip()
        default = None
        if default_str:
            prop_type = self.type_var.get()
            try:
                if prop_type == "float":
                    default = float(default_str)
                elif prop_type == "int32":
                    default = int(default_str)
                elif prop_type == "bool":
                    default = default_str.lower() in ('true', '1', 'yes')
                else:
                    default = default_str
            except ValueError:
                default = default_str
        
        self.result = {
            "name": name,
            "type": self.type_var.get(),
            "default": default,
            "category": self.category_var.get(),
            "description": self.desc_var.get(),
            "blueprint_read_only": self.readonly_var.get()
        }
        self.destroy()
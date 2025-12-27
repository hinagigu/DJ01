#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 属性编辑控件
可复用的属性编辑器控件，根据 schema 定义自动生成
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Any, Callable, List, Optional
from abc import ABC, abstractmethod

from .schema_loader import PropertyDef, StructDef, SchemaLoader


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
        """创建控件"""
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
    
    def pack(self, **kwargs):
        self.frame.pack(**kwargs)
    
    def grid(self, **kwargs):
        self.frame.grid(**kwargs)


class TextInputWidget(PropertyWidget):
    """文本输入控件"""
    
    def _create_widget(self):
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        self.entry = ttk.Entry(self.frame, textvariable=self.var, width=40)
        self.entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        if self.prop_def.default:
            self.var.set(str(self.prop_def.default))
        
        self.var.trace('w', lambda *args: self._notify_change())
        
        # 显示描述提示
        if self.prop_def.description:
            self._create_tooltip(self.entry, self.prop_def.description)
    
    def _create_tooltip(self, widget, text):
        """创建工具提示"""
        def show_tooltip(event):
            tooltip = tk.Toplevel(widget)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = ttk.Label(tooltip, text=text, background="#ffffe0", relief="solid", padding=5)
            label.pack()
            widget._tooltip = tooltip
            widget.after(2000, lambda: tooltip.destroy() if hasattr(widget, '_tooltip') else None)
        
        def hide_tooltip(event):
            if hasattr(widget, '_tooltip'):
                widget._tooltip.destroy()
        
        widget.bind('<Enter>', show_tooltip)
        widget.bind('<Leave>', hide_tooltip)
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(str(value) if value else "")


class SpinBoxWidget(PropertyWidget):
    """数值输入控件"""
    
    def _create_widget(self):
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(side=tk.LEFT, padx=5)
        
        from_val = self.prop_def.min_value if self.prop_def.min_value is not None else 0
        to_val = self.prop_def.max_value if self.prop_def.max_value is not None else 9999
        
        self.var = tk.DoubleVar() if self.prop_def.type == "float" else tk.IntVar()
        if self.prop_def.default is not None:
            self.var.set(self.prop_def.default)
        
        self.spinbox = ttk.Spinbox(self.frame, from_=from_val, to=to_val,
                                    textvariable=self.var, width=10)
        self.spinbox.pack(side=tk.LEFT, padx=5)
        
        self.var.trace('w', lambda *args: self._notify_change())
    
    def get_value(self) -> float:
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
        
        self.check = ttk.Checkbutton(self.frame, text=self.prop_def.display_name,
                                      variable=self.var, command=self._notify_change)
        self.check.pack(side=tk.LEFT, padx=5)
    
    def get_value(self) -> bool:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(bool(value) if value else False)


class ComboBoxWidget(PropertyWidget):
    """下拉选择控件"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 options: List[str] = None, on_change: Callable = None):
        self.options = options or []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        self.combo = ttk.Combobox(self.frame, textvariable=self.var, values=self.options,
                                   state='readonly', width=35)
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        if self.prop_def.default and self.prop_def.default in self.options:
            self.var.set(self.prop_def.default)
        elif self.options:
            self.var.set(self.options[0])
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
    
    def set_options(self, options: List[str]):
        """更新选项"""
        self.options = options
        self.combo['values'] = options
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        if value and value in self.options:
            self.var.set(value)


class TagSelectorWidget(PropertyWidget):
    """Gameplay 标签选择器"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_tags: List[str] = None, on_change: Callable = None):
        self.available_tags = available_tags or []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        
        # 过滤标签（根据 categories）
        filtered_tags = self._filter_tags()
        
        self.combo = ttk.Combobox(self.frame, textvariable=self.var, 
                                   values=filtered_tags, width=40)
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
        self.combo.bind('<KeyRelease>', self._on_key_release)
    
    def _filter_tags(self) -> List[str]:
        """根据类别过滤标签"""
        if not self.prop_def.categories:
            return self.available_tags
        
        prefix = self.prop_def.categories
        return [tag for tag in self.available_tags if tag.startswith(prefix)]
    
    def _on_key_release(self, event):
        """输入时过滤提示"""
        typed = self.var.get().lower()
        if typed:
            filtered = [t for t in self._filter_tags() if typed in t.lower()]
            self.combo['values'] = filtered
        else:
            self.combo['values'] = self._filter_tags()
    
    def set_available_tags(self, tags: List[str]):
        """更新可用标签"""
        self.available_tags = tags
        self.combo['values'] = self._filter_tags()
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(str(value) if value else "")


class AssetPickerWidget(PropertyWidget):
    """资产选择器控件"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_assets: List[str] = None, on_change: Callable = None):
        self.available_assets = available_assets or []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(side=tk.LEFT, padx=5)
        
        self.var = tk.StringVar()
        self.combo = ttk.Combobox(self.frame, textvariable=self.var,
                                   values=self.available_assets, width=45)
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # 浏览按钮
        ttk.Button(self.frame, text="...", width=3, 
                   command=self._browse).pack(side=tk.LEFT, padx=2)
        
        # 清除按钮
        ttk.Button(self.frame, text="✕", width=3,
                   command=self._clear).pack(side=tk.LEFT, padx=2)
        
        self.combo.bind('<<ComboboxSelected>>', lambda e: self._notify_change())
    
    def _browse(self):
        """浏览选择资产（显示可用列表）"""
        if self.available_assets:
            # 创建选择对话框
            dialog = tk.Toplevel(self.frame)
            dialog.title(f"选择 {self.prop_def.display_name}")
            dialog.geometry("400x300")
            dialog.transient(self.frame)
            dialog.grab_set()
            
            # 搜索框
            search_var = tk.StringVar()
            search_entry = ttk.Entry(dialog, textvariable=search_var)
            search_entry.pack(fill=tk.X, padx=10, pady=5)
            
            # 列表
            listbox = tk.Listbox(dialog, selectmode=tk.SINGLE)
            listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
            
            for asset in self.available_assets:
                listbox.insert(tk.END, asset)
            
            def filter_list(*args):
                search = search_var.get().lower()
                listbox.delete(0, tk.END)
                for asset in self.available_assets:
                    if search in asset.lower():
                        listbox.insert(tk.END, asset)
            
            search_var.trace('w', filter_list)
            
            def on_select():
                sel = listbox.curselection()
                if sel:
                    self.var.set(listbox.get(sel[0]))
                    self._notify_change()
                dialog.destroy()
            
            ttk.Button(dialog, text="选择", command=on_select).pack(pady=10)
    
    def _clear(self):
        """清除选择"""
        self.var.set("")
        self._notify_change()
    
    def set_available_assets(self, assets: List[str]):
        """更新可用资产列表"""
        self.available_assets = assets
        self.combo['values'] = assets
    
    def get_value(self) -> str:
        return self.var.get()
    
    def set_value(self, value: Any):
        self.var.set(str(value) if value else "")


class AssetPickerListWidget(PropertyWidget):
    """资产列表选择器（多选）"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_assets: List[str] = None, on_change: Callable = None):
        self.available_assets = available_assets or []
        self.selected_assets: List[str] = []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        # 标签
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(anchor=tk.W, padx=5)
        
        # 列表框
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        self.listbox = tk.Listbox(list_frame, height=4, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # 按钮
        btn_frame = ttk.Frame(self.frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=2)
        
        ttk.Button(btn_frame, text="➕ 添加", command=self._add_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="➖ 移除", command=self._remove_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="⬆", width=3, command=self._move_up).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="⬇", width=3, command=self._move_down).pack(side=tk.LEFT, padx=2)
    
    def _add_item(self):
        """添加资产"""
        if not self.available_assets:
            messagebox.showinfo("提示", "没有可用的资产")
            return
        
        # 创建选择对话框
        dialog = tk.Toplevel(self.frame)
        dialog.title("添加资产")
        dialog.geometry("400x300")
        dialog.transient(self.frame)
        dialog.grab_set()
        
        listbox = tk.Listbox(dialog, selectmode=tk.EXTENDED)
        listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        for asset in self.available_assets:
            if asset not in self.selected_assets:
                listbox.insert(tk.END, asset)
        
        def on_add():
            selections = listbox.curselection()
            for idx in selections:
                asset = listbox.get(idx)
                if asset not in self.selected_assets:
                    self.selected_assets.append(asset)
                    self.listbox.insert(tk.END, asset)
            self._notify_change()
            dialog.destroy()
        
        ttk.Button(dialog, text="添加", command=on_add).pack(pady=10)
    
    def _remove_item(self):
        """移除选中项"""
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            asset = self.listbox.get(idx)
            self.selected_assets.remove(asset)
            self.listbox.delete(idx)
            self._notify_change()
    
    def _move_up(self):
        """上移"""
        sel = self.listbox.curselection()
        if sel and sel[0] > 0:
            idx = sel[0]
            self.selected_assets[idx-1], self.selected_assets[idx] = \
                self.selected_assets[idx], self.selected_assets[idx-1]
            self._refresh_list()
            self.listbox.selection_set(idx-1)
            self._notify_change()
    
    def _move_down(self):
        """下移"""
        sel = self.listbox.curselection()
        if sel and sel[0] < len(self.selected_assets) - 1:
            idx = sel[0]
            self.selected_assets[idx], self.selected_assets[idx+1] = \
                self.selected_assets[idx+1], self.selected_assets[idx]
            self._refresh_list()
            self.listbox.selection_set(idx+1)
            self._notify_change()
    
    def _refresh_list(self):
        """刷新列表"""
        self.listbox.delete(0, tk.END)
        for asset in self.selected_assets:
            self.listbox.insert(tk.END, asset)
    
    def set_available_assets(self, assets: List[str]):
        """更新可用资产列表"""
        self.available_assets = assets
    
    def get_value(self) -> List[str]:
        return self.selected_assets.copy()
    
    def set_value(self, value: Any):
        self.selected_assets = list(value) if value else []
        self._refresh_list()


class StringListWidget(PropertyWidget):
    """字符串列表编辑器"""
    
    def _create_widget(self):
        self.items: List[str] = []
        
        # 标签
        ttk.Label(self.frame, text=self.prop_def.display_name + ":").pack(anchor=tk.W, padx=5)
        
        # 列表框
        list_frame = ttk.Frame(self.frame)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        self.listbox = tk.Listbox(list_frame, height=4)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # 输入框和按钮
        input_frame = ttk.Frame(self.frame)
        input_frame.pack(fill=tk.X, padx=5, pady=2)
        
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_var)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        ttk.Button(input_frame, text="➕", width=3, command=self._add_item).pack(side=tk.LEFT, padx=2)
        ttk.Button(input_frame, text="➖", width=3, command=self._remove_item).pack(side=tk.LEFT, padx=2)
        
        self.input_entry.bind('<Return>', lambda e: self._add_item())
    
    def _add_item(self):
        """添加项"""
        item = self.input_var.get().strip()
        if item and item not in self.items:
            self.items.append(item)
            self.listbox.insert(tk.END, item)
            self.input_var.set("")
            self._notify_change()
    
    def _remove_item(self):
        """移除选中项"""
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            self.items.pop(idx)
            self.listbox.delete(idx)
            self._notify_change()
    
    def get_value(self) -> List[str]:
        return self.items.copy()
    
    def set_value(self, value: Any):
        self.items = list(value) if value else []
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)


class StructArrayEditorWidget(PropertyWidget):
    """结构体数组编辑器"""
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 struct_def: StructDef = None, on_change: Callable = None):
        self.struct_def = struct_def
        self.items: List[dict] = []
        super().__init__(parent, prop_def, on_change)
    
    def _create_widget(self):
        # 标签和展开按钮
        header = ttk.Frame(self.frame)
        header.pack(fill=tk.X, pady=2)
        
        ttk.Label(header, text=f"{self.prop_def.display_name} ({len(self.items)})").pack(side=tk.LEFT, padx=5)
        ttk.Button(header, text="➕ 添加", command=self._add_item).pack(side=tk.RIGHT, padx=5)
        
        # 列表容器
        self.list_frame = ttk.Frame(self.frame)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=5)
    
    def _add_item(self):
        """添加新项"""
        if not self.struct_def:
            return
        
        # 创建编辑对话框
        dialog = tk.Toplevel(self.frame)
        dialog.title(f"添加 {self.struct_def.name}")
        dialog.geometry("500x400")
        dialog.transient(self.frame)
        dialog.grab_set()
        
        # 创建属性编辑器
        values = {}
        widgets = {}
        
        for prop_name, prop in self.struct_def.properties.items():
            frame = ttk.Frame(dialog)
            frame.pack(fill=tk.X, padx=10, pady=5)
            
            widget = TextInputWidget(frame, prop)
            widget.pack(fill=tk.X)
            widgets[prop_name] = widget
        
        def on_save():
            for name, widget in widgets.items():
                values[name] = widget.get_value()
            self.items.append(values)
            self._refresh_list()
            self._notify_change()
            dialog.destroy()
        
        ttk.Button(dialog, text="保存", command=on_save).pack(pady=20)
    
    def _refresh_list(self):
        """刷新列表显示"""
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        for i, item in enumerate(self.items):
            row = ttk.Frame(self.list_frame)
            row.pack(fill=tk.X, pady=1)
            
            # 显示简要信息
            summary = ", ".join(f"{k}={v}" for k, v in list(item.items())[:2])
            ttk.Label(row, text=f"[{i}] {summary[:50]}...").pack(side=tk.LEFT, padx=5)
            
            ttk.Button(row, text="✏️", width=3,
                       command=lambda idx=i: self._edit_item(idx)).pack(side=tk.RIGHT, padx=2)
            ttk.Button(row, text="🗑️", width=3,
                       command=lambda idx=i: self._remove_item(idx)).pack(side=tk.RIGHT, padx=2)
    
    def _edit_item(self, index: int):
        """编辑项"""
        # TODO: 实现编辑对话框
        pass
    
    def _remove_item(self, index: int):
        """移除项"""
        self.items.pop(index)
        self._refresh_list()
        self._notify_change()
    
    def get_value(self) -> List[dict]:
        return self.items.copy()
    
    def set_value(self, value: Any):
        self.items = list(value) if value else []
        self._refresh_list()
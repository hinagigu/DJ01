#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 通用资产编辑器基类
根据 schema 自动生成编辑器界面
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Any, List, Optional, Callable
from abc import ABC, abstractmethod
import json
import os

from .schema_loader import SchemaLoader, DataAssetDef, PropertyDef, StructDef
from .property_widgets import (
    PropertyWidget,
    TextInputWidget,
    SpinBoxWidget,
    CheckboxWidget,
    ComboBoxWidget,
    TagSelectorWidget,
    AssetPickerWidget,
    AssetPickerListWidget,
    StringListWidget,
    StructArrayEditorWidget,
)


class BaseAssetEditor(ABC):
    """
    通用资产编辑器基类
    根据 schema 定义自动生成编辑界面
    """
    
    def __init__(self, parent: tk.Widget, asset_type: str, app=None):
        """
        初始化编辑器
        
        Args:
            parent: 父级 Widget
            asset_type: 资产类型（如 "Experience", "PawnData"）
            app: 主应用实例
        """
        self.parent = parent
        self.asset_type = asset_type
        self.app = app
        
        # 加载 schema
        self.schema_loader = SchemaLoader()
        self.asset_def = self.schema_loader.get_data_asset_def(asset_type)
        
        if not self.asset_def:
            raise ValueError(f"未找到资产类型定义: {asset_type}")
        
        # 当前编辑的资产
        self.current_asset_name: str = ""
        self.current_asset_data: Dict[str, Any] = {}
        
        # 所有资产数据
        self.assets: Dict[str, Dict[str, Any]] = {}
        
        # 属性控件映射
        self.property_widgets: Dict[str, PropertyWidget] = {}
        
        # 创建 UI
        self._create_ui()
        
        # 加载数据
        self.load_data()
    
    def _create_ui(self):
        """创建 UI 布局"""
        # 主框架 - 左右分栏
        self.main_frame = ttk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 左侧 - 资产列表
        self._create_asset_list()
        
        # 右侧 - 属性编辑器
        self._create_property_editor()
    
    def _create_asset_list(self):
        """创建资产列表面板"""
        list_frame = ttk.LabelFrame(self.main_frame, text=f"{self.asset_def.icon} {self.asset_def.display_name}列表")
        self.main_frame.add(list_frame, weight=1)
        
        # 工具栏
        toolbar = ttk.Frame(list_frame)
        toolbar.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(toolbar, text="➕ 新建", command=self._new_asset).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📋 复制", command=self._duplicate_asset).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🗑️ 删除", command=self._delete_asset).pack(side=tk.LEFT, padx=2)
        
        # 搜索框
        search_frame = ttk.Frame(list_frame)
        search_frame.pack(fill=tk.X, padx=5, pady=2)
        
        ttk.Label(search_frame, text="🔍").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self._on_search_changed)
        ttk.Entry(search_frame, textvariable=self.search_var).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # 资产列表
        list_container = ttk.Frame(list_frame)
        list_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.asset_listbox = tk.Listbox(list_container, font=("Consolas", 10))
        self.asset_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=self.asset_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.asset_listbox.config(yscrollcommand=scrollbar.set)
        
        # 绑定选择事件
        self.asset_listbox.bind('<<ListboxSelect>>', self._on_asset_selected)
        self.asset_listbox.bind('<Double-1>', self._on_asset_double_click)
    
    def _create_property_editor(self):
        """创建属性编辑器面板"""
        editor_frame = ttk.LabelFrame(self.main_frame, text="属性编辑")
        self.main_frame.add(editor_frame, weight=3)
        
        # 资产名称
        name_frame = ttk.Frame(editor_frame)
        name_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(name_frame, text="资产名称:", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(name_frame, textvariable=self.name_var, width=40, font=("Arial", 10))
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(name_frame, text="💾 保存", command=self._save_current).pack(side=tk.RIGHT, padx=5)
        
        # 描述信息
        if self.asset_def.description:
            desc_label = ttk.Label(editor_frame, text=self.asset_def.description, 
                                   foreground="gray", font=("Arial", 9))
            desc_label.pack(fill=tk.X, padx=10, pady=5)
        
        # 分隔符
        ttk.Separator(editor_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # 属性编辑区（带滚动）
        canvas = tk.Canvas(editor_frame)
        scrollbar = ttk.Scrollbar(editor_frame, orient=tk.VERTICAL, command=canvas.yview)
        self.props_frame = ttk.Frame(canvas)
        
        self.props_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.props_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 绑定鼠标滚轮
        canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        
        # 根据 schema 生成属性控件
        self._create_property_widgets()
    
    def _create_property_widgets(self):
        """根据 schema 创建属性控件"""
        # 按类别分组
        categories = self.asset_def.get_properties_by_category()
        
        for category, props in categories.items():
            # 类别标签
            cat_frame = ttk.LabelFrame(self.props_frame, text=category)
            cat_frame.pack(fill=tk.X, padx=5, pady=5)
            
            for prop in props:
                widget = self._create_widget_for_property(cat_frame, prop)
                if widget:
                    widget.pack(fill=tk.X, padx=5, pady=3)
                    self.property_widgets[prop.name] = widget
    
    def _create_widget_for_property(self, parent: tk.Widget, prop: PropertyDef) -> Optional[PropertyWidget]:
        """根据属性定义创建对应的控件"""
        on_change = lambda name, value: self._on_property_changed(name, value)
        
        widget_type = prop.widget
        
        if widget_type == "text_input":
            return TextInputWidget(parent, prop, on_change)
        
        elif widget_type == "spin_box":
            return SpinBoxWidget(parent, prop, on_change)
        
        elif widget_type == "checkbox":
            return CheckboxWidget(parent, prop, on_change)
        
        elif widget_type == "combobox":
            return ComboBoxWidget(parent, prop, [], on_change)
        
        elif widget_type == "tag_selector":
            tags = self._get_available_tags(prop.categories)
            return TagSelectorWidget(parent, prop, tags, on_change)
        
        elif widget_type == "asset_picker":
            assets = self._get_available_assets(prop.asset_class, prop.content_path)
            return AssetPickerWidget(parent, prop, assets, on_change)
        
        elif widget_type == "asset_picker_list":
            assets = self._get_available_assets(prop.asset_class, prop.content_path)
            return AssetPickerListWidget(parent, prop, assets, on_change)
        
        elif widget_type == "string_list":
            return StringListWidget(parent, prop, on_change)
        
        elif widget_type == "struct_array_editor":
            struct_def = self.schema_loader.get_struct_def(prop.struct_type)
            return StructArrayEditorWidget(parent, prop, struct_def, on_change)
        
        elif widget_type == "class_picker":
            # 类选择器 - 简化为文本输入
            return TextInputWidget(parent, prop, on_change)
        
        else:
            # 默认文本输入
            return TextInputWidget(parent, prop, on_change)
    
    def _get_available_tags(self, categories: str = "") -> List[str]:
        """获取可用的 Gameplay 标签"""
        # 从配置或其他来源加载标签
        # 这里可以读取 GameplayTagDefinitions.json
        tags_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "..", "AttributeGenerator", "configs", "tags.json"
        )
        if os.path.exists(tags_file):
            try:
                with open(tags_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_tags = [t.get("full_tag", "") for t in data.get("tags", [])]
                    if categories:
                        return [t for t in all_tags if t.startswith(categories)]
                    return all_tags
            except:
                pass
        return []
    
    def _get_available_assets(self, asset_class: str, content_path: str) -> List[str]:
        """获取可用的资产列表"""
        # 从注册表获取
        if self.app and hasattr(self.app, 'registry'):
            # 根据 asset_class 映射到资产类型
            type_map = {
                "DJ01PawnData": "PawnData",
                "DJ01InputConfig": "InputConfig",
                "DJ01AbilitySet": "AbilitySet",
                "DJ01ExperienceActionSet": "ActionSet",
            }
            asset_type = type_map.get(asset_class, "")
            if asset_type:
                assets = self.app.registry.get_by_type(asset_type)
                return [a.asset_path for a in assets]
        
        # 返回示例路径
        if content_path:
            return [f"{content_path}/ExampleAsset"]
        return []
    
    # ===== 事件处理 =====
    
    def _on_search_changed(self, *args):
        """搜索内容变化"""
        search = self.search_var.get().lower()
        self.asset_listbox.delete(0, tk.END)
        for name in self.assets.keys():
            if search in name.lower():
                self.asset_listbox.insert(tk.END, name)
    
    def _on_asset_selected(self, event):
        """资产列表选择变化"""
        sel = self.asset_listbox.curselection()
        if sel:
            name = self.asset_listbox.get(sel[0])
            self._load_asset(name)
    
    def _on_asset_double_click(self, event):
        """双击资产"""
        # 可以实现重命名等功能
        pass
    
    def _on_property_changed(self, name: str, value: Any):
        """属性值变化"""
        if self.current_asset_name:
            self.current_asset_data[name] = value
    
    # ===== 资产操作 =====
    
    def _new_asset(self):
        """新建资产"""
        from tkinter import simpledialog
        name = simpledialog.askstring("新建", f"输入{self.asset_def.display_name}名称:",
                                       parent=self.parent)
        if name:
            if name in self.assets:
                messagebox.showerror("错误", f"'{name}' 已存在")
                return
            
            # 创建空资产
            self.assets[name] = {}
            self._refresh_asset_list()
            
            # 选中新资产
            idx = list(self.assets.keys()).index(name)
            self.asset_listbox.selection_clear(0, tk.END)
            self.asset_listbox.selection_set(idx)
            self._load_asset(name)
    
    def _duplicate_asset(self):
        """复制资产"""
        if not self.current_asset_name:
            return
        
        from tkinter import simpledialog
        new_name = simpledialog.askstring("复制", "输入新名称:",
                                          initialvalue=f"{self.current_asset_name}_Copy",
                                          parent=self.parent)
        if new_name and new_name not in self.assets:
            self.assets[new_name] = self.current_asset_data.copy()
            self._refresh_asset_list()
    
    def _delete_asset(self):
        """删除资产"""
        if not self.current_asset_name:
            return
        
        if messagebox.askyesno("确认删除", f"确定要删除 '{self.current_asset_name}' 吗?"):
            del self.assets[self.current_asset_name]
            self.current_asset_name = ""
            self.current_asset_data = {}
            self._refresh_asset_list()
            self._clear_property_widgets()
    
    def _load_asset(self, name: str):
        """加载资产到编辑器"""
        self.current_asset_name = name
        self.current_asset_data = self.assets.get(name, {}).copy()
        
        self.name_var.set(name)
        
        # 更新所有属性控件
        for prop_name, widget in self.property_widgets.items():
            value = self.current_asset_data.get(prop_name)
            widget.set_value(value)
    
    def _save_current(self):
        """保存当前资产"""
        new_name = self.name_var.get().strip()
        if not new_name:
            messagebox.showerror("错误", "资产名称不能为空")
            return
        
        # 收集所有属性值
        for prop_name, widget in self.property_widgets.items():
            self.current_asset_data[prop_name] = widget.get_value()
        
        # 处理重命名
        if self.current_asset_name and new_name != self.current_asset_name:
            del self.assets[self.current_asset_name]
        
        self.assets[new_name] = self.current_asset_data.copy()
        self.current_asset_name = new_name
        
        self._refresh_asset_list()
        self.save_config()
        
        if self.app:
            self.app.show_status(f"已保存: {new_name}")
    
    def _refresh_asset_list(self):
        """刷新资产列表"""
        self.asset_listbox.delete(0, tk.END)
        for name in sorted(self.assets.keys()):
            self.asset_listbox.insert(tk.END, name)
    
    def _clear_property_widgets(self):
        """清空属性控件"""
        self.name_var.set("")
        for widget in self.property_widgets.values():
            widget.set_value(None)
    
    # ===== 数据持久化 =====
    
    @abstractmethod
    def get_config_file_path(self) -> str:
        """获取配置文件路径"""
        pass
    
    def load_data(self):
        """加载配置数据"""
        config_path = self.get_config_file_path()
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.assets = data.get(self.asset_type.lower(), {})
                    self._refresh_asset_list()
            except Exception as e:
                print(f"加载配置失败: {e}")
    
    def save_config(self):
        """保存配置数据"""
        config_path = self.get_config_file_path()
        
        try:
            # 读取现有数据
            existing_data = {}
            if os.path.exists(config_path):
                with open(config_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            
            # 更新当前类型的数据
            existing_data[self.asset_type.lower()] = self.assets
            existing_data["version"] = "1.0"
            
            # 确保目录存在
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            
            # 写入文件
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存配置失败: {e}")
            messagebox.showerror("错误", f"保存失败: {e}")
    
    def save_current_edit(self):
        """保存当前编辑（供 Ctrl+S 调用）"""
        if self.current_asset_name:
            self._save_current()
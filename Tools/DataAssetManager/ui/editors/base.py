#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 通用资产编辑器基类
职责：提供资产编辑的通用界面和逻辑
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import Dict, Any, List, Optional
import os
import sys

# 确保父目录在路径中
_tool_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _tool_dir not in sys.path:
    sys.path.insert(0, _tool_dir)

from ui.widgets import PropertyWidget
from ui.widgets.factory import WidgetFactory
from core.schema_loader import SchemaLoader
from core.schema import DataAssetDef
from core.data_manager import DataManager
from core.options_scanner import OptionsScanner


class BaseAssetEditor:
    """通用资产编辑器"""
    
    def __init__(self, parent: tk.Widget, asset_type: str, 
                 schema_loader: SchemaLoader, data_manager: DataManager,
                 app=None, options_scanner: OptionsScanner = None):
        self.parent = parent
        self.asset_type = asset_type
        self.schema_loader = schema_loader
        self.data_manager = data_manager
        self.app = app
        self.options_scanner = options_scanner
        
        # 获取资产定义
        self.asset_def = schema_loader.get_data_asset_def(asset_type)
        if not self.asset_def:
            raise ValueError(f"未找到资产类型: {asset_type}")
        
        # 控件工厂（传入选项扫描器）
        self.widget_factory = WidgetFactory(schema_loader, options_scanner)
        
        # 当前编辑状态
        self.current_name: str = ""
        self.current_data: Dict[str, Any] = {}
        self.property_widgets: Dict[str, PropertyWidget] = {}
        
        # 加载数据
        self.assets: Dict[str, Dict[str, Any]] = {}
        
        # 创建 UI
        self._create_ui()
        self._load_data()
    
    def _create_ui(self):
        """创建界面"""
        # 主框架
        self.paned = ttk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)
        
        # 左侧列表
        self._create_list_panel()
        
        # 右侧编辑器
        self._create_editor_panel()
    
    def _create_list_panel(self):
        """创建左侧列表面板"""
        list_frame = ttk.LabelFrame(self.paned, 
                                     text=f"{self.asset_def.icon} {self.asset_def.display_name}")
        self.paned.add(list_frame, weight=1)
        
        # 工具栏
        toolbar = ttk.Frame(list_frame)
        toolbar.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(toolbar, text="➕", width=3, 
                   command=self._new_asset).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="📋", width=3, 
                   command=self._duplicate_asset).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="🗑️", width=3, 
                   command=self._delete_asset).pack(side=tk.LEFT, padx=2)
        
        # 搜索
        search_frame = ttk.Frame(list_frame)
        search_frame.pack(fill=tk.X, padx=5, pady=2)
        
        ttk.Label(search_frame, text="🔍").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self._on_search)
        ttk.Entry(search_frame, textvariable=self.search_var).pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # 列表
        list_container = ttk.Frame(list_frame)
        list_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.listbox = tk.Listbox(list_container, font=("Consolas", 10),
                                   exportselection=False)  # 保持选中状态
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, 
                                  command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        self.listbox.bind('<<ListboxSelect>>', self._on_select)
    
    def _create_editor_panel(self):
        """创建右侧编辑面板"""
        editor_frame = ttk.LabelFrame(self.paned, text="属性编辑")
        self.paned.add(editor_frame, weight=3)
        
        # 名称栏
        name_frame = ttk.Frame(editor_frame)
        name_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(name_frame, text="资产名称:", 
                  font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        self.name_var = tk.StringVar()
        ttk.Entry(name_frame, textvariable=self.name_var, 
                  width=40).pack(side=tk.LEFT, padx=5)
        
        # 状态提示标签
        self.status_label = ttk.Label(name_frame, text="", foreground="green")
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(name_frame, text="💾 保存 (Ctrl+S)", 
                   command=self._save_current).pack(side=tk.RIGHT, padx=5)
        
        # 绑定快捷键
        self.parent.winfo_toplevel().bind('<Control-s>', self._on_ctrl_s)
        
        # 描述
        if self.asset_def.description:
            ttk.Label(editor_frame, text=self.asset_def.description,
                      foreground="gray").pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Separator(editor_frame).pack(fill=tk.X, padx=10, pady=5)
        
        # 可滚动属性区
        self._create_scrollable_props(editor_frame)
    
    def _create_scrollable_props(self, parent):
        """创建可滚动的属性区域"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        self.props_frame = ttk.Frame(canvas)
        
        self.props_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.props_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 鼠标滚轮
        def on_wheel(e):
            canvas.yview_scroll(int(-1*(e.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", on_wheel)
        
        # 创建属性控件
        self._create_property_widgets()
    
    def _create_property_widgets(self):
        """创建属性控件"""
        categories = self.asset_def.get_properties_by_category()
        
        for category, props in categories.items():
            cat_frame = ttk.LabelFrame(self.props_frame, text=category)
            cat_frame.pack(fill=tk.X, padx=5, pady=5)
            
            for prop in props:
                widget = self.widget_factory.create(
                    cat_frame, prop, self._on_prop_change)
                if widget:
                    widget.pack(fill=tk.X, padx=5, pady=3)
                    self.property_widgets[prop.name] = widget
    
    # ===== 事件处理 =====
    
    def _on_search(self, *args):
        search = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for name in sorted(self.assets.keys()):
            if search in name.lower():
                self.listbox.insert(tk.END, name)
    
    def _on_select(self, event):
        sel = self.listbox.curselection()
        if sel:
            display = self.listbox.get(sel[0])
            name = self._get_asset_name_from_display(display)
            self._load_asset(name)
    
    def _on_prop_change(self, name: str, value: Any):
        if self.current_name:
            self.current_data[name] = value
    
    def _on_ctrl_s(self, event=None):
        """Ctrl+S 快捷键保存"""
        if self.current_name:
            self._save_current()
        return "break"  # 阻止事件继续传播
    
    def _show_save_status(self, message: str, is_error: bool = False):
        """显示保存状态提示"""
        self.status_label.config(
            text=message,
            foreground="red" if is_error else "green"
        )
        # 3秒后清除提示
        self.parent.after(3000, lambda: self.status_label.config(text=""))
    
    # ===== 资产操作 =====
    
    def _new_asset(self):
        name = simpledialog.askstring("新建", "输入名称:", parent=self.parent)
        if name:
            if name in self.assets:
                messagebox.showerror("错误", f"'{name}' 已存在")
                return
            self.assets[name] = {}
            self._refresh_list()
            self._select_asset(name)
    
    def _duplicate_asset(self):
        if not self.current_name:
            return
        new_name = simpledialog.askstring(
            "复制", "输入新名称:",
            initialvalue=f"{self.current_name}_Copy",
            parent=self.parent
        )
        if new_name and new_name not in self.assets:
            self.assets[new_name] = self.current_data.copy()
            self._refresh_list()
            self._select_asset(new_name)
    
    def _delete_asset(self):
        if not self.current_name:
            return
        if messagebox.askyesno("确认", f"删除 '{self.current_name}'?"):
            del self.assets[self.current_name]
            self.current_name = ""
            self.current_data = {}
            self._refresh_list()
            self._clear_editor()
    
    def _load_asset(self, name: str):
        self.current_name = name
        self.current_data = self.assets.get(name, {}).copy()
        self.name_var.set(name)
        
        for prop_name, widget in self.property_widgets.items():
            widget.set_value(self.current_data.get(prop_name))
    
    def _save_current(self):
        new_name = self.name_var.get().strip()
        if not new_name:
            self._show_save_status("❌ 名称不能为空", is_error=True)
            return
        
        # 收集数据
        for prop_name, widget in self.property_widgets.items():
            self.current_data[prop_name] = widget.get_value()
        
        # 处理重命名
        if self.current_name and new_name != self.current_name:
            if new_name in self.assets:
                self._show_save_status(f"❌ '{new_name}' 已存在", is_error=True)
                return
            del self.assets[self.current_name]
        
        self.assets[new_name] = self.current_data.copy()
        self.current_name = new_name
        
        self._refresh_list()
        self._select_asset(new_name)  # 保存后重新选中
        self._save_to_file()
        self._show_save_status(f"✅ 已保存: {new_name}")
    
    def _refresh_list(self):
        self.listbox.delete(0, tk.END)
        for name in sorted(self.assets.keys()):
            data = self.assets[name]
            # 标记未配置的扫描资产
            if data.get("_scanned") and len(data) <= 2:
                display = f"📂 {name} (未配置)"
            else:
                display = f"✅ {name}"
            self.listbox.insert(tk.END, display)
    
    def _get_asset_name_from_display(self, display: str) -> str:
        """从显示文本中提取资产名称"""
        # 移除前缀图标和后缀
        name = display
        for prefix in ["📂 ", "✅ "]:
            if name.startswith(prefix):
                name = name[len(prefix):]
        if " (未配置)" in name:
            name = name.replace(" (未配置)", "")
        return name
    
    def _select_asset(self, name: str):
        try:
            idx = list(sorted(self.assets.keys())).index(name)
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(idx)
            self._load_asset(name)
        except ValueError:
            pass
    
    def _clear_editor(self):
        self.name_var.set("")
        for widget in self.property_widgets.values():
            widget.set_value(None)
    
    # ===== 数据持久化 =====
    
    def _load_data(self):
        """加载数据：合并已有配置和扫描到的资产"""
        # 1. 加载已保存的配置
        self.assets = self.data_manager.load_assets(self.asset_type)
        
        # 2. 合并扫描到的资产（作为占位项，尚未配置属性）
        if self.options_scanner:
            scanned_items = self._get_scanned_items()
            for item in scanned_items:
                name = item.get("name", "")
                if name and name not in self.assets:
                    # 添加扫描到的资产，标记为未配置
                    self.assets[name] = {
                        "_scanned": True,  # 标记：来自扫描
                        "_asset_path": item.get("asset_path", ""),
                    }
        
        self._refresh_list()
    
    def _get_scanned_items(self) -> list:
        """获取扫描到的资产列表"""
        if not self.options_scanner:
            return []
        
        scan_method_map = {
            "Experience": lambda: [],  # Experience 暂无扫描
            "PawnData": self.options_scanner.get_pawn_data_options,
            "InputConfig": self.options_scanner.get_input_config_options,
            "AbilitySet": self.options_scanner.get_ability_set_options,
            "ActionSet": self.options_scanner.get_action_set_options,
        }
        
        method = scan_method_map.get(self.asset_type)
        if method:
            return method()
        return []
    
    def _save_to_file(self):
        self.data_manager.save_assets(self.asset_type, self.assets)
    
    def _show_status(self, msg: str):
        if self.app and hasattr(self.app, 'show_status'):
            self.app.show_status(msg)
    
    def save_current_edit(self):
        """保存当前编辑（Ctrl+S）"""
        if self.current_name:
            self._save_current()
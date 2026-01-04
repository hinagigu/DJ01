#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - 组件树面板
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import Optional, List, Callable, Tuple
from copy import deepcopy

from .schema_models import ComponentData, WidgetSchema
from .editor_dialogs import ComponentTypeDialog


class ComponentTreePanel(ttk.LabelFrame):
    """组件树面板"""
    
    def __init__(self, parent, widget_types: dict, component_types: List[str]):
        super().__init__(parent, text="🌳 组件树", padding="5")
        
        self.widget_types = widget_types
        self.component_types = component_types
        self.schema: Optional[WidgetSchema] = None
        self._clipboard: Optional[ComponentData] = None
        
        # 回调
        self.on_select: Optional[Callable[[ComponentData], None]] = None
        self.on_changed: Optional[Callable[[], None]] = None
        
        self._create_ui()
    
    def _create_ui(self):
        """创建 UI"""
        # 工具栏
        toolbar = ttk.Frame(self)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(toolbar, text="+ 添加", command=self._add_component).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="+ 子组件", command=self._add_child_component).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="- 删除", command=self._delete_component).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        ttk.Button(toolbar, text="↑", command=self._move_up, width=3).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="↓", command=self._move_down, width=3).pack(side=tk.LEFT, padx=2)
        
        # 组件树
        tree_frame = ttk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        self.tree = ttk.Treeview(tree_frame, show='tree headings', columns=('type', 'comment'))
        self.tree.heading('#0', text='组件名')
        self.tree.heading('type', text='类型')
        self.tree.heading('comment', text='注释')
        self.tree.column('#0', width=150)
        self.tree.column('type', width=100)
        self.tree.column('comment', width=150)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # 绑定事件
        self.tree.bind('<<TreeviewSelect>>', self._on_select)
        self.tree.bind('<Double-1>', self._on_double_click)
        self.tree.bind('<Button-3>', self._show_context_menu)
        self.tree.bind('<Delete>', lambda e: self._delete_component())
        self.tree.bind('<F2>', lambda e: self._rename_component())
        
        # 右键菜单
        self._create_context_menu()
    
    def _create_context_menu(self):
        """创建右键菜单"""
        self.context_menu = tk.Menu(self.tree, tearoff=0)
        self.context_menu.add_command(label="添加子组件", command=self._add_child_component)
        self.context_menu.add_command(label="重命名 (F2)", command=self._rename_component)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="复制", command=self._copy_component)
        self.context_menu.add_command(label="粘贴", command=self._paste_component)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="删除 (Del)", command=self._delete_component)
    
    def _show_context_menu(self, event):
        """显示右键菜单"""
        item = self.tree.identify_row(event.y)
        if item:
            self.tree.selection_set(item)
            self.context_menu.tk_popup(event.x_root, event.y_root)
    
    def set_schema(self, schema: Optional[WidgetSchema]):
        """设置 Schema"""
        self.schema = schema
        self.refresh()
    
    def refresh(self):
        """刷新组件树"""
        self.tree.delete(*self.tree.get_children())
        
        if not self.schema:
            return
        
        def add_component(comp: ComponentData, parent: str = ""):
            item_id = self.tree.insert(
                parent, 'end',
                text=comp.name,
                values=(comp.type, comp.comment),
                open=True
            )
            for child in comp.children:
                add_component(child, item_id)
        
        for comp in self.schema.components:
            add_component(comp)
    
    def get_selected_component(self) -> Optional[Tuple[ComponentData, List[ComponentData], int]]:
        """获取选中的组件 (组件, 父列表, 索引)"""
        selection = self.tree.selection()
        if not selection or not self.schema:
            return None
        return self._find_component_by_item(selection[0])
    
    def _find_component_by_item(self, item_id: str) -> Optional[Tuple[ComponentData, List[ComponentData], int]]:
        """根据树节点 ID 查找组件"""
        if not self.schema:
            return None
        
        def search(components: List[ComponentData], parent_item: str = "") -> Optional[Tuple[ComponentData, List[ComponentData], int]]:
            children = self.tree.get_children(parent_item)
            for i, comp in enumerate(components):
                if i < len(children) and children[i] == item_id:
                    return (comp, components, i)
                if i < len(children):
                    result = search(comp.children, children[i])
                    if result:
                        return result
            return None
        
        return search(self.schema.components)
    
    def _get_all_names(self) -> set:
        """获取所有组件名称"""
        names = set()
        
        def collect(components: List[ComponentData]):
            for comp in components:
                names.add(comp.name)
                collect(comp.children)
        
        if self.schema:
            collect(self.schema.components)
        return names
    
    def _generate_unique_name(self, base_name: str) -> str:
        """生成唯一名称"""
        existing = self._get_all_names()
        name = base_name
        counter = 1
        while name in existing:
            name = f"{base_name}_{counter}"
            counter += 1
        return name
    
    def _select_component_type(self) -> Optional[str]:
        """选择组件类型"""
        dialog = ComponentTypeDialog(self.winfo_toplevel(), self.component_types, self.widget_types)
        self.wait_window(dialog)
        return dialog.result
    
    def _notify_changed(self):
        """通知变更"""
        if self.on_changed:
            self.on_changed()
    
    # ========== 操作 ==========
    
    def _on_select(self, event):
        """选择事件"""
        result = self.get_selected_component()
        if result and self.on_select:
            self.on_select(result[0])
    
    def _on_double_click(self, event):
        """双击重命名"""
        self._rename_component()
    
    def _add_component(self):
        """添加顶级组件"""
        if not self.schema:
            return
        
        comp_type = self._select_component_type()
        if not comp_type:
            return
        
        name = self._generate_unique_name(comp_type)
        new_comp = ComponentData(name=name, type=comp_type)
        self.schema.components.append(new_comp)
        
        self.refresh()
        self._notify_changed()
    
    def _add_child_component(self):
        """添加子组件"""
        if not self.schema:
            return
        
        result = self.get_selected_component()
        if not result:
            messagebox.showwarning("提示", "请先选择父组件")
            return
        
        parent_comp, _, _ = result
        
        # 检查是否支持子组件
        type_info = self.widget_types.get("types", {}).get(parent_comp.type, {})
        if not type_info.get("is_container", True):
            messagebox.showwarning("提示", f"{parent_comp.type} 不支持子组件")
            return
        
        comp_type = self._select_component_type()
        if not comp_type:
            return
        
        name = self._generate_unique_name(comp_type)
        new_comp = ComponentData(name=name, type=comp_type)
        parent_comp.children.append(new_comp)
        
        self.refresh()
        self._notify_changed()
    
    def _delete_component(self):
        """删除组件"""
        result = self.get_selected_component()
        if not result:
            return
        
        comp, parent_list, index = result
        
        if messagebox.askyesno("确认", f"确定删除组件 '{comp.name}' 及其所有子组件？"):
            del parent_list[index]
            self.refresh()
            self._notify_changed()
    
    def _rename_component(self):
        """重命名组件"""
        result = self.get_selected_component()
        if not result:
            return
        
        comp, _, _ = result
        
        new_name = simpledialog.askstring("重命名", "新名称:", initialvalue=comp.name)
        if new_name and new_name != comp.name:
            existing = self._get_all_names()
            existing.discard(comp.name)
            if new_name in existing:
                messagebox.showwarning("警告", f"组件名 '{new_name}' 已存在")
                return
            
            comp.name = new_name
            self.refresh()
            self._notify_changed()
    
    def _copy_component(self):
        """复制组件"""
        result = self.get_selected_component()
        if result:
            self._clipboard = deepcopy(result[0])
    
    def _paste_component(self):
        """粘贴组件"""
        if not self._clipboard or not self.schema:
            return
        
        new_comp = deepcopy(self._clipboard)
        
        # 重命名避免冲突
        existing = self._get_all_names()
        
        def make_unique(comp: ComponentData):
            if comp.name in existing:
                comp.name = self._generate_unique_name(comp.name)
            existing.add(comp.name)
            for child in comp.children:
                make_unique(child)
        
        make_unique(new_comp)
        
        # 粘贴到选中项或顶级
        result = self.get_selected_component()
        if result:
            result[0].children.append(new_comp)
        else:
            self.schema.components.append(new_comp)
        
        self.refresh()
        self._notify_changed()
    
    def _move_up(self):
        """上移"""
        result = self.get_selected_component()
        if not result:
            return
        
        _, parent_list, index = result
        if index > 0:
            parent_list[index], parent_list[index-1] = parent_list[index-1], parent_list[index]
            self.refresh()
            self._notify_changed()
    
    def _move_down(self):
        """下移"""
        result = self.get_selected_component()
        if not result:
            return
        
        _, parent_list, index = result
        if index < len(parent_list) - 1:
            parent_list[index], parent_list[index+1] = parent_list[index+1], parent_list[index]
            self.refresh()
            self._notify_changed()
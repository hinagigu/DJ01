#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 编辑器基类
提供通用快捷键绑定和基础行为
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from abc import ABC, abstractmethod
from typing import Callable, Optional, List, Dict


class BaseEditorUI(ABC):
    """
    编辑器基类 - 提供通用行为
    
    子类需要实现:
    - load_data(): 加载数据
    - save_config(): 保存配置
    - generate_code(): 生成代码
    - save_current_edit(): 保存当前编辑（Ctrl+S 调用）
    - _get_current_listbox(): 返回当前焦点的 Listbox（用于 F2/Delete）
    - _get_current_tree(): 返回当前焦点的 Treeview（用于 F2/Delete）
    """
    
    def __init__(self, parent, app):
        """
        初始化基类
        
        Args:
            parent: 父级 Frame
            app: 主应用实例（GASGeneratorApp）
        """
        self.parent = parent
        self.app = app
        self._edit_widget = None  # 当前编辑控件
        self._context_menus: Dict[tk.Widget, tk.Menu] = {}  # 存储右键菜单
        self._bind_shortcuts()
    
    def _bind_shortcuts(self):
        """绑定通用快捷键"""
        # F2 重命名
        self.parent.bind('<F2>', self._on_f2_rename)
        # Delete 删除
        self.parent.bind('<Delete>', self._on_delete_key)
        # Escape 取消编辑
        self.parent.bind('<Escape>', self._on_escape)
    
    def _on_f2_rename(self, event):
        """
        F2 重命名 - 通用处理
        子类可重写 _handle_listbox_rename 和 _handle_tree_rename 来自定义行为
        """
        # 检查焦点控件
        focused = self.parent.focus_get()
        
        # 如果是 Listbox
        if isinstance(focused, tk.Listbox):
            selection = focused.curselection()
            if selection:
                self._handle_listbox_rename(focused, selection[0])
            return "break"
        
        # 如果是 Treeview
        if isinstance(focused, ttk.Treeview):
            selection = focused.selection()
            if selection:
                self._handle_tree_rename(focused, selection[0])
            return "break"
    
    def _handle_listbox_rename(self, listbox: tk.Listbox, index: int):
        """
        处理 Listbox 项目重命名
        子类可重写此方法自定义重命名逻辑
        
        Args:
            listbox: Listbox 控件
            index: 选中项索引
        """
        # 默认实现：在原位置创建 Entry 进行编辑
        current_text = listbox.get(index)
        
        # 获取项目位置
        bbox = listbox.bbox(index)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        # 创建编辑 Entry
        self._destroy_edit_widget()
        
        entry = tk.Entry(listbox, font=listbox.cget('font'))
        entry.insert(0, current_text)
        entry.select_range(0, tk.END)
        entry.place(x=x, y=y, width=width, height=height)
        entry.focus_set()
        
        def finish_edit(save=True):
            if self._edit_widget is None:
                return
            new_text = entry.get().strip()
            self._destroy_edit_widget()
            
            if save and new_text and new_text != current_text:
                # 调用子类的重命名回调
                self._on_listbox_item_renamed(listbox, index, current_text, new_text)
        
        entry.bind('<Return>', lambda e: finish_edit(True))
        entry.bind('<Escape>', lambda e: finish_edit(False))
        entry.bind('<FocusOut>', lambda e: finish_edit(True))
        
        self._edit_widget = entry
    
    def _handle_tree_rename(self, tree: ttk.Treeview, item: str):
        """
        处理 Treeview 项目重命名
        子类可重写此方法自定义重命名逻辑
        
        Args:
            tree: Treeview 控件
            item: 选中项 ID
        """
        # 默认实现：编辑第一列
        column = tree['columns'][0] if tree['columns'] else '#0'
        
        bbox = tree.bbox(item, column)
        if not bbox:
            return
        
        x, y, width, height = bbox
        current_text = tree.set(item, column) if column != '#0' else tree.item(item, 'text')
        
        self._destroy_edit_widget()
        
        entry = tk.Entry(tree)
        entry.insert(0, current_text)
        entry.select_range(0, tk.END)
        entry.place(x=x, y=y, width=width, height=height)
        entry.focus_set()
        
        def finish_edit(save=True):
            if self._edit_widget is None:
                return
            new_text = entry.get().strip()
            self._destroy_edit_widget()
            
            if save and new_text and new_text != current_text:
                self._on_tree_item_renamed(tree, item, column, current_text, new_text)
        
        entry.bind('<Return>', lambda e: finish_edit(True))
        entry.bind('<Escape>', lambda e: finish_edit(False))
        entry.bind('<FocusOut>', lambda e: finish_edit(True))
        
        self._edit_widget = entry
    
    def _on_delete_key(self, event):
        """Delete 键删除 - 通用处理"""
        focused = self.parent.focus_get()
        
        # 如果正在编辑，不处理删除
        if isinstance(focused, tk.Entry):
            return
        
        # Listbox 删除
        if isinstance(focused, tk.Listbox):
            selection = focused.curselection()
            if selection:
                self._handle_listbox_delete(focused, selection[0])
            return "break"
        
        # Treeview 删除
        if isinstance(focused, ttk.Treeview):
            selection = focused.selection()
            if selection:
                self._handle_tree_delete(focused, selection[0])
            return "break"
    
    def _on_escape(self, event):
        """Escape 取消编辑"""
        self._destroy_edit_widget()
    
    def _destroy_edit_widget(self):
        """销毁当前编辑控件"""
        if self._edit_widget:
            try:
                self._edit_widget.destroy()
            except:
                pass
            self._edit_widget = None
    
    # ===== 子类需要实现的回调 =====
    
    def _on_listbox_item_renamed(self, listbox: tk.Listbox, index: int, old_name: str, new_name: str):
        """
        Listbox 项目重命名回调 - 子类实现
        
        Args:
            listbox: Listbox 控件
            index: 项目索引
            old_name: 旧名称
            new_name: 新名称
        """
        pass  # 子类重写
    
    def _on_tree_item_renamed(self, tree: ttk.Treeview, item: str, column: str, old_value: str, new_value: str):
        """
        Treeview 项目重命名回调 - 子类实现
        
        Args:
            tree: Treeview 控件
            item: 项目 ID
            column: 列名
            old_value: 旧值
            new_value: 新值
        """
        pass  # 子类重写
    
    def _handle_listbox_delete(self, listbox: tk.Listbox, index: int):
        """
        Listbox 删除回调 - 子类实现
        
        Args:
            listbox: Listbox 控件
            index: 要删除的索引
        """
        pass  # 子类重写
    
    def _handle_tree_delete(self, tree: ttk.Treeview, item: str):
        """
        Treeview 删除回调 - 子类实现
        
        Args:
            tree: Treeview 控件
            item: 要删除的项目 ID
        """
        pass  # 子类重写
    
    # ===== 子类必须实现的抽象方法 =====
    
    @abstractmethod
    def load_data(self):
        """加载数据"""
        pass
    
    @abstractmethod
    def save_config(self):
        """保存配置到文件"""
        pass
    
    @abstractmethod
    def generate_code(self):
        """生成 C++ 代码"""
        pass
    
    @abstractmethod
    def save_current_edit(self):
        """保存当前编辑（Ctrl+S 调用）"""
        pass
    
    # ===== 右键菜单支持 =====
    
    def bind_context_menu(self, widget: tk.Widget, 
                          on_delete: Optional[Callable] = None,
                          on_rename: Optional[Callable] = None,
                          extra_items: Optional[List[tuple]] = None):
        """
        为控件绑定右键上下文菜单
        
        Args:
            widget: Treeview 或 Listbox 控件
            on_delete: 删除回调函数，接收 (widget, selected_item) 参数
            on_rename: 重命名回调函数，接收 (widget, selected_item) 参数
            extra_items: 额外的菜单项列表，格式为 [(label, callback), ...]
                         callback 接收 (widget, selected_item) 参数
                         如果 label 为 "-"，则添加分隔线
        
        使用示例:
            self.bind_context_menu(
                self.my_tree,
                on_delete=lambda w, item: self._delete_item(item),
                on_rename=lambda w, item: self._rename_item(item),
                extra_items=[
                    ("复制", lambda w, item: self._copy_item(item)),
                    ("-", None),  # 分隔线
                    ("移动到...", lambda w, item: self._move_item(item)),
                ]
            )
        """
        menu = tk.Menu(widget, tearoff=0)
        
        # 重命名选项
        if on_rename:
            menu.add_command(label="重命名 (F2)", 
                           command=lambda: self._execute_context_action(widget, on_rename))
        
        # 删除选项
        if on_delete:
            menu.add_command(label="删除 (Del)", 
                           command=lambda: self._execute_context_action(widget, on_delete))
        
        # 额外的菜单项
        if extra_items:
            if on_delete or on_rename:
                menu.add_separator()
            for item in extra_items:
                label, callback = item
                if label == "-":
                    menu.add_separator()
                elif callback:
                    menu.add_command(label=label,
                                   command=lambda cb=callback: self._execute_context_action(widget, cb))
        
        # 存储菜单引用
        self._context_menus[widget] = menu
        
        # 绑定右键事件（同时支持 Windows 和 macOS）
        widget.bind('<Button-3>', lambda e: self._show_context_menu(e, widget, menu))  # Windows/Linux
        widget.bind('<Button-2>', lambda e: self._show_context_menu(e, widget, menu))  # macOS
    
    def _show_context_menu(self, event, widget: tk.Widget, menu: tk.Menu):
        """显示右键菜单"""
        # 先选中点击的项目
        if isinstance(widget, ttk.Treeview):
            item = widget.identify_row(event.y)
            if item:
                widget.selection_set(item)
                widget.focus(item)
            else:
                return  # 没有点击到项目，不显示菜单
        elif isinstance(widget, tk.Listbox):
            index = widget.nearest(event.y)
            if index >= 0:
                widget.selection_clear(0, tk.END)
                widget.selection_set(index)
                widget.activate(index)
            else:
                return
        
        # 显示菜单
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()
    
    def _execute_context_action(self, widget: tk.Widget, callback: Callable):
        """执行右键菜单动作"""
        selected = None
        if isinstance(widget, ttk.Treeview):
            selection = widget.selection()
            if selection:
                selected = selection[0]
        elif isinstance(widget, tk.Listbox):
            selection = widget.curselection()
            if selection:
                selected = selection[0]
        
        if selected is not None and callback:
            callback(widget, selected)
    
    # ===== 工具方法 =====
    
    def show_status(self, message: str):
        """显示状态消息"""
        if self.app:
            self.app.show_status(message)
    
    def confirm_delete(self, item_name: str, item_type: str = "项目") -> bool:
        """
        确认删除对话框
        
        Args:
            item_name: 项目名称
            item_type: 项目类型描述
            
        Returns:
            用户是否确认删除
        """
        return messagebox.askyesno(
            "确认删除",
            f"确定要删除{item_type} \"{item_name}\" 吗？",
            parent=self.parent
        )
    
    def prompt_new_name(self, title: str, prompt: str, initial: str = "") -> str:
        """
        弹出输入框获取新名称
        
        Args:
            title: 对话框标题
            prompt: 提示文字
            initial: 初始值
            
        Returns:
            用户输入的名称，取消返回 None
        """
        return simpledialog.askstring(title, prompt, initialvalue=initial, parent=self.parent)
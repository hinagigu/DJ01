#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 编辑器基类
提供通用快捷键绑定和基础行为
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from abc import ABC, abstractmethod


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
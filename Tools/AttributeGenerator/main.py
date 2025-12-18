#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 主入口
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime
from collections import OrderedDict

from attribute_module import AttributeEditorUI, AttributeCodeGenerator
from execution_module import ExecutionEditorUI, ExecutionCodeGenerator
from tag_module import TagEditorUI, TagCodeGenerator


class GASGeneratorApp:
    """GAS 代码生成器主应用"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("DJ01 GAS 代码生成器")
        self.root.geometry("1200x800")
        
        self._create_ui()
        self._bind_shortcuts()
    
    def _create_ui(self):
        # 创建 Notebook（标签页）
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 1. 属性编辑器标签页
        attr_frame = ttk.Frame(self.notebook)
        self.notebook.add(attr_frame, text=" 📊 属性编辑器 ")
        self.attr_editor = AttributeEditorUI(attr_frame, self)
        
        # 2. 属性代码预览标签页
        attr_preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(attr_preview_frame, text=" 📄 属性代码预览 ")
        self._create_attr_preview(attr_preview_frame)
        
        # 3. Execution 编辑器标签页
        exec_frame = ttk.Frame(self.notebook)
        self.notebook.add(exec_frame, text=" ⚡ Execution 编辑器 ")
        self.exec_editor = ExecutionEditorUI(exec_frame, self)
        
        # 4. Execution 代码预览标签页
        exec_preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(exec_preview_frame, text=" 📄 Execution 代码预览 ")
        self._create_exec_preview(exec_preview_frame)
        
        # 5. GameplayTags 编辑器标签页
        tag_frame = ttk.Frame(self.notebook)
        self.notebook.add(tag_frame, text=" 🏷️ Tags 编辑器 ")
        self.tag_editor = TagEditorUI(tag_frame, self)
        
        # 6. Tags 代码预览标签页
        tag_preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(tag_preview_frame, text=" 📄 Tags 代码预览 ")
        self._create_tag_preview(tag_preview_frame)
        
        # 切换标签页时自动刷新预览
        self.notebook.bind('<<NotebookTabChanged>>', self._on_tab_changed)
    
    def _create_attr_preview(self, parent):
        """创建属性代码预览"""
        # 顶部控制栏
        top_frame = ttk.Frame(parent)
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(top_frame, text="文件类型:").pack(side=tk.LEFT, padx=5)
        self.attr_preview_type = tk.StringVar(value="header")
        ttk.Radiobutton(top_frame, text="Header (.h)", variable=self.attr_preview_type, 
                       value="header", command=self._update_attr_preview).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(top_frame, text="Source (.cpp)", variable=self.attr_preview_type, 
                       value="source", command=self._update_attr_preview).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(top_frame, text="🔄 刷新", command=self._update_attr_preview).pack(side=tk.RIGHT, padx=5)
        
        # 代码显示区
        self.attr_preview_text = scrolledtext.ScrolledText(
            parent, font=("Consolas", 10), wrap=tk.NONE)
        self.attr_preview_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 添加水平滚动条
        h_scroll = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.attr_preview_text.xview)
        h_scroll.pack(fill=tk.X, padx=10)
        self.attr_preview_text.config(xscrollcommand=h_scroll.set)
    
    def _create_exec_preview(self, parent):
        """创建 Execution 代码预览"""
        # 顶部控制栏
        top_frame = ttk.Frame(parent)
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(top_frame, text="选择 Execution:").pack(side=tk.LEFT, padx=5)
        self.exec_preview_select = tk.StringVar()
        self.exec_preview_combo = ttk.Combobox(top_frame, textvariable=self.exec_preview_select, 
                                                width=20, state='readonly')
        self.exec_preview_combo.pack(side=tk.LEFT, padx=5)
        self.exec_preview_combo.bind('<<ComboboxSelected>>', lambda e: self._update_exec_preview())
        
        ttk.Label(top_frame, text="文件类型:").pack(side=tk.LEFT, padx=15)
        self.exec_preview_type = tk.StringVar(value="header")
        ttk.Radiobutton(top_frame, text="Header (.h)", variable=self.exec_preview_type, 
                       value="header", command=self._update_exec_preview).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(top_frame, text="Source (.cpp)", variable=self.exec_preview_type, 
                       value="source", command=self._update_exec_preview).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(top_frame, text="🔄 刷新", command=self._update_exec_preview).pack(side=tk.RIGHT, padx=5)
        
        # 代码显示区
        self.exec_preview_text = scrolledtext.ScrolledText(
            parent, font=("Consolas", 10), wrap=tk.NONE)
        self.exec_preview_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 添加水平滚动条
        h_scroll = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.exec_preview_text.xview)
        h_scroll.pack(fill=tk.X, padx=10)
        self.exec_preview_text.config(xscrollcommand=h_scroll.set)
    
    def _create_tag_preview(self, parent):
        """创建 Tags 代码预览"""
        top_frame = ttk.Frame(parent)
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(top_frame, text="文件类型:").pack(side=tk.LEFT, padx=5)
        self.tag_preview_type = tk.StringVar(value="header")
        ttk.Radiobutton(top_frame, text="Header (.h)", variable=self.tag_preview_type, 
                       value="header", command=self._update_tag_preview).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(top_frame, text="Source (.cpp)", variable=self.tag_preview_type, 
                       value="source", command=self._update_tag_preview).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(top_frame, text="🔄 刷新", command=self._update_tag_preview).pack(side=tk.RIGHT, padx=5)
        
        self.tag_preview_text = scrolledtext.ScrolledText(
            parent, font=("Consolas", 10), wrap=tk.NONE)
        self.tag_preview_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        h_scroll = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.tag_preview_text.xview)
        h_scroll.pack(fill=tk.X, padx=10)
        self.tag_preview_text.config(xscrollcommand=h_scroll.set)
    
    def _on_tab_changed(self, event):
        """标签页切换时刷新预览"""
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab == 1:  # 属性代码预览
            self._update_attr_preview()
        elif current_tab == 3:  # Execution 代码预览
            self._refresh_exec_combo()
            self._update_exec_preview()
        elif current_tab == 5:  # Tags 代码预览
            self._update_tag_preview()
    
    def _update_attr_preview(self):
        """更新属性代码预览"""
        attribute_sets = OrderedDict()
        for attr in self.attr_editor.attributes:
            if attr.set_name not in attribute_sets:
                attribute_sets[attr.set_name] = []
            attribute_sets[attr.set_name].append(attr)
        
        if not attribute_sets:
            content = "// 没有属性定义\n// 请在「属性编辑器」中添加属性"
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.attr_preview_type.get() == "header":
                content = AttributeCodeGenerator.generate_header(attribute_sets, timestamp)
            else:
                content = AttributeCodeGenerator.generate_source(attribute_sets, timestamp)
        
        self.attr_preview_text.delete('1.0', tk.END)
        self.attr_preview_text.insert('1.0', content)
    
    def _refresh_exec_combo(self):
        """刷新 Execution 下拉列表"""
        names = [exe.name for exe in self.exec_editor.executions if exe.name]
        self.exec_preview_combo['values'] = names
        if names and not self.exec_preview_select.get():
            self.exec_preview_select.set(names[0])
    
    def _update_exec_preview(self):
        """更新 Execution 代码预览"""
        selected = self.exec_preview_select.get()
        
        # 查找选中的 Execution
        exe = None
        for e in self.exec_editor.executions:
            if e.name == selected:
                exe = e
                break
        
        if not exe:
            content = "// 没有 Execution 定义\n// 请在「Execution 编辑器」中添加"
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            header, source = ExecutionCodeGenerator.generate(exe, timestamp)
            content = header if self.exec_preview_type.get() == "header" else source
        
        self.exec_preview_text.delete('1.0', tk.END)
        self.exec_preview_text.insert('1.0', content)
    
    def _bind_shortcuts(self):
        self.root.bind('<Control-s>', lambda e: self._on_ctrl_s())
        self.root.bind('<Control-S>', lambda e: self._on_ctrl_s())
    
    def _update_tag_preview(self):
        """更新 Tags 代码预览"""
        tags_by_category = self.tag_editor.get_tags_by_category()
        
        if not tags_by_category:
            content = "// 没有标签定义\n// 请在「Tags 编辑器」中添加标签"
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.tag_preview_type.get() == "header":
                content = TagCodeGenerator.generate_header(tags_by_category, timestamp)
            else:
                content = TagCodeGenerator.generate_source(tags_by_category, timestamp)
        
        self.tag_preview_text.delete('1.0', tk.END)
        self.tag_preview_text.insert('1.0', content)
    
    def _on_ctrl_s(self):
        """Ctrl+S 保存当前编辑内容和配置"""
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab in [0, 1]:  # 属性相关标签页
            self.attr_editor.save_current_edit()
        elif current_tab in [2, 3]:  # Execution 相关标签页
            self.exec_editor.save_current_edit()
        elif current_tab in [4, 5]:  # Tags 相关标签页
            self.tag_editor.save_current_edit()
    
    def show_status(self, message):
        """显示状态消息（标题栏）"""
        self.root.title(f"DJ01 GAS 代码生成器 - {message}")
        self.root.after(2000, lambda: self.root.title("DJ01 GAS 代码生成器"))
    
    def get_attributes(self):
        """供 Execution 模块使用：获取属性列表"""
        return self.attr_editor.attributes


def main():
    root = tk.Tk()
    app = GASGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
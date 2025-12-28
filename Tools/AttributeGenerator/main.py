#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 主入口
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
from datetime import datetime
from collections import OrderedDict

from attribute import AttributeEditorUI, AttributeCodeGenerator
from execution import ExecutionEditorUI, ExecutionCodeGenerator
from mmc import MMCEditorUI, MMCCodeGenerator
from tag import TagEditorUI, TagCodeGenerator
from bindingset import BindingSetEditorUI, BindingSetGenerator


class GASGeneratorApp:
    """GAS 代码生成器主应用"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("DJ01 GAS 代码生成器")
        self.root.geometry("1400x850")
        
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
        
        # 2. Execution 编辑器标签页
        exec_frame = ttk.Frame(self.notebook)
        self.notebook.add(exec_frame, text=" ⚡ Execution 编辑器 ")
        self.exec_editor = ExecutionEditorUI(exec_frame, self)
        
        # 3. MMC 编辑器标签页
        mmc_frame = ttk.Frame(self.notebook)
        self.notebook.add(mmc_frame, text=" 🔢 MMC 编辑器 ")
        self.mmc_editor = MMCEditorUI(mmc_frame, self)
        
        # 4. GameplayTags 编辑器标签页
        tag_frame = ttk.Frame(self.notebook)
        self.notebook.add(tag_frame, text=" 🏷️ Tags 编辑器 ")
        self.tag_editor = TagEditorUI(tag_frame, self)
        
        # 5. BindingSet 编辑器标签页
        bindingset_frame = ttk.Frame(self.notebook)
        self.notebook.add(bindingset_frame, text=" 🔗 BindingSet 编辑器 ")
        self.bindingset_editor = BindingSetEditorUI(bindingset_frame, self)
        
        # 6. 统一代码预览标签页
        preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(preview_frame, text=" 📄 代码预览 ")
        self._create_unified_preview(preview_frame)
        
        # 切换标签页时自动刷新预览
        self.notebook.bind('<<NotebookTabChanged>>', self._on_tab_changed)
    
    def _create_unified_preview(self, parent):
        """创建统一的代码预览标签页"""
        # 顶部控制栏
        top_frame = ttk.Frame(parent)
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # 代码类型选择
        ttk.Label(top_frame, text="代码类型:").pack(side=tk.LEFT, padx=5)
        self.preview_module = tk.StringVar(value="属性 (Attribute)")
        self.preview_module_combo = ttk.Combobox(
            top_frame, 
            textvariable=self.preview_module,
            values=["属性 (Attribute)", "Execution", "MMC", "Tags", "BindingSet"],
            width=18,
            state='readonly'
        )
        self.preview_module_combo.pack(side=tk.LEFT, padx=5)
        self.preview_module_combo.bind('<<ComboboxSelected>>', self._on_module_changed)
        
        # 子项选择（用于 Execution 和 BindingSet）
        ttk.Label(top_frame, text="选择项:").pack(side=tk.LEFT, padx=(15, 5))
        self.preview_item = tk.StringVar()
        self.preview_item_combo = ttk.Combobox(
            top_frame,
            textvariable=self.preview_item,
            width=20,
            state='disabled'
        )
        self.preview_item_combo.pack(side=tk.LEFT, padx=5)
        self.preview_item_combo.bind('<<ComboboxSelected>>', lambda e: self._update_preview())
        
        # 文件类型选择
        ttk.Label(top_frame, text="文件:").pack(side=tk.LEFT, padx=(15, 5))
        self.preview_file_type = tk.StringVar(value="header")
        ttk.Radiobutton(top_frame, text="Header (.h)", variable=self.preview_file_type,
                       value="header", command=self._update_preview).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(top_frame, text="Source (.cpp)", variable=self.preview_file_type,
                       value="source", command=self._update_preview).pack(side=tk.LEFT, padx=5)
        
        # 刷新按钮
        ttk.Button(top_frame, text="🔄 刷新", command=self._update_preview).pack(side=tk.RIGHT, padx=5)
        
        # 代码显示区
        self.preview_text = scrolledtext.ScrolledText(
            parent, font=("Consolas", 10), wrap=tk.NONE)
        self.preview_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # 水平滚动条
        h_scroll = ttk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.preview_text.xview)
        h_scroll.pack(fill=tk.X, padx=10)
        self.preview_text.config(xscrollcommand=h_scroll.set)
    
    def _on_module_changed(self, event=None):
        """代码类型改变时更新子项列表"""
        module = self.preview_module.get()
        
        # 根据模块类型更新子项列表
        if module == "Execution":
            names = [exe.name for exe in self.exec_editor.executions if exe.name]
            self.preview_item_combo['values'] = names
            self.preview_item_combo.config(state='readonly')
            if names:
                self.preview_item.set(names[0])
            else:
                self.preview_item.set("")
        elif module == "BindingSet":
            names = [bs.name for bs in self.bindingset_editor.bindingsets if bs.name]
            self.preview_item_combo['values'] = names
            self.preview_item_combo.config(state='readonly')
            if names:
                self.preview_item.set(names[0])
            else:
                self.preview_item.set("")
        else:
            # 属性、MMC、Tags 不需要子项选择
            self.preview_item_combo['values'] = []
            self.preview_item.set("")
            self.preview_item_combo.config(state='disabled')
        
        self._update_preview()
    
    def _update_preview(self):
        """更新代码预览"""
        module = self.preview_module.get()
        file_type = self.preview_file_type.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = ""
        
        if module == "属性 (Attribute)":
            content = self._generate_attribute_preview(file_type, timestamp)
        elif module == "Execution":
            content = self._generate_execution_preview(file_type, timestamp)
        elif module == "MMC":
            content = self._generate_mmc_preview(file_type, timestamp)
        elif module == "Tags":
            content = self._generate_tags_preview(file_type, timestamp)
        elif module == "BindingSet":
            content = self._generate_bindingset_preview(file_type, timestamp)
        
        self.preview_text.delete('1.0', tk.END)
        self.preview_text.insert('1.0', content)
    
    def _generate_attribute_preview(self, file_type, timestamp):
        """生成属性代码预览"""
        attribute_sets = OrderedDict()
        for attr in self.attr_editor.attributes:
            if attr.set_name not in attribute_sets:
                attribute_sets[attr.set_name] = []
            attribute_sets[attr.set_name].append(attr)
        
        if not attribute_sets:
            return "// 没有属性定义\n// 请在「属性编辑器」中添加属性"
        
        if file_type == "header":
            return AttributeCodeGenerator.generate_header(attribute_sets, timestamp)
        else:
            return AttributeCodeGenerator.generate_source(attribute_sets, timestamp)
    
    def _generate_execution_preview(self, file_type, timestamp):
        """生成 Execution 代码预览"""
        selected = self.preview_item.get()
        
        exe = None
        for e in self.exec_editor.executions:
            if e.name == selected:
                exe = e
                break
        
        if not exe:
            return "// 没有 Execution 定义\n// 请在「Execution 编辑器」中添加"
        
        header, source = ExecutionCodeGenerator.generate(exe, timestamp)
        return header if file_type == "header" else source
    
    def _generate_mmc_preview(self, file_type, timestamp):
        """生成 MMC 代码预览"""
        valid_mmcs = [m for m in self.mmc_editor.mmcs if m.name]
        
        if not valid_mmcs:
            return "// 没有 MMC 定义\n// 请在「MMC 编辑器」中添加"
        
        header, source = MMCCodeGenerator.generate_all(valid_mmcs, timestamp)
        return header if file_type == "header" else source
    
    def _generate_tags_preview(self, file_type, timestamp):
        """生成 Tags 代码预览"""
        tags_by_category = self.tag_editor.get_tags_by_category()
        
        if not tags_by_category:
            return "// 没有标签定义\n// 请在「Tags 编辑器」中添加标签"
        
        if file_type == "header":
            return TagCodeGenerator.generate_header(tags_by_category, timestamp)
        else:
            return TagCodeGenerator.generate_source(tags_by_category, timestamp)
    
    def _generate_bindingset_preview(self, file_type, timestamp):
        """生成 BindingSet 代码预览"""
        selected = self.preview_item.get()
        
        # BindingSet 只生成 header，不生成 source
        if file_type == "source":
            return "// BindingSet 只生成 Header 文件（纯宏定义）"
        
        bindingset = None
        for bs in self.bindingset_editor.bindingsets:
            if bs.name == selected:
                bindingset = bs
                break
        
        if not bindingset:
            return "// 没有 BindingSet 定义\n// 请在「BindingSet 编辑器」中添加"
        
        return BindingSetGenerator.generate_header(bindingset, timestamp)
    
    def _on_tab_changed(self, event):
        """标签页切换时刷新预览"""
        current_tab = self.notebook.index(self.notebook.select())
        
        # 切换到代码预览标签页时刷新
        if current_tab == 5:  # 代码预览
            self._on_module_changed()
    
    def _bind_shortcuts(self):
        self.root.bind('<Control-s>', lambda e: self._on_ctrl_s())
        self.root.bind('<Control-S>', lambda e: self._on_ctrl_s())
    
    def _on_ctrl_s(self):
        """Ctrl+S 保存当前编辑内容和配置"""
        current_tab = self.notebook.index(self.notebook.select())
        if current_tab == 0:  # 属性编辑器
            self.attr_editor.save_current_edit()
        elif current_tab == 1:  # Execution 编辑器
            self.exec_editor.save_current_edit()
        elif current_tab == 2:  # MMC 编辑器
            self.mmc_editor.save_current_edit()
        elif current_tab == 3:  # Tags 编辑器
            self.tag_editor.save_current_edit()
        elif current_tab == 4:  # BindingSet 编辑器
            self.bindingset_editor.save_current_edit()
    
    def show_status(self, message):
        """显示状态消息（标题栏）"""
        self.root.title(f"DJ01 GAS 代码生成器 - {message}")
        self.root.after(2000, lambda: self.root.title("DJ01 GAS 代码生成器"))
    
    def get_attributes(self):
        """供 Execution 模块使用：获取属性列表"""
        return self.attr_editor.attributes
    
    def get_tags(self):
        """供其他模块使用：获取标签列表"""
        return self.tag_editor.tags


def main():
    root = tk.Tk()
    app = GASGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
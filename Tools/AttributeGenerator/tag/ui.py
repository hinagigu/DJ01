#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tag 编辑器 UI
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from collections import OrderedDict

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import TAGS_CONFIG, TAGS_HEADER, TAGS_SOURCE, TAG_CATEGORIES
from ui_base import BaseEditorUI, GroupListWidget, BottomButtonBar
from tag.data import TagData
from tag.generator import TagCodeGenerator


class TagEditorUI(BaseEditorUI):
    """Tag 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.tags = []
        self.current_category = None
        
        super().__init__(parent, app)
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        """创建 UI"""
        # 左侧：分类列表
        self.cat_widget = GroupListWidget(
            self.parent,
            title="分类",
            on_select=self._on_cat_select,
            on_add=self._add_category,
            on_delete=self._on_delete_category,
            show_count=True
        )
        self.cat_widget.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # 中间：Tag 表格
        middle_frame = ttk.Frame(self.parent)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        ttk.Label(middle_frame, text="Tag 列表", font=("", 12, "bold")).pack(pady=5)
        
        columns = ('tag', 'variable', 'description')
        self.tag_tree = ttk.Treeview(middle_frame, columns=columns, show='headings', height=15)
        self.tag_tree.heading('tag', text='Tag')
        self.tag_tree.heading('variable', text='变量名')
        self.tag_tree.heading('description', text='描述')
        self.tag_tree.column('tag', width=200)
        self.tag_tree.column('variable', width=150)
        self.tag_tree.column('description', width=200)
        self.tag_tree.pack(fill=tk.BOTH, expand=True)
        
        self.tag_tree.bind('<Delete>', lambda e: self._delete_tag())
        
        # 底部按钮
        self.button_bar = BottomButtonBar(middle_frame, buttons=[
            ("+ 添加 Tag", self._add_tag, None),
            ("- 删除 Tag", self._delete_tag, None),
        ])
        self.button_bar.add_button("[生成代码]", self.generate_code, side=tk.RIGHT)
        self.button_bar.add_button("重新加载", self.load_data, side=tk.RIGHT)
        self.button_bar.add_button("保存配置", self.save_current_edit, side=tk.RIGHT)
        self.button_bar.pack(fill=tk.X, pady=5)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        self.tags = []
        try:
            if TAGS_CONFIG.exists():
                with open(TAGS_CONFIG, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 支持两种格式："tags" 或 "Tags"
                    items = data.get('tags', data.get('Tags', []))
                    for item in items:
                        self.tags.append(TagData.from_dict(item))
        except Exception as e:
            messagebox.showerror("错误", f"加载配置失败: {e}")
        
        self._refresh_cat_list()
    
    def save_config(self):
        try:
            TAGS_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            data = {'Tags': [t.to_dict() for t in self.tags]}
            with open(TAGS_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {e}")
            return False
    
    def save_current_edit(self):
        if self.save_config():
            self.app.show_status("Tag 配置已保存")
    
    def _refresh_cat_list(self):
        cats = list(OrderedDict.fromkeys(t.category for t in self.tags if t.category))
        counts = {}
        for c in cats:
            counts[c] = len([t for t in self.tags if t.category == c])
        self.cat_widget.refresh(cats, counts)
    
    def _refresh_tag_list(self):
        self.tag_tree.delete(*self.tag_tree.get_children())
        if not self.current_category:
            return
        for i, tag in enumerate(self.tags):
            if tag.category == self.current_category:
                self.tag_tree.insert('', 'end', iid=str(i), values=(
                    tag.tag, tag.variable_name, tag.description))
    
    def _on_cat_select(self, idx, value):
        self.current_category = value
        self._refresh_tag_list()
    
    def _add_category(self):
        from tkinter import simpledialog
        name = simpledialog.askstring("新建分类", "分类名称:")
        if name:
            self.tags.append(TagData(category=name, tag=f"{name}.New", variable_name=f"{name}_New"))
            self._refresh_cat_list()
    
    def _on_delete_category(self, idx, value):
        if messagebox.askyesno("确认", f"确定删除分类 '{value}'?"):
            self.tags = [t for t in self.tags if t.category != value]
            self.current_category = None
            self._refresh_cat_list()
            self._refresh_tag_list()
    
    def _add_tag(self):
        if not self.current_category:
            messagebox.showwarning("警告", "请先选择一个分类")
            return
        tag_name = f"{self.current_category}.NewTag"
        self.tags.append(TagData(
            category=self.current_category,
            tag=tag_name,
            variable_name=tag_name.replace('.', '_'),
            description="新标签"
        ))
        self._refresh_tag_list()
        self._refresh_cat_list()
    
    def _delete_tag(self):
        selection = self.tag_tree.selection()
        if selection:
            idx = int(selection[0])
            del self.tags[idx]
            self._refresh_tag_list()
            self._refresh_cat_list()
    
    def get_tags_by_category(self):
        """获取按分类分组的 tags"""
        result = OrderedDict()
        for tag in self.tags:
            if tag.category not in result:
                result[tag.category] = []
            result[tag.category].append(tag)
        return result
    
    def generate_code(self):
        tags_by_cat = self.get_tags_by_category()
        if not tags_by_cat:
            messagebox.showwarning("提示", "没有可生成的 Tag")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = TagCodeGenerator.generate_header(tags_by_cat, timestamp)
        source = TagCodeGenerator.generate_source(tags_by_cat, timestamp)
        
        try:
            TAGS_HEADER.parent.mkdir(parents=True, exist_ok=True)
            TAGS_SOURCE.parent.mkdir(parents=True, exist_ok=True)
            
            with open(TAGS_HEADER, 'w', encoding='utf-8') as f:
                f.write(header)
            with open(TAGS_SOURCE, 'w', encoding='utf-8') as f:
                f.write(source)
            
            self.save_config()
            
            total = sum(len(tags) for tags in tags_by_cat.values())
            messagebox.showinfo("成功", f"已生成 {total} 个 Tag")
        except Exception as e:
            messagebox.showerror("错误", f"生成失败: {e}")
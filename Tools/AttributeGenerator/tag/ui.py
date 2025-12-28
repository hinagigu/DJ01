#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tag 编辑器 UI
"""

import csv
import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from collections import OrderedDict

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import (
    TAGS_CONFIG, TAGS_CONFIG_CSV, TAGS_CONFIG_JSON, 
    TAGS_HEADER, TAGS_SOURCE, TAG_CATEGORIES, TAGS_CSV_FIELDS
)
from ui_base import BaseEditorUI, GroupListWidget, BottomButtonBar, InlineEditorMixin
from tag.data import TagData
from tag.generator import TagCodeGenerator


class TagEditorUI(BaseEditorUI, InlineEditorMixin):
    """Tag 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.tags = []
        self.current_category = None
        self._editor_ready = False
        
        super().__init__(parent, app)
        self._init_inline_editor()
        
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
        self.tag_tree.column('tag', width=220)
        self.tag_tree.column('variable', width=180)
        self.tag_tree.column('description', width=250)
        self.tag_tree.pack(fill=tk.BOTH, expand=True)
        
        # 绑定 Delete/BackSpace 删除（自动选中上/下行）
        self._bind_tree_delete_key(self.tag_tree, on_after_delete=self._on_tag_deleted)
        # 绑定单击编辑
        self.tag_tree.bind('<Button-1>', self._on_tree_click)
        
        # 右键菜单
        self.bind_context_menu(
            self.tag_tree,
            on_delete=lambda w, item: self._delete_tag_by_item(item)
        )
        
        # 底部按钮
        self.button_bar = BottomButtonBar(middle_frame, buttons=[
            ("+ 添加 Tag", self._add_tag, None),
        ])
        self.button_bar.add_button("[生成代码]", self.generate_code, side=tk.RIGHT)
        self.button_bar.add_button("重新加载", self.load_data, side=tk.RIGHT)
        self.button_bar.add_button("保存配置", self.save_current_edit, side=tk.RIGHT)
        self.button_bar.pack(fill=tk.X, pady=5)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        """加载数据（优先 CSV，后备 JSON）"""
        self.tags = []
        
        try:
            if TAGS_CONFIG_CSV.exists():
                self._load_from_csv()
            elif TAGS_CONFIG_JSON.exists():
                self._load_from_json()
        except Exception as e:
            messagebox.showerror("错误", f"加载配置失败: {e}")
        
        self._refresh_cat_list()
    
    def _load_from_csv(self):
        """从 CSV 文件加载"""
        with open(TAGS_CONFIG_CSV, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.tags.append(TagData(
                    category=row.get('Category', ''),
                    tag=row.get('Tag', ''),
                    variable_name=row.get('VariableName', ''),
                    description=row.get('Description', '')
                ))
    
    def _load_from_json(self):
        """从 JSON 文件加载（后备）"""
        with open(TAGS_CONFIG_JSON, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items = data.get('tags', data.get('Tags', []))
            for item in items:
                self.tags.append(TagData.from_dict(item))
    
    def save_config(self):
        """保存配置到 CSV"""
        try:
            TAGS_CONFIG_CSV.parent.mkdir(parents=True, exist_ok=True)
            
            with open(TAGS_CONFIG_CSV, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=TAGS_CSV_FIELDS)
                writer.writeheader()
                
                for tag in self.tags:
                    writer.writerow({
                        'Category': tag.category,
                        'Tag': tag.tag,
                        'VariableName': tag.variable_name,
                        'Description': tag.description
                    })
            
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
        """删除选中的 Tag（由按钮调用）"""
        self._handle_tree_delete(self.tag_tree, on_after_delete=self._on_tag_deleted)
    
    def _on_tag_deleted(self):
        """Tag 删除后的回调：同步删除数据并刷新"""
        # 重建 tags 列表（根据 tree 中剩余的项）
        remaining_indices = set()
        for item in self.tag_tree.get_children():
            try:
                remaining_indices.add(int(item))
            except ValueError:
                pass
        
        # 保留还在 tree 中的 tags
        new_tags = []
        for i, tag in enumerate(self.tags):
            if i in remaining_indices or tag.category != self.current_category:
                new_tags.append(tag)
        self.tags = new_tags
        
        self._refresh_tag_list()
        self._refresh_cat_list()
    
    def _delete_tag_by_item(self, item: str):
        """通过 item id 删除 Tag（右键菜单调用）"""
        try:
            idx = int(item)
            if idx < len(self.tags):
                del self.tags[idx]
                self._refresh_tag_list()
                self._refresh_cat_list()
        except (ValueError, IndexError):
            pass
    
    def get_tags_by_category(self):
        """获取按分类分组的 tags"""
        result = OrderedDict()
        for tag in self.tags:
            if tag.category not in result:
                result[tag.category] = []
            result[tag.category].append(tag)
        return result
    
    # ========== 行内编辑功能 ==========
    
    def _on_tree_click(self, event):
        """处理 Treeview 单击事件"""
        if self._active_editor:
            try:
                ex = self._active_editor.winfo_x()
                ey = self._active_editor.winfo_y()
                ew = self._active_editor.winfo_width()
                eh = self._active_editor.winfo_height()
                if ex <= event.x <= ex + ew and ey <= event.y <= ey + eh:
                    return
            except:
                pass
        
        self._destroy_active_editor()
        self.tag_tree.after(180, lambda: self._handle_tree_click(event))
    
    def _handle_tree_click(self, event):
        """实际处理单击编辑"""
        cell_info = self._get_cell_info(self.tag_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        x, y, w, h = bbox
        
        self.tag_tree.selection_set(item)
        self.tag_tree.focus(item)
        
        # 获取当前行数据和对应的 tag 对象
        tag_idx = int(item)
        tag = self.tags[tag_idx]
        current_values = list(self.tag_tree.item(item, 'values'))
        
        # 列: tag(0), variable(1), description(2)
        if col_idx == 0:  # tag 名
            self._create_tag_entry(item, col_idx, x, y, w, h, current_values, tag, 'tag')
        elif col_idx == 1:  # variable_name - 只读，显示自动生成提示
            pass  # 变量名自动生成，不可编辑
        elif col_idx == 2:  # description
            self._create_tag_entry(item, col_idx, x, y, w, h, current_values, tag, 'description')
    
    def _create_tag_entry(self, item, col_idx, x, y, w, h, current_values, tag, field_name):
        """创建文本框编辑器"""
        self._destroy_active_editor()
        
        entry = ttk.Entry(self.tag_tree, width=max(5, w // 8))
        entry.insert(0, str(current_values[col_idx]))
        entry.place(x=x, y=y, width=w, height=h)
        entry.select_range(0, tk.END)
        self._active_editor = entry
        self._editor_ready = False
        
        def on_confirm(event=None):
            if self._active_editor != entry:
                return
            new_value = entry.get()
            
            # 更新 tag 数据
            if field_name == 'tag':
                tag.tag = new_value
                tag.variable_name = new_value.replace('.', '_').replace('-', '_')
                current_values[0] = tag.tag
                current_values[1] = tag.variable_name
            elif field_name == 'description':
                tag.description = new_value
                current_values[2] = new_value
            
            self.tag_tree.item(item, values=current_values)
            self._destroy_active_editor()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        def on_focus_out(event):
            if self._editor_ready and self._active_editor == entry:
                self.tag_tree.after(50, on_confirm)
        
        entry.bind('<Return>', on_confirm)
        entry.bind('<Escape>', on_escape)
        entry.bind('<FocusOut>', on_focus_out)
        
        entry.focus_set()
        entry.after(250, lambda: setattr(self, '_editor_ready', True))
    
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
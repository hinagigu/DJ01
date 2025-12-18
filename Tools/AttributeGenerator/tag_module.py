#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - GameplayTags 模块
包含：数据模型、代码生成器、UI 组件
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from collections import OrderedDict

from config import (
    MODULE_NAME, TAGS_CONFIG, TAGS_HEADER, TAGS_SOURCE, TAG_CATEGORIES
)


# ============================================================
# 数据模型
# ============================================================

class TagData:
    """GameplayTag 数据模型"""
    def __init__(self, category="Custom", tag="", variable_name="", description=""):
        self.category = category
        self.tag = tag  # 完整的标签路径，如 "Ability.Skill.Fireball"
        self.variable_name = variable_name  # C++ 变量名，如 "Ability_Skill_Fireball"
        self.description = description
    
    def to_dict(self):
        return {
            'Category': self.category,
            'Tag': self.tag,
            'VariableName': self.variable_name,
            'Description': self.description
        }
    
    @staticmethod
    def from_dict(d):
        return TagData(
            category=d.get('Category', 'Custom'),
            tag=d.get('Tag', ''),
            variable_name=d.get('VariableName', ''),
            description=d.get('Description', '')
        )
    
    @staticmethod
    def tag_to_variable(tag: str) -> str:
        """将 Tag 路径转换为 C++ 变量名"""
        # "Ability.Skill.Fireball" -> "Ability_Skill_Fireball"
        return tag.replace('.', '_')


# ============================================================
# 代码生成器
# ============================================================

class TagCodeGenerator:
    """GameplayTags 代码生成器"""
    
    @staticmethod
    def generate_header(tags_by_category: dict, timestamp: str) -> str:
        lines = []
        
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated Gameplay Tags")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "NativeGameplayTags.h"')
        lines.append("")
        lines.append(f"namespace {MODULE_NAME}GameplayTags")
        lines.append("{")
        
        for category, tags in tags_by_category.items():
            lines.append(f"\t// ============================================================")
            lines.append(f"\t// {category}")
            lines.append(f"\t// ============================================================")
            for tag in tags:
                var_name = tag.variable_name or TagData.tag_to_variable(tag.tag)
                lines.append(f"\t{MODULE_NAME}_API UE_DECLARE_GAMEPLAY_TAG_EXTERN({var_name});")
            lines.append("")
        
        lines.append("}")
        
        return "\n".join(lines)
    
    @staticmethod
    def generate_source(tags_by_category: dict, timestamp: str) -> str:
        lines = []
        
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated Gameplay Tags")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append(f'#include "{MODULE_NAME}/System/Public/{MODULE_NAME}GameplayTags.h"')
        lines.append("")
        lines.append('#include "GameplayTagsManager.h"')
        lines.append("")
        lines.append(f"namespace {MODULE_NAME}GameplayTags")
        lines.append("{")
        
        for category, tags in tags_by_category.items():
            lines.append(f"\t// ============================================================")
            lines.append(f"\t// {category}")
            lines.append(f"\t// ============================================================")
            for tag in tags:
                var_name = tag.variable_name or TagData.tag_to_variable(tag.tag)
                desc = tag.description or tag.tag
                lines.append(f'\tUE_DEFINE_GAMEPLAY_TAG_COMMENT({var_name}, "{tag.tag}", "{desc}");')
            lines.append("")
        
        lines.append("}")
        
        return "\n".join(lines)


# ============================================================
# UI 组件
# ============================================================

class TagEditorUI:
    """GameplayTags 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.tags = []
        self.current_category = tk.StringVar(value="")
        self._last_selected_idx = None
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        # 左侧：分类列表
        left_frame = ttk.Frame(self.parent, width=200)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_frame, text="标签分类", font=("", 12, "bold")).pack(pady=5)
        
        self.category_listbox = tk.Listbox(left_frame, width=20, height=20)
        self.category_listbox.pack(fill=tk.BOTH, expand=True)
        self.category_listbox.bind('<<ListboxSelect>>', self._on_category_select)
        self.category_listbox.bind('<F2>', self._on_rename_category)
        self.category_listbox.bind('<Delete>', lambda e: self._delete_category())
        
        cat_btn_frame = ttk.Frame(left_frame)
        cat_btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(cat_btn_frame, text="+ 新建", command=self._add_category).pack(side=tk.LEFT, expand=True)
        ttk.Button(cat_btn_frame, text="- 删除", command=self._delete_category).pack(side=tk.LEFT, expand=True)
        
        # 中间：标签列表
        middle_frame = ttk.Frame(self.parent)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        ttk.Label(middle_frame, text="标签列表", font=("", 12, "bold")).pack(pady=5)
        
        columns = ('tag', 'variable', 'description')
        self.tag_tree = ttk.Treeview(middle_frame, columns=columns, show='headings', height=15)
        self.tag_tree.heading('tag', text='标签路径')
        self.tag_tree.heading('variable', text='变量名')
        self.tag_tree.heading('description', text='描述')
        
        self.tag_tree.column('tag', width=200)
        self.tag_tree.column('variable', width=200)
        self.tag_tree.column('description', width=300)
        
        self.tag_tree.pack(fill=tk.BOTH, expand=True)
        self.tag_tree.bind('<<TreeviewSelect>>', self._on_tag_select)
        self.tag_tree.bind('<F2>', self._on_rename_tag)
        self.tag_tree.bind('<Delete>', lambda e: self._delete_tag())
        self.tag_tree.bind('<Double-1>', self._on_cell_double_click)
        
        self._edit_widget = None
        
        tag_btn_frame = ttk.Frame(middle_frame)
        tag_btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(tag_btn_frame, text="+ 添加标签", command=self._add_tag).pack(side=tk.LEFT, padx=2)
        ttk.Button(tag_btn_frame, text="- 删除标签", command=self._delete_tag).pack(side=tk.LEFT, padx=2)
        ttk.Button(tag_btn_frame, text="[生成代码]", command=self.generate_code).pack(side=tk.RIGHT, padx=2)
        ttk.Button(tag_btn_frame, text="重新加载", command=self.load_data).pack(side=tk.RIGHT, padx=2)
        ttk.Button(tag_btn_frame, text="保存配置", command=self.save_config).pack(side=tk.RIGHT, padx=2)
        
        # 右侧：标签编辑
        right_frame = ttk.LabelFrame(self.parent, text="编辑标签", width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(right_frame, text="标签路径:").grid(row=0, column=0, sticky='w', padx=5, pady=3)
        self.tag_path_var = tk.StringVar()
        self.tag_path_entry = ttk.Entry(right_frame, textvariable=self.tag_path_var, width=25)
        self.tag_path_entry.grid(row=0, column=1, padx=5, pady=3)
        self.tag_path_var.trace_add('write', self._on_tag_path_changed)
        
        ttk.Label(right_frame, text="变量名:").grid(row=1, column=0, sticky='w', padx=5, pady=3)
        self.tag_var_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.tag_var_var, width=25).grid(row=1, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="描述:").grid(row=2, column=0, sticky='w', padx=5, pady=3)
        self.tag_desc_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.tag_desc_var, width=25).grid(row=2, column=1, padx=5, pady=3)
        
        # 提示标签
        ttk.Label(right_frame, text="提示: 标签路径用 . 分隔", 
                  foreground='gray').grid(row=3, column=0, columnspan=2, pady=5)
        ttk.Label(right_frame, text="如: Ability.Skill.Fireball", 
                  foreground='gray').grid(row=4, column=0, columnspan=2)
        
        ttk.Button(right_frame, text="保存修改", command=self._save_tag).grid(row=5, column=0, columnspan=2, pady=10)
    
    def _on_tag_path_changed(self, *args):
        """标签路径变化时自动生成变量名"""
        tag_path = self.tag_path_var.get()
        if tag_path:
            auto_var = TagData.tag_to_variable(tag_path)
            self.tag_var_var.set(auto_var)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        self.tags.clear()
        if TAGS_CONFIG.exists():
            with open(TAGS_CONFIG, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data.get('tags', []):
                    self.tags.append(TagData.from_dict(item))
        self._refresh_category_list()
    
    def save_config(self):
        try:
            TAGS_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            data = {
                'version': '1.0',
                'tags': [tag.to_dict() for tag in self.tags]
            }
            with open(TAGS_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self.app.show_status("标签配置已保存")
        except Exception as e:
            messagebox.showerror("保存失败", str(e))
    
    def generate_code(self):
        if not self.tags:
            messagebox.showwarning("警告", "没有标签可生成！")
            return
        
        tags_by_category = OrderedDict()
        for tag in self.tags:
            if tag.category not in tags_by_category:
                tags_by_category[tag.category] = []
            tags_by_category[tag.category].append(tag)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            header_content = TagCodeGenerator.generate_header(tags_by_category, timestamp)
            source_content = TagCodeGenerator.generate_source(tags_by_category, timestamp)
            
            TAGS_HEADER.parent.mkdir(parents=True, exist_ok=True)
            TAGS_SOURCE.parent.mkdir(parents=True, exist_ok=True)
            
            with open(TAGS_HEADER, 'w', encoding='utf-8') as f:
                f.write(header_content)
            with open(TAGS_SOURCE, 'w', encoding='utf-8') as f:
                f.write(source_content)
            
            messagebox.showinfo("生成成功",
                f"GameplayTags 代码已生成！\n\n"
                f"Header:\n{TAGS_HEADER}\n\n"
                f"Source:\n{TAGS_SOURCE}\n\n"
                f"共 {len(tags_by_category)} 个分类，{len(self.tags)} 个标签")
        except Exception as e:
            messagebox.showerror("生成失败", str(e))
    
    def get_tags_by_category(self):
        """供其他模块使用"""
        tags_by_category = OrderedDict()
        for tag in self.tags:
            if tag.category not in tags_by_category:
                tags_by_category[tag.category] = []
            tags_by_category[tag.category].append(tag)
        return tags_by_category
    
    # ========== UI 事件 ==========
    
    def _refresh_category_list(self):
        self.category_listbox.delete(0, tk.END)
        categories = list(OrderedDict.fromkeys(tag.category for tag in self.tags))
        for cat in categories:
            count = len([t for t in self.tags if t.category == cat])
            self.category_listbox.insert(tk.END, f"{cat} ({count})")
    
    def _on_category_select(self, event):
        selection = self.category_listbox.curselection()
        if not selection:
            return
        item = self.category_listbox.get(selection[0])
        category = item.split(" (")[0]
        self.current_category.set(category)
        self._refresh_tag_list()
    
    def _refresh_tag_list(self):
        self.tag_tree.delete(*self.tag_tree.get_children())
        category = self.current_category.get()
        for i, tag in enumerate(self.tags):
            if tag.category == category:
                var_name = tag.variable_name or TagData.tag_to_variable(tag.tag)
                self.tag_tree.insert('', 'end', iid=str(i), values=(
                    tag.tag, var_name, tag.description))
    
    def _on_tag_select(self, event):
        if self._last_selected_idx is not None:
            self._save_tag_silent(self._last_selected_idx)
        
        selection = self.tag_tree.selection()
        if not selection:
            self._last_selected_idx = None
            return
        
        idx = int(selection[0])
        self._last_selected_idx = idx
        tag = self.tags[idx]
        
        self.tag_path_var.set(tag.tag)
        self.tag_var_var.set(tag.variable_name or TagData.tag_to_variable(tag.tag))
        self.tag_desc_var.set(tag.description)
    
    def _on_rename_tag(self, event):
        selection = self.tag_tree.selection()
        if not selection:
            return
        self._start_cell_edit(selection[0], '#1')
    
    def _on_cell_double_click(self, event):
        self._destroy_edit_widget()
        
        region = self.tag_tree.identify_region(event.x, event.y)
        if region != 'cell':
            return
        
        column = self.tag_tree.identify_column(event.x)
        item = self.tag_tree.identify_row(event.y)
        if not item:
            return
        
        self._start_cell_edit(item, column)
    
    def _start_cell_edit(self, item, column):
        self._destroy_edit_widget()
        
        idx = int(item)
        if idx >= len(self.tags):
            return
        
        tag = self.tags[idx]
        
        col_map = {
            '#1': ('tag', 'entry'),
            '#2': ('variable', 'entry'),
            '#3': ('description', 'entry'),
        }
        
        if column not in col_map:
            return
        
        col_info = col_map[column]
        field = col_info[0]
        
        bbox = self.tag_tree.bbox(item, column)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        if field == 'tag':
            current_value = tag.tag
        elif field == 'variable':
            current_value = tag.variable_name or TagData.tag_to_variable(tag.tag)
        else:
            current_value = tag.description
        
        widget = ttk.Entry(self.tag_tree)
        widget.insert(0, str(current_value))
        widget.select_range(0, tk.END)
        
        widget.place(x=x, y=y, width=max(width, 80), height=height)
        widget.focus()
        self._edit_widget = widget
        
        widget.bind('<Return>', lambda e: self._finish_cell_edit(True, tag, field, widget))
        widget.bind('<Escape>', lambda e: self._finish_cell_edit(False, tag, field, widget))
        widget.bind('<FocusOut>', lambda e: self._finish_cell_edit(True, tag, field, widget))
    
    def _finish_cell_edit(self, save, tag, field, widget):
        if not self._edit_widget:
            return
        
        if save:
            new_value = widget.get()
            if field == 'tag':
                tag.tag = new_value
                if not tag.variable_name:
                    tag.variable_name = TagData.tag_to_variable(new_value)
            elif field == 'variable':
                tag.variable_name = new_value
            else:
                tag.description = new_value
            self._refresh_tag_list()
            self._sync_right_panel(tag)
        
        self._destroy_edit_widget()
    
    def _destroy_edit_widget(self):
        if self._edit_widget:
            try:
                self._edit_widget.destroy()
            except:
                pass
            self._edit_widget = None
    
    def _sync_right_panel(self, tag):
        self.tag_path_var.set(tag.tag)
        self.tag_var_var.set(tag.variable_name or TagData.tag_to_variable(tag.tag))
        self.tag_desc_var.set(tag.description)
    
    def _on_rename_category(self, event):
        selection = self.category_listbox.curselection()
        if not selection:
            return
        
        idx = selection[0]
        item = self.category_listbox.get(idx)
        old_name = item.split(" (")[0]
        
        bbox = self.category_listbox.bbox(idx)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        entry = ttk.Entry(self.category_listbox, width=15)
        entry.place(x=x, y=y, width=self.category_listbox.winfo_width()-4, height=height)
        entry.insert(0, old_name)
        entry.select_range(0, tk.END)
        entry.focus()
        
        def finish_edit(save=True):
            if save:
                new_name = entry.get().strip()
                if new_name and new_name != old_name:
                    for tag in self.tags:
                        if tag.category == old_name:
                            tag.category = new_name
                    self._refresh_category_list()
                    self.current_category.set(new_name)
                    self._refresh_tag_list()
                    self.app.show_status(f"分类已重命名为 {new_name}")
            entry.destroy()
        
        entry.bind('<Return>', lambda e: finish_edit(True))
        entry.bind('<Escape>', lambda e: finish_edit(False))
        entry.bind('<FocusOut>', lambda e: finish_edit(True))
    
    def save_current_edit(self):
        self._destroy_edit_widget()
        if self._last_selected_idx is not None:
            self._save_tag_silent(self._last_selected_idx)
            self._refresh_tag_list()
        self.save_config()
    
    def _add_category(self):
        from tkinter import simpledialog
        name = simpledialog.askstring("新建分类", "分类名称:")
        if name:
            self.tags.append(TagData(category=name, tag=f"{name}.NewTag", description="新标签"))
            self._refresh_category_list()
    
    def _delete_category(self):
        selection = self.category_listbox.curselection()
        if not selection:
            return
        item = self.category_listbox.get(selection[0])
        category = item.split(" (")[0]
        if messagebox.askyesno("确认", f"确定删除分类 '{category}' 及其所有标签?"):
            self.tags = [t for t in self.tags if t.category != category]
            self._refresh_category_list()
            self.tag_tree.delete(*self.tag_tree.get_children())
    
    def _add_tag(self):
        category = self.current_category.get()
        if not category:
            messagebox.showwarning("警告", "请先选择一个分类")
            return
        self.tags.append(TagData(category=category, tag=f"{category}.NewTag", description="新标签"))
        self._refresh_tag_list()
        self._refresh_category_list()
    
    def _delete_tag(self):
        selection = self.tag_tree.selection()
        if not selection:
            return
        idx = int(selection[0])
        del self.tags[idx]
        self._refresh_tag_list()
        self._refresh_category_list()
    
    def _save_tag_silent(self, idx):
        if idx is None or idx >= len(self.tags):
            return
        try:
            tag = self.tags[idx]
            tag.tag = self.tag_path_var.get()
            tag.variable_name = self.tag_var_var.get()
            tag.description = self.tag_desc_var.get()
        except (ValueError, IndexError):
            pass
    
    def _save_tag(self):
        selection = self.tag_tree.selection()
        if not selection:
            return
        idx = int(selection[0])
        self._save_tag_silent(idx)
        self._refresh_tag_list()
        for item in self.tag_tree.get_children():
            if int(item) == idx:
                self.tag_tree.selection_set(item)
                break
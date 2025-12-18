#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - 属性模块
包含：数据模型、代码生成器、UI 组件
"""

import csv
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from collections import OrderedDict

from config import (
    MODULE_NAME, ATTRIBUTES_CONFIG, ATTRIBUTES_HEADER, ATTRIBUTES_SOURCE,
    ATTRIBUTE_TYPES, ATTRIBUTE_CATEGORIES
)


# ============================================================
# 数据模型
# ============================================================

class AttributeData:
    """属性数据模型"""
    def __init__(self, set_name="", name="", attr_type="Layered", category="Combat",
                 default_base=0.0, default_flat=0.0, default_percent=0.0, 
                 default_current=0.0, description=""):
        self.set_name = set_name
        self.name = name
        self.type = attr_type
        self.category = category
        self.default_base = default_base
        self.default_flat = default_flat
        self.default_percent = default_percent
        self.default_current = default_current  # Resource 类型的当前值初始化
        self.description = description

    def to_dict(self):
        return {
            'SetName': self.set_name,
            'AttributeName': self.name,
            'Type': self.type,
            'Category': self.category,
            'DefaultBase': str(self.default_base) if self.default_base else '',
            'DefaultFlat': str(self.default_flat) if self.default_flat else '',
            'DefaultPercent': str(self.default_percent) if self.default_percent else '',
            'DefaultCurrent': str(self.default_current) if self.default_current else '',
            'Description': self.description
        }

    @staticmethod
    def from_dict(d):
        return AttributeData(
            set_name=d.get('SetName', ''),
            name=d.get('AttributeName', ''),
            attr_type=d.get('Type', 'Layered'),
            category=d.get('Category', 'Combat'),
            default_base=float(d['DefaultBase']) if d.get('DefaultBase') else 0.0,
            default_flat=float(d['DefaultFlat']) if d.get('DefaultFlat') else 0.0,
            default_percent=float(d['DefaultPercent']) if d.get('DefaultPercent') else 0.0,
            default_current=float(d['DefaultCurrent']) if d.get('DefaultCurrent') else 0.0,
            description=d.get('Description', '')
        )


# ============================================================
# 代码生成器
# ============================================================

class AttributeCodeGenerator:
    """属性代码生成器"""
    
    @staticmethod
    def generate_header(attribute_sets: dict, timestamp: str) -> str:
        lines = []
        
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated Attributes")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "DJ01AttributeSet.h"')
        lines.append('#include "DJ01AttributeMacros.h"')
        lines.append("")
        lines.append('#include "DJ01GeneratedAttributes.generated.h"')
        lines.append("")
        
        for set_name, attributes in attribute_sets.items():
            lines.append("")
            lines.append(f"// ############################################################")
            lines.append(f"// UDJ01{set_name}")
            lines.append(f"// ############################################################")
            lines.append("")
            lines.extend(AttributeCodeGenerator._generate_class_header(set_name, attributes))
            lines.append("")
        
        return "\n".join(lines)
    
    @staticmethod
    def _generate_class_header(set_name: str, attributes: list) -> list:
        class_name = f"UDJ01{set_name}"
        
        layered = [a for a in attributes if a.type == 'Layered']
        simple = [a for a in attributes if a.type == 'Simple']
        resource = [a for a in attributes if a.type == 'Resource']
        meta = [a for a in attributes if a.type == 'Meta']
        
        categories = OrderedDict()
        for attr in attributes:
            if attr.category not in categories:
                categories[attr.category] = []
            categories[attr.category].append(attr)
        
        lines = []
        lines.append(f"/** {set_name} - 包含 {len(attributes)} 个属性 */")
        lines.append("UCLASS(BlueprintType)")
        lines.append(f"class {MODULE_NAME}_API {class_name} : public UDJ01AttributeSet")
        lines.append("{")
        lines.append("    GENERATED_BODY()")
        lines.append("")
        lines.append("public:")
        lines.append(f"    {class_name}();")
        lines.append("")
        
        for category, cat_attrs in categories.items():
            lines.append(f"    // ---------- {category} ----------")
            for attr in cat_attrs:
                lines.append(f"    /** {attr.description} */")
                if attr.type == 'Layered':
                    lines.append(f"    DECLARE_LAYERED_ATTRIBUTE({class_name}, {attr.name})")
                elif attr.type == 'Simple':
                    lines.append(f"    DECLARE_SIMPLE_ATTRIBUTE({class_name}, {attr.name})")
                elif attr.type == 'Resource':
                    lines.append(f"    DECLARE_RESOURCE_ATTRIBUTE({class_name}, {attr.name})")
                else:  # Meta
                    lines.append(f"    DECLARE_META_ATTRIBUTE({class_name}, {attr.name})")
                lines.append("")
        
        lines.append("protected:")
        for attr in layered:
            lines.append(f"    DECLARE_LAYERED_ATTRIBUTE_ONREP({attr.name})")
        for attr in simple:
            lines.append(f"    DECLARE_SIMPLE_ATTRIBUTE_ONREP({attr.name})")
        for attr in resource:
            lines.append(f"    DECLARE_RESOURCE_ATTRIBUTE_ONREP({attr.name})")
        # Meta 不需要 OnRep
        
        lines.append("    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;")
        lines.append("};")
        
        return lines
    
    @staticmethod
    def generate_source(attribute_sets: dict, timestamp: str) -> str:
        lines = []
        
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated Attributes")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append('#include "DJ01GeneratedAttributes.h"')
        lines.append('#include "Net/UnrealNetwork.h"')
        lines.append("")
        lines.append("#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GeneratedAttributes)")
        
        for set_name, attributes in attribute_sets.items():
            lines.append("")
            lines.append(f"// ############################################################")
            lines.append(f"// UDJ01{set_name}")
            lines.append(f"// ############################################################")
            lines.append("")
            lines.extend(AttributeCodeGenerator._generate_class_source(set_name, attributes))
        
        lines.append("")
        return "\n".join(lines)
    
    @staticmethod
    def _generate_class_source(set_name: str, attributes: list) -> list:
        class_name = f"UDJ01{set_name}"
        
        layered = [a for a in attributes if a.type == 'Layered']
        simple = [a for a in attributes if a.type == 'Simple']
        resource = [a for a in attributes if a.type == 'Resource']
        
        lines = []
        
        lines.append(f"{class_name}::{class_name}()")
        lines.append("{")
        for attr in attributes:
            if attr.type == 'Layered':
                lines.append(f"    InitBase{attr.name}({attr.default_base}f);")
                lines.append(f"    InitFlat{attr.name}({attr.default_flat}f);")
                lines.append(f"    InitPercent{attr.name}({attr.default_percent}f);")
            elif attr.type == 'Simple':
                lines.append(f"    Init{attr.name}({attr.default_base}f);")
            elif attr.type == 'Resource':
                # Resource: Max (Layered) + Current (Simple)
                lines.append(f"    // {attr.name}: Max (Layered) + Current (Simple)")
                lines.append(f"    InitBaseMax{attr.name}({attr.default_base}f);")
                lines.append(f"    InitFlatMax{attr.name}({attr.default_flat}f);")
                lines.append(f"    InitPercentMax{attr.name}({attr.default_percent}f);")
                # 当前值使用 default_current，如果没设置则用 base
                current_val = attr.default_current if attr.default_current else attr.default_base
                lines.append(f"    Init{attr.name}({current_val}f);")
            # Meta 不需要初始化
        lines.append("}")
        lines.append("")
        
        lines.append(f"void {class_name}::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const")
        lines.append("{")
        lines.append("    Super::GetLifetimeReplicatedProps(OutLifetimeProps);")
        for attr in layered:
            lines.append(f"    REGISTER_LAYERED_ATTRIBUTE_REPLICATION({class_name}, {attr.name})")
        for attr in simple:
            lines.append(f"    REGISTER_SIMPLE_ATTRIBUTE_REPLICATION({class_name}, {attr.name})")
        for attr in resource:
            lines.append(f"    REGISTER_RESOURCE_ATTRIBUTE_REPLICATION({class_name}, {attr.name})")
        lines.append("}")
        lines.append("")
        
        for attr in layered:
            lines.append(f"IMPLEMENT_LAYERED_ATTRIBUTE_ONREP({class_name}, {attr.name})")
        for attr in simple:
            lines.append(f"IMPLEMENT_SIMPLE_ATTRIBUTE_ONREP({class_name}, {attr.name})")
        for attr in resource:
            lines.append(f"IMPLEMENT_RESOURCE_ATTRIBUTE_ONREP({class_name}, {attr.name})")
        
        return lines


# ============================================================
# UI 组件
# ============================================================

class AttributeEditorUI:
    """属性编辑器 UI"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app  # 主应用引用，用于访问共享数据
        self.attributes = []
        self.current_set = tk.StringVar(value="")
        self._last_selected_idx = None
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        # 左侧：属性集列表
        left_frame = ttk.Frame(self.parent, width=200)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_frame, text="属性集", font=("", 12, "bold")).pack(pady=5)
        
        self.set_listbox = tk.Listbox(left_frame, width=20, height=20)
        self.set_listbox.pack(fill=tk.BOTH, expand=True)
        self.set_listbox.bind('<<ListboxSelect>>', self._on_set_select)
        
        set_btn_frame = ttk.Frame(left_frame)
        set_btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(set_btn_frame, text="+ 新建", command=self._add_set).pack(side=tk.LEFT, expand=True)
        ttk.Button(set_btn_frame, text="- 删除", command=self._delete_set).pack(side=tk.LEFT, expand=True)
        
        # 中间：属性列表
        middle_frame = ttk.Frame(self.parent)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        ttk.Label(middle_frame, text="属性列表", font=("", 12, "bold")).pack(pady=5)
        
        columns = ('name', 'type', 'category', 'base', 'description')
        self.attr_tree = ttk.Treeview(middle_frame, columns=columns, show='headings', height=15)
        self.attr_tree.heading('name', text='属性名')
        self.attr_tree.heading('type', text='类型')
        self.attr_tree.heading('category', text='分类')
        self.attr_tree.heading('base', text='默认值')
        self.attr_tree.heading('description', text='描述')
        
        self.attr_tree.column('name', width=120)
        self.attr_tree.column('type', width=80)
        self.attr_tree.column('category', width=80)
        self.attr_tree.column('base', width=80)
        self.attr_tree.column('description', width=200)
        
        self.attr_tree.pack(fill=tk.BOTH, expand=True)
        self.attr_tree.bind('<<TreeviewSelect>>', self._on_attr_select)
        self.attr_tree.bind('<F2>', self._on_rename_attr)
        self.attr_tree.bind('<Delete>', lambda e: self._delete_attribute())
        self.attr_tree.bind('<Double-1>', self._on_cell_double_click)  # 双击编辑
        
        # 属性集也绑定 F2
        self.set_listbox.bind('<F2>', self._on_rename_set)
        self.set_listbox.bind('<Delete>', lambda e: self._delete_set())
        
        # 当前编辑控件
        self._edit_widget = None
        
        attr_btn_frame = ttk.Frame(middle_frame)
        attr_btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(attr_btn_frame, text="+ 添加属性", command=self._add_attribute).pack(side=tk.LEFT, padx=2)
        ttk.Button(attr_btn_frame, text="- 删除属性", command=self._delete_attribute).pack(side=tk.LEFT, padx=2)
        ttk.Button(attr_btn_frame, text="[生成代码]", command=self.generate_code).pack(side=tk.RIGHT, padx=2)
        ttk.Button(attr_btn_frame, text="重新加载", command=self.load_data).pack(side=tk.RIGHT, padx=2)
        ttk.Button(attr_btn_frame, text="保存配置", command=self.save_config).pack(side=tk.RIGHT, padx=2)
        
        # 右侧：属性编辑
        right_frame = ttk.LabelFrame(self.parent, text="编辑属性", width=300)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(right_frame, text="属性名:").grid(row=0, column=0, sticky='w', padx=5, pady=3)
        self.attr_name_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.attr_name_var, width=20).grid(row=0, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="类型:").grid(row=1, column=0, sticky='w', padx=5, pady=3)
        self.attr_type_var = tk.StringVar(value="Layered")
        ttk.Combobox(right_frame, textvariable=self.attr_type_var, values=ATTRIBUTE_TYPES, width=17).grid(row=1, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="分类:").grid(row=2, column=0, sticky='w', padx=5, pady=3)
        self.attr_category_var = tk.StringVar(value="Combat")
        ttk.Combobox(right_frame, textvariable=self.attr_category_var, values=ATTRIBUTE_CATEGORIES, width=17).grid(row=2, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="Base:").grid(row=3, column=0, sticky='w', padx=5, pady=3)
        self.attr_base_var = tk.StringVar(value="0")
        ttk.Entry(right_frame, textvariable=self.attr_base_var, width=20).grid(row=3, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="Flat:").grid(row=4, column=0, sticky='w', padx=5, pady=3)
        self.attr_flat_var = tk.StringVar(value="0")
        ttk.Entry(right_frame, textvariable=self.attr_flat_var, width=20).grid(row=4, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="Percent:").grid(row=5, column=0, sticky='w', padx=5, pady=3)
        self.attr_percent_var = tk.StringVar(value="0")
        ttk.Entry(right_frame, textvariable=self.attr_percent_var, width=20).grid(row=5, column=1, padx=5, pady=3)
        
        # Current (仅 Resource 类型显示)
        self.current_label = ttk.Label(right_frame, text="Current:")
        self.current_label.grid(row=6, column=0, sticky='w', padx=5, pady=3)
        self.attr_current_var = tk.StringVar(value="0")
        self.current_entry = ttk.Entry(right_frame, textvariable=self.attr_current_var, width=20)
        self.current_entry.grid(row=6, column=1, padx=5, pady=3)
        
        ttk.Label(right_frame, text="描述:").grid(row=7, column=0, sticky='w', padx=5, pady=3)
        self.attr_desc_var = tk.StringVar()
        ttk.Entry(right_frame, textvariable=self.attr_desc_var, width=20).grid(row=7, column=1, padx=5, pady=3)
        
        ttk.Button(right_frame, text="保存修改", command=self._save_attribute).grid(row=8, column=0, columnspan=2, pady=10)
        
        # 类型变化时更新界面
        self.attr_type_var.trace_add('write', self._on_type_changed)
        self._update_ui_by_type()
    
    def _on_type_changed(self, *args):
        """类型变化时更新 UI"""
        self._update_ui_by_type()
    
    def _update_ui_by_type(self):
        """根据类型更新 UI 显示"""
        attr_type = self.attr_type_var.get()
        
        if attr_type == 'Resource':
            # Resource: 显示 Max 的三层 + Current
            self.current_label.grid()
            self.current_entry.grid()
        else:
            # Layered/Simple/Meta: 隐藏 Current
            self.current_label.grid_remove()
            self.current_entry.grid_remove()
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        self.attributes.clear()
        if ATTRIBUTES_CONFIG.exists():
            with open(ATTRIBUTES_CONFIG, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.attributes.append(AttributeData.from_dict(row))
        self._refresh_set_list()
    
    def save_config(self):
        try:
            ATTRIBUTES_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            fieldnames = ['SetName', 'AttributeName', 'Type', 'Category', 'DefaultBase', 'DefaultFlat', 'DefaultPercent', 'DefaultCurrent', 'Description']
            with open(ATTRIBUTES_CONFIG, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for attr in self.attributes:
                    writer.writerow(attr.to_dict())
            self.app.show_status("属性配置已保存")
        except Exception as e:
            messagebox.showerror("保存失败", str(e))
    
    def generate_code(self):
        if not self.attributes:
            messagebox.showwarning("警告", "没有属性可生成！")
            return
        
        attribute_sets = OrderedDict()
        for attr in self.attributes:
            if attr.set_name not in attribute_sets:
                attribute_sets[attr.set_name] = []
            attribute_sets[attr.set_name].append(attr)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            header_content = AttributeCodeGenerator.generate_header(attribute_sets, timestamp)
            source_content = AttributeCodeGenerator.generate_source(attribute_sets, timestamp)
            
            ATTRIBUTES_HEADER.parent.mkdir(parents=True, exist_ok=True)
            ATTRIBUTES_SOURCE.parent.mkdir(parents=True, exist_ok=True)
            
            with open(ATTRIBUTES_HEADER, 'w', encoding='utf-8') as f:
                f.write(header_content)
            with open(ATTRIBUTES_SOURCE, 'w', encoding='utf-8') as f:
                f.write(source_content)
            
            messagebox.showinfo("生成成功",
                f"C++ 代码已生成！\n\n"
                f"Header:\n{ATTRIBUTES_HEADER}\n\n"
                f"Source:\n{ATTRIBUTES_SOURCE}\n\n"
                f"共 {len(attribute_sets)} 个属性集，{len(self.attributes)} 个属性")
        except Exception as e:
            messagebox.showerror("生成失败", str(e))
    
    def get_attribute_sets(self):
        """供其他模块使用：获取属性集分组"""
        attribute_sets = OrderedDict()
        for attr in self.attributes:
            if attr.set_name not in attribute_sets:
                attribute_sets[attr.set_name] = []
            attribute_sets[attr.set_name].append(attr)
        return attribute_sets
    
    # ========== UI 事件 ==========
    
    def _refresh_set_list(self):
        self.set_listbox.delete(0, tk.END)
        sets = list(OrderedDict.fromkeys(attr.set_name for attr in self.attributes))
        for s in sets:
            count = len([a for a in self.attributes if a.set_name == s])
            self.set_listbox.insert(tk.END, f"{s} ({count})")
    
    def _on_set_select(self, event):
        selection = self.set_listbox.curselection()
        if not selection:
            return
        item = self.set_listbox.get(selection[0])
        set_name = item.split(" (")[0]
        self.current_set.set(set_name)
        self._refresh_attr_list()
    
    def _refresh_attr_list(self):
        self.attr_tree.delete(*self.attr_tree.get_children())
        set_name = self.current_set.get()
        for i, attr in enumerate(self.attributes):
            if attr.set_name == set_name:
                self.attr_tree.insert('', 'end', iid=str(i), values=(
                    attr.name, attr.type, attr.category, attr.default_base, attr.description))
    
    def _on_attr_select(self, event):
        if self._last_selected_idx is not None:
            self._save_attribute_silent(self._last_selected_idx)
        
        selection = self.attr_tree.selection()
        if not selection:
            self._last_selected_idx = None
            return
        
        idx = int(selection[0])
        self._last_selected_idx = idx
        attr = self.attributes[idx]
        
        self.attr_name_var.set(attr.name)
        self.attr_type_var.set(attr.type)
        self.attr_category_var.set(attr.category)
        self.attr_base_var.set(str(attr.default_base))
        self.attr_flat_var.set(str(attr.default_flat))
        self.attr_percent_var.set(str(attr.default_percent))
        self.attr_current_var.set(str(attr.default_current))
        self.attr_desc_var.set(attr.description)
        self._update_ui_by_type()
    
    def _on_rename_attr(self, event):
        """F2 内联重命名属性（编辑第一列）"""
        selection = self.attr_tree.selection()
        if not selection:
            return
        self._start_cell_edit(selection[0], '#1')
    
    def _on_cell_double_click(self, event):
        """双击单元格进行内联编辑"""
        # 销毁已有的编辑控件
        self._destroy_edit_widget()
        
        # 获取点击位置
        region = self.attr_tree.identify_region(event.x, event.y)
        if region != 'cell':
            return
        
        column = self.attr_tree.identify_column(event.x)
        item = self.attr_tree.identify_row(event.y)
        if not item:
            return
        
        self._start_cell_edit(item, column)
    
    def _start_cell_edit(self, item, column):
        """开始单元格编辑"""
        self._destroy_edit_widget()
        
        idx = int(item)
        if idx >= len(self.attributes):
            return
        
        attr = self.attributes[idx]
        
        # 列映射: column_id -> (field_name, widget_type, [options])
        col_map = {
            '#1': ('name', 'entry'),
            '#2': ('type', 'combo', ATTRIBUTE_TYPES),
            '#3': ('category', 'combo', ATTRIBUTE_CATEGORIES),
            '#4': ('base', 'entry'),
            '#5': ('description', 'entry'),
        }
        
        if column not in col_map:
            return
        
        col_info = col_map[column]
        field = col_info[0]
        widget_type = col_info[1]
        
        # 获取单元格位置
        bbox = self.attr_tree.bbox(item, column)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        # 获取当前值
        current_value = self._get_attr_field(attr, field)
        
        # 创建编辑控件
        if widget_type == 'combo':
            options = col_info[2]
            widget = ttk.Combobox(self.attr_tree, values=options, state='readonly')
            widget.set(current_value)
            widget.bind('<<ComboboxSelected>>', lambda e: self._finish_cell_edit(True, attr, field, widget))
        else:
            widget = ttk.Entry(self.attr_tree)
            widget.insert(0, str(current_value))
            widget.select_range(0, tk.END)
        
        widget.place(x=x, y=y, width=max(width, 80), height=height)
        widget.focus()
        self._edit_widget = widget
        self._edit_info = (attr, field, widget)
        
        widget.bind('<Return>', lambda e: self._finish_cell_edit(True, attr, field, widget))
        widget.bind('<Escape>', lambda e: self._finish_cell_edit(False, attr, field, widget))
        widget.bind('<FocusOut>', lambda e: self._finish_cell_edit(True, attr, field, widget))
    
    def _finish_cell_edit(self, save, attr, field, widget):
        """完成单元格编辑"""
        if not self._edit_widget:
            return
        
        if save:
            new_value = widget.get()
            old_value = str(self._get_attr_field(attr, field))
            if new_value != old_value:
                self._set_attr_field(attr, field, new_value)
                self._refresh_attr_list()
                # 同步更新右侧面板
                self._sync_right_panel(attr)
        
        self._destroy_edit_widget()
    
    def _destroy_edit_widget(self):
        """销毁编辑控件"""
        if self._edit_widget:
            try:
                self._edit_widget.destroy()
            except:
                pass
            self._edit_widget = None
    
    def _get_attr_field(self, attr, field):
        """获取属性字段值"""
        if field == 'name':
            return attr.name
        elif field == 'type':
            return attr.type
        elif field == 'category':
            return attr.category
        elif field == 'base':
            return attr.default_base
        elif field == 'description':
            return attr.description
        return ''
    
    def _set_attr_field(self, attr, field, value):
        """设置属性字段值"""
        if field == 'name':
            attr.name = value
        elif field == 'type':
            attr.type = value
        elif field == 'category':
            attr.category = value
        elif field == 'base':
            try:
                attr.default_base = float(value) if value else 0.0
            except ValueError:
                pass
        elif field == 'description':
            attr.description = value
    
    def _sync_right_panel(self, attr):
        """同步右侧面板显示"""
        self.attr_name_var.set(attr.name)
        self.attr_type_var.set(attr.type)
        self.attr_category_var.set(attr.category)
        self.attr_base_var.set(str(attr.default_base))
        self.attr_flat_var.set(str(attr.default_flat))
        self.attr_percent_var.set(str(attr.default_percent))
        self.attr_current_var.set(str(attr.default_current))
        self.attr_desc_var.set(attr.description)
    
    def _on_rename_set(self, event):
        """F2 内联重命名属性集"""
        selection = self.set_listbox.curselection()
        if not selection:
            return
        
        idx = selection[0]
        item = self.set_listbox.get(idx)
        old_name = item.split(" (")[0]
        
        # 获取选中项的位置
        bbox = self.set_listbox.bbox(idx)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        # 创建内联编辑框
        entry = ttk.Entry(self.set_listbox, width=15)
        entry.place(x=x, y=y, width=self.set_listbox.winfo_width()-4, height=height)
        entry.insert(0, old_name)
        entry.select_range(0, tk.END)
        entry.focus()
        
        def finish_edit(save=True):
            if save:
                new_name = entry.get().strip()
                if new_name and new_name != old_name:
                    for attr in self.attributes:
                        if attr.set_name == old_name:
                            attr.set_name = new_name
                    self._refresh_set_list()
                    self.current_set.set(new_name)
                    self._refresh_attr_list()
                    self.app.show_status(f"属性集已重命名为 {new_name}")
            entry.destroy()
        
        entry.bind('<Return>', lambda e: finish_edit(True))
        entry.bind('<Escape>', lambda e: finish_edit(False))
        entry.bind('<FocusOut>', lambda e: finish_edit(True))
    
    def save_current_edit(self):
        """保存当前正在编辑的属性（供 Ctrl+S 调用）"""
        # 先完成任何正在进行的单元格编辑
        self._destroy_edit_widget()
        
        if self._last_selected_idx is not None:
            self._save_attribute_silent(self._last_selected_idx)
            self._refresh_attr_list()
        self.save_config()
    
    def _add_set(self):
        from tkinter import simpledialog
        name = simpledialog.askstring("新建属性集", "属性集名称:")
        if name:
            self.attributes.append(AttributeData(set_name=name, name="NewAttribute", description="新属性"))
            self._refresh_set_list()
    
    def _delete_set(self):
        selection = self.set_listbox.curselection()
        if not selection:
            return
        item = self.set_listbox.get(selection[0])
        set_name = item.split(" (")[0]
        if messagebox.askyesno("确认", f"确定删除属性集 '{set_name}'?"):
            self.attributes = [a for a in self.attributes if a.set_name != set_name]
            self._refresh_set_list()
            self.attr_tree.delete(*self.attr_tree.get_children())
    
    def _add_attribute(self):
        set_name = self.current_set.get()
        if not set_name:
            messagebox.showwarning("警告", "请先选择一个属性集")
            return
        self.attributes.append(AttributeData(set_name=set_name, name="NewAttribute", description="新属性"))
        self._refresh_attr_list()
        self._refresh_set_list()
    
    def _delete_attribute(self):
        selection = self.attr_tree.selection()
        if not selection:
            return
        idx = int(selection[0])
        del self.attributes[idx]
        self._refresh_attr_list()
        self._refresh_set_list()
    
    def _save_attribute_silent(self, idx):
        if idx is None or idx >= len(self.attributes):
            return
        try:
            attr = self.attributes[idx]
            attr.name = self.attr_name_var.get()
            attr.type = self.attr_type_var.get()
            attr.category = self.attr_category_var.get()
            attr.default_base = float(self.attr_base_var.get() or 0)
            attr.default_flat = float(self.attr_flat_var.get() or 0)
            attr.default_percent = float(self.attr_percent_var.get() or 0)
            attr.default_current = float(self.attr_current_var.get() or 0)
            attr.description = self.attr_desc_var.get()
        except (ValueError, IndexError):
            pass
    
    def _save_attribute(self):
        selection = self.attr_tree.selection()
        if not selection:
            return
        idx = int(selection[0])
        self._save_attribute_silent(idx)
        self._refresh_attr_list()
        for item in self.attr_tree.get_children():
            if int(item) == idx:
                self.attr_tree.selection_set(item)
                break
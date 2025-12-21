#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Execution 编辑器 UI
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import (
    EXECUTIONS_CONFIG, EXECUTIONS_OUTPUT,
    CAPTURE_LAYERS, OUTPUT_OPS, TAG_EFFECTS, TAG_SOURCES
)
from ui_base import BaseEditorUI, GroupListWidget, BottomButtonBar, InlineEditorMixin
from execution.data import ExecutionData
from execution.generator import ExecutionCodeGenerator


class ExecutionEditorUI(BaseEditorUI, InlineEditorMixin):
    """Execution 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.executions = []
        self.current_exe = None
        
        # 当前编辑的 Treeview 及其数据上下文
        self._current_tree = None
        self._current_tree_data = None
        self._editor_ready = False  # 编辑器就绪标志
        
        super().__init__(parent, app)
        self._init_inline_editor()
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        """创建 UI"""
        main_paned = ttk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左侧：Execution 列表
        left_frame = ttk.LabelFrame(main_paned, text="Execution 列表", width=200)
        main_paned.add(left_frame, weight=1)
        
        self.exec_list = GroupListWidget(
            left_frame,
            title="Execution",
            on_select=self._on_exec_select,
            on_add=self._on_add_exec,
            on_delete=self._on_delete_exec,
            show_count=False
        )
        self.exec_list.pack(fill=tk.BOTH, expand=True)
        
        # 右侧：编辑区
        right_frame = ttk.Frame(main_paned)
        main_paned.add(right_frame, weight=4)
        
        self._create_edit_area(right_frame)
        
        # 底部按钮
        self.button_bar = BottomButtonBar(self.parent)
        self.button_bar.add_button("保存配置", self.save_current_edit)
        self.button_bar.add_button("重新加载", self.load_data)
        self.button_bar.add_button("[生成代码]", self.generate_code, side=tk.RIGHT)
        self.button_bar.pack(fill=tk.X, padx=5, pady=5)
        
        # 为所有表格绑定 Delete 快捷键
        self._bind_delete_key()
    
    def _bind_delete_key(self):
        """为所有表格绑定 Delete 快捷键删除功能"""
        trees = [
            (self.capture_tree, self._delete_capture),
            (self.tag_tree, self._delete_tag_cond),
            (self.output_tree, self._delete_output),
        ]
        
        for tree, delete_func in trees:
            tree.bind('<Delete>', lambda e, t=tree, f=delete_func: self._on_delete_key(t, f))
            tree.bind('<BackSpace>', lambda e, t=tree, f=delete_func: self._on_delete_key(t, f))
    
    def _on_delete_key(self, tree, delete_func):
        """处理 Delete 键删除"""
        selected = tree.selection()
        if not selected:
            return
        
        item = selected[0]
        all_items = tree.get_children()
        
        if not all_items:
            return
        
        # 找到当前项的索引
        try:
            current_idx = list(all_items).index(item)
        except ValueError:
            return
        
        # 计算删除后要选中的项
        if len(all_items) <= 1:
            # 只有一项，删除后无需选中
            next_item = None
        elif current_idx == 0:
            # 第一行，选中下一行（删除后变成第一行）
            next_item = all_items[1]
        else:
            # 其他情况，选中上一行
            next_item = all_items[current_idx - 1]
        
        # 执行删除
        tree.delete(item)
        self._refresh_variable_hints()
        
        # 选中新的项
        if next_item and next_item in tree.get_children():
            tree.selection_set(next_item)
            tree.focus(next_item)
    
    def _create_edit_area(self, parent):
        """创建编辑区域"""
        # 描述
        desc_frame = ttk.Frame(parent)
        desc_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(desc_frame, text="描述:").pack(side=tk.LEFT)
        self.desc_var = tk.StringVar()
        ttk.Entry(desc_frame, textvariable=self.desc_var, width=60).pack(side=tk.LEFT, padx=5)
        
        # 使用 PanedWindow 分为上下两部分
        main_paned = ttk.PanedWindow(parent, orient=tk.VERTICAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 上半部分：输入/输出配置（三个表格水平排列）
        config_frame = ttk.Frame(main_paned)
        main_paned.add(config_frame, weight=1)
        self._create_config_panel(config_frame)
        
        # 下半部分：计算公式
        formula_frame = ttk.LabelFrame(main_paned, text="计算公式")
        main_paned.add(formula_frame, weight=1)
        self._create_formula_panel(formula_frame)
    
    def _create_config_panel(self, parent):
        """创建配置面板（捕获属性 + Tag捕获 + 输出属性）"""
        # 使用水平 PanedWindow 放置三个表格
        config_paned = ttk.PanedWindow(parent, orient=tk.HORIZONTAL)
        config_paned.pack(fill=tk.BOTH, expand=True)
        
        # 捕获属性
        cap_frame = ttk.LabelFrame(config_paned, text="捕获属性 (输入)")
        config_paned.add(cap_frame, weight=2)
        self._create_capture_table(cap_frame)
        
        # Tag 捕获
        tag_frame = ttk.LabelFrame(config_paned, text="Tag 捕获")
        config_paned.add(tag_frame, weight=1)
        self._create_tag_table(tag_frame)
        
        # 输出属性
        out_frame = ttk.LabelFrame(config_paned, text="输出属性")
        config_paned.add(out_frame, weight=1)
        self._create_output_table(out_frame)
    
    def _create_capture_table(self, parent):
        """创建捕获属性表格"""
        cols = ("source", "set", "attr", "layer")
        self.capture_tree = ttk.Treeview(parent, columns=cols, show='headings', height=6)
        self.capture_tree.heading("source", text="来源")
        self.capture_tree.heading("set", text="属性集")
        self.capture_tree.heading("attr", text="属性")
        self.capture_tree.heading("layer", text="层级")
        
        self.capture_tree.column("source", width=60)
        self.capture_tree.column("set", width=80)
        self.capture_tree.column("attr", width=100)
        self.capture_tree.column("layer", width=50)
        
        self.capture_tree.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        self.capture_tree.bind('<Button-1>', lambda e: self._on_tree_click(e, self.capture_tree, 'capture'))
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=2, pady=2)
        ttk.Button(btn_frame, text="+", width=3, command=self._add_capture).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="-", width=3, command=self._delete_capture).pack(side=tk.LEFT)
    
    def _create_tag_table(self, parent):
        """创建 Tag 捕获表格（三列：来源、分类、Tag）"""
        cols = ("source", "category", "tag")
        self.tag_tree = ttk.Treeview(parent, columns=cols, show='headings', height=6)
        self.tag_tree.heading("source", text="来源")
        self.tag_tree.heading("category", text="分类")
        self.tag_tree.heading("tag", text="Tag")
        
        self.tag_tree.column("source", width=60)
        self.tag_tree.column("category", width=80)
        self.tag_tree.column("tag", width=120)
        
        self.tag_tree.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        self.tag_tree.bind('<Button-1>', lambda e: self._on_tree_click(e, self.tag_tree, 'tag'))
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=2, pady=2)
        ttk.Button(btn_frame, text="+S", width=3, command=lambda: self._add_tag_cond('Source')).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="+T", width=3, command=lambda: self._add_tag_cond('Target')).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="-", width=3, command=self._delete_tag_cond).pack(side=tk.LEFT)
    
    def _create_output_table(self, parent):
        """创建输出属性表格"""
        cols = ("set", "attr", "op")
        self.output_tree = ttk.Treeview(parent, columns=cols, show='headings', height=6)
        self.output_tree.heading("set", text="属性集")
        self.output_tree.heading("attr", text="属性")
        self.output_tree.heading("op", text="操作")
        
        self.output_tree.column("set", width=80)
        self.output_tree.column("attr", width=80)
        self.output_tree.column("op", width=60)
        
        self.output_tree.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        self.output_tree.bind('<Button-1>', lambda e: self._on_tree_click(e, self.output_tree, 'output'))
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=2, pady=2)
        ttk.Button(btn_frame, text="+", width=3, command=self._add_output).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="-", width=3, command=self._delete_output).pack(side=tk.LEFT)
    
    def _create_formula_panel(self, parent):
        """创建公式编辑面板"""
        # 顶部：可用变量面板（两行：Source 和 Target）
        var_container = ttk.LabelFrame(parent, text="可用变量")
        var_container.pack(fill=tk.X, padx=5, pady=2)
        
        # Source 行
        self.source_var_frame = ttk.Frame(var_container)
        self.source_var_frame.pack(fill=tk.X, padx=2, pady=1)
        
        # Target 行
        self.target_var_frame = ttk.Frame(var_container)
        self.target_var_frame.pack(fill=tk.X, padx=2, pady=1)
        
        # 输出行
        self.output_var_frame = ttk.Frame(var_container)
        self.output_var_frame.pack(fill=tk.X, padx=2, pady=1)
        
        # 公式编辑区
        self.formula_text = tk.Text(parent, height=8, font=("Consolas", 10))
        self.formula_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        # 快捷插入
        snippet_frame = ttk.Frame(parent)
        snippet_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(snippet_frame, text="快捷:", foreground="gray").pack(side=tk.LEFT)
        for text, snippet in [("Max", "FMath::Max(, )"), ("Min", "FMath::Min(, )"), 
                               ("Clamp", "FMath::Clamp(, 0.f, 1.f)"), ("Final=", "float FinalValue = ")]:
            ttk.Button(snippet_frame, text=text, width=6,
                       command=lambda s=snippet: self._insert_snippet(s)).pack(side=tk.LEFT, padx=1)
    

    
    def _insert_snippet(self, snippet):
        """插入代码片段到公式"""
        self.formula_text.insert(tk.INSERT, snippet)
        self.formula_text.focus_set()
    
    def _insert_variable(self, var_name):
        """插入变量到公式"""
        self.formula_text.insert(tk.INSERT, var_name)
        self.formula_text.focus_set()
    
    def _refresh_variable_hints(self):
        """刷新可用变量提示（分 Source/Target 两行显示）"""
        # 清空三行
        for widget in self.source_var_frame.winfo_children():
            widget.destroy()
        for widget in self.target_var_frame.winfo_children():
            widget.destroy()
        for widget in self.output_var_frame.winfo_children():
            widget.destroy()
        
        source_vars = []  # (display_name, insert_text, desc, var_type)
        target_vars = []
        
        # 获取捕获属性变量
        for item in self.capture_tree.get_children():
            values = self.capture_tree.item(item, 'values')
            source = values[0] if len(values) > 0 else 'Source'
            attr = values[2] if len(values) > 2 else ''
            layer = values[3] if len(values) > 3 else 'Total'
            
            if not attr:
                continue
            
            suffix = "_Target" if source == "Target" else ""
            var_name = f"{attr}{suffix}Value"
            desc = f"{attr}" + (" (Total)" if layer == "Total" else f" ({layer})")
            
            var_info = (var_name, var_name, desc, "attr")
            if source == "Target":
                target_vars.append(var_info)
            else:
                source_vars.append(var_info)
        
        # 获取 Tag 变量（生成 if 语句模板）
        for item in self.tag_tree.get_children():
            values = self.tag_tree.item(item, 'values')
            source = values[0] if len(values) > 0 else 'Target'
            tag = values[2] if len(values) > 2 else ''
            
            if not tag:
                continue
            
            var_name = self._get_tag_var_name(source, tag)
            if_template = f"if ({var_name})\n{{\n    \n}}"
            desc = f"{tag}\n点击插入 if 语句"
            
            var_info = (var_name, if_template, desc, "tag")
            if source == "Target":
                target_vars.append(var_info)
            else:
                source_vars.append(var_info)
        
        if not source_vars and not target_vars:
            ttk.Label(self.source_var_frame, text="(添加捕获属性/Tag后显示变量)", 
                      foreground="gray").pack(side=tk.LEFT)
            return
        
        # Source 行
        if source_vars:
            ttk.Label(self.source_var_frame, text="Source:", foreground="blue", 
                      width=8).pack(side=tk.LEFT)
            for display_name, insert_text, desc, var_type in source_vars:
                btn_text = f"if({display_name})" if var_type == "tag" else display_name
                btn = ttk.Button(self.source_var_frame, text=btn_text,
                                command=lambda t=insert_text: self._insert_variable(t))
                btn.pack(side=tk.LEFT, padx=1)
                self._create_tooltip(btn, desc)
        else:
            ttk.Label(self.source_var_frame, text="Source:", foreground="gray", 
                      width=8).pack(side=tk.LEFT)
            ttk.Label(self.source_var_frame, text="(无)", foreground="gray").pack(side=tk.LEFT)
        
        # Target 行
        if target_vars:
            ttk.Label(self.target_var_frame, text="Target:", foreground="red", 
                      width=8).pack(side=tk.LEFT)
            for display_name, insert_text, desc, var_type in target_vars:
                btn_text = f"if({display_name})" if var_type == "tag" else display_name
                btn = ttk.Button(self.target_var_frame, text=btn_text,
                                command=lambda t=insert_text: self._insert_variable(t))
                btn.pack(side=tk.LEFT, padx=1)
                self._create_tooltip(btn, desc)
        else:
            ttk.Label(self.target_var_frame, text="Target:", foreground="gray", 
                      width=8).pack(side=tk.LEFT)
            ttk.Label(self.target_var_frame, text="(无)", foreground="gray").pack(side=tk.LEFT)
        
        # 输出行
        ttk.Label(self.output_var_frame, text="Output:", foreground="green", 
                  width=8).pack(side=tk.LEFT)
        btn = ttk.Button(self.output_var_frame, text="FinalValue",
                        command=lambda: self._insert_variable("FinalValue"))
        btn.pack(side=tk.LEFT, padx=1)
        self._create_tooltip(btn, "输出值 (必须定义)")
    
    def _create_tooltip(self, widget, text):
        """为控件创建简单的 tooltip"""
        def show_tip(event):
            tip = tk.Toplevel(widget)
            tip.wm_overrideredirect(True)
            tip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            label = ttk.Label(tip, text=text, background="#ffffe0", relief="solid", borderwidth=1)
            label.pack()
            widget._tip = tip
            widget.after(1500, lambda: tip.destroy() if hasattr(widget, '_tip') and widget._tip == tip else None)
        
        def hide_tip(event):
            if hasattr(widget, '_tip') and widget._tip:
                widget._tip.destroy()
                widget._tip = None
        
        widget.bind('<Enter>', show_tip)
        widget.bind('<Leave>', hide_tip)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        """加载配置"""
        self.executions = []
        try:
            if EXECUTIONS_CONFIG.exists():
                with open(EXECUTIONS_CONFIG, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 支持两种格式：直接数组 或 {"Executions": [...]}
                    items = data if isinstance(data, list) else data.get('Executions', [])
                    for item in items:
                        self.executions.append(ExecutionData.from_dict(item))
        except Exception as e:
            messagebox.showerror("错误", f"加载配置失败: {e}")
        
        self._refresh_exec_list()
    
    def save_config(self):
        """保存配置"""
        try:
            EXECUTIONS_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            data = {'Executions': [e.to_dict() for e in self.executions]}
            with open(EXECUTIONS_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {e}")
            return False
    
    def save_current_edit(self):
        """保存当前编辑"""
        self._save_current_to_data()
        if self.save_config():
            self.app.show_status("Execution 配置已保存")
    
    def _save_current_to_data(self):
        """保存当前编辑到数据"""
        if not self.current_exe:
            return
        
        self.current_exe.description = self.desc_var.get()
        self.current_exe.formula = self.formula_text.get('1.0', tk.END).strip()
        
        # 保存捕获属性
        self.current_exe.captures = []
        for item in self.capture_tree.get_children():
            values = self.capture_tree.item(item, 'values')
            self.current_exe.captures.append({
                'source': values[0], 'set': values[1], 'attr': values[2], 'layer': values[3]
            })
        
        # 保存输出属性
        self.current_exe.outputs = []
        for item in self.output_tree.get_children():
            values = self.output_tree.item(item, 'values')
            self.current_exe.outputs.append({
                'set': values[0], 'attr': values[1], 'op': values[2]
            })
        
        # 保存 Tag 捕获（三列结构）
        self.current_exe.tag_conditions = []
        for item in self.tag_tree.get_children():
            values = self.tag_tree.item(item, 'values')
            self.current_exe.tag_conditions.append({
                'source': values[0], 
                'category': values[1] if len(values) > 1 else '',
                'tag': values[2] if len(values) > 2 else ''
            })
    
    def _refresh_exec_list(self):
        """刷新列表"""
        names = [e.name for e in self.executions if e.name]
        self.exec_list.refresh(names)
    
    def _on_exec_select(self, idx, name):
        """选择 Execution"""
        if self.current_exe:
            self._save_current_to_data()
        
        self.current_exe = None
        for e in self.executions:
            if e.name == name:
                self.current_exe = e
                break
        
        self._display_exec(self.current_exe)
    
    def _display_exec(self, exe):
        """显示 Execution"""
        self.capture_tree.delete(*self.capture_tree.get_children())
        self.output_tree.delete(*self.output_tree.get_children())
        self.tag_tree.delete(*self.tag_tree.get_children())
        self.formula_text.delete('1.0', tk.END)
        self.desc_var.set('')
        
        if not exe:
            return
        
        self.desc_var.set(exe.description)
        
        for cap in exe.captures:
            self.capture_tree.insert('', tk.END, values=(
                cap.get('source', 'Source'), cap.get('set', ''),
                cap.get('attr', ''), cap.get('layer', 'Total')
            ))
        
        for out in exe.outputs:
            self.output_tree.insert('', tk.END, values=(
                out.get('set', ''), out.get('attr', ''), out.get('op', 'Additive')
            ))
        
        for cond in exe.tag_conditions:
            source = cond.get('source', 'Target')
            tag = cond.get('tag', '')
            # 从 tag 中提取分类（兼容旧数据）
            category = cond.get('category', '')
            if not category and tag and '.' in tag:
                category = tag.split('.')[0]
            self.tag_tree.insert('', tk.END, values=(source, category, tag))
        
        self.formula_text.insert('1.0', exe.formula)
        self._refresh_variable_hints()
    
    def _on_add_exec(self):
        """添加"""
        name = f"NewExecution{len(self.executions) + 1}"
        self.executions.append(ExecutionData(name, "新的 Execution"))
        self._refresh_exec_list()
        self.exec_list.select_item(name)
    
    def _on_delete_exec(self, idx, name):
        """删除"""
        if messagebox.askyesno("确认", f"确定删除 '{name}'?"):
            self.executions = [e for e in self.executions if e.name != name]
            self.current_exe = None
            self._refresh_exec_list()
            self._display_exec(None)
    
    def _add_capture(self):
        """添加捕获"""
        attrs = self.app.get_attributes()
        if not attrs:
            messagebox.showwarning("提示", "请先定义属性")
            return
        
        # 简单添加默认项
        sets = list(set(a.set_name for a in attrs))
        if sets:
            attr_names = [a.name for a in attrs if a.set_name == sets[0]]
            self.capture_tree.insert('', tk.END, values=(
                'Source', sets[0], attr_names[0] if attr_names else '', 'Total'
            ))
        self._refresh_variable_hints()
    
    def _delete_capture(self):
        """删除捕获属性（由按钮调用）"""
        self._on_delete_key(self.capture_tree, None)
    
    def _add_output(self):
        """添加输出"""
        attrs = self.app.get_attributes()
        if not attrs:
            messagebox.showwarning("提示", "请先定义属性")
            return
        
        sets = list(set(a.set_name for a in attrs))
        if sets:
            attr_names = [a.name for a in attrs if a.set_name == sets[0]]
            self.output_tree.insert('', tk.END, values=(
                sets[0], attr_names[0] if attr_names else '', 'Additive'
            ))
    
    def _delete_output(self):
        """删除输出属性（由按钮调用）"""
        self._on_delete_key(self.output_tree, None)
    
    def _add_tag_cond(self, source='Target'):
        """添加 Tag 捕获"""
        # 获取可用的分类
        tag_categories = self._get_tag_categories()
        default_category = tag_categories[0] if tag_categories else 'Status'
        
        # 获取该分类下的第一个Tag
        tags_in_cat = self._get_tags_for_category(default_category)
        default_tag = tags_in_cat[0] if tags_in_cat else f'{default_category}.Example'
        
        self.tag_tree.insert('', tk.END, values=(source, default_category, default_tag))
        self._refresh_variable_hints()
    
    def _get_tag_var_name(self, source, tag):
        """根据 source 和 tag 生成变量名"""
        # 把 tag 中的 . 替换为 _，生成 bool 变量名
        tag_clean = tag.replace('.', '_').replace('-', '_')
        if source == 'Target':
            return f"bTarget_{tag_clean}"
        else:
            return f"bSource_{tag_clean}"
    

    def _delete_tag_cond(self):
        """删除 Tag 捕获（由按钮调用）"""
        self._on_delete_key(self.tag_tree, None)
    
    # ========== 单击编辑功能 ==========
    
    def _on_tree_click(self, event, tree, tree_type):
        """处理 Treeview 单击事件"""
        # 检查是否点击在当前编辑器内，如果是则不处理
        if self._active_editor:
            try:
                ex = self._active_editor.winfo_x()
                ey = self._active_editor.winfo_y()
                ew = self._active_editor.winfo_width()
                eh = self._active_editor.winfo_height()
                if ex <= event.x <= ex + ew and ey <= event.y <= ey + eh:
                    return  # 点击在编辑器内，不处理
            except:
                pass
        
        # 先销毁之前的编辑器
        self._destroy_active_editor()
        
        # 延迟处理以区分单击和双击
        tree.after(180, lambda: self._handle_tree_click(event, tree, tree_type))
    
    def _handle_tree_click(self, event, tree, tree_type):
        """实际处理单击编辑"""
        cell_info = self._get_cell_info(tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        x, y, w, h = bbox
        
        # 先选中行
        tree.selection_set(item)
        tree.focus(item)
        
        # 获取当前行数据
        current_values = list(tree.item(item, 'values'))
        
        # 根据 tree_type 和 col_idx 决定编辑器类型
        if tree_type == 'capture':
            self._edit_capture_cell(tree, item, col_idx, x, y, w, h, current_values)
        elif tree_type == 'output':
            self._edit_output_cell(tree, item, col_idx, x, y, w, h, current_values)
        elif tree_type == 'tag':
            self._edit_tag_cell(tree, item, col_idx, x, y, w, h, current_values)
    
    def _edit_capture_cell(self, tree, item, col_idx, x, y, w, h, current_values):
        """编辑捕获属性单元格"""
        # 列: source(0), set(1), attr(2), layer(3)
        if col_idx == 0:  # source
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, 
                                    ['Source', 'Target'])
        elif col_idx == 1:  # set
            sets = self._get_attribute_sets()
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, sets)
        elif col_idx == 2:  # attr
            set_name = current_values[1] if len(current_values) > 1 else ''
            attrs = self._get_attributes_for_set(set_name)
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, attrs)
        elif col_idx == 3:  # layer
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, CAPTURE_LAYERS)
    
    def _edit_output_cell(self, tree, item, col_idx, x, y, w, h, current_values):
        """编辑输出属性单元格"""
        # 列: set(0), attr(1), op(2)
        if col_idx == 0:  # set
            sets = self._get_attribute_sets()
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, sets)
        elif col_idx == 1:  # attr
            set_name = current_values[0] if len(current_values) > 0 else ''
            attrs = self._get_attributes_for_set(set_name)
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, attrs)
        elif col_idx == 2:  # op
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, OUTPUT_OPS)
    
    def _edit_tag_cell(self, tree, item, col_idx, x, y, w, h, current_values):
        """编辑 Tag 捕获单元格（三列：来源、分类、Tag）"""
        if col_idx == 0:  # source
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, 
                                    ['Source', 'Target'])
        elif col_idx == 1:  # category - 选择分类后联动更新 Tag 列
            categories = self._get_tag_categories()
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, 
                                    categories, on_change=lambda: self._on_tag_category_change(tree, item))
        elif col_idx == 2:  # tag - 根据当前分类筛选
            category = current_values[1] if len(current_values) > 1 else ''
            tags = self._get_tags_for_category(category) if category else self._get_available_tags()
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, tags)
    
    def _on_tag_category_change(self, tree, item):
        """当 Tag 分类改变时，自动更新 Tag 列"""
        current_values = list(tree.item(item, 'values'))
        category = current_values[1] if len(current_values) > 1 else ''
        
        # 获取新分类下的 Tags
        tags_in_cat = self._get_tags_for_category(category)
        
        # 如果当前 Tag 不属于新分类，自动选择第一个
        current_tag = current_values[2] if len(current_values) > 2 else ''
        if current_tag not in tags_in_cat and tags_in_cat:
            current_values[2] = tags_in_cat[0]
            tree.item(item, values=current_values)
        
        self._refresh_variable_hints()
    
    def _get_available_tags(self):
        """获取项目中已定义的 Tag 列表"""
        tags = self.app.get_tags() if hasattr(self.app, 'get_tags') else []
        # TagData 对象使用 .tag 属性存储完整标签路径
        if tags:
            return [t.tag if hasattr(t, 'tag') else str(t) for t in tags]
        return []
    
    def _get_tag_categories(self):
        """获取所有 Tag 的顶级分类"""
        all_tags = self._get_available_tags()
        categories = set()
        for tag in all_tags:
            if '.' in tag:
                categories.add(tag.split('.')[0])
            else:
                categories.add(tag)
        return sorted(categories)
    
    def _get_tags_for_category(self, category):
        """获取指定分类下的所有 Tag"""
        all_tags = self._get_available_tags()
        return sorted([t for t in all_tags if t.startswith(category + '.') or t == category])
    
    def _create_cell_combo(self, tree, item, col_idx, x, y, w, h, current_values, options, on_change=None):
        """创建下拉框编辑器"""
        self._destroy_active_editor()
        
        combo = ttk.Combobox(tree, values=options, width=max(10, w // 8))
        current_val = current_values[col_idx] if col_idx < len(current_values) else ''
        combo.set(current_val)
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        self._editor_ready = False  # 标记编辑器尚未就绪
        
        def do_save():
            if self._active_editor != combo:
                return
            current_values[col_idx] = combo.get()
            tree.item(item, values=current_values)
            self._destroy_active_editor()
            # 执行自定义回调
            if on_change:
                on_change()
            # 如果是捕获属性或Tag条件表格，刷新变量提示
            if tree == self.capture_tree or tree == self.tag_tree:
                self._refresh_variable_hints()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        def on_focus_out(event):
            # 只有就绪后才响应 FocusOut
            if self._editor_ready and self._active_editor == combo:
                tree.after(50, do_save)
        
        # 下拉框选择后保存
        combo.bind('<<ComboboxSelected>>', lambda e: do_save())
        # 回车确认
        combo.bind('<Return>', lambda e: do_save())
        # Escape 取消
        combo.bind('<Escape>', on_escape)
        # 失去焦点时保存（延迟启用）
        combo.bind('<FocusOut>', on_focus_out)
        
        combo.focus_set()
        # 自动展开下拉框，并在之后标记就绪
        def post_and_ready():
            if self._active_editor == combo:
                try:
                    combo.tk.call('ttk::combobox::Post', combo)
                except:
                    pass
                # 延迟标记就绪，确保下拉框已完全展开
                combo.after(200, lambda: setattr(self, '_editor_ready', True))
        
        combo.after(80, post_and_ready)
    
    def _create_cell_entry(self, tree, item, col_idx, x, y, w, h, current_values, value_type=str, on_change=None):
        """创建文本框编辑器"""
        self._destroy_active_editor()
        
        entry = ttk.Entry(tree, width=max(5, w // 8))
        current_val = current_values[col_idx] if col_idx < len(current_values) else ''
        entry.insert(0, str(current_val))
        entry.place(x=x, y=y, width=w, height=h)
        entry.select_range(0, tk.END)
        self._active_editor = entry
        self._editor_ready = False  # 标记编辑器尚未就绪
        
        def on_confirm(event=None):
            if self._active_editor != entry:
                return
            try:
                new_value = value_type(entry.get())
            except ValueError:
                new_value = 0 if value_type in (int, float) else ''
            current_values[col_idx] = new_value
            tree.item(item, values=current_values)
            self._destroy_active_editor()
            # 执行自定义回调
            if on_change:
                on_change()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        def on_focus_out(event):
            # 只有就绪后才响应 FocusOut
            if self._editor_ready and self._active_editor == entry:
                tree.after(50, on_confirm)
        
        # 回车确认
        entry.bind('<Return>', on_confirm)
        # Escape 取消
        entry.bind('<Escape>', on_escape)
        # 失去焦点时保存（延迟启用）
        entry.bind('<FocusOut>', on_focus_out)
        
        entry.focus_set()
        # 延迟标记就绪
        entry.after(250, lambda: setattr(self, '_editor_ready', True))
    
    def _get_attribute_sets(self):
        """获取所有属性集名称"""
        attrs = self.app.get_attributes()
        if not attrs:
            return []
        return list(set(a.set_name for a in attrs))
    
    def _get_attributes_for_set(self, set_name):
        """获取指定属性集的所有属性名"""
        attrs = self.app.get_attributes()
        if not attrs:
            return []
        return [a.name for a in attrs if a.set_name == set_name]
    
    def generate_code(self):
        """生成代码"""
        self._save_current_to_data()
        
        valid_exes = [e for e in self.executions if e.name]
        if not valid_exes:
            messagebox.showwarning("提示", "没有可生成的 Execution")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            EXECUTIONS_OUTPUT.mkdir(parents=True, exist_ok=True)
            
            for exe in valid_exes:
                header, source = ExecutionCodeGenerator.generate(exe, timestamp)
                class_name = f"UDJ01{exe.name}Execution"
                
                h_path = EXECUTIONS_OUTPUT / f"{class_name}.h"
                cpp_path = EXECUTIONS_OUTPUT / f"{class_name}.cpp"
                
                with open(h_path, 'w', encoding='utf-8') as f:
                    f.write(header)
                with open(cpp_path, 'w', encoding='utf-8') as f:
                    f.write(source)
            
            self.save_config()
            messagebox.showinfo("成功", f"已生成 {len(valid_exes)} 个 Execution")
        except Exception as e:
            messagebox.showerror("错误", f"生成失败: {e}")
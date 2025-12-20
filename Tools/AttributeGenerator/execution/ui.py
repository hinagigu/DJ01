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
    
    def _create_edit_area(self, parent):
        """创建编辑区域"""
        # 描述
        desc_frame = ttk.Frame(parent)
        desc_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(desc_frame, text="描述:").pack(side=tk.LEFT)
        self.desc_var = tk.StringVar()
        ttk.Entry(desc_frame, textvariable=self.desc_var, width=60).pack(side=tk.LEFT, padx=5)
        
        # Notebook 分页
        notebook = ttk.Notebook(parent)
        notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 捕获属性页
        cap_frame = ttk.Frame(notebook)
        notebook.add(cap_frame, text="捕获属性")
        self._create_capture_tab(cap_frame)
        
        # 输出属性页
        out_frame = ttk.Frame(notebook)
        notebook.add(out_frame, text="输出属性")
        self._create_output_tab(out_frame)
        
        # Tag 条件页
        tag_frame = ttk.Frame(notebook)
        notebook.add(tag_frame, text="Tag 条件")
        self._create_tag_tab(tag_frame)
        
        # 公式页
        formula_frame = ttk.Frame(notebook)
        notebook.add(formula_frame, text="计算公式")
        self._create_formula_tab(formula_frame)
    
    def _create_capture_tab(self, parent):
        """创建捕获属性页"""
        cols = ("source", "set", "attr", "layer")
        self.capture_tree = ttk.Treeview(parent, columns=cols, show='headings', height=8)
        self.capture_tree.heading("source", text="来源")
        self.capture_tree.heading("set", text="属性集")
        self.capture_tree.heading("attr", text="属性")
        self.capture_tree.heading("layer", text="层级")
        
        self.capture_tree.column("source", width=80)
        self.capture_tree.column("set", width=120)
        self.capture_tree.column("attr", width=120)
        self.capture_tree.column("layer", width=80)
        
        self.capture_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 绑定单击编辑
        self.capture_tree.bind('<Button-1>', lambda e: self._on_tree_click(e, self.capture_tree, 'capture'))
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=5)
        ttk.Button(btn_frame, text="添加", command=self._add_capture).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="删除", command=self._delete_capture).pack(side=tk.LEFT, padx=2)
    
    def _create_output_tab(self, parent):
        """创建输出属性页"""
        cols = ("set", "attr", "op")
        self.output_tree = ttk.Treeview(parent, columns=cols, show='headings', height=8)
        self.output_tree.heading("set", text="属性集")
        self.output_tree.heading("attr", text="属性")
        self.output_tree.heading("op", text="操作")
        
        self.output_tree.column("set", width=120)
        self.output_tree.column("attr", width=120)
        self.output_tree.column("op", width=100)
        
        self.output_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 绑定单击编辑
        self.output_tree.bind('<Button-1>', lambda e: self._on_tree_click(e, self.output_tree, 'output'))
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=5)
        ttk.Button(btn_frame, text="添加", command=self._add_output).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="删除", command=self._delete_output).pack(side=tk.LEFT, padx=2)
    
    def _create_tag_tab(self, parent):
        """创建 Tag 条件页"""
        cols = ("source", "tag", "effect", "value")
        self.tag_tree = ttk.Treeview(parent, columns=cols, show='headings', height=8)
        self.tag_tree.heading("source", text="来源")
        self.tag_tree.heading("tag", text="Tag")
        self.tag_tree.heading("effect", text="效果")
        self.tag_tree.heading("value", text="值")
        
        self.tag_tree.column("source", width=80)
        self.tag_tree.column("tag", width=150)
        self.tag_tree.column("effect", width=100)
        self.tag_tree.column("value", width=80)
        
        self.tag_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 绑定单击编辑
        self.tag_tree.bind('<Button-1>', lambda e: self._on_tree_click(e, self.tag_tree, 'tag'))
        
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=5)
        ttk.Button(btn_frame, text="添加", command=self._add_tag_cond).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="删除", command=self._delete_tag_cond).pack(side=tk.LEFT, padx=2)
    
    def _create_formula_tab(self, parent):
        """创建公式页"""
        hint = "可用变量: 捕获的属性名+Value (如 AttackPowerValue, Defense_TargetValue)"
        ttk.Label(parent, text=hint, foreground="gray").pack(anchor=tk.W, padx=5, pady=5)
        
        self.formula_text = tk.Text(parent, height=10, font=("Consolas", 10))
        self.formula_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
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
        
        # 保存 Tag 条件
        self.current_exe.tag_conditions = []
        for item in self.tag_tree.get_children():
            values = self.tag_tree.item(item, 'values')
            self.current_exe.tag_conditions.append({
                'source': values[0], 'tag': values[1], 'effect': values[2],
                'value': float(values[3]) if values[3] else 0
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
            self.tag_tree.insert('', tk.END, values=(
                cond.get('source', 'Target'), cond.get('tag', ''),
                cond.get('effect', 'Skip'), cond.get('value', 0)
            ))
        
        self.formula_text.insert('1.0', exe.formula)
    
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
    
    def _delete_capture(self):
        selected = self.capture_tree.selection()
        if selected:
            self.capture_tree.delete(selected[0])
    
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
        selected = self.output_tree.selection()
        if selected:
            self.output_tree.delete(selected[0])
    
    def _add_tag_cond(self):
        self.tag_tree.insert('', tk.END, values=('Target', 'Status.Immunity', 'Skip', 0))
    
    def _delete_tag_cond(self):
        selected = self.tag_tree.selection()
        if selected:
            self.tag_tree.delete(selected[0])
    
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
        """编辑 Tag 条件单元格"""
        # 列: source(0), tag(1), effect(2), value(3)
        if col_idx == 0:  # source
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, TAG_SOURCES)
        elif col_idx == 1:  # tag
            self._create_cell_entry(tree, item, col_idx, x, y, w, h, current_values)
        elif col_idx == 2:  # effect
            self._create_cell_combo(tree, item, col_idx, x, y, w, h, current_values, TAG_EFFECTS)
        elif col_idx == 3:  # value
            self._create_cell_entry(tree, item, col_idx, x, y, w, h, current_values, value_type=float)
    
    def _create_cell_combo(self, tree, item, col_idx, x, y, w, h, current_values, options):
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
    
    def _create_cell_entry(self, tree, item, col_idx, x, y, w, h, current_values, value_type=str):
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
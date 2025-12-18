#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - Execution 编辑器 UI
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
from collections import OrderedDict

from config import (
    EXECUTIONS_CONFIG, EXECUTIONS_OUTPUT,
    CAPTURE_LAYERS, OUTPUT_OPS, TAG_EFFECTS, TAG_SOURCES
)
from execution_data import ExecutionData
from execution_generator import ExecutionCodeGenerator
from inline_editor import InlineEditorMixin


class ExecutionEditorUI(InlineEditorMixin):
    """Execution 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.executions = []
        self._current_exec_idx = None
        
        # 初始化内联编辑器
        self._init_inline_editor()
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        # 左侧：Execution 列表
        left_frame = ttk.Frame(self.parent, width=180)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_frame, text="Execution 列表", font=("", 11, "bold")).pack(pady=5)
        
        self.exec_listbox = tk.Listbox(left_frame, width=20, height=20, exportselection=False)
        self.exec_listbox.pack(fill=tk.BOTH, expand=True)
        self.exec_listbox.bind('<<ListboxSelect>>', self._on_exec_select)
        self.exec_listbox.bind('<F2>', self._on_rename_exec)
        self.exec_listbox.bind('<Delete>', lambda e: self._delete_exec())
        
        exec_btn_frame = ttk.Frame(left_frame)
        exec_btn_frame.pack(fill=tk.X, pady=5)
        ttk.Button(exec_btn_frame, text="+ 新建", command=self._add_execution).pack(side=tk.LEFT, expand=True)
        ttk.Button(exec_btn_frame, text="- 删除", command=self._delete_execution).pack(side=tk.LEFT, expand=True)
        
        # 中间：编辑区
        middle_frame = ttk.Frame(self.parent)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 基本信息
        info_frame = ttk.LabelFrame(middle_frame, text="基本信息")
        info_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(info_frame, text="名称:").grid(row=0, column=0, sticky='w', padx=5, pady=3)
        self.exec_name_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.exec_name_var, width=30).grid(row=0, column=1, padx=5, pady=3)
        ttk.Label(info_frame, text="(类名: UDJ01{Name}Execution)").grid(row=0, column=2, sticky='w', padx=5)
        
        ttk.Label(info_frame, text="描述:").grid(row=1, column=0, sticky='w', padx=5, pady=3)
        self.exec_desc_var = tk.StringVar()
        ttk.Entry(info_frame, textvariable=self.exec_desc_var, width=50).grid(row=1, column=1, columnspan=2, padx=5, pady=3, sticky='w')
        
        # 捕获属性
        capture_frame = ttk.LabelFrame(middle_frame, text="捕获属性 - 双击编辑")
        capture_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        capture_columns = ('source', 'set', 'attr', 'layer')
        self.capture_tree = ttk.Treeview(capture_frame, columns=capture_columns, show='headings', height=5)
        self.capture_tree.heading('source', text='来源')
        self.capture_tree.heading('set', text='属性集')
        self.capture_tree.heading('attr', text='属性')
        self.capture_tree.heading('layer', text='层级')
        self.capture_tree.column('source', width=70)
        self.capture_tree.column('set', width=100)
        self.capture_tree.column('attr', width=130)
        self.capture_tree.column('layer', width=70)
        self.capture_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.capture_tree.bind('<Double-1>', self._on_capture_double_click)
        
        capture_btn = ttk.Frame(capture_frame)
        capture_btn.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        ttk.Button(capture_btn, text="+", command=self._add_capture, width=3).pack(pady=2)
        ttk.Button(capture_btn, text="-", command=self._delete_capture, width=3).pack(pady=2)
        
        # Tag 条件
        tag_cond_frame = ttk.LabelFrame(middle_frame, text="Tag 条件 (免疫/弱点/加成)")
        tag_cond_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        tag_cond_columns = ('source', 'tag', 'effect', 'value')
        self.tag_cond_tree = ttk.Treeview(tag_cond_frame, columns=tag_cond_columns, show='headings', height=3)
        self.tag_cond_tree.heading('source', text='检查对象')
        self.tag_cond_tree.heading('tag', text='Tag')
        self.tag_cond_tree.heading('effect', text='效果')
        self.tag_cond_tree.heading('value', text='数值')
        self.tag_cond_tree.column('source', width=80)
        self.tag_cond_tree.column('tag', width=180)
        self.tag_cond_tree.column('effect', width=80)
        self.tag_cond_tree.column('value', width=60)
        self.tag_cond_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tag_cond_tree.bind('<Double-1>', self._on_tag_cond_double_click)
        
        tag_cond_btn = ttk.Frame(tag_cond_frame)
        tag_cond_btn.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        ttk.Button(tag_cond_btn, text="+", command=self._add_tag_condition, width=3).pack(pady=2)
        ttk.Button(tag_cond_btn, text="-", command=self._delete_tag_condition, width=3).pack(pady=2)
        
        # 输出属性
        output_frame = ttk.LabelFrame(middle_frame, text="输出属性 (Target)")
        output_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        output_columns = ('set', 'attr', 'op')
        self.output_tree = ttk.Treeview(output_frame, columns=output_columns, show='headings', height=3)
        self.output_tree.heading('set', text='属性集')
        self.output_tree.heading('attr', text='属性')
        self.output_tree.heading('op', text='操作')
        self.output_tree.column('set', width=120)
        self.output_tree.column('attr', width=150)
        self.output_tree.column('op', width=80)
        self.output_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.output_tree.bind('<Double-1>', self._on_output_double_click)
        
        output_btn = ttk.Frame(output_frame)
        output_btn.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        ttk.Button(output_btn, text="+", command=self._add_output, width=3).pack(pady=2)
        ttk.Button(output_btn, text="-", command=self._delete_output, width=3).pack(pady=2)
        
        # 计算逻辑
        formula_frame = ttk.LabelFrame(middle_frame, text="计算逻辑 (C++ 代码)")
        formula_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.formula_text = scrolledtext.ScrolledText(formula_frame, height=5, font=("Consolas", 10))
        self.formula_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 底部按钮
        bottom_frame = ttk.Frame(middle_frame)
        bottom_frame.pack(fill=tk.X, pady=5)
        ttk.Button(bottom_frame, text="保存当前", command=self._save_execution).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="保存配置", command=self.save_config).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text="[生成代码]", command=self.generate_code).pack(side=tk.LEFT, padx=5)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        """从配置文件加载数据"""
        self.executions.clear()
        if EXECUTIONS_CONFIG.exists():
            try:
                with open(EXECUTIONS_CONFIG, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for d in data:
                    self.executions.append(ExecutionData.from_dict(d))
            except Exception as e:
                print(f"加载 Execution 配置失败: {e}")
        self._refresh_exec_list()
    
    def save_config(self):
        """保存配置到文件"""
        self._save_execution_silent()
        try:
            EXECUTIONS_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            data = [exe.to_dict() for exe in self.executions]
            with open(EXECUTIONS_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            self.app.show_status("Execution 配置已保存")
        except Exception as e:
            messagebox.showerror("保存失败", str(e))
    
    def generate_code(self):
        """生成 C++ 代码"""
        self._save_execution_silent()
        if not self.executions:
            messagebox.showwarning("警告", "没有 Execution 可生成！")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        generated = []
        
        try:
            EXECUTIONS_OUTPUT.mkdir(parents=True, exist_ok=True)
            for exe in self.executions:
                if not exe.name:
                    continue
                header, source = ExecutionCodeGenerator.generate(exe, timestamp)
                
                h_path = EXECUTIONS_OUTPUT / f"DJ01{exe.name}Execution.h"
                cpp_path = EXECUTIONS_OUTPUT / f"DJ01{exe.name}Execution.cpp"
                
                with open(h_path, 'w', encoding='utf-8') as f:
                    f.write(header)
                with open(cpp_path, 'w', encoding='utf-8') as f:
                    f.write(source)
                
                generated.append(exe.name)
            
            messagebox.showinfo("生成成功",
                f"Execution 代码已生成！\n\n"
                f"输出目录:\n{EXECUTIONS_OUTPUT}\n\n"
                f"生成: {', '.join(generated)}")
        except Exception as e:
            messagebox.showerror("生成失败", str(e))
    
    # ========== UI 事件 ==========
    
    def _refresh_exec_list(self):
        """刷新 Execution 列表"""
        self.exec_listbox.delete(0, tk.END)
        for exe in self.executions:
            self.exec_listbox.insert(tk.END, exe.name)
    
    def _on_exec_select(self, event):
        """选择 Execution 时加载其数据"""
        if self._current_exec_idx is not None:
            self._save_execution_silent()
        
        selection = self.exec_listbox.curselection()
        if not selection:
            self._current_exec_idx = None
            return
        
        self._current_exec_idx = selection[0]
        exe = self.executions[self._current_exec_idx]
        
        self.exec_name_var.set(exe.name)
        self.exec_desc_var.set(exe.description)
        
        self.capture_tree.delete(*self.capture_tree.get_children())
        for i, cap in enumerate(exe.captures):
            self.capture_tree.insert('', 'end', iid=f"cap_{i}", values=(
                cap.get('source', 'Source'), cap.get('set'), cap.get('attr'), cap.get('layer', 'Base')))
        
        self.output_tree.delete(*self.output_tree.get_children())
        for i, out in enumerate(exe.outputs):
            self.output_tree.insert('', 'end', iid=f"out_{i}", values=(out.get('set'), out.get('attr'), out.get('op', 'Additive')))
        
        self.tag_cond_tree.delete(*self.tag_cond_tree.get_children())
        for i, cond in enumerate(exe.tag_conditions):
            value_display = cond.get('value', 0) if cond.get('effect') != 'Skip' else '-'
            self.tag_cond_tree.insert('', 'end', iid=f"tag_{i}", values=(
                cond.get('source'), cond.get('tag'), cond.get('effect'), value_display))
        
        self.formula_text.delete('1.0', tk.END)
        self.formula_text.insert('1.0', exe.formula)
    
    def _add_execution(self):
        """添加新的 Execution"""
        from tkinter import simpledialog
        name = simpledialog.askstring("新建 Execution", "名称 (如 Damage):")
        if name:
            exe = ExecutionData(name=name, description=f"{name} 计算")
            exe.formula = "float FinalValue = 0.f;"
            self.executions.append(exe)
            self._refresh_exec_list()
    
    def _delete_execution(self):
        """删除选中的 Execution"""
        selection = self.exec_listbox.curselection()
        if not selection:
            return
        if messagebox.askyesno("确认", "确定删除此 Execution?"):
            del self.executions[selection[0]]
            self._current_exec_idx = None
            self._refresh_exec_list()
    
    def _add_capture(self):
        """添加捕获属性"""
        if self._current_exec_idx is None:
            messagebox.showwarning("警告", "请先选择一个 Execution")
            return
        
        attributes = self.app.get_attributes()
        if not attributes:
            messagebox.showwarning("警告", "请先在属性编辑器中添加属性")
            return
        
        first_attr = attributes[0]
        new_capture = {'source': 'Source', 'set': first_attr.set_name, 'attr': first_attr.name, 'layer': 'Total'}
        exe = self.executions[self._current_exec_idx]
        exe.captures.append(new_capture)
        
        import time
        unique_id = f"cap_{int(time.time() * 1000)}"
        self.capture_tree.insert('', 'end', iid=unique_id, values=(
            new_capture['source'], new_capture['set'], new_capture['attr'], new_capture['layer']))
        self.capture_tree.selection_set(unique_id)
        self.capture_tree.focus(unique_id)
    
    def _delete_capture(self):
        """删除捕获属性"""
        selection = self.capture_tree.selection()
        if not selection or self._current_exec_idx is None:
            return
        item = selection[0]
        all_items = self.capture_tree.get_children()
        idx = list(all_items).index(item) if item in all_items else -1
        exe = self.executions[self._current_exec_idx]
        if 0 <= idx < len(exe.captures):
            del exe.captures[idx]
        self.capture_tree.delete(item)
    
    def _add_output(self):
        """添加输出属性"""
        if self._current_exec_idx is None:
            messagebox.showwarning("警告", "请先选择一个 Execution")
            return
        
        attributes = self.app.get_attributes()
        if not attributes:
            messagebox.showwarning("警告", "请先在属性编辑器中添加属性")
            return
        
        first_attr = attributes[0]
        new_output = {'set': first_attr.set_name, 'attr': first_attr.name, 'op': 'Additive'}
        exe = self.executions[self._current_exec_idx]
        exe.outputs.append(new_output)
        
        import time
        unique_id = f"out_{int(time.time() * 1000)}"
        self.output_tree.insert('', 'end', iid=unique_id, values=(
            new_output['set'], new_output['attr'], new_output['op']))
        self.output_tree.selection_set(unique_id)
        self.output_tree.focus(unique_id)
    
    def _delete_output(self):
        """删除输出属性"""
        selection = self.output_tree.selection()
        if not selection or self._current_exec_idx is None:
            return
        item = selection[0]
        all_items = self.output_tree.get_children()
        idx = list(all_items).index(item) if item in all_items else -1
        exe = self.executions[self._current_exec_idx]
        if 0 <= idx < len(exe.outputs):
            del exe.outputs[idx]
        self.output_tree.delete(item)
    
    def _add_tag_condition(self):
        """添加 Tag 条件"""
        if self._current_exec_idx is None:
            messagebox.showwarning("警告", "请先选择一个 Execution")
            return
        
        tags = self.app.get_tags() if hasattr(self.app, 'get_tags') else []
        if not tags:
            messagebox.showwarning("警告", "请先在 Tags 编辑器中添加标签")
            return
        
        first_tag = tags[0].tag if tags else "Tag.Default"
        new_cond = {'source': 'Target', 'tag': first_tag, 'effect': 'Skip', 'value': 0}
        exe = self.executions[self._current_exec_idx]
        exe.tag_conditions.append(new_cond)
        
        import time
        unique_id = f"tag_{int(time.time() * 1000)}"
        self.tag_cond_tree.insert('', 'end', iid=unique_id, values=(
            new_cond['source'], new_cond['tag'], new_cond['effect'], '-'))
        self.tag_cond_tree.selection_set(unique_id)
        self.tag_cond_tree.focus(unique_id)
    
    def _delete_tag_condition(self):
        """删除 Tag 条件"""
        selection = self.tag_cond_tree.selection()
        if not selection or self._current_exec_idx is None:
            return
        item = selection[0]
        all_items = self.tag_cond_tree.get_children()
        idx = list(all_items).index(item) if item in all_items else -1
        exe = self.executions[self._current_exec_idx]
        if 0 <= idx < len(exe.tag_conditions):
            del exe.tag_conditions[idx]
        self.tag_cond_tree.delete(item)
    
    # ========== 内联编辑 ==========
    
    def _on_capture_double_click(self, event):
        """双击捕获表格进行内联编辑"""
        if self._current_exec_idx is None:
            return
        
        cell_info = self._get_cell_info(self.capture_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        col_name = ['source', 'set', 'attr', 'layer'][col_idx]
        
        all_items = self.capture_tree.get_children()
        data_idx = list(all_items).index(item)
        if data_idx >= len(self.executions[self._current_exec_idx].captures):
            return
        
        capture = self.executions[self._current_exec_idx].captures[data_idx]
        x, y, w, h = bbox
        attributes = self.app.get_attributes()
        
        def refresh(tree, item, data):
            tree.item(item, values=(data.get('source', 'Source'), data.get('set'), data.get('attr'), data.get('layer', 'Base')))
            self._restore_exec_selection()
        
        if col_name == 'source':
            self._create_inline_combo(self.capture_tree, item, column, x, y, w, h,
                                       capture, col_name, ['Source', 'Target'], refresh)
        elif col_name == 'set':
            sets = list(OrderedDict.fromkeys(a.set_name for a in attributes))
            self._create_inline_combo_with_sync(
                self.capture_tree, item, column, x, y, w, h, 
                capture, col_name, sets, 'attr',
                lambda s: [a.name for a in attributes if a.set_name == s], refresh)
        elif col_name == 'attr':
            current_set = capture.get('set', '')
            attrs = [a.name for a in attributes if a.set_name == current_set]
            self._create_inline_combo(self.capture_tree, item, column, x, y, w, h,
                                       capture, col_name, attrs, refresh)
        elif col_name == 'layer':
            self._create_inline_combo(self.capture_tree, item, column, x, y, w, h,
                                       capture, col_name, CAPTURE_LAYERS, refresh)
    
    def _on_output_double_click(self, event):
        """双击输出表格进行内联编辑"""
        if self._current_exec_idx is None:
            return
        
        cell_info = self._get_cell_info(self.output_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        col_name = ['set', 'attr', 'op'][col_idx]
        
        all_items = self.output_tree.get_children()
        data_idx = list(all_items).index(item)
        if data_idx >= len(self.executions[self._current_exec_idx].outputs):
            return
        
        output = self.executions[self._current_exec_idx].outputs[data_idx]
        x, y, w, h = bbox
        attributes = self.app.get_attributes()
        
        def refresh(tree, item, data):
            tree.item(item, values=(data.get('set'), data.get('attr'), data.get('op', 'Additive')))
            self._restore_exec_selection()
        
        if col_name == 'set':
            sets = list(OrderedDict.fromkeys(a.set_name for a in attributes))
            self._create_inline_combo_with_sync(
                self.output_tree, item, column, x, y, w, h,
                output, col_name, sets, 'attr',
                lambda s: [a.name for a in attributes if a.set_name == s], refresh)
        elif col_name == 'attr':
            current_set = output.get('set', '')
            attrs = [a.name for a in attributes if a.set_name == current_set]
            self._create_inline_combo(self.output_tree, item, column, x, y, w, h,
                                       output, col_name, attrs, refresh)
        elif col_name == 'op':
            self._create_inline_combo(self.output_tree, item, column, x, y, w, h,
                                       output, col_name, OUTPUT_OPS, refresh)
    
    def _on_tag_cond_double_click(self, event):
        """双击 Tag 条件表格进行内联编辑"""
        if self._current_exec_idx is None:
            return
        
        cell_info = self._get_cell_info(self.tag_cond_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        col_name = ['source', 'tag', 'effect', 'value'][col_idx]
        
        all_items = self.tag_cond_tree.get_children()
        data_idx = list(all_items).index(item)
        if data_idx >= len(self.executions[self._current_exec_idx].tag_conditions):
            return
        
        cond = self.executions[self._current_exec_idx].tag_conditions[data_idx]
        x, y, w, h = bbox
        
        def refresh(tree, item, data):
            value_display = data.get('value', 0) if data.get('effect') != 'Skip' else '-'
            tree.item(item, values=(data.get('source'), data.get('tag'), data.get('effect'), value_display))
            self._restore_exec_selection()
        
        if col_name == 'source':
            self._create_inline_combo(self.tag_cond_tree, item, column, x, y, w, h,
                                       cond, col_name, TAG_SOURCES, refresh)
        elif col_name == 'tag':
            tags = self.app.get_tags() if hasattr(self.app, 'get_tags') else []
            tag_values = [t.tag for t in tags]
            self._create_inline_combo(self.tag_cond_tree, item, column, x, y, w, h,
                                       cond, col_name, tag_values, refresh)
        elif col_name == 'effect':
            self._create_inline_combo(self.tag_cond_tree, item, column, x, y, w, h,
                                       cond, col_name, TAG_EFFECTS, refresh)
        elif col_name == 'value':
            self._create_inline_entry(self.tag_cond_tree, item, column, x, y, w, h,
                                       cond, col_name, refresh, value_type=float)
    
    def _restore_exec_selection(self):
        """恢复 Execution 列表的选中状态"""
        if self._current_exec_idx is not None and 0 <= self._current_exec_idx < len(self.executions):
            self.exec_listbox.selection_clear(0, tk.END)
            self.exec_listbox.selection_set(self._current_exec_idx)
            self.exec_listbox.activate(self._current_exec_idx)
    
    def _save_execution_silent(self):
        """静默保存当前 Execution"""
        if self._current_exec_idx is None or self._current_exec_idx >= len(self.executions):
            return
        exe = self.executions[self._current_exec_idx]
        exe.name = self.exec_name_var.get()
        exe.description = self.exec_desc_var.get()
        exe.formula = self.formula_text.get('1.0', tk.END).strip()
    
    def _save_execution(self):
        """保存当前 Execution 并刷新列表"""
        self._save_execution_silent()
        self._refresh_exec_list()
    
    def _on_rename_exec(self, event):
        """F2 内联重命名 Execution"""
        selection = self.exec_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        if idx >= len(self.executions):
            return
        
        exe = self.executions[idx]
        bbox = self.exec_listbox.bbox(idx)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        entry = ttk.Entry(self.exec_listbox, width=15)
        entry.place(x=x, y=y, width=self.exec_listbox.winfo_width()-4, height=height)
        entry.insert(0, exe.name)
        entry.select_range(0, tk.END)
        entry.focus()
        
        def finish_edit(save=True):
            if save:
                new_name = entry.get().strip()
                if new_name and new_name != exe.name:
                    exe.name = new_name
                    self._refresh_exec_list()
                    self.exec_listbox.selection_clear(0, tk.END)
                    self.exec_listbox.selection_set(idx)
                    self.exec_name_var.set(new_name)
                    self.app.show_status(f"已重命名为 {new_name}")
            entry.destroy()
        
        entry.bind('<Return>', lambda e: finish_edit(True))
        entry.bind('<Escape>', lambda e: finish_edit(False))
        entry.bind('<FocusOut>', lambda e: finish_edit(True))
    
    def _delete_exec(self):
        """Delete 键删除"""
        self._delete_execution()
    
    def save_current_edit(self):
        """保存当前正在编辑的 Execution（供 Ctrl+S 调用）"""
        self._save_execution_silent()
        self._refresh_exec_list()
        self.save_config()
    def _refresh_tag_item(self, tree, item, data):
        """刷新单行 Tag 数据"""
        tree.item(item, values=(
            data.get('source', 'Target'),
            data.get('tag', ''),
            data.get('effect', 'Skip'),
            data.get('value', 0)
        ))
        self._save_executions()
        self._update_preview()
    
    # ==================== 输出编辑 ====================
    
    def _refresh_output_tree(self):
        """刷新输出列表"""
        self.output_tree.delete(*self.output_tree.get_children())
        if not self.current_execution:
            return
        for i, out in enumerate(self.current_execution.outputs):
            self.output_tree.insert('', tk.END, iid=f'out_{i}', values=(
                out.get('set', ''),
                out.get('attr', ''),
                out.get('op', 'Additive')
            ))
    
    def _add_output(self):
        """添加输出"""
        if not self.current_execution:
            return
        
        attr_sets = self.get_attribute_sets()
        first_set = attr_sets[0] if attr_sets else ''
        first_attrs = self._get_attrs_for_set(first_set)
        first_attr = first_attrs[0] if first_attrs else ''
        
        out = {'set': first_set, 'attr': first_attr, 'op': 'Additive'}
        self.current_execution.outputs.append(out)
        self._refresh_output_tree()
        self._save_executions()
    
    def _delete_output(self):
        """删除输出"""
        if not self.current_execution:
            return
        selection = self.output_tree.selection()
        if selection:
            idx = int(selection[0].split('_')[1])
            del self.current_execution.outputs[idx]
            self._refresh_output_tree()
            self._save_executions()
    
    def _on_output_double_click(self, event):
        """双击编辑输出"""
        cell_info = self._get_cell_info(self.output_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        idx = int(item.split('_')[1])
        out = self.current_execution.outputs[idx]
        
        cols = ['set', 'attr', 'op']
        key = cols[col_idx]
        
        if key == 'set':
            self._create_inline_combo_with_sync(
                self.output_tree, item, column,
                bbox[0], bbox[1], bbox[2], bbox[3],
                out, 'set', self.get_attribute_sets(),
                'attr', self._get_attrs_for_set,
                self._refresh_output_item
            )
        elif key == 'attr':
            attrs = self._get_attrs_for_set(out.get('set', ''))
            self._create_inline_combo(
                self.output_tree, item, column,
                bbox[0], bbox[1], bbox[2], bbox[3],
                out, 'attr', attrs,
                self._refresh_output_item
            )
        elif key == 'op':
            self._create_inline_combo(
                self.output_tree, item, column,
                bbox[0], bbox[1], bbox[2], bbox[3],
                out, 'op', ['Additive', 'Multiplicitive', 'Override'],
                self._refresh_output_item
            )
        
        self._save_executions()
    
    def _refresh_output_item(self, tree, item, data):
        """刷新单行输出数据"""
        tree.item(item, values=(
            data.get('set', ''),
            data.get('attr', ''),
            data.get('op', 'Additive')
        ))
        self._save_executions()
        self._update_preview()
    
    # ==================== 辅助方法 ====================
    
    def _get_attrs_for_set(self, set_name):
        """获取指定属性集的属性列表"""
        # 这个需要从外部获取，简化处理
        # 实际应该从 attribute_module 或 CSV 读取
        try:
            csv_path = os.path.join(get_project_root(), "Tools", "AttributeGenerator", "AttributeDefinitions.csv")
            if not os.path.exists(csv_path):
                return []
            
            attrs = []
            with open(csv_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line in lines[1:]:  # 跳过表头
                parts = line.strip().split(',')
                if len(parts) >= 3 and parts[0] == set_name:
                    attrs.append(parts[1])
            
            return attrs
        except:
            return []
    
    def _get_available_tags(self):
        """获取可用的 Tag 列表"""
        try:
            tag_path = os.path.join(get_project_root(), "Tools", "AttributeGenerator", "tags.json")
            if not os.path.exists(tag_path):
                return []
            
            with open(tag_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            tags = []
            for cat in data.get('Categories', []):
                for tag in cat.get('Tags', []):
                    tags.append(tag.get('Name', ''))
            return tags
        except:
            return []
    
    # ==================== 代码生成 ====================
    
    def generate_code(self):
        """生成所有 Execution 的代码"""
        if not self.executions:
            messagebox.showinfo("提示", "没有 Execution 需要生成")
            return
        
        project_root = get_project_root()
        public_dir = os.path.join(project_root, EXECUTIONS_PUBLIC_PATH)
        private_dir = os.path.join(project_root, EXECUTIONS_PRIVATE_PATH)
        
        os.makedirs(public_dir, exist_ok=True)
        os.makedirs(private_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        for exe in self.executions:
            header, source = ExecutionCodeGenerator.generate(exe, timestamp)
            class_name = f"UDJ01{exe.name}Execution"
            
            header_path = os.path.join(public_dir, f"{class_name}.h")
            source_path = os.path.join(private_dir, f"{class_name}.cpp")
            
            with open(header_path, 'w', encoding='utf-8') as f:
                f.write(header)
            with open(source_path, 'w', encoding='utf-8') as f:
                f.write(source)
        
        messagebox.showinfo("完成", f"已生成 {len(self.executions)} 个 Execution 文件")
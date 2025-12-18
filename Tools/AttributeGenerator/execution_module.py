#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 GAS 代码生成器 - Execution 模块
包含：数据模型、代码生成器、UI 组件
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
from collections import OrderedDict

from config import (
    MODULE_NAME, EXECUTIONS_CONFIG, EXECUTIONS_OUTPUT,
    CAPTURE_LAYERS, OUTPUT_OPS
)


# ============================================================
# 数据模型
# ============================================================

class ExecutionData:
    """Execution 数据模型"""
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description
        self.captures = []  # [{"set": "StatSet", "attr": "AttackPower", "layer": "Total"}]
        self.outputs = []   # [{"set": "ResourceSet", "attr": "Health", "op": "Additive"}]
        self.formula = ""

    def to_dict(self):
        return {
            'Name': self.name,
            'Description': self.description,
            'Captures': self.captures,
            'Outputs': self.outputs,
            'Formula': self.formula
        }

    @staticmethod
    def from_dict(d):
        exe = ExecutionData(d.get('Name', ''), d.get('Description', ''))
        exe.captures = d.get('Captures', [])
        exe.outputs = d.get('Outputs', [])
        exe.formula = d.get('Formula', '')
        return exe


# ============================================================
# 代码生成器
# ============================================================

class ExecutionCodeGenerator:
    """Execution 代码生成器"""
    
    @staticmethod
    def generate(execution: ExecutionData, timestamp: str) -> tuple:
        class_name = f"UDJ01{execution.name}Execution"
        header = ExecutionCodeGenerator._generate_header(execution, class_name, timestamp)
        source = ExecutionCodeGenerator._generate_source(execution, class_name, timestamp)
        return header, source
    
    @staticmethod
    def _generate_header(exe: ExecutionData, class_name: str, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append(f"// {class_name}")
        lines.append("// 自动生成，可根据需要修改计算逻辑")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "GameplayEffectExecutionCalculation.h"')
        lines.append(f'#include "{class_name}.generated.h"')
        lines.append("")
        lines.append(f"/** {exe.description} */")
        lines.append("UCLASS()")
        lines.append(f"class {MODULE_NAME}_API {class_name} : public UGameplayEffectExecutionCalculation")
        lines.append("{")
        lines.append("    GENERATED_BODY()")
        lines.append("")
        lines.append("public:")
        lines.append(f"    {class_name}();")
        lines.append("")
        lines.append("    virtual void Execute_Implementation(")
        lines.append("        const FGameplayEffectCustomExecutionParameters& ExecutionParams,")
        lines.append("        FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;")
        lines.append("};")
        lines.append("")
        return "\n".join(lines)
    
    @staticmethod
    def _generate_source(exe: ExecutionData, class_name: str, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append(f"// {class_name}")
        lines.append("// 自动生成，可根据需要修改计算逻辑")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append(f'#include "{class_name}.h"')
        lines.append('#include "DJ01GeneratedAttributes.h"')
        lines.append('#include "AbilitySystemComponent.h"')
        lines.append("")
        lines.append(f"#include UE_INLINE_GENERATED_CPP_BY_NAME({class_name})")
        lines.append("")
        
        # 分类捕获
        base_captures = []
        total_captures = []
        for cap in exe.captures:
            if cap.get('layer', 'Base') == 'Total':
                total_captures.append(cap)
            else:
                base_captures.append(cap)
        
        # 捕获结构体
        lines.append("namespace")
        lines.append("{")
        lines.append("    struct FCapturedAttributes")
        lines.append("    {")
        
        for cap in total_captures:
            attr = cap['attr']
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF(Base{attr});")
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF(Flat{attr});")
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF(Percent{attr});")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF({prop});")
        
        lines.append("")
        lines.append("        FCapturedAttributes()")
        lines.append("        {")
        
        for cap in total_captures:
            attr, attr_class = cap['attr'], f"UDJ01{cap['set']}"
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, Base{attr}, Source, false);")
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, Flat{attr}, Source, false);")
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, Percent{attr}, Source, false);")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr, attr_class = cap['attr'], f"UDJ01{cap['set']}"
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, {prop}, Source, false);")
        
        lines.append("        }")
        lines.append("    };")
        lines.append("")
        lines.append("    static const FCapturedAttributes& GetCapturedAttributes()")
        lines.append("    {")
        lines.append("        static FCapturedAttributes Attributes;")
        lines.append("        return Attributes;")
        lines.append("    }")
        lines.append("}")
        lines.append("")
        
        # 构造函数
        lines.append(f"{class_name}::{class_name}()")
        lines.append("{")
        lines.append("    const FCapturedAttributes& Attrs = GetCapturedAttributes();")
        
        for cap in total_captures:
            attr = cap['attr']
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.Base{attr}Def);")
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.Flat{attr}Def);")
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.Percent{attr}Def);")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.{prop}Def);")
        
        lines.append("}")
        lines.append("")
        
        # Execute
        lines.append(f"void {class_name}::Execute_Implementation(")
        lines.append("    const FGameplayEffectCustomExecutionParameters& ExecutionParams,")
        lines.append("    FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const")
        lines.append("{")
        lines.append("    const FCapturedAttributes& Attrs = GetCapturedAttributes();")
        lines.append("")
        lines.append("    const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();")
        lines.append("    FAggregatorEvaluateParameters EvalParams;")
        lines.append("    EvalParams.SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();")
        lines.append("    EvalParams.TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();")
        lines.append("")
        lines.append("    // ========== 获取属性值 ==========")
        
        for cap in total_captures:
            attr = cap['attr']
            lines.append(f"    float Base{attr} = 0.f, Flat{attr} = 0.f, Percent{attr} = 0.f;")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Base{attr}Def, EvalParams, Base{attr});")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Flat{attr}Def, EvalParams, Flat{attr});")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Percent{attr}Def, EvalParams, Percent{attr});")
            lines.append(f"    const float {attr}Value = (Base{attr} + Flat{attr}) * (1.f + Percent{attr});")
            lines.append("")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"    float {attr}Value = 0.f;")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.{prop}Def, EvalParams, {attr}Value);")
        
        lines.append("")
        lines.append("    // ========== 计算逻辑 ==========")
        
        if exe.formula:
            for line in exe.formula.split('\n'):
                lines.append(f"    {line}")
        else:
            lines.append("    float FinalValue = 0.f;")
        
        lines.append("")
        lines.append("    // ========== 输出结果 ==========")
        for out in exe.outputs:
            attr_class = f"UDJ01{out['set']}"
            op = out.get('op', 'Additive')
            lines.append(f"    if (FinalValue != 0.f)")
            lines.append(f"    {{")
            lines.append(f"        OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(")
            lines.append(f"            {attr_class}::Get{out['attr']}Attribute(), EGameplayModOp::{op}, FinalValue));")
            lines.append(f"    }}")
        lines.append("}")
        lines.append("")
        
        return "\n".join(lines)


# ============================================================
# 对话框
# ============================================================

class CaptureDialog:
    """捕获属性选择对话框"""
    
    def __init__(self, parent, attributes):
        self.result = None
        self.attributes = attributes
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("添加捕获属性")
        self.dialog.geometry("350x180")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        ttk.Label(self.dialog, text="属性集:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.set_var = tk.StringVar()
        sets = list(OrderedDict.fromkeys(a.set_name for a in attributes))
        self.set_combo = ttk.Combobox(self.dialog, textvariable=self.set_var, values=sets, width=25)
        self.set_combo.grid(row=0, column=1, padx=10, pady=5)
        self.set_combo.bind('<<ComboboxSelected>>', self._on_set_change)
        
        ttk.Label(self.dialog, text="属性:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.attr_var = tk.StringVar()
        self.attr_combo = ttk.Combobox(self.dialog, textvariable=self.attr_var, width=25)
        self.attr_combo.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.dialog, text="层级:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.layer_var = tk.StringVar(value="Total")
        ttk.Combobox(self.dialog, textvariable=self.layer_var, values=CAPTURE_LAYERS, width=25).grid(row=2, column=1, padx=10, pady=5)
        
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)
        ttk.Button(btn_frame, text="确定", command=self._ok).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self._cancel).pack(side=tk.LEFT, padx=10)
        
        self.dialog.wait_window()
    
    def _on_set_change(self, event):
        set_name = self.set_var.get()
        attrs = [a.name for a in self.attributes if a.set_name == set_name]
        self.attr_combo['values'] = attrs
        if attrs:
            self.attr_var.set(attrs[0])
    
    def _ok(self):
        if self.set_var.get() and self.attr_var.get():
            self.result = {'set': self.set_var.get(), 'attr': self.attr_var.get(), 'layer': self.layer_var.get()}
        self.dialog.destroy()
    
    def _cancel(self):
        self.dialog.destroy()


class OutputDialog:
    """输出属性选择对话框"""
    
    def __init__(self, parent, attributes):
        self.result = None
        self.attributes = attributes
        
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("添加输出属性")
        self.dialog.geometry("350x180")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        ttk.Label(self.dialog, text="属性集:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.set_var = tk.StringVar()
        sets = list(OrderedDict.fromkeys(a.set_name for a in attributes))
        self.set_combo = ttk.Combobox(self.dialog, textvariable=self.set_var, values=sets, width=25)
        self.set_combo.grid(row=0, column=1, padx=10, pady=5)
        self.set_combo.bind('<<ComboboxSelected>>', self._on_set_change)
        
        ttk.Label(self.dialog, text="属性:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.attr_var = tk.StringVar()
        self.attr_combo = ttk.Combobox(self.dialog, textvariable=self.attr_var, width=25)
        self.attr_combo.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self.dialog, text="操作:").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.op_var = tk.StringVar(value="Additive")
        ttk.Combobox(self.dialog, textvariable=self.op_var, values=OUTPUT_OPS, width=25).grid(row=2, column=1, padx=10, pady=5)
        
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=15)
        ttk.Button(btn_frame, text="确定", command=self._ok).pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="取消", command=self._cancel).pack(side=tk.LEFT, padx=10)
        
        self.dialog.wait_window()
    
    def _on_set_change(self, event):
        set_name = self.set_var.get()
        attrs = [a.name for a in self.attributes if a.set_name == set_name]
        self.attr_combo['values'] = attrs
        if attrs:
            self.attr_var.set(attrs[0])
    
    def _ok(self):
        if self.set_var.get() and self.attr_var.get():
            self.result = {'set': self.set_var.get(), 'attr': self.attr_var.get(), 'op': self.op_var.get()}
        self.dialog.destroy()
    
    def _cancel(self):
        self.dialog.destroy()


# ============================================================
# UI 组件
# ============================================================

class ExecutionEditorUI:
    """Execution 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.executions = []
        self._current_exec_idx = None
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        # 左侧：Execution 列表
        left_frame = ttk.Frame(self.parent, width=180)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_frame, text="Execution 列表", font=("", 11, "bold")).pack(pady=5)
        
        self.exec_listbox = tk.Listbox(left_frame, width=20, height=20)
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
        capture_frame = ttk.LabelFrame(middle_frame, text="捕获属性 (Source)")
        capture_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        capture_columns = ('set', 'attr', 'layer')
        self.capture_tree = ttk.Treeview(capture_frame, columns=capture_columns, show='headings', height=5)
        self.capture_tree.heading('set', text='属性集')
        self.capture_tree.heading('attr', text='属性')
        self.capture_tree.heading('layer', text='层级')
        self.capture_tree.column('set', width=120)
        self.capture_tree.column('attr', width=150)
        self.capture_tree.column('layer', width=80)
        self.capture_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        capture_btn = ttk.Frame(capture_frame)
        capture_btn.pack(side=tk.RIGHT, fill=tk.Y, padx=5)
        ttk.Button(capture_btn, text="+", command=self._add_capture, width=3).pack(pady=2)
        ttk.Button(capture_btn, text="-", command=self._delete_capture, width=3).pack(pady=2)
        
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
        self.exec_listbox.delete(0, tk.END)
        for exe in self.executions:
            self.exec_listbox.insert(tk.END, exe.name)
    
    def _on_exec_select(self, event):
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
            self.capture_tree.insert('', 'end', iid=str(i), values=(cap.get('set'), cap.get('attr'), cap.get('layer', 'Base')))
        
        self.output_tree.delete(*self.output_tree.get_children())
        for i, out in enumerate(exe.outputs):
            self.output_tree.insert('', 'end', iid=str(i), values=(out.get('set'), out.get('attr'), out.get('op', 'Additive')))
        
        self.formula_text.delete('1.0', tk.END)
        self.formula_text.insert('1.0', exe.formula)
    
    def _add_execution(self):
        from tkinter import simpledialog
        name = simpledialog.askstring("新建 Execution", "名称 (如 Damage):")
        if name:
            exe = ExecutionData(name=name, description=f"{name} 计算")
            exe.formula = "float FinalValue = 0.f;"
            self.executions.append(exe)
            self._refresh_exec_list()
    
    def _delete_execution(self):
        selection = self.exec_listbox.curselection()
        if not selection:
            return
        if messagebox.askyesno("确认", "确定删除此 Execution?"):
            del self.executions[selection[0]]
            self._current_exec_idx = None
            self._refresh_exec_list()
    
    def _add_capture(self):
        if self._current_exec_idx is None:
            messagebox.showwarning("警告", "请先选择一个 Execution")
            return
        
        # 从属性模块获取属性列表
        attributes = self.app.get_attributes()
        dialog = CaptureDialog(self.parent, attributes)
        if dialog.result:
            exe = self.executions[self._current_exec_idx]
            exe.captures.append(dialog.result)
            idx = len(exe.captures) - 1
            self.capture_tree.insert('', 'end', iid=str(idx), values=(
                dialog.result['set'], dialog.result['attr'], dialog.result['layer']))
    
    def _delete_capture(self):
        selection = self.capture_tree.selection()
        if not selection or self._current_exec_idx is None:
            return
        idx = int(selection[0])
        exe = self.executions[self._current_exec_idx]
        if idx < len(exe.captures):
            del exe.captures[idx]
        self.capture_tree.delete(selection[0])
    
    def _add_output(self):
        if self._current_exec_idx is None:
            messagebox.showwarning("警告", "请先选择一个 Execution")
            return
        
        attributes = self.app.get_attributes()
        dialog = OutputDialog(self.parent, attributes)
        if dialog.result:
            exe = self.executions[self._current_exec_idx]
            exe.outputs.append(dialog.result)
            idx = len(exe.outputs) - 1
            self.output_tree.insert('', 'end', iid=str(idx), values=(
                dialog.result['set'], dialog.result['attr'], dialog.result['op']))
    
    def _delete_output(self):
        selection = self.output_tree.selection()
        if not selection or self._current_exec_idx is None:
            return
        idx = int(selection[0])
        exe = self.executions[self._current_exec_idx]
        if idx < len(exe.outputs):
            del exe.outputs[idx]
        self.output_tree.delete(selection[0])
    
    def _save_execution_silent(self):
        if self._current_exec_idx is None or self._current_exec_idx >= len(self.executions):
            return
        exe = self.executions[self._current_exec_idx]
        exe.name = self.exec_name_var.get()
        exe.description = self.exec_desc_var.get()
        exe.formula = self.formula_text.get('1.0', tk.END).strip()
    
    def _save_execution(self):
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
        
        # 获取选中项的位置
        bbox = self.exec_listbox.bbox(idx)
        if not bbox:
            return
        
        x, y, width, height = bbox
        
        # 创建内联编辑框
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
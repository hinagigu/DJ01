#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MMC 编辑器 UI
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import MMC_CONFIG, MMC_HEADER, MMC_SOURCE, CAPTURE_LAYERS
from ui_base import BaseEditorUI, GroupListWidget, BottomButtonBar, InlineEditorMixin
from mmc.data import MMCData
from mmc.generator import MMCCodeGenerator


class MMCEditorUI(BaseEditorUI, InlineEditorMixin):
    """MMC 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.mmcs = []
        self.current_mmc = None
        
        super().__init__(parent, app)
        self._init_inline_editor()
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        """创建 UI"""
        main_paned = ttk.PanedWindow(self.parent, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左侧：MMC 列表
        left_frame = ttk.LabelFrame(main_paned, text="MMC 列表", width=200)
        main_paned.add(left_frame, weight=1)
        
        self.mmc_list = GroupListWidget(
            left_frame,
            title="MMC",
            on_select=self._on_mmc_select,
            on_add=self._on_add_mmc,
            on_delete=self._on_delete_mmc,
            show_count=False
        )
        self.mmc_list.pack(fill=tk.BOTH, expand=True)
        
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
        
        # 捕获属性
        cap_frame = ttk.LabelFrame(parent, text="捕获属性")
        cap_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        cols = ("source", "set", "attr", "layer")
        self.capture_tree = ttk.Treeview(cap_frame, columns=cols, show='headings', height=4)
        self.capture_tree.heading("source", text="来源")
        self.capture_tree.heading("set", text="属性集")
        self.capture_tree.heading("attr", text="属性")
        self.capture_tree.heading("layer", text="层级")
        self.capture_tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        # 绑定 Delete 键和右键菜单
        self._bind_tree_delete_key(self.capture_tree)
        self.bind_context_menu(self.capture_tree, on_delete=lambda w, item: self._delete_capture_by_item(item))
        
        cap_btn = ttk.Frame(cap_frame)
        cap_btn.pack(side=tk.RIGHT, padx=5)
        ttk.Button(cap_btn, text="➕", width=3, command=self._add_capture).pack(pady=2)
        
        # SetByCaller
        sbc_frame = ttk.LabelFrame(parent, text="SetByCaller")
        sbc_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        cols2 = ("tag", "default", "description")
        self.sbc_tree = ttk.Treeview(sbc_frame, columns=cols2, show='headings', height=3)
        self.sbc_tree.heading("tag", text="Tag")
        self.sbc_tree.heading("default", text="默认值")
        self.sbc_tree.heading("description", text="描述")
        self.sbc_tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        # 绑定 Delete 键和右键菜单
        self._bind_tree_delete_key(self.sbc_tree)
        self.bind_context_menu(self.sbc_tree, on_delete=lambda w, item: self._delete_sbc_by_item(item))
        
        sbc_btn = ttk.Frame(sbc_frame)
        sbc_btn.pack(side=tk.RIGHT, padx=5)
        ttk.Button(sbc_btn, text="➕", width=3, command=self._add_sbc).pack(pady=2)
        
        # 公式
        formula_frame = ttk.LabelFrame(parent, text="计算公式 (返回 float)")
        formula_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        hint = "可用变量: 属性名Value (如 SlowResistance_TargetValue), SetByCaller 的 Tag (如 Data_SlowPercent)"
        ttk.Label(formula_frame, text=hint, foreground="gray").pack(anchor=tk.W, padx=5)
        
        self.formula_text = tk.Text(formula_frame, height=6, font=("Consolas", 10))
        self.formula_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        self.mmcs = []
        try:
            if MMC_CONFIG.exists():
                with open(MMC_CONFIG, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data.get('MMCs', []):
                        self.mmcs.append(MMCData.from_dict(item))
        except Exception as e:
            messagebox.showerror("错误", f"加载配置失败: {e}")
        
        self._refresh_mmc_list()
    
    def save_config(self):
        try:
            MMC_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            data = {'MMCs': [m.to_dict() for m in self.mmcs]}
            with open(MMC_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {e}")
            return False
    
    def save_current_edit(self):
        self._save_current_to_data()
        if self.save_config():
            self.app.show_status("MMC 配置已保存")
    
    def _save_current_to_data(self):
        if not self.current_mmc:
            return
        
        self.current_mmc.description = self.desc_var.get()
        self.current_mmc.formula = self.formula_text.get('1.0', tk.END).strip()
        
        self.current_mmc.captures = []
        for item in self.capture_tree.get_children():
            values = self.capture_tree.item(item, 'values')
            self.current_mmc.captures.append({
                'source': values[0], 'set': values[1], 'attr': values[2], 'layer': values[3]
            })
        
        self.current_mmc.set_by_callers = []
        for item in self.sbc_tree.get_children():
            values = self.sbc_tree.item(item, 'values')
            self.current_mmc.set_by_callers.append({
                'tag': values[0], 'default': float(values[1]) if values[1] else 0, 'description': values[2]
            })
    
    def _refresh_mmc_list(self):
        names = [m.name for m in self.mmcs if m.name]
        self.mmc_list.refresh(names)
    
    def _on_mmc_select(self, idx, name):
        if self.current_mmc:
            self._save_current_to_data()
        
        self.current_mmc = None
        for m in self.mmcs:
            if m.name == name:
                self.current_mmc = m
                break
        
        self._display_mmc(self.current_mmc)
    
    def _display_mmc(self, mmc):
        self.capture_tree.delete(*self.capture_tree.get_children())
        self.sbc_tree.delete(*self.sbc_tree.get_children())
        self.formula_text.delete('1.0', tk.END)
        self.desc_var.set('')
        
        if not mmc:
            return
        
        self.desc_var.set(mmc.description)
        
        for cap in mmc.captures:
            self.capture_tree.insert('', tk.END, values=(
                cap.get('source', 'Target'), cap.get('set', ''),
                cap.get('attr', ''), cap.get('layer', 'Total')
            ))
        
        for sbc in mmc.set_by_callers:
            self.sbc_tree.insert('', tk.END, values=(
                sbc.get('tag', ''), sbc.get('default', 0), sbc.get('description', '')
            ))
        
        self.formula_text.insert('1.0', mmc.formula)
    
    def _on_add_mmc(self):
        name = f"NewMMC{len(self.mmcs) + 1}"
        self.mmcs.append(MMCData(name, "新的 MMC"))
        self._refresh_mmc_list()
        self.mmc_list.select_item(name)
    
    def _on_delete_mmc(self, idx, name):
        if messagebox.askyesno("确认", f"确定删除 '{name}'?"):
            self.mmcs = [m for m in self.mmcs if m.name != name]
            self.current_mmc = None
            self._refresh_mmc_list()
            self._display_mmc(None)
    
    def _add_capture(self):
        attrs = self.app.get_attributes()
        if not attrs:
            messagebox.showwarning("提示", "请先定义属性")
            return
        
        sets = list(set(a.set_name for a in attrs))
        if sets:
            attr_names = [a.name for a in attrs if a.set_name == sets[0]]
            self.capture_tree.insert('', tk.END, values=(
                'Target', sets[0], attr_names[0] if attr_names else '', 'Total'
            ))
    
    def _delete_capture(self):
        """删除选中的捕获属性"""
        self._handle_tree_delete(self.capture_tree)
    
    def _delete_capture_by_item(self, item: str):
        """通过 item id 删除捕获属性（右键菜单调用）"""
        if item:
            self.capture_tree.delete(item)
    
    def _add_sbc(self):
        self.sbc_tree.insert('', tk.END, values=('Data.Value', '0', ''))
    
    def _delete_sbc(self):
        """删除选中的 SetByCaller"""
        self._handle_tree_delete(self.sbc_tree)
    
    def _delete_sbc_by_item(self, item: str):
        """通过 item id 删除 SetByCaller（右键菜单调用）"""
        if item:
            self.sbc_tree.delete(item)
    
    def generate_code(self):
        self._save_current_to_data()
        
        valid_mmcs = [m for m in self.mmcs if m.name]
        if not valid_mmcs:
            messagebox.showwarning("提示", "没有可生成的 MMC")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header, source = MMCCodeGenerator.generate_all(valid_mmcs, timestamp)
        
        try:
            MMC_HEADER.parent.mkdir(parents=True, exist_ok=True)
            MMC_SOURCE.parent.mkdir(parents=True, exist_ok=True)
            
            with open(MMC_HEADER, 'w', encoding='utf-8') as f:
                f.write(header)
            with open(MMC_SOURCE, 'w', encoding='utf-8') as f:
                f.write(source)
            
            self.save_config()
            messagebox.showinfo("成功", f"已生成 {len(valid_mmcs)} 个 MMC")
        except Exception as e:
            messagebox.showerror("错误", f"生成失败: {e}")
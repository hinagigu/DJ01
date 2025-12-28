#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
属性编辑器 UI
"""

import csv
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from collections import OrderedDict

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import (
    ATTRIBUTES_CONFIG, ATTRIBUTES_BEHAVIORS, ATTRIBUTES_HEADER, ATTRIBUTES_SOURCE,
    ATTRIBUTE_TYPES, ATTRIBUTE_CATEGORIES, ATTRIBUTES_CSV_FIELDS
)
from ui_base import BaseEditorUI, GroupListWidget, BottomButtonBar, InlineEditorMixin
from attribute.data import AttributeData, ResourceConfig
from attribute.generator import AttributeCodeGenerator


class AttributeEditorUI(BaseEditorUI, InlineEditorMixin):
    """属性编辑器 UI"""
    
    def __init__(self, parent, app):
        self.attributes = []
        self._current_set = None
        self._last_selected_idx = None
        
        super().__init__(parent, app)
        self._init_inline_editor()
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        """创建三栏布局"""
        # 左侧：属性集列表
        self.set_widget = GroupListWidget(
            self.parent,
            title="属性集",
            on_select=self._on_set_select,
            on_add=self._add_set,
            on_delete=self._on_delete_set,
            show_count=True
        )
        self.set_widget.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        self.set_widget.listbox.bind('<F2>', self._on_rename_set)
        
        # 中间：属性表格
        middle_frame = ttk.Frame(self.parent)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        ttk.Label(middle_frame, text="属性列表", font=("", 12, "bold")).pack(pady=5)
        
        columns = ('name', 'type', 'category', 'base', 'description', 'delete')
        self.attr_tree = ttk.Treeview(middle_frame, columns=columns, show='headings', height=15)
        self.attr_tree.heading('name', text='属性名')
        self.attr_tree.heading('type', text='类型')
        self.attr_tree.heading('category', text='分类')
        self.attr_tree.heading('base', text='默认值')
        self.attr_tree.heading('description', text='描述')
        self.attr_tree.heading('delete', text='')
        
        self.attr_tree.column('name', width=120)
        self.attr_tree.column('type', width=80)
        self.attr_tree.column('category', width=80)
        self.attr_tree.column('base', width=80)
        self.attr_tree.column('description', width=180)
        self.attr_tree.column('delete', width=40, anchor='center')
        
        self.attr_tree.pack(fill=tk.BOTH, expand=True)
        self.attr_tree.bind('<<TreeviewSelect>>', self._on_attr_select)
        self.attr_tree.bind('<F2>', self._on_rename_attr)
        # 绑定 Delete/BackSpace 删除（自动选中上/下行）
        self._bind_tree_delete_key(self.attr_tree, on_after_delete=self._on_attr_deleted)
        
        # 设置单击即可编辑功能（不包括删除列）
        self._setup_single_click_editing(
            self.attr_tree,
            column_handlers={
                0: {'type': 'entry', 'key': 'name', 'value_type': str},          # 属性名
                1: {'type': 'combo', 'key': 'type', 'values': ATTRIBUTE_TYPES},   # 类型
                2: {'type': 'combo', 'key': 'category', 'values': ATTRIBUTE_CATEGORIES},  # 分类
                3: {'type': 'entry', 'key': 'default_base', 'value_type': float}, # 默认值
                4: {'type': 'entry', 'key': 'description', 'value_type': str},    # 描述
                # 5 是删除列，不处理编辑
            },
            refresh_callback=self._on_inline_edit_refresh
        )
        
        # 绑定删除列的点击事件
        self.attr_tree.bind('<ButtonRelease-1>', self._on_tree_click)
        
        # 右键菜单
        self.bind_context_menu(
            self.attr_tree,
            on_delete=lambda w, item: self._delete_attr_by_item(item),
            on_rename=lambda w, item: self._rename_attr_by_item(item)
        )
        
        # 底部按钮
        self.button_bar = BottomButtonBar(middle_frame, buttons=[
            ("+ 添加属性", self._add_attribute, None),
        ])
        self.button_bar.add_button("[生成代码]", self.generate_code, side=tk.RIGHT)
        self.button_bar.add_button("重新加载", self.load_data, side=tk.RIGHT)
        self.button_bar.add_button("保存配置", self.save_config, side=tk.RIGHT)
        self.button_bar.pack(fill=tk.X, pady=5)
        
        # 右侧：编辑面板
        self._create_edit_panel()
    
    def _create_edit_panel(self):
        """创建右侧编辑面板 - 使用 Notebook 选项卡"""
        right_frame = ttk.LabelFrame(self.parent, text="编辑属性", width=350)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        right_frame.pack_propagate(False)
        
        # 创建 Notebook (选项卡容器)
        self.notebook = ttk.Notebook(right_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 选项卡1: 基础信息
        self._create_basic_tab()
        
        # 选项卡2: 行为配置
        self._create_behavior_tab()
        
        # 保存按钮
        ttk.Button(right_frame, text="保存修改", command=self._save_attribute).pack(pady=10)
        
        self.attr_type_var.trace_add('write', self._on_type_changed)
        self._update_ui_by_type()
    
    def _set_right_panel_state(self, state):
        """设置右侧面板的启用状态
        
        Args:
            state: 'normal' 或 'disabled'
        """
        # 这里可以遍历并设置所有输入控件的状态
        # 目前仅作为占位，后续可以根据需要实现
        pass
    
    def _clear_right_panel(self):
        """清空右侧面板的内容"""
        self.attr_name_var.set('')
        self.attr_type_var.set('Layered')
        self.attr_category_var.set('Combat')
        self.attr_base_var.set('0')
        self.attr_flat_var.set('0')
        self.attr_percent_var.set('0')
        self.attr_current_var.set('0')
        self.attr_desc_var.set('')
        
        # Clamp
        self.clamp_enabled_var.set(False)
        self.clamp_min_var.set('')
        self.clamp_max_value_var.set('')
        self.clamp_max_attr_var.set('')
        
        # Delegate
        self.delegate_change_var.set(False)
        self.delegate_increase_var.set(False)
        self.delegate_decrease_var.set(False)
        self.delegate_decrease_alias_var.set('')
        
        # Event
        self.event_zero_tag_var.set('')
        self.event_full_tag_var.set('')
        self.event_threshold_low_var.set('')
        self.event_threshold_low_tag_var.set('')
        
        # Cue
        self.cue_decrease_var.set('')
        self.cue_zero_var.set('')
        self.cue_increase_var.set('')
        
        # Meta
        self.meta_target_set_var.set('')
        self.meta_target_var.set('')
        self.meta_mode_var.set('Add')
        self.meta_broadcast_var.set(False)
        self.meta_event_tag_var.set('')
        
        # Resource
        self.resource_mode_var.set('KeepCurrent')
    
    def _create_basic_tab(self):
        """创建基础信息选项卡"""
        basic_frame = ttk.Frame(self.notebook)
        self.notebook.add(basic_frame, text="基础信息")
        
        row = 0
        ttk.Label(basic_frame, text="属性名:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_name_var = tk.StringVar()
        ttk.Entry(basic_frame, textvariable=self.attr_name_var, width=20).grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        ttk.Label(basic_frame, text="类型:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_type_var = tk.StringVar(value="Layered")
        ttk.Combobox(basic_frame, textvariable=self.attr_type_var, values=ATTRIBUTE_TYPES, width=17).grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        ttk.Label(basic_frame, text="分类:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_category_var = tk.StringVar(value="Combat")
        ttk.Combobox(basic_frame, textvariable=self.attr_category_var, values=ATTRIBUTE_CATEGORIES, width=17).grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        ttk.Separator(basic_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky='ew', pady=10)
        
        row += 1
        ttk.Label(basic_frame, text="Base:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_base_var = tk.StringVar(value="0")
        ttk.Entry(basic_frame, textvariable=self.attr_base_var, width=20).grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        ttk.Label(basic_frame, text="Flat:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_flat_var = tk.StringVar(value="0")
        ttk.Entry(basic_frame, textvariable=self.attr_flat_var, width=20).grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        ttk.Label(basic_frame, text="Percent:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_percent_var = tk.StringVar(value="0")
        ttk.Entry(basic_frame, textvariable=self.attr_percent_var, width=20).grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        self.current_label = ttk.Label(basic_frame, text="Current:")
        self.current_label.grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_current_var = tk.StringVar(value="0")
        self.current_entry = ttk.Entry(basic_frame, textvariable=self.attr_current_var, width=20)
        self.current_entry.grid(row=row, column=1, padx=5, pady=3)
        
        row += 1
        ttk.Separator(basic_frame, orient='horizontal').grid(row=row, column=0, columnspan=2, sticky='ew', pady=10)
        
        row += 1
        ttk.Label(basic_frame, text="描述:").grid(row=row, column=0, sticky='w', padx=5, pady=3)
        self.attr_desc_var = tk.StringVar()
        ttk.Entry(basic_frame, textvariable=self.attr_desc_var, width=20).grid(row=row, column=1, padx=5, pady=3)
    
    def _create_behavior_tab(self):
        """创建行为配置选项卡 - 按使用场景组织"""
        behavior_frame = ttk.Frame(self.notebook)
        self.notebook.add(behavior_frame, text="行为配置")
        
        # 使用 Canvas + Scrollbar 支持滚动
        canvas = tk.Canvas(behavior_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(behavior_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # 绑定鼠标滚轮
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # ===== 1. 值范围 =====
        range_frame = ttk.LabelFrame(scrollable_frame, text="📏 值范围")
        range_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Resource 类型提示
        self.range_auto_label = ttk.Label(range_frame, 
            text="💡 Resource 类型自动限制在 [0, MaxXxx]", 
            foreground="gray", font=("", 8))
        self.range_auto_label.grid(row=0, column=0, columnspan=3, sticky='w', padx=5, pady=2)
        
        self.clamp_enabled_var = tk.BooleanVar()
        ttk.Checkbutton(range_frame, text="自定义范围限制", 
                       variable=self.clamp_enabled_var,
                       command=self._on_clamp_toggle).grid(
            row=1, column=0, columnspan=2, sticky='w', padx=5, pady=3)
        
        self.clamp_min_label = ttk.Label(range_frame, text="最小值:")
        self.clamp_min_label.grid(row=2, column=0, sticky='w', padx=5, pady=3)
        self.clamp_min_var = tk.StringVar()
        self.clamp_min_entry = ttk.Entry(range_frame, textvariable=self.clamp_min_var, width=12)
        self.clamp_min_entry.grid(row=2, column=1, padx=5, pady=3)
        
        self.clamp_max_label = ttk.Label(range_frame, text="最大值:")
        self.clamp_max_label.grid(row=3, column=0, sticky='w', padx=5, pady=3)
        self.clamp_max_value_var = tk.StringVar()
        self.clamp_max_entry = ttk.Entry(range_frame, textvariable=self.clamp_max_value_var, width=12)
        self.clamp_max_entry.grid(row=3, column=1, padx=5, pady=3)
        ttk.Label(range_frame, text="或", font=("", 8)).grid(row=3, column=2)
        
        self.clamp_max_attr_label = ttk.Label(range_frame, text="限制于属性:")
        self.clamp_max_attr_label.grid(row=4, column=0, sticky='w', padx=5, pady=3)
        self.clamp_max_attr_var = tk.StringVar()
        self.clamp_max_attr_entry = ttk.Entry(range_frame, textvariable=self.clamp_max_attr_var, width=12)
        self.clamp_max_attr_entry.grid(row=4, column=1, padx=5, pady=3)
        ttk.Label(range_frame, text="如 MaxMana", font=("", 8), foreground="gray").grid(row=4, column=2, sticky='w')
        
        # ===== 2. 变化监听 =====
        listen_frame = ttk.LabelFrame(scrollable_frame, text="📡 变化监听")
        listen_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(listen_frame, text="当属性值变化时，通知其他系统响应", 
                 foreground="gray", font=("", 8)).grid(row=0, column=0, columnspan=3, sticky='w', padx=5, pady=2)
        
        # C++ 委托回调
        callback_subframe = ttk.Frame(listen_frame)
        callback_subframe.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        
        ttk.Label(callback_subframe, text="C++ 回调:", font=("", 9, "bold")).pack(anchor='w')
        
        self.delegate_change_var = tk.BooleanVar()
        ttk.Checkbutton(callback_subframe, text="任何变化时回调", 
                       variable=self.delegate_change_var).pack(anchor='w', padx=10)
        
        self.delegate_increase_var = tk.BooleanVar()
        ttk.Checkbutton(callback_subframe, text="增加时回调", 
                       variable=self.delegate_increase_var).pack(anchor='w', padx=10)
        
        decrease_frame = ttk.Frame(callback_subframe)
        decrease_frame.pack(anchor='w', padx=10)
        self.delegate_decrease_var = tk.BooleanVar()
        ttk.Checkbutton(decrease_frame, text="减少时回调", 
                       variable=self.delegate_decrease_var).pack(side=tk.LEFT)
        ttk.Label(decrease_frame, text="别名:", font=("", 8)).pack(side=tk.LEFT, padx=(10,2))
        self.delegate_decrease_alias_var = tk.StringVar()
        ttk.Entry(decrease_frame, textvariable=self.delegate_decrease_alias_var, width=15).pack(side=tk.LEFT)
        ttk.Label(decrease_frame, text="如 OnDamageReceived", font=("", 7), foreground="gray").pack(side=tk.LEFT, padx=3)
        
        ttk.Separator(listen_frame, orient='horizontal').grid(row=2, column=0, columnspan=3, sticky='ew', pady=8)
        
        # 视觉表现
        visual_subframe = ttk.Frame(listen_frame)
        visual_subframe.grid(row=3, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        
        ttk.Label(visual_subframe, text="视觉表现 (GameplayCue):", font=("", 9, "bold")).pack(anchor='w')
        
        decrease_cue_frame = ttk.Frame(visual_subframe)
        decrease_cue_frame.pack(anchor='w', padx=10, pady=2)
        ttk.Label(decrease_cue_frame, text="减少时:").pack(side=tk.LEFT)
        self.cue_decrease_var = tk.StringVar()
        ttk.Entry(decrease_cue_frame, textvariable=self.cue_decrease_var, width=22).pack(side=tk.LEFT, padx=3)
        ttk.Label(decrease_cue_frame, text="如受击闪红", font=("", 7), foreground="gray").pack(side=tk.LEFT)
        
        increase_cue_frame = ttk.Frame(visual_subframe)
        increase_cue_frame.pack(anchor='w', padx=10, pady=2)
        ttk.Label(increase_cue_frame, text="增加时:").pack(side=tk.LEFT)
        self.cue_increase_var = tk.StringVar()
        ttk.Entry(increase_cue_frame, textvariable=self.cue_increase_var, width=22).pack(side=tk.LEFT, padx=3)
        ttk.Label(increase_cue_frame, text="如回血绿光", font=("", 7), foreground="gray").pack(side=tk.LEFT)
        
        # ===== 3. 关键状态触发 =====
        state_frame = ttk.LabelFrame(scrollable_frame, text="⚡ 关键状态触发")
        state_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(state_frame, text="当属性达到关键值时，触发游戏状态变化", 
                 foreground="gray", font=("", 8)).grid(row=0, column=0, columnspan=3, sticky='w', padx=5, pady=2)
        
        # 归零状态
        zero_subframe = ttk.LabelFrame(state_frame, text="归零时（如死亡/耗尽）")
        zero_subframe.grid(row=1, column=0, columnspan=3, sticky='ew', padx=5, pady=5)
        
        zero_tag_frame = ttk.Frame(zero_subframe)
        zero_tag_frame.pack(anchor='w', padx=5, pady=2)
        ttk.Label(zero_tag_frame, text="添加状态标签:").pack(side=tk.LEFT)
        self.event_zero_tag_var = tk.StringVar()
        ttk.Entry(zero_tag_frame, textvariable=self.event_zero_tag_var, width=20).pack(side=tk.LEFT, padx=3)
        ttk.Label(zero_tag_frame, text="如 State.Dead", font=("", 7), foreground="gray").pack(side=tk.LEFT)
        
        zero_cue_frame = ttk.Frame(zero_subframe)
        zero_cue_frame.pack(anchor='w', padx=5, pady=2)
        ttk.Label(zero_cue_frame, text="播放表现:").pack(side=tk.LEFT)
        self.cue_zero_var = tk.StringVar()
        ttk.Entry(zero_cue_frame, textvariable=self.cue_zero_var, width=20).pack(side=tk.LEFT, padx=3)
        ttk.Label(zero_cue_frame, text="如死亡动画", font=("", 7), foreground="gray").pack(side=tk.LEFT)
        
        # 满值状态
        full_subframe = ttk.LabelFrame(state_frame, text="满值时（如完全恢复）")
        full_subframe.grid(row=2, column=0, columnspan=3, sticky='ew', padx=5, pady=5)
        
        full_tag_frame = ttk.Frame(full_subframe)
        full_tag_frame.pack(anchor='w', padx=5, pady=2)
        ttk.Label(full_tag_frame, text="添加状态标签:").pack(side=tk.LEFT)
        self.event_full_tag_var = tk.StringVar()
        ttk.Entry(full_tag_frame, textvariable=self.event_full_tag_var, width=20).pack(side=tk.LEFT, padx=3)
        ttk.Label(full_tag_frame, text="如 State.FullHealth", font=("", 7), foreground="gray").pack(side=tk.LEFT)
        
        # 低阈值警告
        low_subframe = ttk.LabelFrame(state_frame, text="低于阈值时（如危险警告）")
        low_subframe.grid(row=3, column=0, columnspan=3, sticky='ew', padx=5, pady=5)
        
        low_threshold_frame = ttk.Frame(low_subframe)
        low_threshold_frame.pack(anchor='w', padx=5, pady=2)
        ttk.Label(low_threshold_frame, text="当低于").pack(side=tk.LEFT)
        self.event_threshold_low_var = tk.StringVar()
        ttk.Entry(low_threshold_frame, textvariable=self.event_threshold_low_var, width=5).pack(side=tk.LEFT, padx=3)
        ttk.Label(low_threshold_frame, text="% 时").pack(side=tk.LEFT)
        
        low_tag_frame = ttk.Frame(low_subframe)
        low_tag_frame.pack(anchor='w', padx=5, pady=2)
        ttk.Label(low_tag_frame, text="添加状态标签:").pack(side=tk.LEFT)
        self.event_threshold_low_tag_var = tk.StringVar()
        ttk.Entry(low_tag_frame, textvariable=self.event_threshold_low_tag_var, width=20).pack(side=tk.LEFT, padx=3)
        ttk.Label(low_tag_frame, text="如 State.LowHealth", font=("", 7), foreground="gray").pack(side=tk.LEFT)
        
        # ===== 4. Resource 属性配置 =====
        self.resource_frame = ttk.LabelFrame(scrollable_frame, text="💚 Resource 联动配置")
        self.resource_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(self.resource_frame, text="当 MaxXxx 变化时，Xxx 如何联动？", 
                 foreground="gray", font=("", 8)).grid(row=0, column=0, columnspan=3, sticky='w', padx=5, pady=2)
        
        # 联动模式选择
        mode_frame = ttk.Frame(self.resource_frame)
        mode_frame.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        ttk.Label(mode_frame, text="联动模式:").pack(side=tk.LEFT)
        self.resource_mode_var = tk.StringVar(value=ResourceConfig.MODE_KEEP_CURRENT)
        self.resource_mode_combo = ttk.Combobox(
            mode_frame, 
            textvariable=self.resource_mode_var, 
            values=ResourceConfig.MODES,
            width=15,
            state='readonly'
        )
        self.resource_mode_combo.pack(side=tk.LEFT, padx=3)
        
        # 模式说明
        self.resource_mode_desc = ttk.Label(self.resource_frame, text="", foreground="blue", font=("", 8))
        self.resource_mode_desc.grid(row=2, column=0, columnspan=3, sticky='w', padx=5, pady=2)
        
        # 绑定事件更新说明
        self.resource_mode_combo.bind('<<ComboboxSelected>>', self._on_resource_mode_changed)
        self._update_resource_mode_desc()
        
        # ===== 5. Meta 属性配置 =====
        self.meta_frame = ttk.LabelFrame(scrollable_frame, text="🔄 Meta 属性配置")
        self.meta_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(self.meta_frame, text="Meta 属性用于临时存储计算值（如待处理的伤害）", 
                 foreground="gray", font=("", 8)).grid(row=0, column=0, columnspan=3, sticky='w', padx=5, pady=2)
        
        # 目标属性集（下拉选择）
        target_set_frame = ttk.Frame(self.meta_frame)
        target_set_frame.grid(row=1, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        ttk.Label(target_set_frame, text="目标属性集:").pack(side=tk.LEFT)
        self.meta_target_set_var = tk.StringVar()
        self.meta_target_set_combo = ttk.Combobox(target_set_frame, textvariable=self.meta_target_set_var, width=15, state='readonly')
        self.meta_target_set_combo.pack(side=tk.LEFT, padx=3)
        self.meta_target_set_combo.bind('<<ComboboxSelected>>', self._on_meta_target_set_changed)
        
        # 目标属性（下拉选择）
        target_attr_frame = ttk.Frame(self.meta_frame)
        target_attr_frame.grid(row=2, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        ttk.Label(target_attr_frame, text="目标属性:").pack(side=tk.LEFT)
        self.meta_target_var = tk.StringVar()
        self.meta_target_combo = ttk.Combobox(target_attr_frame, textvariable=self.meta_target_var, width=15, state='readonly')
        self.meta_target_combo.pack(side=tk.LEFT, padx=3)
        
        # 应用模式
        mode_frame = ttk.Frame(self.meta_frame)
        mode_frame.grid(row=3, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        ttk.Label(mode_frame, text="应用模式:").pack(side=tk.LEFT)
        self.meta_mode_var = tk.StringVar(value="Add")
        ttk.Combobox(mode_frame, textvariable=self.meta_mode_var, 
                    values=["Add", "Set", "Multiply"], width=10).pack(side=tk.LEFT, padx=3)
        
        # 事件广播
        event_frame = ttk.Frame(self.meta_frame)
        event_frame.grid(row=4, column=0, columnspan=3, sticky='w', padx=5, pady=3)
        self.meta_broadcast_var = tk.BooleanVar()
        ttk.Checkbutton(event_frame, text="广播事件", 
                       variable=self.meta_broadcast_var).pack(side=tk.LEFT)
        ttk.Label(event_frame, text="Tag:").pack(side=tk.LEFT, padx=(10,2))
        self.meta_event_tag_var = tk.StringVar()
        ttk.Entry(event_frame, textvariable=self.meta_event_tag_var, width=20).pack(side=tk.LEFT)
        ttk.Label(event_frame, text="如 Event.DamageReceived", font=("", 7), foreground="gray").pack(side=tk.LEFT, padx=3)
    
    def _on_clamp_toggle(self):
        """切换自定义范围限制时，更新 UI 状态"""
        enabled = self.clamp_enabled_var.get()
        state = 'normal' if enabled else 'disabled'
        self.clamp_min_entry.configure(state=state)
        self.clamp_max_entry.configure(state=state)
        self.clamp_max_attr_entry.configure(state=state)
    
    def _on_resource_mode_changed(self, event=None):
        """Resource 联动模式变化时更新说明"""
        self._update_resource_mode_desc()
    
    def _update_resource_mode_desc(self):
        """更新 Resource 联动模式说明"""
        mode = self.resource_mode_var.get()
        desc = ResourceConfig.MODE_DESCRIPTIONS.get(mode, "")
        
        # 添加示例说明
        examples = {
            ResourceConfig.MODE_KEEP_CURRENT: "例: MaxHP 100→200, HP 80→80 (不变)",
            ResourceConfig.MODE_KEEP_RATIO: "例: MaxHP 100→200, HP 80→160 (保持80%)",
            ResourceConfig.MODE_ADD_DIFFERENCE: "例: MaxHP 100→200, HP 80→180 (+100)"
        }
        example = examples.get(mode, "")
        
        if hasattr(self, 'resource_mode_desc'):
            self.resource_mode_desc.configure(text=f"{desc}\n{example}")
    
    def _on_type_changed(self, *args):
        self._update_ui_by_type()
    
    def _update_ui_by_type(self):
        attr_type = self.attr_type_var.get()
        if attr_type == 'Resource':
            self.current_label.grid()
            self.current_entry.grid()
            # 更新范围提示
            if hasattr(self, 'range_auto_label'):
                self.range_auto_label.configure(
                    text="💡 Resource 类型自动限制在 [0, MaxXxx]",
                    foreground="green")
            # 显示 Resource 配置
            if hasattr(self, 'resource_frame'):
                self.resource_frame.pack(fill=tk.X, padx=5, pady=5)
            # 隐藏 Meta 配置
            if hasattr(self, 'meta_frame'):
                self.meta_frame.pack_forget()
        elif attr_type == 'Meta':
            self.current_label.grid_remove()
            self.current_entry.grid_remove()
            # 更新范围提示
            if hasattr(self, 'range_auto_label'):
                self.range_auto_label.configure(
                    text="💡 Meta 类型仅用于临时计算，不参与网络复制",
                    foreground="blue")
            # 隐藏 Resource 配置
            if hasattr(self, 'resource_frame'):
                self.resource_frame.pack_forget()
            # 显示 Meta 配置
            if hasattr(self, 'meta_frame'):
                self.meta_frame.pack(fill=tk.X, padx=5, pady=5)
        else:
            self.current_label.grid_remove()
            self.current_entry.grid_remove()
            # 更新范围提示
            if hasattr(self, 'range_auto_label'):
                self.range_auto_label.configure(
                    text="💡 如需限制范围，请勾选下方自定义选项",
                    foreground="gray")
            # 隐藏 Resource 配置
            if hasattr(self, 'resource_frame'):
                self.resource_frame.pack_forget()
            # 隐藏 Meta 配置
            if hasattr(self, 'meta_frame'):
                self.meta_frame.pack_forget()
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        """加载数据 - 支持新旧两种格式"""
        self.attributes.clear()
        
        if ATTRIBUTES_CONFIG.exists():
            with open(ATTRIBUTES_CONFIG, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.attributes.append(AttributeData.from_dict(row))
        
        # 尝试加载行为配置 JSON（新格式）
        if ATTRIBUTES_BEHAVIORS.exists():
            try:
                with open(ATTRIBUTES_BEHAVIORS, 'r', encoding='utf-8') as f:
                    behavior_data = json.load(f)
                    behaviors = behavior_data.get('Behaviors', {})
                    
                    # 为每个属性应用行为配置
                    for attr in self.attributes:
                        key = attr.get_behavior_key()
                        if key in behaviors:
                            attr.apply_behavior_dict(behaviors[key])
            except (json.JSONDecodeError, IOError) as e:
                print(f"警告: 加载行为配置失败: {e}")
        
        self._refresh_set_list()
    
    def save_config(self):
        """保存配置 - 分别写入 CSV 和 JSON"""
        try:
            # 先同步当前编辑中的属性到内存
            # 优先使用当前选中的索引，其次使用 _last_selected_idx
            current_idx = None
            selection = self.attr_tree.selection()
            if selection:
                try:
                    current_idx = int(selection[0])
                except ValueError:
                    pass
            
            if current_idx is not None and current_idx < len(self.attributes):
                self._save_attribute_silent(current_idx)
            elif self._last_selected_idx is not None and self._last_selected_idx < len(self.attributes):
                self._save_attribute_silent(self._last_selected_idx)
            
            # 确保目录存在
            ATTRIBUTES_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            
            # 1. 保存 CSV（基础信息，不含 BehaviorConfig）
            with open(ATTRIBUTES_CONFIG, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=ATTRIBUTES_CSV_FIELDS)
                writer.writeheader()
                for attr in self.attributes:
                    writer.writerow(attr.to_csv_dict())
            
            # 2. 保存 JSON（行为配置，只保存非默认值）
            behaviors = {}
            for attr in self.attributes:
                if attr.has_non_default_behavior():
                    behaviors[attr.get_behavior_key()] = attr.to_behavior_dict()
            
            behavior_data = {
                "Version": "1.0",
                "Behaviors": behaviors
            }
            
            with open(ATTRIBUTES_BEHAVIORS, 'w', encoding='utf-8') as f:
                json.dump(behavior_data, f, ensure_ascii=False, indent=2)
            
            self.app.show_status("属性配置已保存（CSV + JSON）")
        except Exception as e:
            messagebox.showerror("保存失败", str(e))
    
    def save_current_edit(self):
        self._destroy_edit_widget()
        # 获取当前选中的属性索引
        selection = self.attr_tree.selection()
        if selection:
            try:
                current_idx = int(selection[0])
                if current_idx < len(self.attributes):
                    self._save_attribute_silent(current_idx)
                    self._last_selected_idx = current_idx
            except (ValueError, IndexError):
                pass
        elif self._last_selected_idx is not None and self._last_selected_idx < len(self.attributes):
            self._save_attribute_silent(self._last_selected_idx)
        self._refresh_attr_list()
        self.save_config()
    
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
    
    # ========== UI 刷新和事件处理（简化版，完整版请参考原 attribute_module.py）==========
    
    def _refresh_set_list(self):
        sets = list(OrderedDict.fromkeys(attr.set_name for attr in self.attributes))
        counts = {}
        for s in sets:
            counts[s] = len([a for a in self.attributes if a.set_name == s])
        self.set_widget.refresh(sets, counts)
    
    def _refresh_attr_list(self, preserve_selection=True):
        """刷新属性列表
        
        Args:
            preserve_selection: 是否保持当前选择状态，默认为 True
        """
        # 保存当前选择状态
        selected_iid = None
        if preserve_selection:
            selection = self.attr_tree.selection()
            if selection:
                selected_iid = selection[0]
        
        self.attr_tree.delete(*self.attr_tree.get_children())
        if not self._current_set:
            return
        
        for i, attr in enumerate(self.attributes):
            if attr.set_name == self._current_set:
                self.attr_tree.insert('', 'end', iid=str(i), values=(
                    attr.name, attr.type, attr.category, attr.default_base, attr.description, '❌'))
        
        # 恢复选择状态
        if preserve_selection and selected_iid:
            children = self.attr_tree.get_children()
            if selected_iid in children:
                self.attr_tree.selection_set(selected_iid)
                self.attr_tree.focus(selected_iid)
            elif self._last_selected_idx is not None:
                # 如果原 iid 不存在，尝试用 _last_selected_idx 恢复
                fallback_iid = str(self._last_selected_idx)
                if fallback_iid in children:
                    self.attr_tree.selection_set(fallback_iid)
                    self.attr_tree.focus(fallback_iid)
    
    def _on_set_select(self, idx, value):
        # 保存当前编辑的属性（如果有）
        if self._last_selected_idx is not None and self._last_selected_idx < len(self.attributes):
            self._save_attribute_silent(self._last_selected_idx)
        
        self._current_set = value
        self._last_selected_idx = None
        self._refresh_attr_list(preserve_selection=False)
        
        # 自动选中新属性集的第一个属性
        children = self.attr_tree.get_children()
        if children:
            first_item = children[0]
            self.attr_tree.selection_set(first_item)
            self.attr_tree.focus(first_item)
            try:
                new_idx = int(first_item)
                if new_idx < len(self.attributes):
                    self._last_selected_idx = new_idx
                    self._sync_right_panel(self.attributes[new_idx])
            except (ValueError, IndexError):
                pass
        else:
            self._clear_right_panel()
    
    def _add_set(self):
        name = simpledialog.askstring("新建属性集", "属性集名称:")
        if name:
            self.attributes.append(AttributeData(set_name=name, name="NewAttribute", description="新属性"))
            self._refresh_set_list()
    
    def _on_delete_set(self, idx, value):
        if messagebox.askyesno("确认", f"确定删除属性集 '{value}'?"):
            self.attributes = [a for a in self.attributes if a.set_name != value]
            self._current_set = None
            self._refresh_set_list()
            self._refresh_attr_list()
    
    def _on_rename_set(self, event):
        idx, value = self.set_widget.get_selection()
        if value:
            new_name = simpledialog.askstring("重命名", "新名称:", initialvalue=value)
            if new_name and new_name != value:
                for attr in self.attributes:
                    if attr.set_name == value:
                        attr.set_name = new_name
                self._current_set = new_name
                self._refresh_set_list()
    
    def _on_attr_select(self, event):
        # 先保存之前选中的属性（如果有效）
        if self._last_selected_idx is not None and self._last_selected_idx < len(self.attributes):
            self._save_attribute_silent(self._last_selected_idx)
        
        selection = self.attr_tree.selection()
        if not selection:
            self._last_selected_idx = None
            return
        
        try:
            idx = int(selection[0])
            if idx >= len(self.attributes):
                self._last_selected_idx = None
                return
            self._last_selected_idx = idx
            attr = self.attributes[idx]
            self._sync_right_panel(attr)
        except (ValueError, IndexError):
            self._last_selected_idx = None
    
    def _add_attribute(self):
        if not self._current_set:
            messagebox.showwarning("警告", "请先选择一个属性集")
            return
        self.attributes.append(AttributeData(set_name=self._current_set, name="NewAttribute", description="新属性"))
        self._refresh_attr_list()
        self._refresh_set_list()
    
    def _delete_attribute(self):
        """删除选中的属性（由按钮调用）"""
        self._handle_tree_delete(self.attr_tree, on_after_delete=self._on_attr_deleted)
    
    def _on_attr_deleted(self):
        """属性删除后的回调：同步删除数据并刷新"""
        # 重建 attributes 列表（根据 tree 中剩余的项）
        remaining_indices = set()
        for item in self.attr_tree.get_children():
            try:
                remaining_indices.add(int(item))
            except ValueError:
                pass
        
        # 保留还在 tree 中的 attributes 或不属于当前 set 的
        new_attrs = []
        for i, attr in enumerate(self.attributes):
            if i in remaining_indices or attr.set_name != self._current_set:
                new_attrs.append(attr)
        self.attributes = new_attrs
        
        # 重置选中索引，避免索引错误
        self._last_selected_idx = None
        
        # 刷新列表（不保持选择，因为已删除）
        self._refresh_attr_list(preserve_selection=False)
        self._refresh_set_list()
        
        # 自动选中第一个剩余项
        children = self.attr_tree.get_children()
        if children:
            first_item = children[0]
            self.attr_tree.selection_set(first_item)
            self.attr_tree.focus(first_item)
            try:
                new_idx = int(first_item)
                if new_idx < len(self.attributes):
                    self._last_selected_idx = new_idx
                    self._sync_right_panel(self.attributes[new_idx])
            except (ValueError, IndexError):
                pass
    
    def _on_tree_click(self, event):
        """处理树形控件点击 - 检测删除列"""
        region = self.attr_tree.identify_region(event.x, event.y)
        if region != 'cell':
            return
        
        column = self.attr_tree.identify_column(event.x)
        if column != '#6':  # 第6列是删除列
            return
        
        item = self.attr_tree.identify_row(event.y)
        if not item:
            return
        
        # 直接删除该行，不需要确认
        try:
            idx = int(item)
            if idx < len(self.attributes):
                del self.attributes[idx]
                self._last_selected_idx = None
                self._refresh_attr_list()
                self._refresh_set_list()
        except (ValueError, IndexError):
            pass
    
    def _on_rename_attr(self, event):
        selection = self.attr_tree.selection()
        if selection:
            self._rename_attr_by_item(selection[0])
    
    def _rename_attr_by_item(self, item: str):
        """通过 item id 重命名属性"""
        try:
            idx = int(item)
            if idx < len(self.attributes):
                attr = self.attributes[idx]
                new_name = simpledialog.askstring("重命名", "新名称:", initialvalue=attr.name)
                if new_name:
                    attr.name = new_name
                    self._refresh_attr_list()
        except (ValueError, IndexError):
            pass
    
    def _delete_attr_by_item(self, item: str):
        """通过 item id 删除属性（右键菜单调用）"""
        try:
            idx = int(item)
            if idx < len(self.attributes):
                del self.attributes[idx]
                self._last_selected_idx = None
                self._refresh_attr_list()
                self._refresh_set_list()
        except (ValueError, IndexError):
            pass
    
    def _on_inline_edit_refresh(self, idx):
        """单击编辑后刷新表格"""
        # 刷新列表并保持选择
        self._refresh_attr_list(preserve_selection=True)
        
        # 确保选中项和 _last_selected_idx 一致
        if idx < len(self.attributes):
            self._last_selected_idx = idx
            attr = self.attributes[idx]
            self._sync_right_panel(attr)
            
            # 确保 Treeview 选中正确的项
            iid = str(idx)
            if iid in self.attr_tree.get_children():
                self.attr_tree.selection_set(iid)
                self.attr_tree.focus(iid)
    
    def _get_attribute_value(self, idx, key):
        """获取属性值 - 用于单击编辑"""
        if idx >= len(self.attributes):
            return None
        attr = self.attributes[idx]
        return getattr(attr, key, None)
    
    def _set_attribute_value(self, idx, key, value):
        """设置属性值 - 用于单击编辑"""
        if idx >= len(self.attributes):
            return
        attr = self.attributes[idx]
        setattr(attr, key, value)
    
    def _destroy_edit_widget(self):
        """销毁编辑控件 - 兼容旧接口"""
        self._destroy_active_editor()
    
    def _save_attribute(self):
        """保存当前编辑的属性（由"保存修改"按钮调用）"""
        # 优先使用当前选中的项
        selection = self.attr_tree.selection()
        if selection:
            try:
                idx = int(selection[0])
                if idx < len(self.attributes):
                    self._save_attribute_silent(idx)
                    self._last_selected_idx = idx
                    self._refresh_attr_list(preserve_selection=True)
                    return
            except (ValueError, IndexError):
                pass
        
        # 如果没有选中项，尝试使用 _last_selected_idx
        if self._last_selected_idx is not None and self._last_selected_idx < len(self.attributes):
            self._save_attribute_silent(self._last_selected_idx)
            self._refresh_attr_list(preserve_selection=True)
    
    def _save_attribute_silent(self, idx):
        if idx is None or idx >= len(self.attributes):
            return
        try:
            attr = self.attributes[idx]
            # 基础信息
            attr.name = self.attr_name_var.get()
            attr.type = self.attr_type_var.get()
            attr.category = self.attr_category_var.get()
            attr.default_base = float(self.attr_base_var.get() or 0)
            attr.default_flat = float(self.attr_flat_var.get() or 0)
            attr.default_percent = float(self.attr_percent_var.get() or 0)
            attr.default_current = float(self.attr_current_var.get() or 0)
            attr.description = self.attr_desc_var.get()
            
            # Clamp 配置
            attr.clamp.enabled = self.clamp_enabled_var.get()
            attr.clamp.min_value = self._parse_float_or_none(self.clamp_min_var.get())
            attr.clamp.max_value = self._parse_float_or_none(self.clamp_max_value_var.get())
            attr.clamp.max_attribute = self.clamp_max_attr_var.get() or None
            
            # 委托配置
            attr.delegate.on_change = self.delegate_change_var.get()
            attr.delegate.on_increase = self.delegate_increase_var.get()
            attr.delegate.on_decrease = self.delegate_decrease_var.get()
            attr.delegate.decrease_alias = self.delegate_decrease_alias_var.get()
            
            # 事件配置
            attr.event.on_zero_tag = self.event_zero_tag_var.get()
            attr.event.on_full_tag = self.event_full_tag_var.get()
            attr.event.threshold_low = self._parse_float_or_none(self.event_threshold_low_var.get())
            attr.event.threshold_low_tag = self.event_threshold_low_tag_var.get()
            
            # Cue 配置
            attr.cue.on_decrease_cue = self.cue_decrease_var.get()
            attr.cue.on_zero_cue = self.cue_zero_var.get()
            attr.cue.on_increase_cue = self.cue_increase_var.get()
            
            # Meta 配置 - 保存为 "SetName.AttributeName" 格式
            target_set = self.meta_target_set_var.get()
            target_attr = self.meta_target_var.get()
            if target_set and target_attr:
                attr.meta_config.target_attribute = f"{target_set}.{target_attr}"
            else:
                attr.meta_config.target_attribute = target_attr  # 兼容空值
            attr.meta_config.apply_mode = self.meta_mode_var.get()
            attr.meta_config.broadcast_event = self.meta_broadcast_var.get()
            attr.meta_config.event_tag = self.meta_event_tag_var.get()
            
            # Resource 配置
            attr.resource_config.max_change_mode = self.resource_mode_var.get()
        except (ValueError, IndexError):
            pass
    
    def _parse_float_or_none(self, value):
        """解析浮点数，空值返回 None"""
        if not value or value.strip() == '':
            return None
        try:
            return float(value)
        except ValueError:
            return None
    
    def _on_meta_target_set_changed(self, event=None):
        """当目标属性集改变时，更新目标属性下拉框"""
        selected_set = self.meta_target_set_var.get()
        if not selected_set:
            self.meta_target_combo['values'] = []
            return
        
        # 获取该属性集中的所有属性（排除 Meta 类型）
        options = []
        for a in self.attributes:
            if a.set_name != selected_set:
                continue
            if a.type == 'Meta':
                continue  # Meta 属性不能转发到另一个 Meta
            
            # 根据类型生成正确的属性名
            if a.type == 'Resource':
                options.append(a.name)  # Health, Mana
            elif a.type == 'Layered':
                options.append(a.name)  # 使用基础名，生成器会处理 Base 前缀
            else:
                options.append(a.name)
        
        self.meta_target_combo['values'] = options
        
        # 如果当前选中的属性不在新列表中，清空
        if self.meta_target_var.get() not in options:
            self.meta_target_var.set(options[0] if options else '')
    
    def _refresh_meta_target_set_options(self):
        """刷新目标属性集下拉框的选项"""
        # 获取所有属性集（排除当前 Meta 属性所在的属性集，避免自引用）
        sets = list(set(a.set_name for a in self.attributes if a.type != 'Meta'))
        self.meta_target_set_combo['values'] = sorted(sets)
    
    def _sync_right_panel(self, attr):
        """同步右侧编辑面板的内容"""
        # 启用编辑（如果之前被禁用）
        self._set_right_panel_state('normal')
        
        # 基础信息
        self.attr_name_var.set(attr.name)
        self.attr_type_var.set(attr.type)
        self.attr_category_var.set(attr.category)
        self.attr_base_var.set(str(attr.default_base))
        self.attr_flat_var.set(str(attr.default_flat))
        self.attr_percent_var.set(str(attr.default_percent))
        self.attr_current_var.set(str(attr.default_current))
        self.attr_desc_var.set(attr.description)
        
        # Clamp 配置
        self.clamp_enabled_var.set(attr.clamp.enabled)
        self.clamp_min_var.set(str(attr.clamp.min_value) if attr.clamp.min_value is not None else '')
        self.clamp_max_value_var.set(str(attr.clamp.max_value) if attr.clamp.max_value is not None else '')
        self.clamp_max_attr_var.set(attr.clamp.max_attribute or '')
        self._on_clamp_toggle()  # 更新控件启用状态
        
        # 委托配置
        self.delegate_change_var.set(attr.delegate.on_change)
        self.delegate_increase_var.set(attr.delegate.on_increase)
        self.delegate_decrease_var.set(attr.delegate.on_decrease)
        self.delegate_decrease_alias_var.set(attr.delegate.decrease_alias)
        
        # 事件配置
        self.event_zero_tag_var.set(attr.event.on_zero_tag)
        self.event_full_tag_var.set(attr.event.on_full_tag)
        self.event_threshold_low_var.set(str(attr.event.threshold_low) if attr.event.threshold_low is not None else '')
        self.event_threshold_low_tag_var.set(attr.event.threshold_low_tag)
        
        # Cue 配置
        self.cue_decrease_var.set(attr.cue.on_decrease_cue)
        self.cue_zero_var.set(attr.cue.on_zero_cue)
        self.cue_increase_var.set(attr.cue.on_increase_cue)
        
        # Meta 配置 - 解析 "SetName.AttributeName" 格式
        target_full = attr.meta_config.target_attribute or ''
        if '.' in target_full:
            target_set, target_attr = target_full.split('.', 1)
        else:
            # 兼容旧格式，尝试查找属性所在的集
            target_attr = target_full
            target_set = ''
            if target_attr:
                for a in self.attributes:
                    if a.name == target_attr and a.type != 'Meta':
                        target_set = a.set_name
                        break
        
        self._refresh_meta_target_set_options()
        self.meta_target_set_var.set(target_set)
        self._on_meta_target_set_changed()  # 刷新属性列表
        self.meta_target_var.set(target_attr)
        
        self.meta_mode_var.set(attr.meta_config.apply_mode)
        self.meta_broadcast_var.set(attr.meta_config.broadcast_event)
        self.meta_event_tag_var.set(attr.meta_config.event_tag)
        
        # Resource 配置
        self.resource_mode_var.set(attr.resource_config.max_change_mode)
        self._update_resource_mode_desc()
        
        self._update_ui_by_type()
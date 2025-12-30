#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BindingSet 编辑器 UI
支持 Tag 绑定和 Attribute 绑定，用于 AnimInstance、UI Widget 等任意部件
"""

import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from typing import List, Optional
from collections import OrderedDict

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import PROJECT_ROOT, BINDINGSET_CONFIG, BINDINGSET_OUTPUT
from ui_base import (
    BaseEditorUI, GroupListWidget, BottomButtonBar, InlineEditorMixin,
    show_selection_dialog, show_search_list_dialog, SearchListDialog, DialogBase
)
from .data import BindingSetData, TagBinding, AttributeBinding
from .generator import BindingSetGenerator
from .class_scanner import ClassScanner, BindingSetInjector, UClassInfo

# Attribute 绑定的变量类型选项
ATTRIBUTE_VAR_TYPES = ["float", "int32", "FGameplayAttributeData"]


class BindingSetEditorUI(BaseEditorUI, InlineEditorMixin):
    """BindingSet 编辑器 UI"""
    
    def __init__(self, parent, app):
        self.bindingsets: List[BindingSetData] = []
        self.current_bindingset: Optional[BindingSetData] = None
        self._editor_ready = False
        
        super().__init__(parent, app)
        self._init_inline_editor()
        
        self._create_ui()
        self.load_data()
    
    def _create_ui(self):
        """创建 UI"""
        # 左侧：BindingSet 列表
        self.set_widget = GroupListWidget(
            self.parent,
            title="BindingSet",
            on_select=self._on_set_select,
            on_add=self._add_bindingset,
            on_delete=self._on_delete_bindingset,
            show_count=True
        )
        self.set_widget.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        # 中间：Binding 表格
        middle_frame = ttk.Frame(self.parent)
        middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # BindingSet 描述
        desc_frame = ttk.Frame(middle_frame)
        desc_frame.pack(fill=tk.X, pady=5)
        ttk.Label(desc_frame, text="描述:").pack(side=tk.LEFT, padx=5)
        self.desc_var = tk.StringVar()
        self.desc_entry = ttk.Entry(desc_frame, textvariable=self.desc_var, width=50)
        self.desc_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.desc_entry.bind('<FocusOut>', self._on_desc_changed)
        self.desc_entry.bind('<Return>', self._on_desc_changed)
        
        # ============ Tag 绑定区域 ============
        tag_frame = ttk.LabelFrame(middle_frame, text="Tag 绑定列表")
        tag_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Tag 表格
        tag_columns = ('tag', 'variable', 'event_type', 'description')
        self.binding_tree = ttk.Treeview(tag_frame, columns=tag_columns, show='headings', height=8)
        self.binding_tree.heading('tag', text='GameplayTag')
        self.binding_tree.heading('variable', text='变量名')
        self.binding_tree.heading('event_type', text='事件类型')
        self.binding_tree.heading('description', text='描述')
        self.binding_tree.column('tag', width=200)
        self.binding_tree.column('variable', width=120)
        self.binding_tree.column('event_type', width=120)
        self.binding_tree.column('description', width=150)
        self.binding_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        # Tag 绑定事件
        self._bind_tree_delete_key(self.binding_tree, on_after_delete=self._on_tag_binding_deleted)
        self.binding_tree.bind('<Button-1>', self._on_tag_tree_click)
        
        # Tag 右键菜单
        self.bind_context_menu(
            self.binding_tree,
            on_delete=lambda w, item: self._delete_tag_binding_item(item)
        )
        
        # Tag 按钮栏
        tag_btn_frame = ttk.Frame(tag_frame)
        tag_btn_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Button(tag_btn_frame, text="+ 添加 Tag 绑定", command=self._add_tag_binding).pack(side=tk.LEFT, padx=2)
        ttk.Button(tag_btn_frame, text="从 Tags 导入", command=self._import_from_tags).pack(side=tk.LEFT, padx=2)
        
        # ============ Attribute 绑定区域 ============
        attr_frame = ttk.LabelFrame(middle_frame, text="Attribute 绑定列表")
        attr_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Attribute 表格
        attr_columns = ('attribute', 'variable', 'var_type', 'value_type', 'description')
        self.attr_tree = ttk.Treeview(attr_frame, columns=attr_columns, show='headings', height=8)
        self.attr_tree.heading('attribute', text='AttributeSet.Attribute')
        self.attr_tree.heading('variable', text='变量名')
        self.attr_tree.heading('var_type', text='变量类型')
        self.attr_tree.heading('value_type', text='值类型')
        self.attr_tree.heading('description', text='描述')
        self.attr_tree.column('attribute', width=200)
        self.attr_tree.column('variable', width=120)
        self.attr_tree.column('var_type', width=80)
        self.attr_tree.column('value_type', width=100)
        self.attr_tree.column('description', width=120)
        self.attr_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)
        
        # Attribute 绑定事件
        self._bind_tree_delete_key(self.attr_tree, on_after_delete=self._on_attr_binding_deleted)
        self.attr_tree.bind('<Button-1>', self._on_attr_tree_click)
        
        # Attribute 右键菜单
        self.bind_context_menu(
            self.attr_tree,
            on_delete=lambda w, item: self._delete_attr_binding_item(item)
        )
        
        # Attribute 按钮栏
        attr_btn_frame = ttk.Frame(attr_frame)
        attr_btn_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Button(attr_btn_frame, text="+ 添加 Attribute 绑定", command=self._add_attribute_binding).pack(side=tk.LEFT, padx=2)
        ttk.Button(attr_btn_frame, text="从 Attributes 导入", command=self._import_from_attributes).pack(side=tk.LEFT, padx=2)
        
        # ============ 底部操作按钮 ============
        self.button_bar = BottomButtonBar(middle_frame, buttons=[])
        self.button_bar.add_button("[生成代码]", self.generate_code, side=tk.RIGHT)
        self.button_bar.add_button("应用到类...", self._apply_to_class, side=tk.RIGHT)
        self.button_bar.add_button("重新加载", self.load_data, side=tk.RIGHT)
        self.button_bar.add_button("保存配置", self.save_current_edit, side=tk.RIGHT)
        self.button_bar.pack(fill=tk.X, pady=5)
        
        # 右侧：预览（可选）
        self._create_preview_panel(middle_frame)
    
    def _create_preview_panel(self, parent):
        """创建代码预览面板"""
        preview_frame = ttk.LabelFrame(parent, text="宏预览")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.preview_text = tk.Text(preview_frame, height=8, font=("Consolas", 9), wrap=tk.NONE)
        self.preview_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 水平滚动条
        h_scroll = ttk.Scrollbar(preview_frame, orient=tk.HORIZONTAL, command=self.preview_text.xview)
        h_scroll.pack(fill=tk.X, padx=5)
        self.preview_text.config(xscrollcommand=h_scroll.set)
    
    # ========== 数据操作 ==========
    
    def load_data(self):
        """加载数据"""
        self.bindingsets = []
        
        try:
            if BINDINGSET_CONFIG.exists():
                with open(BINDINGSET_CONFIG, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data.get('BindingSets', []):
                        self.bindingsets.append(BindingSetData.from_dict(item))
        except Exception as e:
            messagebox.showerror("错误", f"加载配置失败: {e}")
        
        self._refresh_set_list()
    
    def save_config(self) -> bool:
        """保存配置"""
        try:
            BINDINGSET_CONFIG.parent.mkdir(parents=True, exist_ok=True)
            
            data = {
                'BindingSets': [bs.to_dict() for bs in self.bindingsets]
            }
            
            with open(BINDINGSET_CONFIG, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            messagebox.showerror("错误", f"保存失败: {e}")
            return False
    
    def save_current_edit(self):
        if self.save_config():
            self.app.show_status("BindingSet 配置已保存")
    
    def _refresh_set_list(self):
        """刷新左侧 BindingSet 列表"""
        names = [bs.name for bs in self.bindingsets]
        counts = {bs.name: bs.total_bindings for bs in self.bindingsets}
        self.set_widget.refresh(names, counts)
    
    def _refresh_binding_list(self):
        """刷新绑定列表（Tag 和 Attribute）"""
        # 刷新 Tag 绑定列表
        self.binding_tree.delete(*self.binding_tree.get_children())
        # 刷新 Attribute 绑定列表
        self.attr_tree.delete(*self.attr_tree.get_children())
        
        if not self.current_bindingset:
            self.desc_var.set("")
            return
        
        self.desc_var.set(self.current_bindingset.description)
        
        # 填充 Tag 绑定
        for i, binding in enumerate(self.current_bindingset.tag_bindings):
            self.binding_tree.insert('', 'end', iid=f"tag_{i}", values=(
                binding.tag, binding.variable_name, binding.event_type, binding.description
            ))
        
        # 填充 Attribute 绑定
        for i, binding in enumerate(self.current_bindingset.attribute_bindings):
            listen_mode = self._get_listen_mode_display(binding)
            self.attr_tree.insert('', 'end', iid=f"attr_{i}", values=(
                binding.full_attribute_name, binding.variable_name, 
                binding.var_type, listen_mode, binding.description
            ))
        
        self._update_preview()
    
    def _get_listen_mode_display(self, binding: AttributeBinding) -> str:
        """获取监听模式的显示文本（基于 value_types 列表）"""
        if hasattr(binding, 'value_types') and binding.value_types:
            return ", ".join(binding.value_types)
        # 兼容旧数据
        return binding.value_type if binding.value_type else "Current"
    
    def _update_preview(self):
        """更新代码预览"""
        self.preview_text.delete('1.0', tk.END)
        
        if not self.current_bindingset or self.current_bindingset.total_bindings == 0:
            return
        
        # 显示宏名称预览
        prefix = self.current_bindingset.macro_prefix
        preview = f"// 生成的宏名称:\n"
        preview += f"DJ01_BINDING_SET_{prefix}_VARS()\n"
        preview += f"DJ01_BINDING_SET_{prefix}_CALLBACKS()\n"
        preview += f"DJ01_BINDING_SET_{prefix}_REGISTER(ASC)\n"
        preview += f"DJ01_BINDING_SET_{prefix}_UNREGISTER(ASC)\n"
        if self.current_bindingset.has_attribute_bindings:
            preview += f"DJ01_BINDING_SET_{prefix}_INIT_VALUES(ASC)\n"
        
        self.preview_text.insert('1.0', preview)
    
    def _on_set_select(self, idx, value):
        """选中 BindingSet"""
        for bs in self.bindingsets:
            if bs.name == value:
                self.current_bindingset = bs
                break
        self._refresh_binding_list()
    
    def _on_desc_changed(self, event=None):
        """描述变更"""
        if self.current_bindingset:
            self.current_bindingset.description = self.desc_var.get()
    
    def _get_tag_categories(self) -> List[str]:
        """获取所有 Tag 的一级分类（Category）"""
        try:
            tags = self.app.get_tags()
            categories = list(OrderedDict.fromkeys(t.category for t in tags if t.category))
            return categories
        except:
            return []
    
    def _get_all_tags(self) -> List[str]:
        """获取所有 Tag 名称"""
        try:
            tags = self.app.get_tags()
            return [t.tag for t in tags if t.tag]
        except:
            return []
    
    def _get_all_attributes(self) -> List[tuple]:
        """获取所有属性（返回 (SetName, AttributeName, Type, Description) 元组列表）"""
        try:
            attributes = self.app.get_attributes()
            return [(a.set_name, a.name, a.type, a.description) for a in attributes if a.set_name and a.name]
        except:
            return []
    
    def _get_attribute_sets(self) -> List[str]:
        """获取所有 AttributeSet 名称"""
        try:
            attributes = self.app.get_attributes()
            sets = list(OrderedDict.fromkeys(a.set_name for a in attributes if a.set_name))
            return sets
        except:
            return []
    
    def _add_bindingset(self):
        """添加新的 BindingSet - 使用选择框选择一级分类"""
        categories = self._get_tag_categories()
        
        if not categories:
            # 如果没有可选的分类，回退到手动输入
            name = simpledialog.askstring("新建 BindingSet", "BindingSet 名称 (如 CommonStatus, PlayerHUD):")
            if name:
                if any(bs.name == name for bs in self.bindingsets):
                    messagebox.showwarning("警告", f"BindingSet '{name}' 已存在")
                    return
                self.bindingsets.append(BindingSetData(name=name, description=f"{name} 绑定集"))
                self._refresh_set_list()
            return
        
        # 使用通用选择对话框
        name = show_selection_dialog(
            self.parent,
            title="新建 BindingSet",
            label="选择 Tag 一级分类或输入自定义名称:",
            options=categories,
            allow_custom=True
        )
        
        if name:
            if any(bs.name == name for bs in self.bindingsets):
                messagebox.showwarning("警告", f"BindingSet '{name}' 已存在")
                return
            self.bindingsets.append(BindingSetData(name=name, description=f"{name} 绑定集"))
            self._refresh_set_list()
    
    def _on_delete_bindingset(self, idx, value):
        """删除 BindingSet"""
        if messagebox.askyesno("确认", f"确定删除 BindingSet '{value}'?"):
            self.bindingsets = [bs for bs in self.bindingsets if bs.name != value]
            self.current_bindingset = None
            self._refresh_set_list()
            self._refresh_binding_list()
    
    def _add_tag_binding(self):
        """添加 Tag 绑定 - 使用选择框从已有 Tags 中选择"""
        if not self.current_bindingset:
            messagebox.showwarning("警告", "请先选择一个 BindingSet")
            return
        
        all_tags = self._get_all_tags()
        
        if not all_tags:
            # 如果没有可选的 Tag，创建默认绑定
            binding = TagBinding(
                tag="Status.New",
                variable_name="bNew",
                event_type="NewOrRemoved",
                description="新绑定"
            )
            self.current_bindingset.tag_bindings.append(binding)
            self._refresh_binding_list()
            self._refresh_set_list()
            return
        
        # 过滤掉已经添加的 tags
        existing_tags = {b.tag for b in self.current_bindingset.tag_bindings}
        available_tags = [t for t in all_tags if t not in existing_tags]
        
        if not available_tags:
            messagebox.showinfo("提示", "所有 Tag 都已添加到当前 BindingSet")
            return
        
        # 事件类型变量（需要在对话框外定义以便回调访问）
        event_type_var = tk.StringVar(value="NewOrRemoved")
        
        def add_event_type_widgets(dialog: SearchListDialog):
            """添加事件类型选择组件"""
            event_frame = ttk.Frame(dialog)
            event_frame.pack(fill=tk.X, padx=20, pady=10)
            ttk.Label(event_frame, text="事件类型:").pack(side=tk.LEFT)
            ttk.Radiobutton(event_frame, text="NewOrRemoved (bool)", 
                           variable=event_type_var, value="NewOrRemoved").pack(side=tk.LEFT, padx=10)
            ttk.Radiobutton(event_frame, text="AnyCountChange (int32)", 
                           variable=event_type_var, value="AnyCountChange").pack(side=tk.LEFT, padx=10)
        
        # 使用通用搜索列表对话框
        selected_tags = show_search_list_dialog(
            self.parent,
            title="添加 Tag 绑定",
            label="选择要添加的 Tag:",
            items=available_tags,
            select_mode=tk.MULTIPLE,
            extra_widgets=add_event_type_widgets
        )
        
        if not selected_tags:
            return
        
        added = 0
        event_type = event_type_var.get()
        
        for tag_name in selected_tags:
            # 生成变量名：从 tag 名提取最后一部分
            parts = tag_name.split('.')
            var_suffix = parts[-1] if parts else "New"
            
            # 根据事件类型决定变量名前缀
            if event_type == "NewOrRemoved":
                var_name = f"b{var_suffix}"
            else:
                var_name = f"{var_suffix}Count"
            
            # 获取 tag 的描述
            desc = ""
            try:
                tags = self.app.get_tags()
                for t in tags:
                    if t.tag == tag_name:
                        desc = t.description
                        break
            except:
                pass
            
            binding = TagBinding(
                tag=tag_name,
                variable_name=var_name,
                event_type=event_type,
                description=desc
            )
            self.current_bindingset.tag_bindings.append(binding)
            added += 1
        
        self._refresh_binding_list()
        self._refresh_set_list()
        
        if added > 0:
            self.app.show_status(f"已添加 {added} 个 Tag 绑定")
    
    def _delete_tag_binding(self):
        """删除选中的 Tag 绑定"""
        self._handle_tree_delete(self.binding_tree, on_after_delete=self._on_tag_binding_deleted)
    
    def _on_tag_binding_deleted(self):
        """Tag 绑定删除后的回调"""
        if not self.current_bindingset:
            return
        
        remaining_indices = set()
        for item in self.binding_tree.get_children():
            try:
                # 解析 "tag_X" 格式的 iid
                idx = int(item.split('_')[1])
                remaining_indices.add(idx)
            except (ValueError, IndexError):
                pass
        
        new_bindings = []
        for i, binding in enumerate(self.current_bindingset.tag_bindings):
            if i in remaining_indices:
                new_bindings.append(binding)
        
        self.current_bindingset.tag_bindings = new_bindings
        self._refresh_binding_list()
        self._refresh_set_list()
    
    def _delete_attr_binding(self):
        """删除选中的 Attribute 绑定"""
        self._handle_tree_delete(self.attr_tree, on_after_delete=self._on_attr_binding_deleted)
    
    def _on_attr_binding_deleted(self):
        """Attribute 绑定删除后的回调"""
        if not self.current_bindingset:
            return
        
        remaining_indices = set()
        for item in self.attr_tree.get_children():
            try:
                # 解析 "attr_X" 格式的 iid
                idx = int(item.split('_')[1])
                remaining_indices.add(idx)
            except (ValueError, IndexError):
                pass
        
        new_bindings = []
        for i, binding in enumerate(self.current_bindingset.attribute_bindings):
            if i in remaining_indices:
                new_bindings.append(binding)
        
        self.current_bindingset.attribute_bindings = new_bindings
        self._refresh_binding_list()
        self._refresh_set_list()
    
    def _delete_tag_binding_item(self, item: str):
        """右键菜单删除指定的 Tag 绑定"""
        if not self.current_bindingset:
            return
        try:
            # 解析 "tag_X" 格式的 iid
            idx = int(item.split('_')[1])
            if 0 <= idx < len(self.current_bindingset.tag_bindings):
                del self.current_bindingset.tag_bindings[idx]
                self._refresh_binding_list()
                self._refresh_set_list()
        except (ValueError, IndexError):
            pass
    
    def _delete_attr_binding_item(self, item: str):
        """右键菜单删除指定的 Attribute 绑定"""
        if not self.current_bindingset:
            return
        try:
            # 解析 "attr_X" 格式的 iid
            idx = int(item.split('_')[1])
            if 0 <= idx < len(self.current_bindingset.attribute_bindings):
                del self.current_bindingset.attribute_bindings[idx]
                self._refresh_binding_list()
                self._refresh_set_list()
        except (ValueError, IndexError):
            pass
    
    def _add_attribute_binding(self):
        """添加 Attribute 绑定"""
        if not self.current_bindingset:
            messagebox.showwarning("警告", "请先选择一个 BindingSet")
            return
        
        all_attrs = self._get_all_attributes()
        
        if not all_attrs:
            # 如果没有可选的属性，创建默认绑定
            binding = AttributeBinding(
                attribute_set="CharacterAttributeSet",
                attribute_name="Health",
                variable_name="CurrentHealth",
                var_type="float",
                listen_current=True,
                listen_base=False,
                description="新属性绑定"
            )
            self.current_bindingset.attribute_bindings.append(binding)
            self._refresh_binding_list()
            self._refresh_set_list()
            return
        
        # 过滤掉已经添加的属性
        existing_attrs = {(b.attribute_set, b.attribute_name) for b in self.current_bindingset.attribute_bindings}
        available_attrs = [(s, n, t, d) for s, n, t, d in all_attrs if (s, n) not in existing_attrs]
        
        if not available_attrs:
            messagebox.showinfo("提示", "所有属性都已添加到当前 BindingSet")
            return
        
        # 转换为显示列表
        display_items = [f"{s}.{n}" for s, n, t, d in available_attrs]
        
        # 变量类型和值类型（多选）
        var_type_var = tk.StringVar(value="float")
        value_type_vars = {}  # 每个值类型对应一个 BooleanVar
        
        from .data import VALID_VALUE_TYPES
        
        def add_extra_widgets(dialog: SearchListDialog):
            """添加额外的配置组件"""
            config_frame = ttk.Frame(dialog)
            config_frame.pack(fill=tk.X, padx=20, pady=10)
            
            # 变量类型
            type_frame = ttk.Frame(config_frame)
            type_frame.pack(fill=tk.X, pady=2)
            ttk.Label(type_frame, text="变量类型:").pack(side=tk.LEFT)
            for vtype in ATTRIBUTE_VAR_TYPES[:2]:  # 只显示 float 和 int32
                ttk.Radiobutton(type_frame, text=vtype, variable=var_type_var, value=vtype).pack(side=tk.LEFT, padx=5)
            
            # 值类型（多选复选框）
            value_frame = ttk.Frame(config_frame)
            value_frame.pack(fill=tk.X, pady=2)
            ttk.Label(value_frame, text="值类型:").pack(side=tk.LEFT)
            
            for vt in VALID_VALUE_TYPES:
                var = tk.BooleanVar(value=(vt == "Current"))  # 默认选中 Current
                value_type_vars[vt] = var
                cb = ttk.Checkbutton(value_frame, text=vt, variable=var)
                cb.pack(side=tk.LEFT, padx=3)
            
            # 值类型说明
            hint_frame = ttk.Frame(config_frame)
            hint_frame.pack(fill=tk.X, pady=2)
            hint_label = ttk.Label(hint_frame, text="提示: Current=当前值, Max=最大值, Total=计算总值, Base/Flat/Percent=三层属性", 
                                   foreground='gray')
            hint_label.pack(side=tk.LEFT, padx=5)
        
        # 使用通用搜索列表对话框
        selected_items = show_search_list_dialog(
            self.parent,
            title="添加 Attribute 绑定",
            label="选择要添加的属性:",
            items=display_items,
            select_mode=tk.MULTIPLE,
            extra_widgets=add_extra_widgets
        )
        
        if not selected_items:
            return
        
        added = 0
        var_type = var_type_var.get()
        
        # 收集选中的值类型
        selected_value_types = [vt for vt, var in value_type_vars.items() if var.get()]
        if not selected_value_types:
            selected_value_types = ["Current"]  # 默认至少选中 Current
        
        for item in selected_items:
            # 解析 SetName.AttributeName
            parts = item.split('.', 1)
            if len(parts) != 2:
                continue
            set_name, attr_name = parts
            
            # 获取描述和类型
            desc = ""
            attr_type = "Layered"
            for s, n, t, d in available_attrs:
                if s == set_name and n == attr_name:
                    desc = d
                    attr_type = t
                    break
            
            # 根据属性类型过滤有效的值类型
            effective_value_types = []
            for vt in selected_value_types:
                if attr_type == "Meta":
                    # Meta 属性不应绑定，跳过
                    continue
                elif attr_type == "Resource":
                    # Resource 类型只有 Current 和 Max
                    if vt in ["Current", "Max"]:
                        effective_value_types.append(vt)
                elif attr_type == "Simple":
                    # Simple 类型只有 Current
                    if vt == "Current":
                        effective_value_types.append(vt)
                else:
                    # Layered 类型支持所有（除了 Current 和 Max）
                    if vt not in ["Current", "Max"]:
                        effective_value_types.append(vt)
            
            if not effective_value_types:
                continue
            
            # 变量名使用属性名作为基础（前缀由生成器根据值类型添加）
            var_name = attr_name
            
            binding = AttributeBinding(
                attribute_set=set_name,
                attribute_name=attr_name,
                variable_name=var_name,
                var_type=var_type,
                value_types=effective_value_types,
                description=desc
            )
            self.current_bindingset.attribute_bindings.append(binding)
            added += 1
        
        self._refresh_binding_list()
        self._refresh_set_list()
        
        if added > 0:
            self.app.show_status(f"已添加 {added} 个 Attribute 绑定")
    
    def _import_from_attributes(self):
        """从 Attributes 编辑器批量导入"""
        if not self.current_bindingset:
            messagebox.showwarning("警告", "请先选择一个 BindingSet")
            return
        
        # 获取所有属性
        all_attrs = self._get_all_attributes()
        if not all_attrs:
            messagebox.showwarning("警告", "无法获取 Attributes 数据")
            return
        
        # 过滤已存在的
        existing_attrs = {(b.attribute_set, b.attribute_name) for b in self.current_bindingset.attribute_bindings}
        available_attrs = [(s, n, t, d) for s, n, t, d in all_attrs if (s, n) not in existing_attrs]
        
        if not available_attrs:
            messagebox.showinfo("提示", "没有可导入的属性")
            return
        
        display_items = [f"{s}.{n}" for s, n, t, d in available_attrs]
        
        # 使用通用搜索列表对话框
        selected_items = show_search_list_dialog(
            self.parent,
            title="选择要导入的 Attributes",
            label="选择要导入到当前 BindingSet 的属性:",
            items=display_items,
            select_mode=tk.MULTIPLE
        )
        
        if not selected_items:
            return
        
        imported = 0
        for item in selected_items:
            parts = item.split('.', 1)
            if len(parts) != 2:
                continue
            set_name, attr_name = parts
            
            # 获取描述
            desc = ""
            for s, n, t, d in available_attrs:
                if s == set_name and n == attr_name:
                    desc = d
                    break
            
            # 检查是否已存在
            if not any(b.attribute_set == set_name and b.attribute_name == attr_name 
                       for b in self.current_bindingset.attribute_bindings):
                binding = AttributeBinding(
                    attribute_set=set_name,
                    attribute_name=attr_name,
                    variable_name=attr_name,
                    var_type="float",
                    value_types=["Current"],
                    description=desc
                )
                self.current_bindingset.attribute_bindings.append(binding)
                imported += 1
        
        self._refresh_binding_list()
        self._refresh_set_list()
        
        if imported > 0:
            messagebox.showinfo("完成", f"已导入 {imported} 个 Attribute 绑定")

    def _import_from_tags(self):
        """从 Tags 编辑器导入"""
        if not self.current_bindingset:
            messagebox.showwarning("警告", "请先选择一个 BindingSet")
            return
        
        # 获取所有 tags
        try:
            tags = self.app.get_tags()
        except:
            messagebox.showwarning("警告", "无法获取 Tags 数据")
            return
        
        # 过滤已存在的
        existing_tags = {b.tag for b in self.current_bindingset.tag_bindings}
        available_tags = [t.tag for t in tags if t.tag and t.tag not in existing_tags]
        
        if not available_tags:
            messagebox.showinfo("提示", "没有可导入的 Tag")
            return
        
        # 使用通用搜索列表对话框
        selected_tags = show_search_list_dialog(
            self.parent,
            title="选择要导入的 Tags",
            label="选择要导入到当前 BindingSet 的 Tags:",
            items=available_tags,
            select_mode=tk.MULTIPLE
        )
        
        if not selected_tags:
            return
        
        imported = 0
        for tag_name in selected_tags:
            # 获取 tag 信息
            desc = ""
            try:
                for t in tags:
                    if t.tag == tag_name:
                        desc = t.description
                        break
            except:
                pass
            
            # 生成变量名
            parts = tag_name.split('.')
            var_suffix = parts[-1] if parts else "New"
            var_name = f"b{var_suffix}"
            
            # 检查是否已存在
            if not any(b.tag == tag_name for b in self.current_bindingset.tag_bindings):
                binding = TagBinding(
                    tag=tag_name,
                    variable_name=var_name,
                    event_type="NewOrRemoved",
                    description=desc
                )
                self.current_bindingset.tag_bindings.append(binding)
                imported += 1
        
        self._refresh_binding_list()
        self._refresh_set_list()
        
        if imported > 0:
            messagebox.showinfo("完成", f"已导入 {imported} 个 Tag 绑定")
    
    # ========== 行内编辑 ==========
    
    def _on_tag_tree_click(self, event):
        """处理 Tag 表格的单击事件"""
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
        self.binding_tree.after(180, lambda: self._handle_tag_tree_click(event))
    
    def _on_attr_tree_click(self, event):
        """处理 Attribute 表格的单击事件"""
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
        self.attr_tree.after(180, lambda: self._handle_attr_tree_click(event))
    
    def _handle_tag_tree_click(self, event):
        """实际处理 Tag 表格的单击编辑"""
        cell_info = self._get_cell_info(self.binding_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        x, y, w, h = bbox
        
        self.binding_tree.selection_set(item)
        self.binding_tree.focus(item)
        
        try:
            # 解析 "tag_X" 格式的 iid
            binding_idx = int(item.split('_')[1])
            binding = self.current_bindingset.tag_bindings[binding_idx]
        except:
            return
        
        current_values = list(self.binding_tree.item(item, 'values'))
        
        # 列: tag(0), variable(1), event_type(2), description(3)
        if col_idx == 0:  # tag - 下拉选择框
            self._create_tag_combo(item, col_idx, x, y, w, h, current_values, binding)
        elif col_idx == 2:  # event_type - 下拉框
            self._create_event_type_combo(item, col_idx, x, y, w, h, current_values, binding)
        else:  # variable(1), description(3) - 文本框
            field_map = {1: 'variable_name', 3: 'description'}
            if col_idx in field_map:
                self._create_binding_entry(self.binding_tree, item, col_idx, x, y, w, h, current_values, binding, field_map[col_idx])
    
    def _handle_attr_tree_click(self, event):
        """实际处理 Attribute 表格的单击编辑"""
        cell_info = self._get_cell_info(self.attr_tree, event)
        if not cell_info:
            return
        
        item, column, col_idx, bbox = cell_info
        x, y, w, h = bbox
        
        self.attr_tree.selection_set(item)
        self.attr_tree.focus(item)
        
        try:
            # 解析 "attr_X" 格式的 iid
            binding_idx = int(item.split('_')[1])
            binding = self.current_bindingset.attribute_bindings[binding_idx]
        except:
            return
        
        current_values = list(self.attr_tree.item(item, 'values'))
        
        # 列: attribute(0), variable(1), var_type(2), listen_mode(3), description(4)
        if col_idx == 0:  # attribute - 下拉选择框
            self._create_attr_combo(item, col_idx, x, y, w, h, current_values, binding)
        elif col_idx == 2:  # var_type - 下拉框
            self._create_var_type_combo(item, col_idx, x, y, w, h, current_values, binding)
        elif col_idx == 3:  # listen_mode - 下拉框
            self._create_listen_mode_combo(item, col_idx, x, y, w, h, current_values, binding)
        else:  # variable(1), description(4) - 文本框
            field_map = {1: 'variable_name', 4: 'description'}
            if col_idx in field_map:
                self._create_binding_entry(self.attr_tree, item, col_idx, x, y, w, h, current_values, binding, field_map[col_idx])
    
    def _create_binding_entry(self, tree, item, col_idx, x, y, w, h, current_values, binding, field_name):
        """创建文本框编辑器"""
        self._destroy_active_editor()
        
        entry = ttk.Entry(tree, width=max(5, w // 8))
        entry.insert(0, str(current_values[col_idx]))
        entry.place(x=x, y=y, width=w, height=h)
        entry.select_range(0, tk.END)
        self._active_editor = entry
        self._editor_ready = False
        
        def on_confirm(event=None):
            if self._active_editor != entry:
                return
            new_value = entry.get()
            
            setattr(binding, field_name, new_value)
            current_values[col_idx] = new_value
            
            tree.item(item, values=current_values)
            self._destroy_active_editor()
            self._update_preview()
        
        def on_escape(event):
            self._destroy_active_editor()
        
        def on_focus_out(event):
            if self._editor_ready and self._active_editor == entry:
                tree.after(50, on_confirm)
        
        entry.bind('<Return>', on_confirm)
        entry.bind('<Escape>', on_escape)
        entry.bind('<FocusOut>', on_focus_out)
        
        entry.focus_set()
        entry.after(250, lambda: setattr(self, '_editor_ready', True))
    
    def _create_tag_combo(self, item, col_idx, x, y, w, h, current_values, binding):
        """创建 Tag 选择下拉框"""
        self._destroy_active_editor()
        
        # 获取所有可用的 tags
        all_tags = self._get_all_tags()
        if not all_tags:
            # 如果没有可选的 tags，改用文本输入
            self._create_binding_entry(item, col_idx, x, y, w, h, current_values, binding, 'tag')
            return
        
        combo = ttk.Combobox(self.binding_tree, values=all_tags, width=max(5, w // 8))
        combo.set(current_values[col_idx])
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        self._editor_ready = False
        
        def on_select(event=None):
            if self._active_editor != combo:
                return
            new_value = combo.get()
            
            binding.tag = new_value
            current_values[col_idx] = new_value
            
            self.binding_tree.item(item, values=current_values)
            self._destroy_active_editor()
            self._update_preview()
        
        def on_focus_out(event):
            if self._editor_ready and self._active_editor == combo:
                self.binding_tree.after(50, on_select)
        
        combo.bind('<<ComboboxSelected>>', on_select)
        combo.bind('<Return>', on_select)
        combo.bind('<FocusOut>', on_focus_out)
        combo.bind('<Escape>', lambda e: self._destroy_active_editor())
        
        combo.focus_set()
        combo.after(250, lambda: setattr(self, '_editor_ready', True))
    
    def _create_event_type_combo(self, item, col_idx, x, y, w, h, current_values, binding):
        """创建事件类型下拉框"""
        self._destroy_active_editor()
        
        combo = ttk.Combobox(self.binding_tree, values=["NewOrRemoved", "AnyCountChange"], 
                            state='readonly', width=max(5, w // 10))
        combo.set(current_values[col_idx])
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        self._editor_ready = False
        
        def on_select(event=None):
            if self._active_editor != combo:
                return
            new_value = combo.get()
            
            binding.event_type = new_value
            current_values[col_idx] = new_value
            
            self.binding_tree.item(item, values=current_values)
            self._destroy_active_editor()
            self._update_preview()
        
        def on_focus_out(event):
            if self._editor_ready and self._active_editor == combo:
                self.binding_tree.after(50, on_select)
        
        combo.bind('<<ComboboxSelected>>', on_select)
        combo.bind('<FocusOut>', on_focus_out)
        combo.bind('<Escape>', lambda e: self._destroy_active_editor())
        
        combo.focus_set()
        combo.after(250, lambda: setattr(self, '_editor_ready', True))
    
    def _create_attr_combo(self, item, col_idx, x, y, w, h, current_values, binding):
        """创建 Attribute 选择下拉框"""
        self._destroy_active_editor()
        
        all_attrs = self._get_all_attributes()
        if not all_attrs:
            self._create_binding_entry(self.attr_tree, item, col_idx, x, y, w, h, current_values, binding, 'attribute_name')
            return
        
        display_items = [f"{s}.{n}" for s, n, t, d in all_attrs]
        
        combo = ttk.Combobox(self.attr_tree, values=display_items, width=max(5, w // 8))
        combo.set(current_values[col_idx])
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        self._editor_ready = False
        
        def on_select(event=None):
            if self._active_editor != combo:
                return
            new_value = combo.get()
            
            # 解析 SetName.AttributeName
            parts = new_value.split('.', 1)
            if len(parts) == 2:
                binding.attribute_set = parts[0]
                binding.attribute_name = parts[1]
            
            current_values[col_idx] = new_value
            self.attr_tree.item(item, values=current_values)
            self._destroy_active_editor()
            self._update_preview()
        
        def on_focus_out(event):
            if self._editor_ready and self._active_editor == combo:
                self.attr_tree.after(50, on_select)
        
        combo.bind('<<ComboboxSelected>>', on_select)
        combo.bind('<Return>', on_select)
        combo.bind('<FocusOut>', on_focus_out)
        combo.bind('<Escape>', lambda e: self._destroy_active_editor())
        
        combo.focus_set()
        combo.after(250, lambda: setattr(self, '_editor_ready', True))
    
    def _create_var_type_combo(self, item, col_idx, x, y, w, h, current_values, binding):
        """创建变量类型下拉框"""
        self._destroy_active_editor()
        
        combo = ttk.Combobox(self.attr_tree, values=ATTRIBUTE_VAR_TYPES, 
                            state='readonly', width=max(5, w // 10))
        combo.set(current_values[col_idx])
        combo.place(x=x, y=y, width=w, height=h)
        self._active_editor = combo
        self._editor_ready = False
        
        def on_select(event=None):
            if self._active_editor != combo:
                return
            new_value = combo.get()
            
            binding.var_type = new_value
            current_values[col_idx] = new_value
            
            self.attr_tree.item(item, values=current_values)
            self._destroy_active_editor()
            self._update_preview()
        
        def on_focus_out(event):
            if self._editor_ready and self._active_editor == combo:
                self.attr_tree.after(50, on_select)
        
        combo.bind('<<ComboboxSelected>>', on_select)
        combo.bind('<FocusOut>', on_focus_out)
        combo.bind('<Escape>', lambda e: self._destroy_active_editor())
        
        combo.focus_set()
        combo.after(250, lambda: setattr(self, '_editor_ready', True))
    
    def _create_listen_mode_combo(self, item, col_idx, x, y, w, h, current_values, binding):
        """创建值类型多选弹出框"""
        self._destroy_active_editor()
        
        from .data import VALID_VALUE_TYPES
        
        # 创建一个弹出窗口用于多选
        popup = tk.Toplevel(self.attr_tree)
        popup.wm_overrideredirect(True)  # 无边框
        popup.wm_geometry(f"+{self.attr_tree.winfo_rootx() + x}+{self.attr_tree.winfo_rooty() + y + h}")
        
        self._active_editor = popup
        self._editor_ready = False
        
        # 获取当前选中的值类型
        current_types = binding.value_types if hasattr(binding, 'value_types') and binding.value_types else [binding.value_type or "Current"]
        
        # 创建复选框
        check_vars = {}
        frame = ttk.Frame(popup, relief='solid', borderwidth=1)
        frame.pack(fill=tk.BOTH, expand=True)
        
        for vt in VALID_VALUE_TYPES:
            var = tk.BooleanVar(value=(vt in current_types))
            check_vars[vt] = var
            cb = ttk.Checkbutton(frame, text=vt, variable=var)
            cb.pack(anchor='w', padx=5, pady=1)
        
        # 确认按钮
        def on_confirm():
            if self._active_editor != popup:
                return
            
            # 收集选中的值类型
            selected = [vt for vt, var in check_vars.items() if var.get()]
            if not selected:
                selected = ["Current"]
            
            # 更新 binding
            binding.value_types = selected
            
            # 更新显示
            current_values[col_idx] = ", ".join(selected)
            self.attr_tree.item(item, values=current_values)
            
            self._destroy_active_editor()
            self._update_preview()
        
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill=tk.X, padx=5, pady=3)
        ttk.Button(btn_frame, text="确定", command=on_confirm, width=6).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="取消", command=self._destroy_active_editor, width=6).pack(side=tk.LEFT, padx=2)
        
        # 点击外部关闭
        def on_focus_out(event):
            # 检查焦点是否仍在弹出窗口内
            try:
                if popup.focus_get() and str(popup.focus_get()).startswith(str(popup)):
                    return
            except:
                pass
            popup.after(100, self._destroy_active_editor)
        
        popup.bind('<FocusOut>', on_focus_out)
        popup.bind('<Escape>', lambda e: self._destroy_active_editor())
        
        popup.focus_set()
        popup.after(250, lambda: setattr(self, '_editor_ready', True))

    # ========== 应用到类 ==========
    
    def _apply_to_class(self):
        """将当前 BindingSet 应用到指定的 C++ 类"""
        if not self.current_bindingset:
            messagebox.showwarning("警告", "请先选择一个 BindingSet")
            return
        
        if self.current_bindingset.total_bindings == 0:
            messagebox.showwarning("警告", "当前 BindingSet 没有任何绑定")
            return
        
        # 弹出应用对话框
        ApplyToClassDialog(self.parent, self.current_bindingset, self.app)
    
    # ========== 代码生成 ==========
    
    def generate_code(self):
        """生成代码"""
        valid_sets = [bs for bs in self.bindingsets if bs.name and bs.total_bindings > 0]
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            BINDINGSET_OUTPUT.mkdir(parents=True, exist_ok=True)
            
            # 清理旧的生成文件
            valid_filenames = {bs.header_filename for bs in valid_sets}
            valid_filenames.add("BindingSets.h")  # 保留汇总文件
            
            deleted_count = 0
            for old_file in BINDINGSET_OUTPUT.glob("BindingSet_*.h"):
                if old_file.name not in valid_filenames:
                    old_file.unlink()
                    deleted_count += 1
            
            if not valid_sets:
                # 没有有效的 BindingSet，清理汇总文件
                index_file = BINDINGSET_OUTPUT / "BindingSets.h"
                if index_file.exists():
                    index_file.unlink()
                    deleted_count += 1
                
                self.save_config()
                
                if deleted_count > 0:
                    messagebox.showinfo("完成", f"已清理 {deleted_count} 个旧文件\n当前没有 BindingSet 需要生成")
                else:
                    messagebox.showinfo("提示", "没有可生成的 BindingSet")
                return
            
            # 生成每个 BindingSet 的头文件
            for bindingset in valid_sets:
                header = BindingSetGenerator.generate_header(bindingset, timestamp)
                output_path = BINDINGSET_OUTPUT / bindingset.header_filename
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(header)
            
            # 生成汇总头文件
            index_header = BindingSetGenerator.generate_index_header(valid_sets, timestamp)
            with open(BINDINGSET_OUTPUT / "BindingSets.h", 'w', encoding='utf-8') as f:
                f.write(index_header)
            
            self.save_config()
            
            total_bindings = sum(bs.total_bindings for bs in valid_sets)
            msg = f"已生成 {len(valid_sets)} 个 BindingSet\n共 {total_bindings} 个绑定 (Tag + Attribute)"
            if deleted_count > 0:
                msg += f"\n已清理 {deleted_count} 个旧文件"
            messagebox.showinfo("成功", msg)
            
        except Exception as e:
            messagebox.showerror("错误", f"生成失败: {e}")


class ApplyToClassDialog(DialogBase):
    """应用 BindingSet 到 C++ 类的对话框"""
    
    def __init__(self, parent, bindingset: BindingSetData, app):
        self.bindingset = bindingset
        self.app = app
        self.scanner = ClassScanner()
        self.classes: List[UClassInfo] = []
        self.filtered_classes: List[UClassInfo] = []
        
        # 调用父类初始化（会自动居中）
        super().__init__(parent, f"应用 BindingSet: {bindingset.name}", width=900, height=600)
        
        self._create_ui()
        self._scan_classes()
    
    def _create_ui(self):
        """创建 UI"""
        # 顶部：过滤栏
        filter_frame = ttk.Frame(self)
        filter_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(filter_frame, text="搜索:").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace('w', lambda *args: self._filter_classes())
        search_entry = ttk.Entry(filter_frame, textvariable=self.search_var, width=30)
        search_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(filter_frame, text="类型:").pack(side=tk.LEFT, padx=(20, 5))
        self.filter_type = tk.StringVar(value="全部")
        type_combo = ttk.Combobox(filter_frame, textvariable=self.filter_type, 
                                  values=["全部", "AnimInstance", "Widget", "Actor/Pawn", "Component"],
                                  state='readonly', width=15)
        type_combo.pack(side=tk.LEFT)
        type_combo.bind('<<ComboboxSelected>>', lambda e: self._filter_classes())
        
        ttk.Button(filter_frame, text="🔄 刷新", command=self._scan_classes).pack(side=tk.RIGHT)
        
        # 中间：类列表
        list_frame = ttk.LabelFrame(self, text=f"选择要添加 BindingSet '{self.bindingset.name}' 的类")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        columns = ('class', 'base', 'bindings', 'path')
        self.class_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        self.class_tree.heading('class', text='类名')
        self.class_tree.heading('base', text='基类')
        self.class_tree.heading('bindings', text='已添加的 BindingSet')
        self.class_tree.heading('path', text='文件路径')
        self.class_tree.column('class', width=180)
        self.class_tree.column('base', width=120)
        self.class_tree.column('bindings', width=250)
        self.class_tree.column('path', width=300)
        
        # 滚动条
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.class_tree.yview)
        self.class_tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.class_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 双击打开文件
        self.class_tree.bind('<Double-1>', self._on_double_click)
        
        # 底部：状态和按钮
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.status_label = ttk.Label(bottom_frame, text="正在扫描...")
        self.status_label.pack(side=tk.LEFT)
        
        ttk.Button(bottom_frame, text="关闭", command=self.destroy).pack(side=tk.RIGHT, padx=5)
        ttk.Button(bottom_frame, text="移除 BindingSet", command=self._remove_binding_set).pack(side=tk.RIGHT, padx=5)
        ttk.Button(bottom_frame, text="✅ 添加 BindingSet", command=self._add_binding_set).pack(side=tk.RIGHT, padx=5)
    
    def _scan_classes(self):
        """扫描项目中的类"""
        self.status_label.config(text="正在扫描...")
        self.update()
        
        try:
            # 显示扫描路径
            scan_paths = self.scanner.search_paths
            path_info = ", ".join(str(p) for p in scan_paths)
            
            print(f"[DEBUG] Scanning paths: {scan_paths}")
            print(f"[DEBUG] Paths exist: {[p.exists() for p in scan_paths]}")
            
            self.classes = self.scanner.scan()
            print(f"[DEBUG] Found {len(self.classes)} classes")
            
            self._filter_classes()
            print(f"[DEBUG] Filtered to {len(self.filtered_classes)} classes")
            
            if self.classes:
                self.status_label.config(text=f"找到 {len(self.classes)} 个类（{len(self.filtered_classes)} 个显示）")
            else:
                # 检查扫描路径是否存在
                missing_paths = [str(p) for p in scan_paths if not p.exists()]
                if missing_paths:
                    self.status_label.config(text=f"⚠️ 未找到类。路径不存在: {missing_paths[0]}")
                else:
                    self.status_label.config(text=f"⚠️ 未找到匹配的类（扫描路径: {path_info}）")
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.status_label.config(text=f"❌ 扫描失败: {e}")
    
    def _filter_classes(self):
        """根据搜索和类型过滤"""
        search_text = self.search_var.get().lower()
        filter_type = self.filter_type.get()
        
        self.filtered_classes = []
        for cls in self.classes:
            # 搜索过滤
            if search_text:
                if search_text not in cls.class_name.lower() and \
                   search_text not in cls.base_class.lower() and \
                   search_text not in str(cls.file_path).lower():
                    continue
            
            # 类型过滤
            if filter_type == "AnimInstance" and not cls.is_anim_instance:
                continue
            elif filter_type == "Widget" and not cls.is_widget:
                continue
            elif filter_type == "Actor/Pawn" and not cls.is_actor:
                continue
            elif filter_type == "Component" and 'Component' not in cls.base_class:
                continue
            
            self.filtered_classes.append(cls)
        
        self._refresh_list()
    
    def _refresh_list(self):
        """刷新类列表"""
        self.class_tree.delete(*self.class_tree.get_children())
        
        for i, cls in enumerate(self.filtered_classes):
            bindings_str = ", ".join(cls.binding_sets) if cls.binding_sets else "(无)"
            
            # 高亮已添加当前 BindingSet 的类
            tags = ()
            if self.bindingset.name in cls.binding_sets:
                tags = ('has_binding',)
            
            self.class_tree.insert('', 'end', iid=str(i), values=(
                cls.class_name, cls.base_class, bindings_str, cls.relative_path
            ), tags=tags)
        
        # 设置高亮样式
        self.class_tree.tag_configure('has_binding', background='#d4edda')
    
    def _get_selected_class(self) -> Optional[UClassInfo]:
        """获取选中的类"""
        selection = self.class_tree.selection()
        if not selection:
            return None
        try:
            idx = int(selection[0])
            return self.filtered_classes[idx]
        except:
            return None
    
    def _add_binding_set(self):
        """添加 BindingSet 到选中的类"""
        cls = self._get_selected_class()
        if not cls:
            messagebox.showwarning("警告", "请先选择一个类")
            return
        
        success, message = BindingSetInjector.add_binding_set(cls, self.bindingset.name)
        
        if success:
            self.status_label.config(text=message)
            self._refresh_list()
            messagebox.showinfo("成功", message)
        else:
            messagebox.showwarning("警告", message)
    
    def _remove_binding_set(self):
        """从选中的类移除 BindingSet"""
        cls = self._get_selected_class()
        if not cls:
            messagebox.showwarning("警告", "请先选择一个类")
            return
        
        if self.bindingset.name not in cls.binding_sets:
            messagebox.showwarning("警告", f"该类未添加 BindingSet '{self.bindingset.name}'")
            return
        
        if not messagebox.askyesno("确认", f"确定从 {cls.class_name} 移除 BindingSet '{self.bindingset.name}'?"):
            return
        
        success, message = BindingSetInjector.remove_binding_set(cls, self.bindingset.name)
        
        if success:
            self.status_label.config(text=message)
            self._refresh_list()
            messagebox.showinfo("成功", message)
        else:
            messagebox.showwarning("警告", message)
    
    def _on_double_click(self, event):
        """双击打开文件"""
        cls = self._get_selected_class()
        if cls:
            import subprocess
            import os
            # 尝试用 VS Code 打开
            try:
                subprocess.Popen(['code', '-g', f'{cls.file_path}:{cls.line_number}'])
            except:
                # 回退到系统默认
                os.startfile(cls.file_path)


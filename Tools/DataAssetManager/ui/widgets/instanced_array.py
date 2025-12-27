#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 实例化数组控件
用于编辑 UE 中 Instanced 多态对象数组（如 GameFeature Actions）

注意：Actions 配置会保存到 JSON，需要在 UE 编辑器中手动配置到资产
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, List, Dict, Callable, Optional

from ui.widgets.base import PropertyWidget
from ui.widgets.action_schema import ACTION_PROPERTIES
from ui.widgets.action_item_editor import ActionEditorMixin
from core.schema import PropertyDef


class InstancedArrayEditorWidget(ActionEditorMixin, PropertyWidget):
    """
    实例化数组编辑器
    支持编辑每个 Action 的详细属性
    """
    
    def __init__(self, parent: tk.Widget, prop_def: PropertyDef,
                 available_types: Dict[str, Dict] = None,
                 schema_loader = None,
                 widget_factory = None,
                 on_change: Callable = None):
        self.available_types = available_types or {}
        self.schema_loader = schema_loader
        self.widget_factory = widget_factory
        self.items: List[Dict[str, Any]] = []
        self.expanded_items: Dict[int, bool] = {}
        self.nested_expanded: Dict[str, bool] = {}
        self.item_widgets: Dict[int, Dict] = {}
        super().__init__(parent, prop_def, on_change)
    
    # === UI 创建 ===
    
    def _create_widget(self):
        self.frame.columnconfigure(0, weight=1)
        self._create_header()
        self._create_list_container()
        self._create_hint()
    
    def _create_header(self):
        """创建标题栏"""
        header = ttk.Frame(self.frame)
        header.grid(row=0, column=0, sticky="ew", pady=2)
        header.columnconfigure(0, weight=1)
        
        self.count_label = ttk.Label(header, text=f"{self.prop_def.display_name} (0)")
        self.count_label.pack(side=tk.LEFT, padx=5)
        
        self.add_btn = ttk.Menubutton(header, text="➕ 添加 Action")
        self.add_menu = tk.Menu(self.add_btn, tearoff=0)
        self.add_btn["menu"] = self.add_menu
        
        for type_name, type_def in self.available_types.items():
            display_name = type_def.get("display_name", type_name)
            self.add_menu.add_command(
                label=display_name,
                command=lambda t=type_name: self._add_item(t)
            )
        self.add_btn.pack(side=tk.RIGHT, padx=5)
    
    def _create_list_container(self):
        """创建列表容器"""
        list_container = ttk.Frame(self.frame)
        list_container.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.frame.rowconfigure(1, weight=1)
        
        self.canvas = tk.Canvas(list_container, highlightthickness=0, height=350)
        scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=self.canvas.yview)
        
        self.list_frame = ttk.Frame(self.canvas)
        self.list_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.list_frame, anchor=tk.NW)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        
        self.list_frame.bind("<Enter>", lambda e: self._bind_mousewheel())
        self.list_frame.bind("<Leave>", lambda e: self._unbind_mousewheel())
        
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def _create_hint(self):
        """创建提示信息"""
        hint_label = ttk.Label(
            self.frame,
            text="⚠️ Actions 配置会保存到 JSON，需要在 UE 编辑器中手动配置到资产",
            foreground="#FF8C00",
            font=("", 9)
        )
        hint_label.grid(row=2, column=0, sticky="w", padx=5, pady=(5, 2))
    
    # === 事件处理 ===
    
    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)
    
    def _bind_mousewheel(self):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
    
    def _unbind_mousewheel(self):
        self.canvas.unbind_all("<MouseWheel>")
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    
    # === 列表操作 ===
    
    def _update_count(self):
        self.count_label.config(text=f"{self.prop_def.display_name} ({len(self.items)})")
    
    def _add_item(self, type_name: str):
        new_item = {"_type": type_name}
        action_def = ACTION_PROPERTIES.get(type_name, {})
        for prop_name, prop_def in action_def.get("properties", {}).items():
            if prop_def.get("type") == "array":
                new_item[prop_name] = []
        
        self.items.append(new_item)
        self.expanded_items[len(self.items) - 1] = True
        self._refresh_list()
        self._update_count()
        self._notify_change()
    
    def _remove_item(self, index: int):
        if index < len(self.items):
            self.items.pop(index)
            new_expanded = {}
            for i, expanded in self.expanded_items.items():
                if i < index:
                    new_expanded[i] = expanded
                elif i > index:
                    new_expanded[i - 1] = expanded
            self.expanded_items = new_expanded
            self._refresh_list()
            self._update_count()
            self._notify_change()
    
    def _move_item_up(self, index: int):
        if index > 0:
            self.items[index], self.items[index-1] = self.items[index-1], self.items[index]
            exp_cur = self.expanded_items.get(index, False)
            exp_prev = self.expanded_items.get(index-1, False)
            self.expanded_items[index] = exp_prev
            self.expanded_items[index-1] = exp_cur
            self._refresh_list()
            self._notify_change()
    
    def _move_item_down(self, index: int):
        if index < len(self.items) - 1:
            self.items[index], self.items[index+1] = self.items[index+1], self.items[index]
            exp_cur = self.expanded_items.get(index, False)
            exp_next = self.expanded_items.get(index+1, False)
            self.expanded_items[index] = exp_next
            self.expanded_items[index+1] = exp_cur
            self._refresh_list()
            self._notify_change()
    
    def _toggle_expand(self, index: int):
        self.expanded_items[index] = not self.expanded_items.get(index, False)
        self._refresh_list()
    
    def _refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        self.item_widgets.clear()
        
        if not self.items:
            ttk.Label(self.list_frame, text="(无 Action，点击上方按钮添加)", 
                     foreground="gray").pack(pady=20)
            return
        
        for i, item in enumerate(self.items):
            self._create_item_card(i, item)
    
    def _create_item_card(self, index: int, item: Dict):
        type_name = item.get("_type", "Unknown")
        action_def = ACTION_PROPERTIES.get(type_name, {})
        type_def = self.available_types.get(type_name, {})
        display_name = action_def.get("display_name", type_def.get("display_name", type_name))
        description = action_def.get("description", type_def.get("description", ""))
        is_expanded = self.expanded_items.get(index, False)
        
        card = ttk.LabelFrame(self.list_frame, text=f"[{index}] {display_name}")
        card.pack(fill=tk.X, pady=3, padx=2)
        
        header_frame = ttk.Frame(card)
        header_frame.pack(fill=tk.X, padx=5, pady=3)
        
        expand_text = "▼" if is_expanded else "▶"
        ttk.Button(header_frame, text=expand_text, width=2,
                   command=lambda idx=index: self._toggle_expand(idx)).pack(side=tk.LEFT, padx=(0, 5))
        
        ttk.Label(header_frame, text=description, foreground="gray",
                 wraplength=300).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        btn_frame = ttk.Frame(header_frame)
        btn_frame.pack(side=tk.RIGHT)
        ttk.Button(btn_frame, text="▲", width=2,
                  command=lambda idx=index: self._move_item_up(idx)).pack(side=tk.LEFT, padx=1)
        ttk.Button(btn_frame, text="▼", width=2,
                  command=lambda idx=index: self._move_item_down(idx)).pack(side=tk.LEFT, padx=1)
        ttk.Button(btn_frame, text="🗑️", width=3,
                  command=lambda idx=index: self._remove_item(idx)).pack(side=tk.LEFT, padx=1)
        
        if is_expanded:
            self._create_property_editors(card, index, item, action_def)
    
    # === 属性编辑器 ===
    
    def _create_property_editors(self, parent: ttk.Widget, index: int, item: Dict, action_def: Dict):
        properties = action_def.get("properties", {})
        if not properties:
            ttk.Label(parent, text="(此 Action 类型暂无可编辑属性)", 
                     foreground="gray").pack(padx=10, pady=5)
            return
        
        props_frame = ttk.Frame(parent)
        props_frame.pack(fill=tk.X, padx=10, pady=5)
        self.item_widgets[index] = {}
        
        for prop_name, prop_def in properties.items():
            self._create_single_property_editor(props_frame, index, item, prop_name, prop_def)
    
    def _create_single_property_editor(self, parent: ttk.Widget, index: int, 
                                       item: Dict, prop_name: str, prop_def: Dict):
        prop_type = prop_def.get("type", "string")
        display_name = prop_def.get("display_name", prop_name)
        
        prop_frame = ttk.LabelFrame(parent, text=display_name)
        prop_frame.pack(fill=tk.X, pady=3)
        
        if prop_type == "array":
            self._create_array_property_editor(prop_frame, index, item, prop_name, prop_def)
        else:
            self._create_simple_property_editor(prop_frame, index, item, prop_name, prop_def)
    
    def _create_array_property_editor(self, parent: ttk.Widget, index: int, 
                                      item: Dict, prop_name: str, prop_def: Dict):
        current_value = item.get(prop_name, [])
        
        header = ttk.Frame(parent)
        header.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(header, text=f"共 {len(current_value)} 项").pack(side=tk.LEFT)
        ttk.Button(header, text="➕", width=3,
                  command=lambda: self._add_array_item(index, prop_name, prop_def)).pack(side=tk.RIGHT)
        
        list_frame = ttk.Frame(parent)
        list_frame.pack(fill=tk.X, padx=5, pady=2)
        
        for arr_idx, arr_item in enumerate(current_value):
            self._create_array_item_row(list_frame, index, prop_name, arr_idx, arr_item, prop_def)
    
    def _create_array_item_row(self, parent: ttk.Widget, action_index: int, prop_name: str,
                               arr_idx: int, arr_item: Any, prop_def: Dict):
        item_schema = prop_def.get("item_schema", {})
        item_type = prop_def.get("item_type", "object")
        options_source = prop_def.get("options_source")
        is_complex = item_schema and len(item_schema) > 1
        
        if is_complex:
            self._create_complex_array_item(parent, action_index, prop_name, arr_idx, arr_item, item_schema)
        else:
            row = ttk.Frame(parent)
            row.pack(fill=tk.X, pady=2)
            row.columnconfigure(1, weight=1)
            
            ttk.Label(row, text=f"[{arr_idx}]", width=4).pack(side=tk.LEFT)
            
            if item_type == "asset" or item_schema:
                src = options_source
                if item_schema and len(item_schema) == 1:
                    src = list(item_schema.values())[0].get("options_source")
                options = self._get_options(src)
                
                combo = ttk.Combobox(row, values=options, width=50)
                if isinstance(arr_item, dict) and item_schema:
                    first_key = list(item_schema.keys())[0]
                    combo.set(arr_item.get(first_key, ""))
                else:
                    combo.set(str(arr_item) if arr_item else "")
                combo.pack(side=tk.LEFT, padx=8, fill=tk.X, expand=True)
                combo.bind("<<ComboboxSelected>>", 
                          lambda e, ai=action_index, pn=prop_name, ai2=arr_idx: 
                          self._on_array_item_change(ai, pn, ai2, e.widget.get(), prop_def))
                combo.bind("<FocusOut>",
                          lambda e, ai=action_index, pn=prop_name, ai2=arr_idx: 
                          self._on_array_item_change(ai, pn, ai2, e.widget.get(), prop_def))
            else:
                entry = ttk.Entry(row, width=55)
                entry.insert(0, str(arr_item) if arr_item else "")
                entry.pack(side=tk.LEFT, padx=8, fill=tk.X, expand=True)
            
            ttk.Button(row, text="✕", width=3,
                      command=lambda ai=action_index, pn=prop_name, ai2=arr_idx: 
                      self._remove_array_item(ai, pn, ai2)).pack(side=tk.RIGHT, padx=2)
    
    def _create_complex_array_item(self, parent: ttk.Widget, action_index: int, 
                                   prop_name: str, arr_idx: int, arr_item: Dict, item_schema: Dict):
        if not isinstance(arr_item, dict):
            arr_item = {}
        
        expand_key = f"{action_index}_{prop_name}_{arr_idx}"
        is_expanded = self.nested_expanded.get(expand_key, True)
        preview = self._get_complex_item_preview(arr_item, item_schema)
        
        card = ttk.Frame(parent, relief="groove", borderwidth=1)
        card.pack(fill=tk.X, pady=4, padx=0)
        card.columnconfigure(0, weight=1)
        
        header = ttk.Frame(card)
        header.pack(fill=tk.X, padx=8, pady=4)
        
        expand_text = "▼" if is_expanded else "▶"
        ttk.Button(header, text=expand_text, width=2,
                   command=lambda ek=expand_key: self._toggle_nested_expand(ek)).pack(side=tk.LEFT)
        ttk.Label(header, text=f"[{arr_idx}]", font=("", 9, "bold")).pack(side=tk.LEFT, padx=(8, 15))
        
        if not is_expanded:
            ttk.Label(header, text=preview, foreground="gray").pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        ttk.Button(header, text="🗑️", width=3,
                  command=lambda ai=action_index, pn=prop_name, ai2=arr_idx: 
                  self._remove_array_item(ai, pn, ai2)).pack(side=tk.RIGHT, padx=2)
        
        if is_expanded:
            fields_frame = ttk.Frame(card)
            fields_frame.pack(fill=tk.X, padx=15, pady=(0, 10))
            fields_frame.columnconfigure(1, weight=1)
            
            row = 0
            for field_name, field_def in item_schema.items():
                self._create_nested_field_editor_grid(
                    fields_frame, row, action_index, prop_name, arr_idx, 
                    arr_item, field_name, field_def
                )
                row += 1
    
    def _get_complex_item_preview(self, arr_item: Dict, item_schema: Dict) -> str:
        if not arr_item:
            return "(未配置)"
        parts = []
        for key in list(item_schema.keys())[:2]:
            val = arr_item.get(key, "")
            if val:
                if isinstance(val, list):
                    parts.append(f"{len(val)}项")
                else:
                    str_val = str(val)
                    if "/" in str_val:
                        str_val = str_val.split("/")[-1].split(".")[0]
                    if len(str_val) > 20:
                        str_val = str_val[:20] + "..."
                    parts.append(str_val)
        return " | ".join(parts) if parts else "(未配置)"
    
    def _toggle_nested_expand(self, expand_key: str):
        self.nested_expanded[expand_key] = not self.nested_expanded.get(expand_key, True)
        self._refresh_list()
    
    def _create_simple_property_editor(self, parent: ttk.Widget, index: int,
                                       item: Dict, prop_name: str, prop_def: Dict):
        prop_type = prop_def.get("type", "string")
        options_source = prop_def.get("options_source")
        current_value = item.get(prop_name, "")
        
        inner_frame = ttk.Frame(parent)
        inner_frame.pack(fill=tk.X, padx=5, pady=2)
        
        if options_source:
            options = self._get_options(options_source)
            widget = ttk.Combobox(inner_frame, values=options, width=50)
            widget.set(current_value)
            widget.pack(fill=tk.X, expand=True)
            widget.bind("<<ComboboxSelected>>", 
                       lambda e, i=index, pn=prop_name: self._on_property_change(i, pn, e.widget.get()))
        elif prop_type == "integer":
            widget = ttk.Spinbox(inner_frame, from_=-9999, to=9999, width=10)
            widget.set(current_value if current_value else 0)
            widget.pack(side=tk.LEFT)
            widget.bind("<FocusOut>",
                       lambda e, i=index, pn=prop_name: self._on_property_change(i, pn, int(e.widget.get())))
        else:
            widget = ttk.Entry(inner_frame, width=50)
            widget.insert(0, str(current_value) if current_value else "")
            widget.pack(fill=tk.X, expand=True)
            widget.bind("<FocusOut>",
                       lambda e, i=index, pn=prop_name: self._on_property_change(i, pn, e.widget.get()))
    
    # === 选项与路径转换 ===
    
    def _get_options(self, options_source: Optional[str]) -> List[str]:
        if not options_source:
            return []
        if self.widget_factory:
            try:
                return self.widget_factory._get_options_from_source(options_source)
            except:
                pass
        return []
    
    def _get_options_with_paths(self, options_source: Optional[str]) -> Dict[str, str]:
        if not options_source:
            return {}
        
        if self.widget_factory and hasattr(self.widget_factory, 'options_scanner'):
            scanner = self.widget_factory.options_scanner
            if scanner:
                method_map = {
                    "pawn_classes": "get_pawn_class_options",
                    "gameplay_abilities": "get_gameplay_ability_options",
                    "attribute_sets": "get_attribute_set_options",
                    "ability_sets": "get_ability_set_options",
                    "input_configs": "get_input_config_options",
                    "input_mapping_contexts": "get_input_mapping_context_options",
                    "widget_classes": "get_widget_class_options",
                    "activatable_widgets": "get_activatable_widget_options",
                    "ui_layer_tags": "get_ui_layer_tag_options",
                    "ui_slot_tags": "get_ui_slot_tag_options",
                }
                method_name = method_map.get(options_source)
                if method_name and hasattr(scanner, method_name):
                    items = getattr(scanner, method_name)()
                    return {item.get("display_name", item["name"]): item["name"] for item in items}
        return {}
    
    def _display_to_path(self, display_name: str, options_source: Optional[str]) -> str:
        if not display_name or not options_source:
            return display_name
        mapping = self._get_options_with_paths(options_source)
        return mapping.get(display_name, display_name)
    
    def _path_to_display(self, path: str, options_source: Optional[str]) -> str:
        if not path or not options_source:
            return path
        mapping = self._get_options_with_paths(options_source)
        for display, asset_path in mapping.items():
            if asset_path == path:
                return display
        if "/" in path:
            name = path.split("/")[-1]
            if "." in name:
                name = name.split(".")[0]
            return name
        return path
    
    # === 回调方法 ===
    
    def _on_property_change(self, action_index: int, prop_name: str, value: Any):
        if action_index < len(self.items):
            self.items[action_index][prop_name] = value
            self._notify_change()
    
    def _on_array_item_change(self, action_index: int, prop_name: str, 
                              arr_index: int, value: Any, prop_def: Dict):
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_index < len(arr):
                item_schema = prop_def.get("item_schema", {})
                item_type = prop_def.get("item_type", "object")
                
                if item_type == "asset":
                    arr[arr_index] = value
                elif item_schema and len(item_schema) == 1:
                    first_key = list(item_schema.keys())[0]
                    if isinstance(arr[arr_index], dict):
                        arr[arr_index][first_key] = value
                    else:
                        arr[arr_index] = {first_key: value}
                else:
                    arr[arr_index] = value
                self.items[action_index][prop_name] = arr
                self._notify_change()
    
    def _add_array_item(self, action_index: int, prop_name: str, prop_def: Dict):
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            item_schema = prop_def.get("item_schema", {})
            item_type = prop_def.get("item_type", "object")
            
            if item_type == "asset":
                arr.append("")
            elif item_schema:
                arr.append(self._create_default_struct(item_schema))
            else:
                arr.append("")
            
            self.items[action_index][prop_name] = arr
            new_idx = len(arr) - 1
            expand_key = f"{action_index}_{prop_name}_{new_idx}"
            self.nested_expanded[expand_key] = True
            self._refresh_list()
            self._notify_change()
    
    def _create_default_struct(self, schema: Dict) -> Dict:
        result = {}
        for key, key_def in schema.items():
            key_type = key_def.get("type", "string")
            if key_type == "array":
                result[key] = []
            elif key_type == "integer":
                result[key] = key_def.get("default", 0)
            else:
                result[key] = key_def.get("default", "")
        return result
    
    def _remove_array_item(self, action_index: int, prop_name: str, arr_index: int):
        if action_index < len(self.items):
            arr = self.items[action_index].get(prop_name, [])
            if arr_index < len(arr):
                arr.pop(arr_index)
                self.items[action_index][prop_name] = arr
                self._refresh_list()
                self._notify_change()
    
    # === 值获取/设置 ===
    
    def get_value(self) -> List[Dict[str, Any]]:
        return self._normalize_items_for_save(self.items.copy())
    
    def _normalize_items_for_save(self, items: List[Dict]) -> List[Dict]:
        normalized = []
        for item in items:
            normalized_item = {"_type": item.get("_type", "")}
            type_name = item.get("_type", "")
            action_def = ACTION_PROPERTIES.get(type_name, {})
            
            for prop_name, prop_def in action_def.get("properties", {}).items():
                if prop_name in item:
                    normalized_item[prop_name] = self._normalize_property(item[prop_name], prop_def)
            normalized.append(normalized_item)
        return normalized
    
    def _normalize_property(self, value: Any, prop_def: Dict) -> Any:
        prop_type = prop_def.get("type", "string")
        options_source = prop_def.get("options_source")
        
        if prop_type == "array":
            item_schema = prop_def.get("item_schema", {})
            item_type = prop_def.get("item_type", "object")
            item_options = prop_def.get("options_source")
            
            if isinstance(value, list):
                normalized_list = []
                for arr_item in value:
                    if item_schema:
                        normalized_obj = {}
                        for field_name, field_def in item_schema.items():
                            if isinstance(arr_item, dict) and field_name in arr_item:
                                normalized_obj[field_name] = self._normalize_property(
                                    arr_item[field_name], field_def)
                        normalized_list.append(normalized_obj)
                    elif item_type == "asset" and item_options:
                        normalized_list.append(self._display_to_path(str(arr_item), item_options))
                    else:
                        normalized_list.append(arr_item)
                return normalized_list
        elif options_source or prop_type in ("class", "asset", "tag"):
            return self._display_to_path(str(value), options_source) if value else ""
        return value
    
    def set_value(self, value: Any):
        self.items = list(value) if value else []
        self.expanded_items = {i: False for i in range(len(self.items))}
        self._refresh_list()
        self._update_count()
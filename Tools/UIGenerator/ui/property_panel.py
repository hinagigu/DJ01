#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - Property Editing Panels
"""

import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, List, Callable, Dict, Any

from .schema_models import ComponentData, PropertyData, WidgetSchema
from .editor_dialogs import PropertyEditDialog


class BindingSetManager:
    """Manages BindingSet definitions from project"""
    
    _instance = None
    
    @classmethod
    def get_instance(cls) -> 'BindingSetManager':
        if cls._instance is None:
            cls._instance = BindingSetManager()
        return cls._instance
    
    def __init__(self):
        self._binding_sets: Dict[str, Any] = {}
        self._load_binding_sets()
    
    def _load_binding_sets(self):
        """Load BindingSet definitions from project"""
        # Find project root: ui/ -> UIGenerator/ -> Tools/ -> ProjectRoot/
        current_dir = os.path.dirname(os.path.abspath(__file__))  # ui/
        ui_generator_dir = os.path.dirname(current_dir)           # UIGenerator/
        tools_dir = os.path.dirname(ui_generator_dir)             # Tools/
        project_root = os.path.dirname(tools_dir)                 # DJ01/
        
        config_path = os.path.join(
            project_root,
            "Source", "DJ01", "AbilitySystem", "Attributes", 
            "BindingSets", "Config", "BindingSetDefinitions.json"
        )
        
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                for bs in data.get("BindingSets", []):
                    name = bs.get("Name", "")
                    if name:
                        self._binding_sets[name] = bs
                
                print(f"[BindingSetManager] Loaded {len(self._binding_sets)} BindingSets")
            except Exception as e:
                print(f"[BindingSetManager] Failed to load: {e}")
        else:
            print(f"[BindingSetManager] Config not found: {config_path}")
    
    def get_binding_set_names(self) -> List[str]:
        """Get list of available BindingSet names"""
        return list(self._binding_sets.keys())
    
    def get_binding_set(self, name: str) -> Optional[Dict]:
        """Get BindingSet definition by name"""
        return self._binding_sets.get(name)
    
    def get_available_bindings(self, binding_set_name: str) -> List[str]:
        """Get available binding variable names for a BindingSet
        
        Returns list like: ['CurrentHealth', 'MaxHealth', 'PercentHealth', 'CurrentMana', 'MaxMana', 'PercentMana']
        """
        bs = self._binding_sets.get(binding_set_name)
        if not bs:
            return []
        
        bindings = []
        
        # Process attribute bindings
        for attr in bs.get("AttributeBindings", []):
            var_name = attr.get("VariableName", attr.get("AttributeName", ""))
            value_types = attr.get("ValueTypes", ["Current"])
            
            for vt in value_types:
                # Generate variable name: {ValueType}{VariableName}
                # e.g., Current + Health = CurrentHealth, Percent + Health = PercentHealth
                bindings.append(f"{vt}{var_name}")
        
        # Process tag bindings
        for tag in bs.get("TagBindings", []):
            var_name = tag.get("VariableName", "")
            if var_name:
                bindings.append(var_name)
        
        return bindings


class ComponentPropertyPanel(ttk.LabelFrame):
    """Component property editor panel - Single column layout with BindingSet support"""
    
    def __init__(self, parent, component_types: List[str]):
        super().__init__(parent, text="Component Properties", padding="10")
        
        self.component_types = component_types
        self.current_component: Optional[ComponentData] = None
        self.current_binding_set: Optional[str] = None  # Current schema's binding set
        
        # Get BindingSet manager
        self.binding_manager = BindingSetManager.get_instance()
        
        # Callback
        self.on_apply: Optional[Callable[[ComponentData], None]] = None
        
        self._create_ui()
        self._set_state(False)
    
    def set_binding_set(self, binding_set_name: Optional[str]):
        """Set the current BindingSet for property binding dropdowns"""
        self.current_binding_set = binding_set_name
        self._update_binding_options()
    
    def _update_binding_options(self):
        """Update binding combobox options based on current BindingSet"""
        if self.current_binding_set:
            bindings = self.binding_manager.get_available_bindings(self.current_binding_set)
            # Add empty option at start
            options = [""] + bindings
        else:
            options = [""]
        
        self.bind_percent_combo['values'] = options
        self.bind_text_combo['values'] = options
        self.bind_image_combo['values'] = options
    
    def _create_ui(self):
        """Create UI with single column grid layout"""
        # Configure grid
        self.columnconfigure(1, weight=1)
        
        row = 0
        
        # Name
        ttk.Label(self, text="Name:", anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self, textvariable=self.name_var)
        self.name_entry.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        row += 1
        
        # Type
        ttk.Label(self, text="Type:", anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(self, textvariable=self.type_var, 
                                       values=self.component_types, state='readonly')
        self.type_combo.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        row += 1
        
        # Comment
        ttk.Label(self, text="Comment:", anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.comment_var = tk.StringVar()
        self.comment_entry = ttk.Entry(self, textvariable=self.comment_var)
        self.comment_entry.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        row += 1
        
        # Optional checkbox
        self.optional_var = tk.BooleanVar()
        self.optional_check = ttk.Checkbutton(self, text="Optional (BindWidgetOptional)", 
                                              variable=self.optional_var)
        self.optional_check.grid(row=row, column=0, columnspan=2, sticky=tk.W, pady=3)
        row += 1
        
        # Separator
        ttk.Separator(self, orient=tk.HORIZONTAL).grid(row=row, column=0, columnspan=2, sticky=tk.EW, pady=8)
        row += 1
        
        # Binding properties section with BindingSet indicator
        self.binding_header_var = tk.StringVar(value="Property Bindings:")
        ttk.Label(self, textvariable=self.binding_header_var, font=("", 9, "bold")).grid(
            row=row, column=0, columnspan=2, sticky=tk.W, pady=(0, 5))
        row += 1
        
        # Bind Percent (Combobox instead of Entry)
        ttk.Label(self, text="Percent:", anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=2)
        self.bind_percent_var = tk.StringVar()
        self.bind_percent_combo = ttk.Combobox(self, textvariable=self.bind_percent_var)
        self.bind_percent_combo.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=2)
        row += 1
        
        # Bind Text (Combobox)
        ttk.Label(self, text="Text:", anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=2)
        self.bind_text_var = tk.StringVar()
        self.bind_text_combo = ttk.Combobox(self, textvariable=self.bind_text_var)
        self.bind_text_combo.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=2)
        row += 1
        
        # Bind Image (Combobox)
        ttk.Label(self, text="Image:", anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=2)
        self.bind_image_var = tk.StringVar()
        self.bind_image_combo = ttk.Combobox(self, textvariable=self.bind_image_var)
        self.bind_image_combo.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=2)
        row += 1
        
        # Apply button
        self.apply_btn = ttk.Button(self, text="Apply Changes", command=self._apply_changes)
        self.apply_btn.grid(row=row, column=0, columnspan=2, sticky=tk.E, pady=(10, 0))
        
        # Initialize with empty options
        self._update_binding_options()
    
    def _set_state(self, enabled: bool):
        """Set control states"""
        state = tk.NORMAL if enabled else tk.DISABLED
        
        self.name_entry.config(state=state)
        self.type_combo.config(state='readonly' if enabled else tk.DISABLED)
        self.comment_entry.config(state=state)
        self.optional_check.config(state=state)
        self.bind_percent_combo.config(state=state)
        self.bind_text_combo.config(state=state)
        self.bind_image_combo.config(state=state)
        self.apply_btn.config(state=state)
        
        # Update binding header to show current BindingSet
        if self.current_binding_set:
            self.binding_header_var.set(f"Property Bindings: [{self.current_binding_set}]")
        else:
            self.binding_header_var.set("Property Bindings: (Select BindingSet)")
    
    def set_component(self, comp: Optional[ComponentData]):
        """Set the component to edit"""
        self.current_component = comp
        
        if not comp:
            self._clear()
            self._set_state(False)
            return
        
        self.name_var.set(comp.name)
        self.type_var.set(comp.type)
        self.comment_var.set(comp.comment or "")
        self.optional_var.set(comp.optional)
        
        # Handle bindings - check both old style (bind_xxx) and new style (bindings dict)
        if hasattr(comp, 'bindings') and comp.bindings:
            self.bind_percent_var.set(comp.bindings.get('percent', ''))
            self.bind_text_var.set(comp.bindings.get('text', ''))
            self.bind_image_var.set(comp.bindings.get('image', ''))
        else:
            self.bind_percent_var.set(getattr(comp, 'bind_percent', '') or '')
            self.bind_text_var.set(getattr(comp, 'bind_text', '') or '')
            self.bind_image_var.set(getattr(comp, 'bind_image', '') or '')
        
        self._set_state(True)
    
    def _clear(self):
        """Clear all fields"""
        self.name_var.set("")
        self.type_var.set("")
        self.comment_var.set("")
        self.optional_var.set(False)
        self.bind_percent_var.set("")
        self.bind_text_var.set("")
        self.bind_image_var.set("")
    
    def _apply_changes(self):
        """Apply changes to component"""
        if not self.current_component:
            return
        
        name = self.name_var.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Component name cannot be empty")
            return
        
        self.current_component.name = name
        self.current_component.type = self.type_var.get()
        self.current_component.comment = self.comment_var.get()
        self.current_component.optional = self.optional_var.get()
        
        # Store bindings in both formats for compatibility
        percent = self.bind_percent_var.get()
        text = self.bind_text_var.get()
        image = self.bind_image_var.get()
        
        # New style bindings dict
        bindings = {}
        if percent:
            bindings['percent'] = percent
        if text:
            bindings['text'] = text
        if image:
            bindings['image'] = image
        
        self.current_component.bindings = bindings if bindings else None
        
        # Old style for compatibility
        self.current_component.bind_percent = percent
        self.current_component.bind_text = text
        self.current_component.bind_image = image
        
        if self.on_apply:
            self.on_apply(self.current_component)


class CustomPropertyPanel(ttk.LabelFrame):
    """Custom properties panel"""
    
    def __init__(self, parent):
        super().__init__(parent, text="Custom Properties", padding="5")
        
        self.schema: Optional[WidgetSchema] = None
        
        # Callback
        self.on_changed: Optional[Callable[[], None]] = None
        
        self._create_ui()
    
    def _create_ui(self):
        """Create UI"""
        # Toolbar
        toolbar = ttk.Frame(self)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Button(toolbar, text="+ Add", command=self._add_property).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="- Remove", command=self._delete_property).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Edit", command=self._edit_property).pack(side=tk.LEFT, padx=2)
        
        # Properties table - simpler columns for single column view
        columns = ('name', 'type', 'default')
        self.tree = ttk.Treeview(self, columns=columns, show='headings', height=8)
        self.tree.heading('name', text='Name')
        self.tree.heading('type', text='Type')
        self.tree.heading('default', text='Default')
        self.tree.column('name', width=120, minwidth=80)
        self.tree.column('type', width=80, minwidth=60)
        self.tree.column('default', width=80, minwidth=60)
        
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Double click to edit
        self.tree.bind('<Double-1>', self._on_double_click)
        
        # Description display
        self.desc_var = tk.StringVar(value="")
        desc_label = ttk.Label(self, textvariable=self.desc_var, foreground="gray", wraplength=300)
        desc_label.pack(fill=tk.X, pady=(5, 0))
        
        # Show description on select
        self.tree.bind('<<TreeviewSelect>>', self._on_select)
    
    def set_schema(self, schema: Optional[WidgetSchema]):
        """设置 Schema"""
        self.schema = schema
        self.refresh()
    
    def refresh(self):
        """Refresh list"""
        self.tree.delete(*self.tree.get_children())
        self.desc_var.set("")
        
        if not self.schema:
            return
        
        for prop in self.schema.properties:
            self.tree.insert('', 'end', values=(
                prop.name, prop.type,
                str(prop.default) if prop.default is not None else ""
            ))
    
    def _on_select(self, event):
        """Show description when selected"""
        selection = self.tree.selection()
        if not selection or not self.schema:
            self.desc_var.set("")
            return
        
        index = self.tree.index(selection[0])
        if 0 <= index < len(self.schema.properties):
            prop = self.schema.properties[index]
            desc = prop.description or "(No description)"
            category = f"[{prop.category}] " if prop.category else ""
            self.desc_var.set(f"{category}{desc}")
    
    def _notify_changed(self):
        """Notify change"""
        if self.on_changed:
            self.on_changed()
    
    def _add_property(self):
        """Add property"""
        if not self.schema:
            return
        
        dialog = PropertyEditDialog(self.winfo_toplevel())
        self.winfo_toplevel().wait_window(dialog)
        
        if dialog.result:
            prop = PropertyData(**dialog.result)
            self.schema.properties.append(prop)
            self.refresh()
            self._notify_changed()
    
    def _delete_property(self):
        """Delete property"""
        selection = self.tree.selection()
        if not selection or not self.schema:
            return
        
        index = self.tree.index(selection[0])
        if 0 <= index < len(self.schema.properties):
            prop_name = self.schema.properties[index].name
            if messagebox.askyesno("Confirm", f"Delete property '{prop_name}'?"):
                del self.schema.properties[index]
                self.refresh()
                self._notify_changed()
    
    def _edit_property(self):
        """Edit selected property"""
        selection = self.tree.selection()
        if not selection or not self.schema:
            return
        self._do_edit(self.tree.index(selection[0]))
    
    def _on_double_click(self, event):
        """Double click to edit"""
        selection = self.tree.selection()
        if not selection or not self.schema:
            return
        self._do_edit(self.tree.index(selection[0]))
    
    def _do_edit(self, index: int):
        """Edit property at index"""
        if 0 <= index < len(self.schema.properties):
            prop = self.schema.properties[index]
            
            dialog = PropertyEditDialog(self.winfo_toplevel(), prop)
            self.winfo_toplevel().wait_window(dialog)
            
            if dialog.result:
                self.schema.properties[index] = PropertyData(**dialog.result)
                self.refresh()
                self._notify_changed()
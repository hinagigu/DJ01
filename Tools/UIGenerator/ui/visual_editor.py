#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - Visual Schema Editor (Main Component)
"""

import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from typing import Optional, Callable
from pathlib import Path

from .schema_models import WidgetSchema, ComponentData
from .component_tree import ComponentTreePanel
from .property_panel import ComponentPropertyPanel, CustomPropertyPanel, BindingSetManager


class VisualSchemaEditor(ttk.Frame):
    """Visual Schema Editor"""
    
    PARENT_CLASSES = [
        "UserWidget",
        "CommonUserWidget", 
        "CommonActivatableWidget",
        "CommonActivatableStackWidget"
    ]
    
    def __init__(self, parent, schemas_dir: str):
        super().__init__(parent)
        
        self.schemas_dir = schemas_dir
        self.current_schema: Optional[WidgetSchema] = None
        self.current_file_path: Optional[str] = None
        self._modified = False
        
        self._load_widget_types()
        
        self.on_schema_changed: Optional[Callable[[dict], None]] = None
        self.on_save: Optional[Callable[[str, dict], None]] = None
        
        self._create_ui()
    
    def _load_widget_types(self):
        """Load widget types config"""
        try:
            config_path = Path(__file__).parent.parent / "configs" / "widget_types.json"
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    self.widget_types = json.load(f)
            else:
                self.widget_types = {"types": {}}
        except Exception as e:
            print(f"Failed to load widget types: {e}")
            self.widget_types = {"types": {}}
        
        self.component_types = list(self.widget_types.get("types", {}).keys())
        if not self.component_types:
            self.component_types = [
                "CanvasPanel", "HorizontalBox", "VerticalBox", "Overlay",
                "SizeBox", "Border", "ScaleBox",
                "TextBlock", "RichTextBlock", "Image", "ProgressBar",
                "Button", "CheckBox", "ComboBoxString", "EditableText",
                "Slider", "SpinBox"
            ]
    
    def _create_ui(self):
        """Create UI with improved layout"""
        main_paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True)
        
        # Left panel
        left_frame = ttk.Frame(main_paned, width=500)
        main_paned.add(left_frame, weight=2)
        
        self._create_basic_info_panel(left_frame)
        
        # Component tree
        self.component_tree = ComponentTreePanel(left_frame, self.widget_types, self.component_types)
        self.component_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.component_tree.on_select = self._on_component_select
        self.component_tree.on_changed = self._on_tree_changed
        
        # Right panel
        right_frame = ttk.Frame(main_paned, width=400)
        main_paned.add(right_frame, weight=1)
        
        # Component properties
        self.comp_property_panel = ComponentPropertyPanel(right_frame, self.component_types)
        self.comp_property_panel.pack(fill=tk.X, padx=5, pady=5)
        self.comp_property_panel.on_apply = self._on_component_apply
        
        # Custom properties
        self.custom_property_panel = CustomPropertyPanel(right_frame)
        self.custom_property_panel.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.custom_property_panel.on_changed = self._on_property_changed
    
    def _create_basic_info_panel(self, parent):
        """Create basic info panel using vertical layout"""
        frame = ttk.LabelFrame(parent, text="Widget Info", padding="8")
        frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Configure grid - single column expands
        frame.columnconfigure(1, weight=1)
        
        row = 0
        
        # Row 0: Name
        ttk.Label(frame, text="Name:", width=12, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.name_var = tk.StringVar()
        self.name_var.trace('w', lambda *args: self._on_basic_info_changed())
        ttk.Entry(frame, textvariable=self.name_var).grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        row += 1
        
        # Row 1: Parent Class
        ttk.Label(frame, text="Parent Class:", width=12, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.parent_class_var = tk.StringVar(value="CommonUserWidget")
        parent_combo = ttk.Combobox(frame, textvariable=self.parent_class_var, 
                                    values=self.PARENT_CLASSES, state='readonly')
        parent_combo.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        parent_combo.bind('<<ComboboxSelected>>', lambda e: self._on_basic_info_changed())
        row += 1
        
        # Row 2: BindingSet
        ttk.Label(frame, text="BindingSet:", width=12, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.binding_set_var = tk.StringVar(value="")
        
        # Get available binding sets from manager
        self.binding_manager = BindingSetManager.get_instance()
        binding_set_names = ["(None)"] + self.binding_manager.get_binding_set_names()
        print(f"[VisualEditor] Available BindingSets: {binding_set_names}")
        
        self.binding_set_combo = ttk.Combobox(frame, textvariable=self.binding_set_var,
                                              values=binding_set_names, state='readonly')
        self.binding_set_combo.grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        self.binding_set_combo.bind('<<ComboboxSelected>>', self._on_binding_set_changed)
        row += 1
        
        # Row 3: Description
        ttk.Label(frame, text="Description:", width=12, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.desc_var = tk.StringVar()
        self.desc_var.trace('w', lambda *args: self._on_basic_info_changed())
        ttk.Entry(frame, textvariable=self.desc_var).grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        row += 1
        
        # Row 4: C++ Output Path
        ttk.Label(frame, text="C++ Path:", width=12, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.output_path_var = tk.StringVar(value="Source/DJ01/UI/Generated")
        self.output_path_var.trace('w', lambda *args: self._on_basic_info_changed())
        ttk.Entry(frame, textvariable=self.output_path_var).grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
        row += 1
        
        # Row 5: Blueprint Path
        ttk.Label(frame, text="BP Path:", width=12, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=3)
        self.bp_path_var = tk.StringVar(value="/Game/UI/Generated")
        self.bp_path_var.trace('w', lambda *args: self._on_basic_info_changed())
        ttk.Entry(frame, textvariable=self.bp_path_var).grid(row=row, column=1, sticky=tk.EW, padx=(5, 0), pady=3)
    
    # ========== Data Operations ==========
    
    def load_schema(self, file_path: str) -> bool:
        """Load schema file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.current_schema = WidgetSchema.from_dict(data)
            self.current_file_path = file_path
            self._modified = False
            
            self._update_ui_from_schema()
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Load failed: {e}")
            return False
    
    def load_template(self):
        """Load blank template"""
        self.current_schema = WidgetSchema.create_template()
        self.current_file_path = None
        self._modified = False
        self._update_ui_from_schema()
    
    def get_schema(self) -> Optional[dict]:
        """Get current schema"""
        if self.current_schema:
            return self.current_schema.to_dict()
        return None
    
    def save_schema(self, file_path: Optional[str] = None) -> bool:
        """Save schema"""
        if not self.current_schema:
            return False
        
        if not file_path:
            file_path = self.current_file_path
        
        if not file_path:
            name = simpledialog.askstring("Save", "Enter filename (without extension):")
            if not name:
                return False
            file_path = os.path.join(self.schemas_dir, f"{name}.json")
        
        try:
            data = self.current_schema.to_dict()
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            self.current_file_path = file_path
            self._modified = False
            
            if self.on_save:
                self.on_save(file_path, data)
            
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {e}")
            return False
    
    def _update_ui_from_schema(self):
        """Update UI from schema"""
        if not self.current_schema:
            return
        
        self.name_var.set(self.current_schema.name)
        self.parent_class_var.set(self.current_schema.parent_class)
        self.desc_var.set(self.current_schema.description)
        self.output_path_var.set(self.current_schema.output_path)
        self.bp_path_var.set(self.current_schema.blueprint_path)
        
        # Load BindingSet
        binding_set_name = ""
        if self.current_schema.binding_set:
            binding_set_name = self.current_schema.binding_set.get("name", "")
        
        # Set combo value (use "(None)" if empty)
        self.binding_set_var.set(binding_set_name if binding_set_name else "(None)")
        self.comp_property_panel.set_binding_set(binding_set_name if binding_set_name else None)
        
        print(f"[VisualEditor] Loaded BindingSet: '{binding_set_name}'")
        
        self.component_tree.set_schema(self.current_schema)
        self.custom_property_panel.set_schema(self.current_schema)
        self.comp_property_panel.set_component(None)
    
    # ========== Callbacks ==========
    
    def _on_binding_set_changed(self, event=None):
        """BindingSet selection changed"""
        binding_set_name = self.binding_set_var.get()
        
        # Handle "(None)" selection
        if binding_set_name == "(None)" or not binding_set_name:
            binding_set_name = ""
        
        print(f"[VisualEditor] BindingSet changed to: '{binding_set_name}'")
        
        # Update property panel with available bindings
        self.comp_property_panel.set_binding_set(binding_set_name if binding_set_name else None)
        
        # Update schema
        if self.current_schema:
            if binding_set_name:
                # Create or update binding_set in schema
                if not self.current_schema.binding_set:
                    self.current_schema.binding_set = {"name": binding_set_name, "component_bindings": []}
                else:
                    self.current_schema.binding_set["name"] = binding_set_name
            else:
                self.current_schema.binding_set = {}
            
            self._modified = True
            self._notify_schema_changed()
    
    def _on_basic_info_changed(self):
        """Basic info changed"""
        if not self.current_schema:
            return
        
        self.current_schema.name = self.name_var.get()
        self.current_schema.description = self.desc_var.get()
        self.current_schema.parent_class = self.parent_class_var.get()
        self.current_schema.output_path = self.output_path_var.get()
        self.current_schema.blueprint_path = self.bp_path_var.get()
        
        self._modified = True
        self._notify_schema_changed()
    
    def _on_component_select(self, comp: ComponentData):
        """Component selected"""
        self.comp_property_panel.set_component(comp)
    
    def _on_component_apply(self, comp: ComponentData):
        """Component properties applied"""
        self._modified = True
        self.component_tree.refresh()
        self._notify_schema_changed()
    
    def _on_tree_changed(self):
        """Component tree changed"""
        self._modified = True
        self._notify_schema_changed()
    
    def _on_property_changed(self):
        """Custom property changed"""
        self._modified = True
        self._notify_schema_changed()
    
    def _notify_schema_changed(self):
        """Notify schema changed"""
        if self.on_schema_changed and self.current_schema:
            self.on_schema_changed(self.current_schema.to_dict())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - UI 模块
"""

from .app import UIGeneratorApp
from .panels import FlowPanel, SchemaListPanel, EditorPanel, OutputPanel
from .dialogs import CompileReminderDialog, EngineSelectDialog, ManualCompileDialog
from .schema_models import WidgetSchema, ComponentData, PropertyData
from .editor_dialogs import ComponentTypeDialog, PropertyEditDialog
from .component_tree import ComponentTreePanel
from .property_panel import ComponentPropertyPanel, CustomPropertyPanel
from .visual_editor import VisualSchemaEditor

__all__ = [
    # 主应用
    'UIGeneratorApp',
    
    # 面板组件
    'FlowPanel',
    'SchemaListPanel', 
    'EditorPanel',
    'OutputPanel',
    
    # 对话框
    'CompileReminderDialog',
    'EngineSelectDialog',
    'ManualCompileDialog',
    'ComponentTypeDialog',
    'PropertyEditDialog',
    
    # 数据模型
    'WidgetSchema',
    'ComponentData', 
    'PropertyData',
    
    # 可视化编辑器组件
    'ComponentTreePanel',
    'ComponentPropertyPanel',
    'CustomPropertyPanel',
    'VisualSchemaEditor'
]
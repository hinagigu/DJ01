"""
UI Generator 主应用
"""
import os
import json
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, scrolledtext
from typing import Optional
from datetime import datetime

from utils.paths import paths
from utils.logger import Logger
from core.state_manager import StateManager, GenerationStage
from core.schema_validator import SchemaValidator, load_and_validate
from core.cpp_generator import CppGenerator
from core.ue_compiler import UECompiler, UECommandSender

from ui.panels import FlowPanel, SchemaListPanel, EditorPanel
from ui.dialogs import CompileReminderDialog, EngineSelectDialog, ManualCompileDialog, NewSchemaDialog
from ui.visual_editor import VisualSchemaEditor


class UIGeneratorApp:
    """UI Generator 主应用"""
    
    VERSION = "3.0"  # 版本升级：添加可视化编辑器
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"UI Generator - Schema 驱动的 UI 生成工具 v{self.VERSION}")
        self.root.geometry("1400x900")  # 增大窗口尺寸
        
        # 初始化组件
        self.logger = Logger()
        self.state = StateManager()
        self.compiler = UECompiler()
        
        # 当前 Schema
        self.current_schema: Optional[dict] = None
        
        # 编辑模式：'visual' 或 'json'
        self.edit_mode = tk.StringVar(value='visual')
        
        # 设置回调
        self._setup_callbacks()
        
        # 创建 UI
        self._create_ui()
        
        # 加载状态
        self._load_state()
    
    def _setup_callbacks(self):
        """设置各种回调"""
        # 状态变化回调
        self.state.add_stage_callback(self._on_stage_changed)
        
        # 编译器回调
        self.compiler.on_output = lambda msg: self.root.after(0, lambda: self.logger.info(f"  {msg}"))
        self.compiler.on_success = lambda: self.root.after(0, self._on_compile_success)
        self.compiler.on_failed = lambda lines: self.root.after(0, lambda: self._on_compile_failed(lines))
        self.compiler.on_error = lambda msg: self.root.after(0, lambda: self._on_compile_error(msg))
    
    def _create_ui(self):
        """创建 UI"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 流程面板
        self.flow_panel = FlowPanel(main_frame)
        self.flow_panel.pack(fill=tk.X, pady=(0, 10))
        
        # 工具栏
        self._create_toolbar(main_frame)
        
        # 主内容区（水平分割）
        content_paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        content_paned.pack(fill=tk.BOTH, expand=True)
        
        # 左侧：Schema 列表 (固定宽度)
        list_frame = ttk.Frame(content_paned, width=180)
        content_paned.add(list_frame, weight=0)
        
        self.schema_list = SchemaListPanel(list_frame, paths.schemas_dir)
        self.schema_list.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        self.schema_list.on_select = self._on_schema_select
        
        # 中间：编辑器区域（占主要空间）
        editor_frame = ttk.Frame(content_paned)
        content_paned.add(editor_frame, weight=4)
        
        self._create_editor_area(editor_frame)
        
        # 右侧：日志面板（较窄，仅用于查看和复制）
        log_frame = ttk.LabelFrame(content_paned, text="Log", padding="5", width=250)
        content_paned.add(log_frame, weight=0)
        
        self._create_log_panel(log_frame)
        
        # 设置日志控件
        self.logger.set_widget(self.log_text)
        
        # 刷新列表
        self._refresh_schema_list()
    
    def _create_editor_area(self, parent):
        """Create editor area - full space for editors"""
        # Mode switch bar
        mode_frame = ttk.Frame(parent)
        mode_frame.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(mode_frame, text="Mode:").pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text="Visual", variable=self.edit_mode, 
                       value='visual', command=self._switch_edit_mode).pack(side=tk.LEFT, padx=10)
        ttk.Radiobutton(mode_frame, text="JSON", variable=self.edit_mode,
                       value='json', command=self._switch_edit_mode).pack(side=tk.LEFT, padx=10)
        
        ttk.Separator(mode_frame, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        ttk.Button(mode_frame, text="Save", command=self._save_current_schema).pack(side=tk.LEFT, padx=5)
        
        # Editor container - full space
        self.editor_container = ttk.Frame(parent)
        self.editor_container.pack(fill=tk.BOTH, expand=True)
        
        # Visual editor
        self.visual_editor = VisualSchemaEditor(self.editor_container, paths.schemas_dir)
        self.visual_editor.on_schema_changed = self._on_visual_editor_changed
        self.visual_editor.on_save = self._on_visual_editor_save
        
        # JSON editor
        self.json_editor = EditorPanel(self.editor_container)
        self.json_editor.on_save = self._on_save_schema
        
        # Default: visual editor
        self.visual_editor.pack(fill=tk.BOTH, expand=True)
    
    def _create_log_panel(self, parent):
        """Create simplified log panel"""
        # Log text area (read-only style, but copyable)
        self.log_text = scrolledtext.ScrolledText(
            parent,
            font=("Consolas", 8),
            wrap=tk.WORD,
            width=30
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Buttons
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(btn_frame, text="Clear", width=8,
                   command=lambda: self.log_text.delete("1.0", tk.END)).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="Copy All", width=8,
                   command=self._copy_log).pack(side=tk.LEFT, padx=2)
    
    def _copy_log(self):
        """Copy log content to clipboard"""
        content = self.log_text.get("1.0", tk.END).strip()
        self.root.clipboard_clear()
        self.root.clipboard_append(content)
        self.logger.info("Log copied to clipboard")
    
    def _switch_edit_mode(self):
        """切换编辑模式"""
        mode = self.edit_mode.get()
        
        if mode == 'visual':
            # 切换到可视化模式：从 JSON 编辑器同步数据
            if hasattr(self, 'json_editor') and self.json_editor.winfo_ismapped():
                schema = self.json_editor.get_schema()
                if schema:
                    self.current_schema = schema
                    self.visual_editor.current_schema = None
                    self.visual_editor.load_template()
                    try:
                        from ui.visual_editor import WidgetSchema
                        self.visual_editor.current_schema = WidgetSchema.from_dict(schema)
                        self.visual_editor._update_ui_from_schema()
                    except Exception as e:
                        self.logger.error(f"转换 Schema 失败: {e}")
            
            self.json_editor.pack_forget()
            self.visual_editor.pack(fill=tk.BOTH, expand=True)
            self.logger.info("切换到可视化编辑模式")
            
        else:
            # 切换到 JSON 模式：从可视化编辑器同步数据
            if hasattr(self, 'visual_editor') and self.visual_editor.current_schema:
                schema = self.visual_editor.get_schema()
                if schema:
                    self.current_schema = schema
                    self.json_editor.load_template(schema)
            
            self.visual_editor.pack_forget()
            self.json_editor.pack(fill=tk.BOTH, expand=True)
            self.logger.info("切换到 JSON 编辑模式")
    
    def _save_current_schema(self):
        """保存当前 Schema"""
        mode = self.edit_mode.get()
        
        if mode == 'visual':
            if self.visual_editor.save_schema():
                self.logger.success("Schema 已保存")
                self._refresh_schema_list()
        else:
            content = self.json_editor.get_content()
            path = self.json_editor.current_path
            self._on_save_schema(path, content)
    
    def _on_visual_editor_changed(self, schema: dict):
        """可视化编辑器内容变更"""
        self.current_schema = schema
    
    def _on_visual_editor_save(self, file_path: str, schema: dict):
        """可视化编辑器保存"""
        self.current_schema = schema
        self._refresh_schema_list()
    
    def _create_toolbar(self, parent):
        """创建工具栏"""
        toolbar = ttk.Frame(parent)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        # 左侧按钮
        left = ttk.Frame(toolbar)
        left.pack(side=tk.LEFT)
        
        ttk.Button(left, text="🔄 Refresh", command=self._refresh_schema_list).pack(side=tk.LEFT, padx=2)
        ttk.Button(left, text="✅ Validate", command=self._validate_schema).pack(side=tk.LEFT, padx=2)
        ttk.Button(left, text="📝 New", command=self._new_schema_dialog).pack(side=tk.LEFT, padx=2)
        ttk.Button(left, text="🗑️ Delete", command=self._delete_schema).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(left, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # 步骤按钮 - 根据文件状态智能控制
        self.btn_cpp = ttk.Button(left, text="生成C++", command=self._generate_cpp)
        self.btn_cpp.pack(side=tk.LEFT, padx=2)
        
        self.btn_compile = ttk.Button(left, text="编译", command=self._compile_project)
        self.btn_compile.pack(side=tk.LEFT, padx=2)
        
        self.btn_bp = ttk.Button(left, text="生成蓝图", command=self._generate_blueprint)
        self.btn_bp.pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(left, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        ttk.Button(left, text="🚀 全部生成C++", command=self._generate_all_cpp).pack(side=tk.LEFT, padx=2)
        ttk.Button(left, text="🎮 生成GF配置", command=self._generate_gamefeature_config).pack(side=tk.LEFT, padx=2)
        
        # 状态标签
        self.status_var = tk.StringVar(value="就绪")
        ttk.Label(toolbar, textvariable=self.status_var, font=("", 9)).pack(side=tk.RIGHT, padx=5)
    
    def _load_state(self):
        """加载保存的状态"""
        if self.state.load():
            self.logger.info(f"📋 恢复上次状态: {self.state.stage.value}")
    
    def _on_stage_changed(self, stage: GenerationStage):
        """状态变化处理"""
        time_str = self.state.cpp_generated_time.strftime('%H:%M:%S') if self.state.cpp_generated_time else ""
        self.flow_panel.update_stage(stage, time_str, self.state.pending_schemas)
        # 按钮状态现在由 _update_button_states 智能控制
        self._update_button_states()
    
    def _update_button_states(self):
        """根据当前 Schema 的文件状态更新按钮"""
        # 更新编译按钮模式
        self._update_compile_button_mode()
        
        if not hasattr(self, 'current_schema') or not self.current_schema:
            self.btn_cpp.config(text="生成C++")
            self.btn_bp.config(text="生成蓝图")
            return
        
        schema_name = self.current_schema.get('name', '')
        output_path = self.current_schema.get('output_path', 'Source/DJ01/UI/Generated')
        
        # 检测 C++ 文件是否存在
        cpp_header = os.path.join(paths.project_root, output_path, f"{schema_name}Base.h")
        cpp_source = os.path.join(paths.project_root, output_path, f"{schema_name}Base.cpp")
        cpp_exists = os.path.exists(cpp_header) and os.path.exists(cpp_source)
        
        if cpp_exists:
            cpp_mtime = os.path.getmtime(cpp_header)
            cpp_time_str = datetime.fromtimestamp(cpp_mtime).strftime('%H:%M')
            self.btn_cpp.config(text=f"生成C++ ✓{cpp_time_str}")
            self.btn_bp.config(text="生成蓝图")
        else:
            self.btn_cpp.config(text="生成C++")
            self.btn_bp.config(text="生成蓝图 (需C++)")
    
    def _update_compile_button_mode(self):
        """更新编译按钮显示当前模式"""
        try:
            if UECommandSender.is_ue_running():
                self.btn_compile.config(text="编译 (Live)")
            else:
                self.btn_compile.config(text="编译")
        except:
            self.btn_compile.config(text="编译")
    
    # ==================== Schema 操作 ====================
    
    def _refresh_schema_list(self):
        count = self.schema_list.refresh()
        self.logger.info(f"找到 {count} 个 Schema 文件")
        
        if count == 0:
            self._create_example_schema()
            self.schema_list.refresh()
    
    def _create_example_schema(self):
        """创建示例 Schema"""
        example = {
            "$schema": "../ui_schema_v1.json",
            "name": "DJ01HealthBar",
            "description": "玩家血条 UI",
            "parent_class": "CommonUserWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/HUD",
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {"name": "HealthBar", "type": "ProgressBar", "comment": "血量进度条"},
                        {"name": "HealthText", "type": "TextBlock", "comment": "血量文字"}
                    ]
                }
            ],
            "properties": [
                {"name": "HealthPercent", "type": "float", "default": 1.0, "description": "血量百分比"}
            ]
        }
        
        path = os.path.join(paths.schemas_dir, "HealthBar.json")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(example, f, indent=2, ensure_ascii=False)
        
        self.logger.success("已创建示例 Schema: HealthBar.json")
    
    def _on_schema_select(self, file_path: str):
        """选择 Schema 文件"""
        mode = self.edit_mode.get()
        
        if mode == 'visual':
            # 可视化模式
            if self.visual_editor.load_schema(file_path):
                self.current_schema = self.visual_editor.get_schema()
                self.status_var.set(f"Loaded: {os.path.basename(file_path)}")
                self.logger.success(f"Loaded: {os.path.basename(file_path)}")
                self._update_button_states()  # 更新按钮状态
            else:
                self.logger.error(f"Load failed: {file_path}")
        else:
            # JSON 模式
            schema = self.json_editor.load_file(file_path)
            if schema:
                self.current_schema = schema
                self.status_var.set(f"Loaded: {os.path.basename(file_path)}")
                self.logger.success(f"Loaded: {os.path.basename(file_path)}")
                self._update_button_states()  # 更新按钮状态
            else:
                self.logger.error(f"Load failed: {file_path}")
    
    def _on_save_schema(self, path: Optional[str], content: str):
        """保存 Schema"""
        if not path:
            name = simpledialog.askstring("保存", "输入文件名（不含扩展名）：")
            if not name:
                return
            path = os.path.join(paths.schemas_dir, f"{name}.json")
        
        try:
            json.loads(content)  # 验证 JSON
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.logger.success(f"已保存: {os.path.basename(path)}")
            self._refresh_schema_list()
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON 格式错误: {e}")
    
    # Schema templates
    SCHEMA_TEMPLATES = {
        "Empty Widget": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyWidget",
            "description": "",
            "parent_class": "CommonUserWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/Generated",
            "components": [{"name": "RootCanvas", "type": "CanvasPanel", "children": []}],
            "properties": []
        },
        "HUD Element": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyHUDElement",
            "description": "HUD UI Element",
            "parent_class": "CommonUserWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/HUD",
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {"name": "BackgroundImage", "type": "Image", "optional": True},
                        {"name": "ContentBox", "type": "VerticalBox", "children": []}
                    ]
                }
            ],
            "properties": []
        },
        "Health Bar": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyHealthBar",
            "description": "Health bar with progress and text",
            "parent_class": "CommonUserWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/HUD",
            "binding_set": {
                "name": "ReSources",
                "component_bindings": [
                    {"source": "CurrentHealth", "component": "HealthBar", "property": "Percent", "transform": "ToPercent", "max_source": "MaxHealth"}
                ]
            },
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {
                            "name": "ContentBox",
                            "type": "HorizontalBox",
                            "children": [
                                {"name": "IconImage", "type": "Image", "optional": True},
                                {"name": "HealthBar", "type": "ProgressBar"},
                                {"name": "HealthText", "type": "TextBlock"}
                            ]
                        }
                    ]
                }
            ],
            "properties": [
                {"name": "HealthPercent", "type": "float", "default": 1.0, "category": "Health"}
            ]
        },
        "Menu Screen": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyMenuScreen",
            "description": "Full screen menu with input handling",
            "parent_class": "CommonActivatableWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/Menus",
            "input_config": {
                "mode": "Menu",
                "mouse_capture": "NoCapture"
            },
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {"name": "BackgroundImage", "type": "Image"},
                        {
                            "name": "ContentPanel",
                            "type": "VerticalBox",
                            "children": [
                                {"name": "TitleText", "type": "TextBlock"},
                                {"name": "ButtonContainer", "type": "VerticalBox", "children": []}
                            ]
                        }
                    ]
                }
            ],
            "properties": []
        },
        "Popup Dialog": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyPopupDialog",
            "description": "Modal popup dialog",
            "parent_class": "CommonActivatableWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/Common",
            "input_config": {
                "mode": "Menu",
                "mouse_capture": "NoCapture"
            },
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {"name": "BackgroundOverlay", "type": "Image", "comment": "Dim background"},
                        {
                            "name": "DialogBorder",
                            "type": "Border",
                            "children": [
                                {
                                    "name": "ContentBox",
                                    "type": "VerticalBox",
                                    "children": [
                                        {"name": "TitleText", "type": "TextBlock"},
                                        {"name": "MessageText", "type": "TextBlock"},
                                        {
                                            "name": "ButtonRow",
                                            "type": "HorizontalBox",
                                            "children": [
                                                {"name": "ConfirmButton", "type": "Button"},
                                                {"name": "CancelButton", "type": "Button", "optional": True}
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ],
            "properties": [
                {"name": "TitleString", "type": "FText", "category": "Content"},
                {"name": "MessageString", "type": "FText", "category": "Content"}
            ],
            "events": [
                {"name": "OnConfirmed", "description": "Fired when confirm button clicked"},
                {"name": "OnCancelled", "description": "Fired when cancel button clicked"}
            ]
        },
        "GameFeature HUD": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyGameFeatureHUD",
            "description": "HUD Widget for GameFeature integration (Lyra-style)",
            "parent_class": "CommonUserWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/HUD",
            "gamefeature": {
                "is_layout": False,
                "slot": "UI.Slot.MainHUD",
                "auto_activate": True
            },
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {
                            "name": "ContentBox",
                            "type": "VerticalBox",
                            "children": [
                                {"name": "StatusBar", "type": "HorizontalBox", "children": []},
                                {"name": "ActionBar", "type": "HorizontalBox", "children": []}
                            ]
                        }
                    ]
                }
            ],
            "properties": []
        },
        "Primary Game Layout": {
            "$schema": "../ui_schema_v1.json",
            "name": "MyPrimaryGameLayout",
            "description": "Primary UI Layout with CommonUI Layers (Lyra-style)",
            "parent_class": "CommonActivatableWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/Layout",
            "gamefeature": {
                "is_layout": True,
                "layer": "UI.Layer.Game",
                "auto_activate": True
            },
            "input_config": {
                "mode": "Game",
                "mouse_capture": "NoCapture"
            },
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": [
                        {
                            "name": "GameLayer",
                            "type": "CommonActivatableWidgetStack",
                            "comment": "UI.Layer.Game - HUD elements"
                        },
                        {
                            "name": "GameMenuLayer",
                            "type": "CommonActivatableWidgetStack",
                            "comment": "UI.Layer.GameMenu - In-game menus"
                        },
                        {
                            "name": "MenuLayer",
                            "type": "CommonActivatableWidgetStack",
                            "comment": "UI.Layer.Menu - Full screen menus"
                        },
                        {
                            "name": "ModalLayer",
                            "type": "CommonActivatableWidgetStack",
                            "comment": "UI.Layer.Modal - Modal dialogs"
                        }
                    ]
                }
            ],
            "properties": []
        }
    }
    
    def _new_schema_dialog(self):
        """Show new schema dialog with template selection"""
        dialog = NewSchemaDialog(self.root, list(self.SCHEMA_TEMPLATES.keys()))
        result = dialog.show()
        
        if result:
            template_name, widget_name = result
            self._create_schema_from_template(template_name, widget_name)
    
    def _create_schema_from_template(self, template_name: str, widget_name: str):
        """Create schema from selected template"""
        import copy
        
        if template_name not in self.SCHEMA_TEMPLATES:
            self.logger.error(f"Unknown template: {template_name}")
            return
        
        # Deep copy template
        template = copy.deepcopy(self.SCHEMA_TEMPLATES[template_name])
        
        # Update name
        template["name"] = widget_name
        
        # Save to file
        file_name = widget_name.replace("DJ01", "").replace("My", "")
        if not file_name:
            file_name = widget_name
        file_path = os.path.join(paths.schemas_dir, f"{file_name}.json")
        
        # Check if file exists
        if os.path.exists(file_path):
            if not messagebox.askyesno("File Exists", f"{file_name}.json already exists.\nOverwrite?"):
                return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(template, f, indent=2, ensure_ascii=False)
            
            self.logger.success(f"Created: {file_name}.json (from '{template_name}' template)")
            self._refresh_schema_list()
            
            # Load the new file
            self._on_schema_select(file_path)
            
        except Exception as e:
            self.logger.error(f"Failed to create schema: {e}")
    
    def _new_schema(self):
        """Create blank schema (legacy, now shows dialog)"""
        self._new_schema_dialog()
    
    def _delete_schema(self):
        """Delete selected schema file"""
        # Get selected file from schema list
        selected = self.schema_list.get_selected()
        
        if not selected:
            messagebox.showwarning("No Selection", "Please select a schema file to delete.")
            return
        
        file_name = os.path.basename(selected)
        
        if not messagebox.askyesno("Confirm Delete", 
                                   f"Are you sure you want to delete:\n\n{file_name}\n\nThis cannot be undone!"):
            return
        
        try:
            os.remove(selected)
            self.logger.success(f"Deleted: {file_name}")
            self._refresh_schema_list()
            
            # Clear editors
            mode = self.edit_mode.get()
            if mode == 'visual':
                self.visual_editor.load_template()
            else:
                self.json_editor.load_template(self.SCHEMA_TEMPLATES["Empty Widget"])
            
            self.current_schema = None
            
        except Exception as e:
            self.logger.error(f"Failed to delete: {e}")
    
    def _validate_schema(self) -> bool:
        """验证 Schema"""
        mode = self.edit_mode.get()
        
        if mode == 'visual':
            schema = self.visual_editor.get_schema()
        else:
            schema = self.json_editor.get_schema()
        
        if not schema:
            self.logger.error("Schema 解析错误")
            return False
        
        validator = SchemaValidator(paths.widget_types_config)
        is_valid, errors, warnings = validator.validate(schema)
        
        self.logger.separator()
        for err in errors:
            self.logger.error(err)
        for warn in warnings:
            self.logger.warning(warn)
        
        if is_valid:
            self.logger.success("Schema validated!")
            self.current_schema = schema
        else:
            self.logger.error("Schema validation failed")
        
        return is_valid
    
    # ==================== 生成操作 ====================
    
    def _generate_cpp(self):
        """生成当前 Schema 的 C++"""
        if not self._validate_schema():
            return
        
        output_dir = paths.get_output_dir(self.current_schema)
        has_gamefeature = self.current_schema.get('gamefeature') is not None
        
        msg = f"将生成到:\n{output_dir}"
        if has_gamefeature:
            msg += "\n\n检测到 GameFeature 配置，将同时更新 UI Tags 和配置"
        msg += "\n\n继续？"
        
        if not messagebox.askyesno("生成 C++", msg):
            return
        
        try:
            generator = CppGenerator(paths.widget_types_config)
            result = generator.generate(self.current_schema, output_dir)
            
            self.logger.separator()
            self.logger.success("C++ 生成成功！")
            self.logger.info(f"  → {result['header']}")
            self.logger.info(f"  → {result['source']}")
            
            # 如果有 GameFeature 配置，自动更新
            if has_gamefeature:
                self._update_gamefeature_config_silent([self.current_schema])
            
            # 获取当前文件路径
            mode = self.edit_mode.get()
            if mode == 'visual':
                current_path = self.visual_editor.current_file_path
            else:
                current_path = self.json_editor.current_path
            
            # 更新状态
            if current_path:
                self.state.set_pending_schemas([current_path])
            self.state.mark_cpp_generated()
            self.state.save()
            
            # 显示编译提醒
            dialog = CompileReminderDialog(self.root, paths.project_root)
            dialog.on_compile = self._compile_project
            dialog.show()
            
        except Exception as e:
            self.logger.error(f"生成失败: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
    
    def _generate_all_cpp(self):
        """生成所有 Schema 的 C++"""
        schema_files = self.schema_list.get_all_files()
        if not schema_files:
            self.logger.warning("没有找到 Schema 文件")
            return
        
        if not messagebox.askyesno("批量生成", f"将为 {len(schema_files)} 个 Schema 生成 C++\n\n继续？"):
            return
        
        success, failed = 0, 0
        generated = []
        gf_schemas = []  # 收集有 GameFeature 配置的 Schema
        
        for file_path in schema_files:
            try:
                schema, errors, _ = load_and_validate(file_path, paths.widget_types_config)
                if schema:
                    output_dir = paths.get_output_dir(schema)
                    generator = CppGenerator(paths.widget_types_config)
                    generator.generate(schema, output_dir)
                    self.logger.success(f"✅ {os.path.basename(file_path)}")
                    success += 1
                    generated.append(file_path)
                    # 收集有 GameFeature 配置的 Schema
                    if schema.get('gamefeature'):
                        gf_schemas.append(schema)
                else:
                    self.logger.error(f"❌ {os.path.basename(file_path)}: {errors}")
                    failed += 1
            except Exception as e:
                self.logger.error(f"❌ {os.path.basename(file_path)}: {e}")
                failed += 1
        
        self.logger.separator()
        self.logger.info(f"完成: 成功 {success}, 失败 {failed}")
        
        # 自动更新 GameFeature 配置
        if gf_schemas:
            self._update_gamefeature_config_silent(gf_schemas)
        
        if success > 0:
            self.state.set_pending_schemas(generated)
            self.state.mark_cpp_generated()
            self.state.save()
            
            dialog = CompileReminderDialog(self.root, paths.project_root)
            dialog.on_compile = self._compile_project
            dialog.show()
    
    # ==================== 编译操作 ====================
    
    def _compile_project(self):
        """编译项目 - 支持外部编译和 Live Coding"""
        # 检测引擎路径
        ue_paths = self.compiler.detect_engine_paths()
        
        if not ue_paths['engine_dir']:
            result = EngineSelectDialog.show(self.root)
            if result == "MANUAL":
                self._manual_compile()
                return
            elif result:
                self.compiler.set_engine_dir(result)
            else:
                return
        
        if not self.compiler.can_compile():
            self.logger.error("未找到编译工具")
            self._manual_compile()
            return
        
        if not messagebox.askyesno(
            "编译项目",
            f"引擎: {self.compiler.engine_dir}\n\n开始编译？"
        ):
            return
        
        # 开始编译
        self.btn_compile.config(state=tk.DISABLED, text="⏳ 编译中...")
        self.btn_cpp.config(state=tk.DISABLED)
        self.flow_panel.set_compiling()
        
        self.logger.separator()
        self.logger.info("🔧 开始编译...")
        
        self.compiler.compile_async()
    
    def _manual_compile(self):
        """手动编译模式"""
        if ManualCompileDialog.show(self.root):
            self._on_compile_success()
    
    def _on_compile_success(self):
        """编译成功"""
        self.logger.success("编译成功！")
        self.btn_compile.config(state=tk.NORMAL, text="② 编译")
        self.btn_cpp.config(state=tk.NORMAL)
        
        self.state.mark_compiled()
        self.state.save()
        
        if messagebox.askyesno("生成蓝图", f"是否生成 {len(self.state.pending_schemas)} 个蓝图？"):
            self._generate_all_blueprints()
    
    def _on_compile_failed(self, output_lines: list):
        """编译失败"""
        self.logger.error("编译失败！")
        self.btn_compile.config(state=tk.NORMAL, text="② 编译")
        self.btn_cpp.config(state=tk.NORMAL)
        self.flow_panel.set_compile_failed()
        
        errors = [l for l in output_lines if 'error' in l.lower()][:10]
        if errors:
            self.logger.separator()
            for e in errors:
                self.logger.error(e)
        
        messagebox.showerror("编译失败", "请查看日志了解详情")
    
    def _on_compile_error(self, error: str):
        """编译出错"""
        self.logger.error(f"编译出错: {error}")
        self.btn_compile.config(state=tk.NORMAL, text="② 编译")
        self.btn_cpp.config(state=tk.NORMAL)
        self._manual_compile()
    
    # ==================== 蓝图生成 ====================
    
    def _generate_blueprint(self):
        """生成当前蓝图"""
        if not self.current_schema:
            self.logger.error("请先加载 Schema")
            return
        
        schema_name = self.current_schema.get('name', '')
        output_path = self.current_schema.get('output_path', 'Source/DJ01/UI/Generated')
        
        # 检测 C++ 文件是否存在
        cpp_header = os.path.join(paths.project_root, output_path, f"{schema_name}Base.h")
        cpp_source = os.path.join(paths.project_root, output_path, f"{schema_name}Base.cpp")
        
        if not os.path.exists(cpp_header) or not os.path.exists(cpp_source):
            self.logger.error(f"C++ 基类不存在，请先生成 C++ 代码")
            self.logger.info(f"  期望文件: {cpp_header}")
            messagebox.showwarning("需要生成 C++", 
                f"找不到 C++ 基类文件:\n{schema_name}Base.h\n\n请先点击 '生成C++' 按钮")
            return
        
        # 保存临时 Schema
        temp_path = os.path.join(paths.intermediate_dir, "temp_schema.json")
        os.makedirs(os.path.dirname(temp_path), exist_ok=True)
        with open(temp_path, 'w', encoding='utf-8') as f:
            json.dump(self.current_schema, f, indent=2, ensure_ascii=False)
        
        code = f"""
import sys
sys.path.insert(0, r'{paths.ue_scripts_dir}')
from generate_widget_bp import generate_from_schema
generate_from_schema(r'{temp_path}')
"""
        
        self.logger.info(f"📤 发送蓝图生成命令: {schema_name}")
        self.logger.info(f"   基类: U{schema_name}Base (C++ 文件存在 ✓)")
        
        if UECommandSender.send(code):
            self.logger.success("📤 蓝图生成命令已发送到 UE")
            self.logger.info("   ⚠️ 如果 UE 找不到基类，请确保已编译项目")
        else:
            self.logger.error("发送命令失败，请确保 UE 编辑器已打开")
        
        # 重置状态（如果之前处于等待蓝图状态）
        if self.state.stage == GenerationStage.READY_FOR_BLUEPRINT:
            self.state.reset()
            self.state.save()
    
    # ==================== GameFeature 配置生成 ====================
    
    def _update_gamefeature_config_silent(self, schemas: list):
        """静默更新 GameFeature 配置（在 C++ 生成时自动调用）"""
        try:
            from core.gamefeature_generator import GameFeatureUIGenerator
            generator = GameFeatureUIGenerator(paths.widget_types_config)
            
            # 生成 Tags
            tags_path = os.path.join(paths.project_root, "Config", "Tags", "UITags.ini")
            generator.generate_gameplay_tags_ini(tags_path)
            self.logger.info(f"  → 更新 UI Tags")
            
            # 生成配置 JSON
            config_path = os.path.join(paths.project_root, "Config", "UIConfig.json")
            generator.generate_gamefeature_ui_config(schemas, config_path)
            self.logger.info(f"  → 更新 UIConfig.json")
            
        except Exception as e:
            self.logger.warning(f"GameFeature 配置更新失败: {e}")
    
    def _generate_gamefeature_config(self):
        """生成 GameFeature UI 配置"""
        from core.gamefeature_generator import GameFeatureUIGenerator
        
        schema_files = self.schema_list.get_all_files()
        if not schema_files:
            self.logger.warning("没有找到 Schema 文件")
            return
        
        # 收集所有包含 gamefeature 配置的 Schema
        gf_schemas = []
        for file_path in schema_files:
            try:
                schema, errors, _ = load_and_validate(file_path, paths.widget_types_config)
                if schema and schema.get('gamefeature'):
                    gf_schemas.append(schema)
            except Exception as e:
                self.logger.warning(f"跳过 {os.path.basename(file_path)}: {e}")
        
        if not gf_schemas:
            self.logger.warning("没有找到包含 gamefeature 配置的 Schema")
            messagebox.showinfo("提示", "没有 Schema 配置了 GameFeature 集成。\n请在 Schema 中添加 'gamefeature' 字段。")
            return
        
        if not messagebox.askyesno(
            "生成 GameFeature 配置",
            f"将为 {len(gf_schemas)} 个 Widget 生成 GameFeature 配置:\n\n"
            "• UI Tags (Config/Tags/UITags.ini)\n"
            "• UI 配置 JSON (Config/UIConfig.json)\n"
            "• PrimaryGameLayout 基类 (可选)\n\n"
            "继续？"
        ):
            return
        
        try:
            generator = GameFeatureUIGenerator(paths.widget_types_config)
            
            self.logger.separator()
            self.logger.info("🎮 开始生成 GameFeature UI 配置...")
            
            # 1. 生成 GameplayTags
            tags_path = os.path.join(paths.project_root, "Config", "Tags", "UITags.ini")
            generator.generate_gameplay_tags_ini(tags_path)
            self.logger.success(f"✅ 生成 UI Tags: {tags_path}")
            
            # 2. 生成 UI 配置 JSON
            config_path = os.path.join(paths.project_root, "Config", "UIConfig.json")
            generator.generate_gamefeature_ui_config(gf_schemas, config_path)
            self.logger.success(f"✅ 生成 UI 配置: {config_path}")
            
            # 3. 询问是否生成 PrimaryGameLayout
            if messagebox.askyesno(
                "生成 PrimaryGameLayout",
                "是否生成 PrimaryGameLayout C++ 基类？\n\n"
                "这是 Lyra 风格 UI 的核心布局 Widget，用于管理 UI Layers。"
            ):
                layout_dir = os.path.join(paths.project_root, "Source", "DJ01", "UI", "Generated")
                result = generator.generate_primary_layout_header(layout_dir)
                self.logger.success(f"✅ 生成 PrimaryGameLayout:")
                self.logger.info(f"   → {result['header']}")
                self.logger.info(f"   → {result['source']}")
            
            self.logger.separator()
            self.logger.success("GameFeature UI 配置生成完成！")
            
            # 提示后续步骤
            messagebox.showinfo(
                "完成",
                "GameFeature UI 配置已生成！\n\n"
                "后续步骤：\n"
                "1. 重新编译项目\n"
                "2. 创建 WBP_PrimaryGameLayout 蓝图\n"
                "3. 在 GameFeatureData 中添加 'Add Widgets' Action\n"
                "4. 配置 Widget 对应的 Layer/Slot"
            )
            
        except Exception as e:
            self.logger.error(f"生成失败: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
    
    def _generate_all_blueprints(self):
        """生成所有待处理蓝图"""
        if not self.state.pending_schemas:
            self.logger.warning("没有待生成的蓝图")
            return
        
        self.logger.separator()
        self.logger.info(f"开始生成 {len(self.state.pending_schemas)} 个蓝图...")
        
        if UECommandSender.send_blueprint_generation(paths.schemas_dir):
            self.logger.success("📤 批量生成命令已发送到 UE")
        
        self.state.reset()
        self.state.save()
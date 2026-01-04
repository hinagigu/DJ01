"""
UI 面板组件
"""
import os
import json
import tkinter as tk
from tkinter import ttk, scrolledtext
from typing import Optional, Callable, List

from core.state_manager import GenerationStage


class FlowPanel(ttk.LabelFrame):
    """流程状态面板"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="📋 生成流程", padding="10", **kwargs)
        
        self._create_widgets()
    
    def _create_widgets(self):
        # 流程步骤指示器
        steps_frame = ttk.Frame(self)
        steps_frame.pack(fill=tk.X)
        
        # 步骤 1
        step1_frame = ttk.Frame(steps_frame)
        step1_frame.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.step1_indicator = ttk.Label(step1_frame, text="⚪", font=("", 16))
        self.step1_indicator.pack(side=tk.LEFT, padx=5)
        ttk.Label(step1_frame, text="步骤1: 生成 C++", font=("", 10, "bold")).pack(side=tk.LEFT)
        ttk.Label(step1_frame, text="(Python)", font=("", 8)).pack(side=tk.LEFT, padx=5)
        
        # 箭头
        ttk.Label(steps_frame, text="→", font=("", 14)).pack(side=tk.LEFT, padx=10)
        
        # 步骤 2
        step2_frame = ttk.Frame(steps_frame)
        step2_frame.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.step2_indicator = ttk.Label(step2_frame, text="⚪", font=("", 16))
        self.step2_indicator.pack(side=tk.LEFT, padx=5)
        ttk.Label(step2_frame, text="步骤2: 编译项目", font=("", 10, "bold")).pack(side=tk.LEFT)
        ttk.Label(step2_frame, text="(UBT)", font=("", 8)).pack(side=tk.LEFT, padx=5)
        
        # 箭头
        ttk.Label(steps_frame, text="→", font=("", 14)).pack(side=tk.LEFT, padx=10)
        
        # 步骤 3
        step3_frame = ttk.Frame(steps_frame)
        step3_frame.pack(side=tk.LEFT, expand=True, fill=tk.X)
        self.step3_indicator = ttk.Label(step3_frame, text="⚪", font=("", 16))
        self.step3_indicator.pack(side=tk.LEFT, padx=5)
        ttk.Label(step3_frame, text="步骤3: 生成蓝图", font=("", 10, "bold")).pack(side=tk.LEFT)
        ttk.Label(step3_frame, text="(UE Python)", font=("", 8)).pack(side=tk.LEFT, padx=5)
        
        # 状态提示
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(self, textvariable=self.status_var, 
                                      font=("", 9), foreground="gray")
        self.status_label.pack(fill=tk.X, pady=(10, 0))
        
        # 待处理列表
        self.pending_frame = ttk.Frame(self)
        self.pending_listbox = tk.Listbox(self.pending_frame, height=2, font=("Consolas", 9))
        self.pending_listbox.pack(fill=tk.X, expand=True)
    
    def update_stage(self, stage: GenerationStage, time_str: str = "", pending: List[str] = None):
        """更新流程状态显示"""
        if stage == GenerationStage.IDLE:
            self.step1_indicator.config(text="⚪")
            self.step2_indicator.config(text="⚪")
            self.step3_indicator.config(text="⚪")
            self.status_var.set("")
            self.pending_frame.pack_forget()
            
        elif stage == GenerationStage.CPP_GENERATED:
            self.step1_indicator.config(text="✅")
            self.step2_indicator.config(text="🔄")
            self.step3_indicator.config(text="⚪")
            self.status_var.set(f"⏳ 等待编译... C++ 生成于 {time_str}")
            
            # 显示待处理列表
            if pending:
                self.pending_listbox.delete(0, tk.END)
                for p in pending:
                    self.pending_listbox.insert(tk.END, os.path.basename(p))
                self.pending_frame.pack(fill=tk.X, pady=(5, 0))
            
        elif stage == GenerationStage.READY_FOR_BLUEPRINT:
            self.step1_indicator.config(text="✅")
            self.step2_indicator.config(text="✅")
            self.step3_indicator.config(text="🔄")
            self.status_var.set("✅ 编译完成，可以生成蓝图")
    
    def set_compiling(self):
        """设置编译中状态"""
        self.step2_indicator.config(text="🔄")
        self.status_var.set("⏳ 正在编译项目...")
    
    def set_compile_failed(self):
        """设置编译失败状态"""
        self.step2_indicator.config(text="❌")
        self.status_var.set("❌ 编译失败，请查看日志")


class SchemaListPanel(ttk.LabelFrame):
    """Schema 文件列表面板"""
    
    def __init__(self, parent, schemas_dir: str, **kwargs):
        super().__init__(parent, text="📁 UI Schemas", padding="5", **kwargs)
        
        self.schemas_dir = schemas_dir
        self.on_select: Optional[Callable[[str], None]] = None
        
        self._create_widgets()
    
    def _create_widgets(self):
        # 列表框 + 滚动条
        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True)
        
        self.listbox = tk.Listbox(container, font=("Consolas", 10))
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self._on_select)
        
        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
    
    def _on_select(self, event):
        selection = self.listbox.curselection()
        if selection and self.on_select:
            filename = self.listbox.get(selection[0])
            file_path = os.path.join(self.schemas_dir, filename)
            self.on_select(file_path)
    
    def refresh(self) -> int:
        """刷新文件列表，返回文件数量"""
        self.listbox.delete(0, tk.END)
        
        if not os.path.exists(self.schemas_dir):
            os.makedirs(self.schemas_dir, exist_ok=True)
            return 0
        
        schema_files = sorted([f for f in os.listdir(self.schemas_dir) if f.endswith('.json')])
        
        for f in schema_files:
            self.listbox.insert(tk.END, f)
        
        return len(schema_files)
    
    def get_all_files(self) -> List[str]:
        """获取所有 Schema 文件路径"""
        if not os.path.exists(self.schemas_dir):
            return []
        
        return [
            os.path.join(self.schemas_dir, f) 
            for f in os.listdir(self.schemas_dir) 
            if f.endswith('.json')
        ]
    
    def get_selected(self) -> Optional[str]:
        """获取当前选中的文件路径"""
        selection = self.listbox.curselection()
        if not selection:
            return None
        
        filename = self.listbox.get(selection[0])
        return os.path.join(self.schemas_dir, filename)


class EditorPanel(ttk.LabelFrame):
    """Schema 编辑器面板"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Schema 编辑器", padding="5", **kwargs)
        
        self.current_path: Optional[str] = None
        self.on_save: Optional[Callable[[str, str], None]] = None
        
        self._create_widgets()
    
    def _create_widgets(self):
        self.editor = scrolledtext.ScrolledText(
            self, 
            font=("Consolas", 10),
            wrap=tk.NONE
        )
        self.editor.pack(fill=tk.BOTH, expand=True)
        
        ttk.Button(self, text="💾 保存 Schema", command=self._save).pack(pady=5)
    
    def _save(self):
        content = self.editor.get("1.0", tk.END).strip()
        if self.on_save:
            self.on_save(self.current_path, content)
    
    def load_file(self, file_path: str) -> Optional[dict]:
        """加载文件到编辑器"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.editor.delete("1.0", tk.END)
            self.editor.insert("1.0", content)
            self.current_path = file_path
            
            return json.loads(content)
        except Exception:
            return None
    
    def load_template(self, template: dict):
        """加载模板"""
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", json.dumps(template, indent=2, ensure_ascii=False))
        self.current_path = None
    
    def set_content(self, content: str):
        """设置编辑器内容"""
        self.editor.delete("1.0", tk.END)
        self.editor.insert("1.0", content)
    
    def get_content(self) -> str:
        """获取编辑器内容"""
        return self.editor.get("1.0", tk.END).strip()
    
    def get_schema(self) -> Optional[dict]:
        """解析并返回 Schema"""
        try:
            return json.loads(self.get_content())
        except json.JSONDecodeError:
            return None


class OutputPanel(ttk.Notebook):
    """输出面板（日志、预览、组件树）"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        self._create_tabs()
    
    def _create_tabs(self):
        # 日志标签页
        log_frame = ttk.Frame(self, padding="5")
        self.add(log_frame, text="📋 日志")
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # 预览标签页
        preview_frame = ttk.Frame(self, padding="5")
        self.add(preview_frame, text="👁️ 代码预览")
        
        self.preview_text = scrolledtext.ScrolledText(
            preview_frame,
            font=("Consolas", 9),
            wrap=tk.NONE
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        
        # 组件树标签页
        tree_frame = ttk.Frame(self, padding="5")
        self.add(tree_frame, text="🌳 组件树")
        
        self.component_tree = ttk.Treeview(tree_frame, show="tree")
        self.component_tree.pack(fill=tk.BOTH, expand=True)
    
    def set_preview(self, content: str):
        """设置预览内容"""
        self.preview_text.delete("1.0", tk.END)
        self.preview_text.insert("1.0", content)
    
    def update_component_tree(self, schema: Optional[dict]):
        """更新组件树"""
        # 清空
        for item in self.component_tree.get_children():
            self.component_tree.delete(item)
        
        if not schema:
            return
        
        def add_components(components, parent=""):
            for comp in components:
                name = comp['name']
                comp_type = comp['type']
                node_id = self.component_tree.insert(
                    parent, "end", 
                    text=f"[{comp_type}] {name}"
                )
                if 'children' in comp:
                    add_components(comp['children'], node_id)
        
        add_components(schema.get('components', []))
        
        # 展开所有
        def expand_all(item):
            self.component_tree.item(item, open=True)
            for child in self.component_tree.get_children(item):
                expand_all(child)
        
        for item in self.component_tree.get_children():
            expand_all(item)
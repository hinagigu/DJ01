#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI Generator - Schema 驱动的 UI 生成工具
主入口文件
"""

import os
import sys
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext

# 添加 core 到路径
TOOL_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOL_ROOT)

from core.schema_validator import SchemaValidator, load_and_validate
from core.cpp_generator import CppGenerator


class UIGeneratorApp:
    """UI Generator 主应用"""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("UI Generator - Schema 驱动的 UI 生成工具")
        self.root.geometry("1000x700")
        
        # 路径配置
        self.tool_root = TOOL_ROOT
        self.widget_types_path = os.path.join(TOOL_ROOT, "configs", "widget_types.json")
        self.project_root = os.path.dirname(os.path.dirname(TOOL_ROOT))  # DJ01
        
        # 当前加载的 Schema
        self.current_schema_path = None
        self.current_schema = None
        
        self._create_ui()
    
    def _create_ui(self):
        """创建 UI"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 顶部工具栏
        toolbar = ttk.Frame(main_frame)
        toolbar.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(toolbar, text="� 刷新列表", command=self._refresh_schema_list).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="✅ 验证", command=self._validate_schema).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="⚙️ 生成 C++", command=self._generate_cpp).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🔷 生成蓝图", command=self._generate_blueprint).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="🚀 全部生成", command=self._generate_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="📝 新建 Schema", command=self._new_schema).pack(side=tk.LEFT, padx=5)
        
        # 状态标签
        self.status_var = tk.StringVar(value="就绪")
        ttk.Label(toolbar, textvariable=self.status_var).pack(side=tk.RIGHT, padx=5)
        
        # 分割面板
        paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # 左侧：Schema 列表 + 编辑器
        left_frame = ttk.Frame(paned)
        paned.add(left_frame, weight=1)
        
        # Schema 文件列表
        list_frame = ttk.LabelFrame(left_frame, text="📁 UI Schemas", padding="5")
        list_frame.pack(fill=tk.X, pady=(0, 5))
        
        # 列表框 + 滚动条
        list_container = ttk.Frame(list_frame)
        list_container.pack(fill=tk.X)
        
        self.schema_listbox = tk.Listbox(list_container, height=6, font=("Consolas", 10))
        self.schema_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.schema_listbox.bind('<<ListboxSelect>>', self._on_schema_select)
        
        list_scrollbar = ttk.Scrollbar(list_container, orient=tk.VERTICAL, command=self.schema_listbox.yview)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.schema_listbox.config(yscrollcommand=list_scrollbar.set)
        
        # Schema 编辑器
        editor_frame = ttk.LabelFrame(left_frame, text="Schema 编辑器", padding="5")
        editor_frame.pack(fill=tk.BOTH, expand=True)
        
        self.schema_editor = scrolledtext.ScrolledText(
            editor_frame, 
            font=("Consolas", 10),
            wrap=tk.NONE
        )
        self.schema_editor.pack(fill=tk.BOTH, expand=True)
        
        # 保存按钮
        ttk.Button(editor_frame, text="💾 保存 Schema", command=self._save_schema).pack(pady=5)
        
        # 右侧：输出/预览
        right_frame = ttk.Notebook(paned)
        paned.add(right_frame, weight=1)
        
        # 日志标签页
        log_frame = ttk.Frame(right_frame, padding="5")
        right_frame.add(log_frame, text="📋 日志")
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # 预览标签页
        preview_frame = ttk.Frame(right_frame, padding="5")
        right_frame.add(preview_frame, text="👁️ 代码预览")
        
        self.preview_text = scrolledtext.ScrolledText(
            preview_frame,
            font=("Consolas", 9),
            wrap=tk.NONE
        )
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        
        # 组件树标签页
        tree_frame = ttk.Frame(right_frame, padding="5")
        right_frame.add(tree_frame, text="🌳 组件树")
        
        self.component_tree = ttk.Treeview(tree_frame, show="tree")
        self.component_tree.pack(fill=tk.BOTH, expand=True)
        
        # 初始化 Schema 目录并加载列表
        self.schemas_dir = os.path.join(TOOL_ROOT, "schemas", "widgets")
        os.makedirs(self.schemas_dir, exist_ok=True)
        self._refresh_schema_list()
    
    def _refresh_schema_list(self):
        """刷新 Schema 文件列表"""
        self.schema_listbox.delete(0, tk.END)
        
        if not os.path.exists(self.schemas_dir):
            os.makedirs(self.schemas_dir, exist_ok=True)
            return
        
        # 扫描所有 .json 文件
        schema_files = []
        for f in os.listdir(self.schemas_dir):
            if f.endswith('.json'):
                schema_files.append(f)
        
        schema_files.sort()
        
        for f in schema_files:
            self.schema_listbox.insert(tk.END, f)
        
        self._log(f"找到 {len(schema_files)} 个 Schema 文件", "info")
        
        # 如果没有文件，创建示例
        if len(schema_files) == 0:
            self._create_example_schema()
            self._refresh_schema_list()
    
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
                        {
                            "name": "HealthBar",
                            "type": "ProgressBar",
                            "bind_percent": "HealthPercent",
                            "comment": "血量进度条"
                        },
                        {
                            "name": "HealthText",
                            "type": "TextBlock",
                            "bind_text": "HealthDisplayText",
                            "comment": "血量文字"
                        }
                    ]
                }
            ],
            "properties": [
                {
                    "name": "HealthPercent",
                    "type": "float",
                    "category": "Health",
                    "default": 1.0,
                    "description": "血量百分比 0-1"
                },
                {
                    "name": "HealthDisplayText",
                    "type": "FText",
                    "category": "Health",
                    "description": "血量显示文本"
                }
            ],
            "functions": [
                {
                    "name": "SetHealth",
                    "description": "设置血量",
                    "parameters": [
                        {"name": "Current", "type": "float"},
                        {"name": "Max", "type": "float"}
                    ],
                    "body_hint": "计算百分比并更新显示"
                }
            ],
            "events": [
                {
                    "name": "OnHealthChanged",
                    "description": "血量变化事件",
                    "parameters": [
                        {"name": "NewPercent", "type": "float"}
                    ]
                }
            ]
        }
        
        example_path = os.path.join(self.schemas_dir, "HealthBar.json")
        with open(example_path, 'w', encoding='utf-8') as f:
            json.dump(example, f, indent=2, ensure_ascii=False)
        
        self._log("已创建示例 Schema: HealthBar.json", "success")
    
    def _on_schema_select(self, event):
        """选中 Schema 文件时加载"""
        selection = self.schema_listbox.curselection()
        if not selection:
            return
        
        filename = self.schema_listbox.get(selection[0])
        file_path = os.path.join(self.schemas_dir, filename)
        self._load_schema_file(file_path)
    
    def _save_schema(self):
        """保存当前编辑的 Schema"""
        if not self.current_schema_path:
            # 新文件，要求输入名称
            from tkinter import simpledialog
            name = simpledialog.askstring("保存 Schema", "输入文件名（不含扩展名）：")
            if not name:
                return
            self.current_schema_path = os.path.join(self.schemas_dir, f"{name}.json")
        
        try:
            content = self.schema_editor.get("1.0", tk.END)
            # 验证 JSON 格式
            json.loads(content)
            
            with open(self.current_schema_path, 'w', encoding='utf-8') as f:
                f.write(content.strip())
            
            self._log(f"已保存: {os.path.basename(self.current_schema_path)}", "success")
            self._refresh_schema_list()
            
        except json.JSONDecodeError as e:
            self._log(f"JSON 格式错误: {e}", "error")
        except Exception as e:
            self._log(f"保存失败: {e}", "error")
    
    def _generate_all(self):
        """生成所有 Schema 的代码"""
        if not os.path.exists(self.schemas_dir):
            self._log("Schema 目录不存在", "error")
            return
        
        schema_files = [f for f in os.listdir(self.schemas_dir) if f.endswith('.json')]
        
        if not schema_files:
            self._log("没有找到 Schema 文件", "warning")
            return
        
        if not messagebox.askyesno(
            "批量生成",
            f"将为 {len(schema_files)} 个 Schema 生成 C++ 代码\n\n继续？"
        ):
            return
        
        success_count = 0
        fail_count = 0
        
        for filename in schema_files:
            file_path = os.path.join(self.schemas_dir, filename)
            try:
                schema, errors, warnings = load_and_validate(file_path, self.widget_types_path)
                
                if schema:
                    output_dir = schema.get('output_path', 'Source/DJ01/UI/Generated')
                    full_output_dir = os.path.join(self.project_root, output_dir)
                    
                    generator = CppGenerator(self.widget_types_path)
                    generator.generate(schema, full_output_dir)
                    
                    self._log(f"✅ {filename} -> {schema['name']}Base.h/cpp", "success")
                    success_count += 1
                else:
                    self._log(f"❌ {filename}: {errors}", "error")
                    fail_count += 1
                    
            except Exception as e:
                self._log(f"❌ {filename}: {e}", "error")
                fail_count += 1
        
        self._log("-" * 40)
        self._log(f"生成完成: 成功 {success_count}, 失败 {fail_count}", "info")
        self._log("⚠️ 请重新编译项目", "warning")
    
    def _log(self, message: str, level: str = "info"):
        """添加日志"""
        prefix = {"info": "ℹ️", "warning": "⚠️", "error": "❌", "success": "✅"}.get(level, "")
        self.log_text.insert(tk.END, f"{prefix} {message}\n")
        self.log_text.see(tk.END)
    

    def _load_schema_file(self, file_path: str):
        """加载指定的 Schema 文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.schema_editor.delete("1.0", tk.END)
            self.schema_editor.insert("1.0", content)
            
            self.current_schema_path = file_path
            self.current_schema = json.loads(content)
            
            self._log(f"已加载: {os.path.basename(file_path)}", "success")
            self._update_component_tree()
            self.status_var.set(f"已加载: {os.path.basename(file_path)}")
            
        except Exception as e:
            self._log(f"加载失败: {e}", "error")
    
    def _validate_schema(self):
        """验证当前 Schema"""
        try:
            content = self.schema_editor.get("1.0", tk.END)
            schema = json.loads(content)
        except json.JSONDecodeError as e:
            self._log(f"JSON 解析错误: {e}", "error")
            return False
        
        validator = SchemaValidator(self.widget_types_path)
        is_valid, errors, warnings = validator.validate(schema)
        
        self._log("-" * 40)
        self._log("验证结果:")
        
        if errors:
            for err in errors:
                self._log(f"  {err}", "error")
        
        if warnings:
            for warn in warnings:
                self._log(f"  {warn}", "warning")
        
        if is_valid:
            self._log("Schema 验证通过！", "success")
            self.current_schema = schema
            self._update_component_tree()
        else:
            self._log("Schema 验证失败", "error")
        
        return is_valid
    
    def _generate_cpp(self):
        """生成 C++ 代码"""
        if not self._validate_schema():
            return
        
        # 确定输出目录
        output_dir = self.current_schema.get('output_path', 'Source/DJ01/UI/Generated')
        full_output_dir = os.path.join(self.project_root, output_dir)
        
        # 确认
        if not messagebox.askyesno(
            "确认生成",
            f"将生成 C++ 代码到:\n{full_output_dir}\n\n继续？"
        ):
            return
        
        try:
            generator = CppGenerator(self.widget_types_path)
            result = generator.generate(self.current_schema, full_output_dir)
            
            self._log("-" * 40)
            self._log("C++ 代码生成成功！", "success")
            self._log(f"  头文件: {result['header']}")
            self._log(f"  源文件: {result['source']}")
            self._log("-" * 40)
            self._log("⚠️ 请重新编译项目后再生成蓝图", "warning")
            
            # 预览生成的代码
            with open(result['header'], 'r', encoding='utf-8') as f:
                header_content = f.read()
            
            self.preview_text.delete("1.0", tk.END)
            self.preview_text.insert("1.0", header_content)
            
        except Exception as e:
            self._log(f"生成失败: {e}", "error")
            import traceback
            self._log(traceback.format_exc(), "error")
    
    def _generate_blueprint(self):
        """生成蓝图（需要 UE 连接）"""
        if not self.current_schema:
            self._log("请先加载并验证 Schema", "error")
            return
        
        # 保存当前 Schema 到临时文件
        temp_schema_path = os.path.join(
            self.project_root, 
            "Intermediate", 
            "UIGenerator", 
            "temp_schema.json"
        )
        os.makedirs(os.path.dirname(temp_schema_path), exist_ok=True)
        
        with open(temp_schema_path, 'w', encoding='utf-8') as f:
            json.dump(self.current_schema, f, indent=2, ensure_ascii=False)
        
        # 发送命令到 UE
        self._log("-" * 40)
        self._log("正在向 UE 发送蓝图生成命令...", "info")
        
        # 使用与 DataAssetManager 相同的 IPC 机制
        cmd_dir = os.path.join(self.project_root, "Intermediate", "DataAssetManager")
        cmd_file = os.path.join(cmd_dir, "pending_command.json")
        
        script_path = os.path.join(TOOL_ROOT, "ue_scripts", "generate_widget_bp.py")
        
        # 生成带参数的执行代码
        code = f"""
import sys
sys.path.insert(0, r'{os.path.join(TOOL_ROOT, "ue_scripts")}')
from generate_widget_bp import generate_from_schema
generate_from_schema(r'{temp_schema_path}')
"""
        
        cmd = {
            "type": "execute_code",
            "code": code
        }
        
        os.makedirs(cmd_dir, exist_ok=True)
        with open(cmd_file, 'w', encoding='utf-8') as f:
            json.dump(cmd, f, indent=2)
        
        self._log("命令已发送！请查看 UE 输出日志", "success")
        self._log("如果 UE 未响应，请确保已启动命令监控器", "warning")
    
    def _new_schema(self):
        """新建 Schema"""
        template = {
            "$schema": "../ui_schema_v1.json",
            "name": "MyWidget",
            "description": "Widget 描述",
            "parent_class": "CommonUserWidget",
            "output_path": "Source/DJ01/UI/Generated",
            "blueprint_path": "/Game/UI/Generated",
            "components": [
                {
                    "name": "RootCanvas",
                    "type": "CanvasPanel",
                    "children": []
                }
            ],
            "properties": [],
            "functions": [],
            "events": []
        }
        
        self.schema_editor.delete("1.0", tk.END)
        self.schema_editor.insert("1.0", json.dumps(template, indent=2, ensure_ascii=False))
        
        self.current_schema_path = None
        self.current_schema = template
        self._log("已创建新 Schema 模板", "info")
        self._update_component_tree()
    
    def _update_component_tree(self):
        """更新组件树显示"""
        # 清空树
        for item in self.component_tree.get_children():
            self.component_tree.delete(item)
        
        if not self.current_schema:
            return
        
        # 递归添加组件
        def add_components(components, parent=""):
            for comp in components:
                name = comp['name']
                comp_type = comp['type']
                node_id = self.component_tree.insert(
                    parent, 
                    "end", 
                    text=f"[{comp_type}] {name}"
                )
                if 'children' in comp:
                    add_components(comp['children'], node_id)
        
        add_components(self.current_schema.get('components', []))
        
        # 展开所有节点
        def expand_all(item):
            self.component_tree.item(item, open=True)
            for child in self.component_tree.get_children(item):
                expand_all(child)
        
        for item in self.component_tree.get_children():
            expand_all(item)


def main():
    """主函数"""
    root = tk.Tk()
    app = UIGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
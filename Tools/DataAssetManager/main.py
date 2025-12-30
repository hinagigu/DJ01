#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 主入口
职责：启动应用程序
"""

import sys
import os

# 确保能导入模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import ttk, messagebox

from config import (
    CONFIG_FILES, PROJECT_PREFIX, APP_TITLE, APP_VERSION, 
    ASSET_TYPES, CONFIG_DIR, PROJECT_ROOT
)
from core import SchemaLoader, AssetRegistry, ValidationEngine, DataManager, OptionsScanner
from core.ue_remote import UERemoteExecutor
from ui.editors import BaseAssetEditor

# 延迟导入各编辑器模块（待实现）
# from experience import ExperienceEditorUI
# from pawn_data import PawnDataEditorUI
# from input_config import InputConfigEditorUI
# from ability_set import AbilitySetEditorUI


class DataAssetManagerApp:
    """DataAsset 管理器主应用"""
    
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1500x900")
        
        # 初始化核心组件
        self.schema_loader = SchemaLoader(CONFIG_FILES["schema_dir"])
        self.registry = AssetRegistry(CONFIG_FILES["registry"])
        self.data_manager = DataManager()
        self.validator = ValidationEngine()
        
        # 初始化选项扫描器（用于下拉选择）
        self.options_scanner = OptionsScanner(
            PROJECT_ROOT, 
            CONFIG_FILES["options_dir"],
            CONFIG_FILES.get("scan_paths")
        )
        # 启动时扫描 GameFeatures
        self._scan_game_features_on_start()
        
        # 编辑器实例
        self.editors = {}
        
        self._create_menu()
        self._create_ui()
        self._bind_shortcuts()
    
    def _scan_game_features_on_start(self):
        """启动时扫描所有可选项"""
        try:
            results = self.options_scanner.update_all()
            total_new = sum(results.values())
            if total_new > 0:
                print(f"扫描完成，发现 {total_new} 个新选项:")
                for key, count in results.items():
                    if count > 0:
                        print(f"  - {key}: {count}")
        except Exception as e:
            print(f"扫描可选项失败: {e}")
    
    def _create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="保存所有配置", command=self._save_all, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="导出到 UE", command=self._export_to_ue)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        
        # 工具菜单
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="工具", menu=tools_menu)
        tools_menu.add_command(label="验证所有配置", command=self._validate_all)
        tools_menu.add_command(label="查看依赖关系", command=self._show_dependencies)
        tools_menu.add_separator()
        tools_menu.add_command(label="刷新可选项", command=self._refresh_options)
        tools_menu.add_separator()
        tools_menu.add_command(label="打开属性生成器", command=self._open_attribute_generator)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="使用说明", command=self._show_help)
        help_menu.add_command(label="关于", command=self._show_about)
    
    def _create_ui(self):
        """创建主界面"""
        # 顶部生成工具栏
        self._create_generate_bar()
        
        # 创建主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 左侧：资产树视图
        left_frame = ttk.LabelFrame(main_frame, text="资产浏览器", width=300)
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 5))
        left_frame.pack_propagate(False)
        
        self._create_asset_tree(left_frame)
        
        # 右侧：标签页编辑器
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self._create_notebook(right_frame)
        
        # 底部状态栏
        self._create_status_bar()
    
    def _create_asset_tree(self, parent):
        """创建资产树视图"""
        # 搜索框
        search_frame = ttk.Frame(parent)
        search_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(search_frame, text="🔍").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self._on_search_changed)
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        # 树视图
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.asset_tree = ttk.Treeview(tree_frame, show='tree')
        self.asset_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.asset_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.asset_tree.configure(yscrollcommand=scrollbar.set)
        
        # 绑定事件
        self.asset_tree.bind('<Double-1>', self._on_tree_double_click)
        self.asset_tree.bind('<Button-3>', self._on_tree_right_click)
        
        # 初始化树节点
        self._init_tree_nodes()
    
    def _init_tree_nodes(self):
        """初始化树节点 - 显示扫描到的资产"""
        # 清空树
        for item in self.asset_tree.get_children():
            self.asset_tree.delete(item)
        
        # 分类配置：(分类ID, 显示名, 资产类型, 获取选项方法名)
        categories = [
            ("experiences", "📦 Experiences", "Experience", None),
            ("pawn_data", "👤 Pawn Data", "PawnData", "get_pawn_data_options"),
            ("input_configs", "🎮 Input Configs", "InputConfig", "get_input_config_options"),
            ("ability_sets", "⚔️ Ability Sets", "AbilitySet", "get_ability_set_options"),
            ("action_sets", "📋 Action Sets", "ActionSet", "get_action_set_options"),
        ]
        
        for cat_id, cat_name, asset_type, getter_name in categories:
            node = self.asset_tree.insert('', 'end', cat_id, text=cat_name, open=True)
            
            existing_names = set()
            
            # 从扫描结果获取资产列表
            if getter_name and hasattr(self.options_scanner, getter_name):
                getter = getattr(self.options_scanner, getter_name)
                options = getter()
                for opt in options:
                    name = opt.get("name", "Unknown")
                    existing_names.add(name)
                    self.asset_tree.insert(node, 'end', 
                                           f"{asset_type}:{name}",
                                           text=f"  {name}")
            
            # Experience 从配置文件加载
            if asset_type == "Experience":
                exp_assets = self.data_manager.load_assets("Experience")
                for name in exp_assets.keys():
                    if name != "version" and not name.startswith("_"):
                        existing_names.add(name)
                        self.asset_tree.insert(node, 'end',
                                               f"{asset_type}:{name}",
                                               text=f"  {name}")
            
            # 也添加 registry 中的（通过工具创建但还未生成到 Content 的）
            registry_assets = self.registry.get_by_type(asset_type)
            for asset in registry_assets:
                if asset.asset_name not in existing_names:
                    self.asset_tree.insert(node, 'end', 
                                           f"{asset_type}:{asset.asset_name}",
                                           text=f"  {asset.asset_name} (新)")
    
    def _create_notebook(self, parent):
        """创建标签页编辑器"""
        self.notebook = ttk.Notebook(parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # 1. 概览页面
        overview_frame = ttk.Frame(self.notebook)
        self.notebook.add(overview_frame, text=" 📊 概览 ")
        self._create_overview_page(overview_frame)
        
        # 2. Experience 编辑器
        exp_frame = ttk.Frame(self.notebook)
        self.notebook.add(exp_frame, text=" 📦 Experience ")
        self._create_asset_editor(exp_frame, "Experience")
        
        # 3. PawnData 编辑器
        pawn_frame = ttk.Frame(self.notebook)
        self.notebook.add(pawn_frame, text=" 👤 PawnData ")
        self._create_asset_editor(pawn_frame, "PawnData")
        
        # 4. InputConfig 编辑器
        input_frame = ttk.Frame(self.notebook)
        self.notebook.add(input_frame, text=" 🎮 InputConfig ")
        self._create_asset_editor(input_frame, "InputConfig")
        
        # 5. AbilitySet 编辑器
        ability_frame = ttk.Frame(self.notebook)
        self.notebook.add(ability_frame, text=" ⚔️ AbilitySet ")
        self._create_asset_editor(ability_frame, "AbilitySet")
        
        # 6. ActionSet 编辑器
        action_frame = ttk.Frame(self.notebook)
        self.notebook.add(action_frame, text=" 📋 ActionSet ")
        self._create_asset_editor(action_frame, "ActionSet")
        
        # 7. 依赖关系图
        deps_frame = ttk.Frame(self.notebook)
        self.notebook.add(deps_frame, text=" 🔗 依赖关系 ")
        self._create_placeholder(deps_frame, "依赖关系可视化")
    
    def _create_overview_page(self, parent):
        """创建概览页面"""
        # 统计信息
        stats_frame = ttk.LabelFrame(parent, text="资产统计")
        stats_frame.pack(fill=tk.X, padx=10, pady=10)
        
        stats_text = tk.Text(stats_frame, height=8, font=("Consolas", 11))
        stats_text.pack(fill=tk.X, padx=10, pady=10)
        
        # 更新统计
        stats = self._get_statistics()
        stats_text.insert('1.0', stats)
        stats_text.config(state='disabled')
        
        # 快速操作
        actions_frame = ttk.LabelFrame(parent, text="快速操作")
        actions_frame.pack(fill=tk.X, padx=10, pady=10)
        
        btn_frame = ttk.Frame(actions_frame)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="➕ 新建 Experience", 
                   command=lambda: self._new_asset("Experience")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="➕ 新建 PawnData", 
                   command=lambda: self._new_asset("PawnData")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="➕ 新建 InputConfig", 
                   command=lambda: self._new_asset("InputConfig")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="➕ 新建 AbilitySet", 
                   command=lambda: self._new_asset("AbilitySet")).pack(side=tk.LEFT, padx=5)
        
        # 最近修改
        recent_frame = ttk.LabelFrame(parent, text="最近修改")
        recent_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.recent_list = ttk.Treeview(recent_frame, columns=('type', 'name', 'time'), show='headings')
        self.recent_list.heading('type', text='类型')
        self.recent_list.heading('name', text='名称')
        self.recent_list.heading('time', text='修改时间')
        self.recent_list.column('type', width=120)
        self.recent_list.column('name', width=200)
        self.recent_list.column('time', width=180)
        self.recent_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self._refresh_recent_list()
    
    def _create_placeholder(self, parent, text):
        """创建占位页面"""
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True)
        
        label = ttk.Label(frame, text=f"🚧 {text}\n\n即将实现...", 
                         font=("Arial", 16), justify='center')
        label.pack(expand=True)
    
    def _create_asset_editor(self, parent, asset_type: str):
        """创建资产编辑器"""
        try:
            editor = BaseAssetEditor(
                parent=parent,
                asset_type=asset_type,
                schema_loader=self.schema_loader,
                data_manager=self.data_manager,
                app=self,
                options_scanner=self.options_scanner
            )
            self.editors[asset_type] = editor
            
        except Exception as e:
            import traceback
            traceback.print_exc()
            self._create_placeholder(parent, f"{asset_type} 编辑器 (加载失败: {e})")
    
    def _create_generate_bar(self):
        """创建生成操作栏"""
        bar = ttk.Frame(self.root)
        bar.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(bar, text="UE 资产生成:", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(bar, text="🚀 生成到 UE", 
                   command=self._generate_to_ue).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(bar, text="� 测试连接", 
                   command=self._test_ue_connection).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(bar, text="�📋 复制命令", 
                   command=self._copy_generate_command).pack(side=tk.LEFT, padx=5)
        
        # UE 连接状态
        self.ue_status = ttk.Label(bar, text="● UE 未连接", foreground="gray")
        self.ue_status.pack(side=tk.LEFT, padx=10)
        
        # 生成状态
        self.generate_status = ttk.Label(bar, text="", foreground="gray")
        self.generate_status.pack(side=tk.LEFT, padx=10)
        
        ttk.Separator(self.root).pack(fill=tk.X, padx=10, pady=2)
        
        # 初始化远程执行器
        self.ue_executor = UERemoteExecutor(PROJECT_ROOT)
        
        # 启动时检查连接
        self.root.after(1000, self._check_ue_connection)
    
    def _check_ue_connection(self):
        """检查 UE 连接状态"""
        if self.ue_executor.is_ue_running():
            self.ue_status.config(text="● UE 已连接", foreground="green")
        else:
            self.ue_status.config(text="● UE 未连接", foreground="gray")
        
        # 每 5 秒检查一次
        self.root.after(5000, self._check_ue_connection)
    
    def _test_ue_connection(self):
        """测试 UE 连接"""
        self.generate_status.config(text="正在连接...", foreground="blue")
        self.root.update()
        
        if self.ue_executor.is_ue_running():
            if self.ue_executor.connect():
                # 发送测试代码
                success, result = self.ue_executor.execute_code('import unreal; unreal.log("DataAsset Manager 连接成功!")')
                self.ue_executor.disconnect()
                
                if success:
                    self.ue_status.config(text="● UE 已连接", foreground="green")
                    self.generate_status.config(text="✅ 连接测试成功", foreground="green")
                else:
                    self.generate_status.config(text=f"⚠️ 执行失败: {result}", foreground="orange")
            else:
                self.generate_status.config(text="❌ 连接失败", foreground="red")
        else:
            self.ue_status.config(text="● UE 未连接", foreground="gray")
            self.generate_status.config(text="❌ UE 未运行或未启用远程执行", foreground="red")
            self._show_remote_setup_guide()
        
        self.root.after(3000, lambda: self.generate_status.config(text=""))
    
    def _generate_to_ue(self):
        """生成资产到 UE（通过远程执行）"""
        script_path = os.path.join(os.path.dirname(__file__), "ue_scripts", "generate_all.py")
        
        # 检查 UE 是否运行
        if not self.ue_executor.is_ue_running():
            self.generate_status.config(text="❌ UE 未运行", foreground="red")
            self._show_generate_guide(script_path)
            self.root.after(3000, lambda: self.generate_status.config(text=""))
            return
        
        self.generate_status.config(text="正在生成...", foreground="blue")
        self.root.update()
        
        # 连接并执行
        if self.ue_executor.connect():
            success, result = self.ue_executor.execute_file(script_path)
            self.ue_executor.disconnect()
            
            if success:
                self.generate_status.config(text="✅ 生成完成!", foreground="green")
                self.show_status("资产已生成到 UE")
            else:
                self.generate_status.config(text=f"⚠️ 生成失败", foreground="red")
                messagebox.showerror("生成失败", f"执行脚本时出错:\n\n{result}")
        else:
            self.generate_status.config(text="❌ 连接失败", foreground="red")
            self._show_generate_guide(script_path)
        
        self.root.after(5000, lambda: self.generate_status.config(text=""))
    
    def _copy_generate_command(self):
        """复制生成命令到剪贴板"""
        script_path = os.path.join(os.path.dirname(__file__), "ue_scripts", "generate_all.py")
        command = f'py "{script_path}"'
        
        self.root.clipboard_clear()
        self.root.clipboard_append(command)
        
        self.generate_status.config(text="✅ 命令已复制", foreground="green")
        self.root.after(2000, lambda: self.generate_status.config(text=""))
    
    def _show_remote_setup_guide(self):
        """显示远程执行设置指南"""
        monitor_script = os.path.join(os.path.dirname(__file__), "ue_scripts", "command_monitor.py").replace("\\", "/")
        
        guide = f"""UE 命令监控未运行

方法1：在 UE Output Log 底部执行：
ExecutePythonScript {monitor_script}

方法2：重启 UE 编辑器
已配置自动启动脚本 (Content/Python/init_unreal.py)

启动后，本工具可直接发送命令到 UE 执行。
"""
        # 复制命令
        cmd = f'ExecutePythonScript {monitor_script}'
        self.root.clipboard_clear()
        self.root.clipboard_append(cmd)
        
        messagebox.showinfo("启动命令监控", guide + "\n\n命令已复制到剪贴板。")
    
    def _show_generate_guide(self, script_path: str):
        """显示手动生成指南（备用方案）"""
        command = f'py "{script_path}"'
        
        # 复制命令
        self.root.clipboard_clear()
        self.root.clipboard_append(command)
        
        guide = f"""无法自动连接 UE，请手动执行：

1. 在 UE 中打开 Output Log
   (Window → Developer Tools → Output Log)

2. 在底部命令栏粘贴执行：
   {command}

命令已复制到剪贴板。

提示：启用 Python Remote Execution 可实现自动生成。
"""
        messagebox.showinfo("手动执行", guide)
    
    def _create_status_bar(self):
        """创建状态栏"""
        self.status_bar = ttk.Label(self.root, text="就绪", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def _bind_shortcuts(self):
        """绑定快捷键"""
        self.root.bind('<Control-s>', lambda e: self._save_all())
        self.root.bind('<Control-S>', lambda e: self._save_all())
        self.root.bind('<F5>', lambda e: self._refresh_all())
    
    # ===== 事件处理 =====
    
    def _on_search_changed(self, *args):
        """搜索框内容变化"""
        search_text = self.search_var.get().lower()
        # TODO: 实现搜索过滤
    
    def _on_tree_double_click(self, event):
        """树节点双击"""
        item = self.asset_tree.selection()
        if item:
            item_id = item[0]
            if ':' in item_id:  # 是资产节点
                asset_type, asset_name = item_id.split(':', 1)
                self._edit_asset(asset_type, asset_name)
    
    def _on_tree_right_click(self, event):
        """树节点右键菜单"""
        item = self.asset_tree.identify_row(event.y)
        if item:
            self.asset_tree.selection_set(item)
            menu = tk.Menu(self.root, tearoff=0)
            
            if ':' in item:  # 是资产节点
                menu.add_command(label="编辑", command=lambda: self._edit_asset(*item.split(':', 1)))
                menu.add_command(label="复制", command=lambda: self._duplicate_asset(*item.split(':', 1)))
                menu.add_command(label="删除", command=lambda: self._delete_asset(*item.split(':', 1)))
                menu.add_separator()
                menu.add_command(label="查看依赖", command=lambda: self._show_asset_deps(*item.split(':', 1)))
            else:  # 是分类节点
                menu.add_command(label="新建", command=lambda: self._new_asset_for_category(item))
            
            menu.post(event.x_root, event.y_root)
    
    # ===== 功能方法 =====
    
    def _get_statistics(self) -> str:
        """获取统计信息"""
        # 从扫描结果获取实际资产数量
        game_features = len(self.options_scanner.get_game_features())
        pawn_data = len(self.options_scanner.get_pawn_data_options())
        input_configs = len(self.options_scanner.get_input_config_options())
        ability_sets = len(self.options_scanner.get_ability_set_options())
        action_sets = len(self.options_scanner.get_action_set_options())
        input_actions = len(self.options_scanner.get_input_action_options())
        input_tags = len(self.options_scanner.get_input_tags())
        
        total = pawn_data + input_configs + ability_sets + action_sets
        
        stats = []
        stats.append(f"{'='*50}")
        stats.append(f"  {PROJECT_PREFIX} DataAsset 配置统计")
        stats.append(f"{'='*50}")
        stats.append(f"")
        stats.append(f"  🎮 GameFeatures:     {game_features} 个")
        stats.append(f"  👤 PawnData:         {pawn_data} 个")
        stats.append(f"  🎮 InputConfig:      {input_configs} 个")
        stats.append(f"  ⚔️ AbilitySet:       {ability_sets} 个")
        stats.append(f"  📋 ActionSet:        {action_sets} 个")
        stats.append(f"")
        stats.append(f"  📥 InputAction:      {input_actions} 个")
        stats.append(f"  🏷️ InputTag:         {input_tags} 个")
        stats.append(f"")
        stats.append(f"  资产总计: {total} 个")
        return '\n'.join(stats)
    
    def _refresh_recent_list(self):
        """刷新最近修改列表"""
        for item in self.recent_list.get_children():
            self.recent_list.delete(item)
        
        # 按更新时间排序
        sorted_assets = sorted(
            self.registry.assets.values(),
            key=lambda x: x.updated_at or '',
            reverse=True
        )[:10]  # 最近10个
        
        for asset in sorted_assets:
            self.recent_list.insert('', 'end', values=(
                asset.asset_type,
                asset.asset_name,
                asset.updated_at[:19] if asset.updated_at else ''
            ))
    
    def _refresh_all(self):
        """刷新所有"""
        self._init_tree_nodes()
        self._refresh_recent_list()
        self.show_status("已刷新")
    
    def _save_all(self):
        """保存所有配置"""
        self.registry.save()
        self.show_status("所有配置已保存")
    
    def _validate_all(self):
        """验证所有配置"""
        errors = self.registry.validate_dependencies()
        if errors:
            messagebox.showwarning("验证结果", f"发现 {len(errors)} 个问题:\n\n" + "\n".join(errors[:10]))
        else:
            messagebox.showinfo("验证结果", "所有配置验证通过！")
    
    def _export_to_ue(self):
        """导出到 UE"""
        # TODO: 实现导出逻辑
        messagebox.showinfo("导出", "导出功能即将实现...\n\n将生成 UE DataAsset 蓝图文件")
    
    def _show_dependencies(self):
        """显示依赖关系"""
        self.notebook.select(6)  # 切换到依赖关系页
    
    def _show_help(self):
        """显示帮助"""
        help_text = """
DJ01 DataAsset 配置管理器

功能说明：
1. 统一管理 Experience、PawnData、InputConfig、AbilitySet 等配置
2. 可视化编辑各种 DataAsset 的属性
3. 自动追踪资产之间的依赖关系
4. 支持导出到 Unreal Engine 资产

快捷键：
- Ctrl+S: 保存所有配置
- F5: 刷新
- F2: 重命名选中项
- Delete: 删除选中项

使用流程：
1. 在左侧资产树中选择或创建资产
2. 在右侧编辑器中配置属性
3. 保存配置并导出到 UE
        """
        messagebox.showinfo("使用说明", help_text)
    
    def _show_about(self):
        """显示关于"""
        messagebox.showinfo("关于", 
            f"{PROJECT_PREFIX} DataAsset 配置管理器\n\n"
            "版本: 1.0.0\n"
            "基于 Lyra 架构设计")
    
    def _new_asset(self, asset_type: str):
        """新建资产"""
        # TODO: 实现新建资产对话框
        messagebox.showinfo("新建", f"新建 {asset_type} 功能即将实现...")
    
    def _new_asset_for_category(self, category_id: str):
        """根据分类新建资产"""
        type_map = {
            "experiences": "Experience",
            "pawn_data": "PawnData",
            "input_configs": "InputConfig",
            "ability_sets": "AbilitySet",
            "ability_templates": "AbilityTemplate",
        }
        if category_id in type_map:
            self._new_asset(type_map[category_id])
    
    def _edit_asset(self, asset_type: str, asset_name: str):
        """编辑资产"""
        # 切换到对应的编辑器页面
        tab_map = {
            "Experience": 1,
            "PawnData": 2,
            "InputConfig": 3,
            "AbilitySet": 4,
            "AbilityTemplate": 5,
        }
        if asset_type in tab_map:
            self.notebook.select(tab_map[asset_type])
        # TODO: 加载资产数据到编辑器
    
    def _duplicate_asset(self, asset_type: str, asset_name: str):
        """复制资产"""
        # TODO: 实现复制功能
        pass
    
    def _delete_asset(self, asset_type: str, asset_name: str):
        """删除资产"""
        if messagebox.askyesno("确认删除", f"确定要删除 {asset_name} 吗？"):
            self.registry.unregister(asset_type, asset_name)
            self._init_tree_nodes()
            self.show_status(f"已删除 {asset_name}")
    
    def _show_asset_deps(self, asset_type: str, asset_name: str):
        """显示资产依赖"""
        deps = self.registry.get_dependencies(asset_type, asset_name)
        dependents = self.registry.get_dependents(asset_type, asset_name)
        
        msg = f"{asset_name} 的依赖关系:\n\n"
        msg += "依赖的资产:\n"
        for dep in deps:
            msg += f"  - {dep.asset_type}: {dep.asset_name}\n"
        if not deps:
            msg += "  (无)\n"
        
        msg += "\n被以下资产依赖:\n"
        for dep in dependents:
            msg += f"  - {dep.asset_type}: {dep.asset_name}\n"
        if not dependents:
            msg += "  (无)\n"
        
        messagebox.showinfo("依赖关系", msg)
    
    def _open_attribute_generator(self):
        """打开属性生成器"""
        import subprocess
        attr_gen_path = os.path.join(os.path.dirname(__file__), "..", "AttributeGenerator", "main.py")
        if os.path.exists(attr_gen_path):
            subprocess.Popen([sys.executable, attr_gen_path])
        else:
            messagebox.showerror("错误", "找不到属性生成器")
    
    def _refresh_options(self):
        """刷新可选项（重新扫描 GameFeatures 和 Content 目录等）"""
        try:
            # 扫描所有可选项
            results = self.options_scanner.update_all()
            
            # 同步已创建的配置到选项
            for asset_type in ["PawnData", "AbilitySet", "ActionSet", "InputConfig"]:
                config_data = self.data_manager.load_assets(asset_type)
                if config_data:
                    self.options_scanner.sync_from_config(asset_type, config_data)
            
            total_new = sum(results.values())
            
            details = "\n".join([f"  - {key}: {count} 个新增" 
                                 for key, count in results.items() if count > 0])
            if not details:
                details = "  (无新增)"
            
            self.show_status(f"已刷新可选项 (发现 {total_new} 个新选项)")
            messagebox.showinfo("刷新完成", 
                f"已刷新可选项配置:\n\n{details}\n\n"
                f"请重新打开编辑器以查看更新后的选项。")
        except Exception as e:
            import traceback
            traceback.print_exc()
            messagebox.showerror("错误", f"刷新可选项失败: {e}")
    
    def show_status(self, message: str):
        """显示状态消息"""
        self.status_bar.config(text=message)
        self.root.after(3000, lambda: self.status_bar.config(text="就绪"))


def main():
    root = tk.Tk()
    app = DataAssetManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
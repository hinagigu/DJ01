#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DJ01 DataAsset Manager - 选项扫描器
职责：扫描项目中的 GameFeature 插件和其他可选资产
"""

import os
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

@dataclass
class OptionItem:
    """可选项"""
    name: str
    display_name: str
    description: str = ""
    path: str = ""
    extra: Dict[str, Any] = field(default_factory=dict)

class OptionsScanner:
    """选项扫描器"""
    
    # 标签定义文件路径（相对于项目根目录）
    GAMEPLAY_TAGS_CSV = "Source/DJ01/System/Config/GameplayTagDefinitions.csv"
    GAMEPLAY_TAGS_JSON = "Source/DJ01/System/Config/GameplayTagDefinitions.json"  # 后备
    
    def __init__(self, project_root: str, options_path: str, scan_paths_file: str = None):
        """
        初始化选项扫描器
        
        Args:
            project_root: 项目根目录
            options_path: 选项配置路径（可以是文件或目录）
            scan_paths_file: 扫描路径配置文件
        """
        self.project_root = project_root
        self.options_path = options_path
        self.scan_paths_file = scan_paths_file
        self.options_data: Dict[str, Any] = {}
        self.scan_paths: Dict[str, Any] = {}
        self._gameplay_tags_cache: Dict[str, List[Dict[str, str]]] = {}
        
        self._load_scan_paths()
        self._load_options()
        self._load_gameplay_tags()
    
    def _load_scan_paths(self):
        """加载扫描路径配置"""
        if self.scan_paths_file and os.path.exists(self.scan_paths_file):
            try:
                with open(self.scan_paths_file, 'r', encoding='utf-8') as f:
                    self.scan_paths = json.load(f)
            except Exception as e:
                print(f"加载扫描路径配置失败: {e}")
                self.scan_paths = {}
        else:
            self.scan_paths = {}
    
    def save_scan_paths(self):
        """保存扫描路径配置"""
        if self.scan_paths_file:
            try:
                with open(self.scan_paths_file, 'w', encoding='utf-8') as f:
                    json.dump(self.scan_paths, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"保存扫描路径配置失败: {e}")
    
    def get_scan_config(self, key: str) -> Dict[str, Any]:
        """获取指定类型的扫描配置"""
        return self.scan_paths.get(key, {})
    
    def update_scan_config(self, key: str, config: Dict[str, Any]):
        """更新扫描配置"""
        self.scan_paths[key] = config
        self.save_scan_paths()
    
    def _load_options(self):
        """加载选项配置（支持目录或单文件）"""
        if os.path.isdir(self.options_path):
            self._load_options_from_directory()
        elif os.path.exists(self.options_path):
            self._load_options_from_file(self.options_path)
        else:
            # 创建目录
            os.makedirs(self.options_path, exist_ok=True)
            self.options_data = {}
    
    def _load_options_from_directory(self):
        """从目录加载多个选项文件"""
        self.options_data = {}
        for filename in os.listdir(self.options_path):
            if filename.endswith('.json'):
                file_path = os.path.join(self.options_path, filename)
                key = filename[:-5]  # 去掉 .json
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        self.options_data[key] = json.load(f)
                except Exception as e:
                    print(f"加载选项文件 {filename} 失败: {e}")
    
    def _load_options_from_file(self, file_path: str):
        """从单个文件加载选项"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.options_data = json.load(f)
        except Exception as e:
            print(f"加载选项配置失败: {e}")
            self.options_data = {}
    
    def _load_gameplay_tags(self):
        """加载 Gameplay 标签（优先 CSV，后备 JSON）"""
        csv_file = os.path.join(self.project_root, self.GAMEPLAY_TAGS_CSV)
        json_file = os.path.join(self.project_root, self.GAMEPLAY_TAGS_JSON)
        
        # 优先使用 CSV
        if os.path.exists(csv_file):
            self._load_tags_from_csv(csv_file)
        elif os.path.exists(json_file):
            self._load_tags_from_json(json_file)
        else:
            print(f"标签定义文件不存在")
    
    def _load_tags_from_csv(self, csv_file: str):
        """从 CSV 文件加载标签"""
        import csv
        
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                self._gameplay_tags_cache = {}
                count = 0
                
                for row in reader:
                    category = row.get("Category", "Other")
                    tag = row.get("Tag", "")
                    description = row.get("Description", "")
                    variable = row.get("VariableName", "")
                    
                    if not tag:
                        continue
                    
                    if category not in self._gameplay_tags_cache:
                        self._gameplay_tags_cache[category] = []
                    
                    self._gameplay_tags_cache[category].append({
                        "tag": tag,
                        "description": description,
                        "variable": variable
                    })
                    count += 1
                
                print(f"已从 CSV 加载 {count} 个 Gameplay 标签")
                
        except Exception as e:
            print(f"加载 CSV 标签失败: {e}")
    
    def _load_tags_from_json(self, json_file: str):
        """从 JSON 文件加载标签（后备方案）"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            self._gameplay_tags_cache = {}
            for tag_entry in tags_data.get("Tags", []):
                category = tag_entry.get("Category", "Other")
                tag = tag_entry.get("Tag", "")
                description = tag_entry.get("Description", "")
                
                if category not in self._gameplay_tags_cache:
                    self._gameplay_tags_cache[category] = []
                
                self._gameplay_tags_cache[category].append({
                    "tag": tag,
                    "description": description,
                    "variable": tag_entry.get("VariableName", "")
                })
            
            print(f"已从 JSON 加载 {sum(len(v) for v in self._gameplay_tags_cache.values())} 个 Gameplay 标签")
            
        except Exception as e:
            print(f"加载 JSON 标签失败: {e}")
    
    def save_options(self):
        """保存选项配置（支持目录或单文件）"""
        if os.path.isdir(self.options_path):
            self._save_options_to_directory()
        else:
            self._save_options_to_file(self.options_path)
    
    def _save_options_to_directory(self):
        """保存到目录（每个 key 一个文件）"""
        os.makedirs(self.options_path, exist_ok=True)
        for key, data in self.options_data.items():
            file_path = os.path.join(self.options_path, f"{key}.json")
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print(f"保存选项文件 {key}.json 失败: {e}")
    
    def _save_options_to_file(self, file_path: str):
        """保存到单个文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.options_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"保存选项配置失败: {e}")
    
    def scan_game_features(self) -> List[OptionItem]:
        """扫描项目中的 GameFeature 插件"""
        game_features_path = os.path.join(self.project_root, "Plugins", "GameFeatures")
        items = []
        
        if not os.path.exists(game_features_path):
            return items
        
        for entry in os.listdir(game_features_path):
            entry_path = os.path.join(game_features_path, entry)
            if os.path.isdir(entry_path):
                # 查找 .uplugin 文件来确认是插件
                uplugin_file = os.path.join(entry_path, f"{entry}.uplugin")
                if os.path.exists(uplugin_file):
                    # 尝试读取插件信息
                    display_name = entry
                    description = ""
                    try:
                        with open(uplugin_file, 'r', encoding='utf-8') as f:
                            plugin_data = json.load(f)
                            display_name = plugin_data.get("FriendlyName", entry)
                            description = plugin_data.get("Description", "")
                    except:
                        pass
                    
                    items.append(OptionItem(
                        name=entry,
                        display_name=display_name,
                        description=description,
                        path=f"Plugins/GameFeatures/{entry}"
                    ))
        
        return items
    
    def scan_content_assets(self, content_path: str, asset_type: str) -> List[OptionItem]:
        """
        扫描 Content 目录下的 .uasset 文件
        
        Args:
            content_path: 相对于 Content 的路径，如 "Characters/PawnData"
            asset_type: 资产类型名称，如 "PawnData"
        """
        full_path = os.path.join(self.project_root, "Content", content_path)
        items = []
        
        if not os.path.exists(full_path):
            return items
        
        for entry in os.listdir(full_path):
            if entry.endswith('.uasset'):
                name = entry[:-7]  # 移除 .uasset 后缀
                items.append(OptionItem(
                    name=name,
                    display_name=name,
                    description=f"{asset_type} 资产",
                    path=f"/Game/{content_path}/{name}"
                ))
        
        return items
    
    def update_pawn_data(self) -> int:
        """扫描并更新 PawnData 选项"""
        scanned = self.scan_content_assets("Characters/PawnData", "PawnData")
        return self._update_options("pawn_data", scanned)
    
    def update_ability_sets(self) -> int:
        """扫描并更新 AbilitySet 选项"""
        scanned = self.scan_content_assets("Gameplay/Abilities/AbilitySets", "AbilitySet")
        return self._update_options("ability_sets", scanned)
    
    def update_action_sets(self) -> int:
        """扫描并更新 ActionSet 选项"""
        scanned = self.scan_content_assets("System/ActionSets", "ActionSet")
        return self._update_options("action_sets", scanned)
    
    def update_input_configs(self) -> int:
        """扫描并更新 InputConfig 选项"""
        scanned = self.scan_content_assets("Input/InputConfig", "InputConfig")
        return self._update_options("input_configs", scanned)
    
    def update_input_actions(self) -> int:
        """扫描并更新 InputAction 选项（递归扫描）"""
        items = []
        config = self.get_scan_config("input_actions")
        prefixes = tuple(config.get("prefixes", ["IA_"]))
        
        for bp_path in config.get("blueprint_paths", ["Content/Input/Actions"]):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_input_action_assets_recursive(full_path, content_path, prefixes, items)
        
        return self._update_options_list("input_actions", items)
    
    def _scan_input_action_assets_recursive(self, full_path: str, content_path: str,
                                             prefixes: tuple, items: List[Dict]):
        """递归扫描 InputAction 资产"""
        if not os.path.exists(full_path):
            return
        
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            
            if os.path.isdir(entry_path):
                # 递归扫描子目录
                sub_content_path = f"{content_path}/{entry}"
                self._scan_input_action_assets_recursive(entry_path, sub_content_path, prefixes, items)
            elif entry.endswith('.uasset'):
                name = entry[:-7]
                # 检查前缀
                if not prefixes or name.startswith(prefixes):
                    asset_path = f"/Game/{content_path}/{name}"
                    items.append({
                        "name": name,  # 只存储名称，方便匹配
                        "display_name": name,
                        "description": "InputAction 资产",
                        "asset_path": asset_path
                    })
    
    def _update_options(self, option_key: str, scanned: List[OptionItem]) -> int:
        """更新指定类型的选项"""
        if option_key not in self.options_data:
            self.options_data[option_key] = {"items": []}
        
        existing_names = {item["name"] for item in self.options_data[option_key].get("items", [])}
        new_count = 0
        
        for item in scanned:
            if item.name not in existing_names:
                self.options_data[option_key]["items"].append({
                    "name": item.name,
                    "display_name": item.display_name,
                    "description": item.description,
                    "asset_path": item.path
                })
                new_count += 1
        
        if new_count > 0:
            self.save_options()
        
        return new_count
    
    def update_all(self) -> Dict[str, int]:
        """扫描并更新所有选项，返回各类型新增数量"""
        # 重新加载 Gameplay 标签
        self._load_gameplay_tags()
        
        results = {
            "game_features": self.update_game_features(),
            "pawn_data": self.update_pawn_data(),
            "ability_sets": self.update_ability_sets(),
            "action_sets": self.update_action_sets(),
            "input_configs": self.update_input_configs(),
            "input_actions": self.update_input_actions(),
            "input_tags": self._update_input_tags(),
            "pawn_classes": self._update_pawn_classes(),
            "camera_modes": self._update_camera_modes(),
            "gamefeature_actions": self._update_gamefeature_actions(),
            # GameFeature Actions 相关资产
            "input_mapping_contexts": self._update_input_mapping_contexts(),
            "gameplay_abilities": self._update_gameplay_abilities(),
            "attribute_sets": self._update_attribute_sets(),
            "gameplay_effects": self._update_gameplay_effects(),
            "widget_classes": self._update_widget_classes(),
            "activatable_widgets": self._update_activatable_widgets(),
            "ui_layer_tags": self._update_ui_layer_tags(),
            "ui_slot_tags": self._update_ui_slot_tags(),
        }
        return results
    
    def _update_pawn_classes(self) -> int:
        """根据配置扫描 Pawn/Character 类"""
        items = []
        config = self.get_scan_config("pawn_classes")
        
        # 1. 扫描 C++ 路径
        for cpp_path in config.get("cpp_paths", []):
            cpp_classes = self._scan_cpp_classes_in_path(cpp_path)
            items.extend(cpp_classes)
        
        # 2. 扫描蓝图路径
        for bp_path in config.get("blueprint_paths", []):
            # 去掉 Content/ 前缀
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            bp_classes = self._scan_blueprint_classes(content_path, "")
            items.extend(bp_classes)
        
        return self._update_options_list("pawn_classes", items)
    
    def _scan_cpp_classes_in_path(self, relative_path: str) -> List[Dict[str, str]]:
        """扫描指定路径下的 C++ 类"""
        import re
        items = []
        
        full_path = os.path.join(self.project_root, relative_path)
        if not os.path.exists(full_path):
            return items
        
        # 匹配类定义
        class_pattern = re.compile(
            r'class\s+\w*_API\s+(A\w+)\s*:\s*public\s+(A\w+)'
        )
        
        for filename in os.listdir(full_path):
            if not filename.endswith('.h'):
                continue
            
            file_path = os.path.join(full_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                for match in class_pattern.finditer(content):
                    class_name = match.group(1)
                    parent_class = match.group(2)
                    
                    # 去掉 A 前缀
                    short_name = class_name[1:] if class_name.startswith('A') else class_name
                    
                    items.append({
                        "name": f"/Script/DJ01.{short_name}",
                        "display_name": f"{short_name} (C++)",
                        "description": f"继承自 {parent_class}"
                    })
            except Exception as e:
                print(f"扫描文件 {file_path} 失败: {e}")
        
        return items
    
    def _update_camera_modes(self) -> int:
        """扫描并更新相机模式选项"""
        items = []
        
        # 扫描 Content/Characters/Cameras 下的相机模式蓝图
        camera_bps = self._scan_blueprint_classes("Characters/Cameras", "CM_")
        items.extend(camera_bps)
        
        return self._update_options_list("camera_modes", items)
    
    def _update_gamefeature_actions(self) -> int:
        """扫描并更新 GameFeature Actions 选项"""
        items = []
        config = self.get_scan_config("gamefeature_actions")
        
        # 1. 添加内置 GameFeature Actions
        builtin_actions = config.get("builtin_actions", [])
        for action in builtin_actions:
            action_name = action.get("name", "")
            items.append({
                "name": f"UGameFeatureAction_{action_name}",
                "display_name": action.get("display_name", action_name),
                "description": action.get("description", ""),
                "type": "builtin"
            })
        
        # 2. 扫描蓝图 Action 资产（递归）
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if os.path.exists(full_path):
                self._scan_gfa_assets_recursive(full_path, content_path, items)
        
        # 3. 扫描 GameFeature 插件中的 Actions（递归）
        gf_path = os.path.join(self.project_root, "Plugins", "GameFeatures")
        if os.path.exists(gf_path):
            for gf_name in os.listdir(gf_path):
                gf_content = os.path.join(gf_path, gf_name, "Content")
                if os.path.exists(gf_content):
                    self._scan_gfa_in_gamefeature_recursive(gf_content, gf_name, items)
        
        return self._update_options_list("gamefeature_actions", items)
    
    def _scan_gfa_assets_recursive(self, full_path: str, content_path: str, items: List[Dict]):
        """递归扫描 GameFeature Action 蓝图资产"""
        if not os.path.exists(full_path):
            return
        
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            
            if os.path.isdir(entry_path):
                sub_content_path = f"{content_path}/{entry}"
                self._scan_gfa_assets_recursive(entry_path, sub_content_path, items)
            elif entry.endswith('.uasset'):
                name = entry[:-7]
                if name.startswith(("GFA_", "Action_")):
                    asset_path = f"/Game/{content_path}/{name}"
                    items.append({
                        "name": asset_path,
                        "display_name": name,
                        "description": f"自定义 Action",
                        "type": "blueprint"
                    })
    
    def _scan_gfa_in_gamefeature_recursive(self, gf_content: str, gf_name: str, items: List[Dict]):
        """递归扫描 GameFeature 插件中的 Action 资产"""
        if not os.path.exists(gf_content):
            return
        
        for entry in os.listdir(gf_content):
            entry_path = os.path.join(gf_content, entry)
            
            if os.path.isdir(entry_path):
                self._scan_gfa_in_gamefeature_recursive(entry_path, gf_name, items)
            elif entry.endswith('.uasset'):
                name = entry[:-7]
                if name.startswith(("GFA_", "Action_")):
                    # 计算相对路径
                    rel_path = os.path.relpath(os.path.dirname(entry_path), 
                                               os.path.join(self.project_root, "Plugins", "GameFeatures", gf_name, "Content"))
                    if rel_path == ".":
                        asset_path = f"/{gf_name}/{name}"
                    else:
                        asset_path = f"/{gf_name}/{rel_path.replace(os.sep, '/')}/{name}"
                    items.append({
                        "name": asset_path,
                        "display_name": f"{name} ({gf_name})",
                        "description": f"来自 GameFeature: {gf_name}",
                        "type": "gamefeature"
                    })
    
    def get_gamefeature_action_options(self) -> List[Dict[str, str]]:
        """获取所有 GameFeature Actions 选项"""
        return self.options_data.get("gamefeature_actions", {}).get("items", [])
    
    def _update_input_mapping_contexts(self) -> int:
        """扫描并更新 InputMappingContext 选项（递归扫描）"""
        items = []
        config = self.get_scan_config("input_mapping_contexts")
        prefixes = tuple(config.get("prefixes", ["IMC_", "Mapping_"]))
        keywords = config.get("keywords", ["Mapping", "Context"])
        
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_assets_recursive_with_keywords(
                full_path, content_path, prefixes, keywords, items, "输入映射上下文"
            )
        
        return self._update_options_list("input_mapping_contexts", items)
    
    def _scan_assets_recursive_with_keywords(self, full_path: str, content_path: str,
                                              prefixes: tuple, keywords: List[str],
                                              items: List[Dict], description: str):
        """递归扫描资产，支持前缀和关键字匹配"""
        if not os.path.exists(full_path):
            return
        
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            
            if os.path.isdir(entry_path):
                # 递归扫描子目录
                sub_content_path = f"{content_path}/{entry}"
                self._scan_assets_recursive_with_keywords(
                    entry_path, sub_content_path, prefixes, keywords, items, description
                )
            elif entry.endswith('.uasset'):
                name = entry[:-7]
                # 检查前缀或关键字
                matches_prefix = name.startswith(prefixes) if prefixes else False
                matches_keyword = any(kw in name for kw in keywords) if keywords else False
                
                if matches_prefix or matches_keyword:
                    asset_path = f"/Game/{content_path}/{name}"
                    items.append({
                        "name": asset_path,
                        "display_name": name,
                        "description": description
                    })
    
    def get_input_mapping_context_options(self) -> List[Dict[str, str]]:
        """获取所有 InputMappingContext 选项"""
        return self.options_data.get("input_mapping_contexts", {}).get("items", [])
    
    def _update_gameplay_abilities(self) -> int:
        """扫描并更新 GameplayAbility 选项"""
        items = []
        config = self.get_scan_config("gameplay_abilities")
        prefixes = tuple(config.get("prefixes", ["GA_", "Ability_"]))
        
        # 1. 扫描 C++ 路径
        for cpp_path in config.get("cpp_paths", []):
            cpp_items = self._scan_cpp_ability_classes(cpp_path)
            items.extend(cpp_items)
        
        # 2. 扫描蓝图路径
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_blueprint_assets_recursive(full_path, content_path, prefixes, items, "技能")
        
        # 3. 扫描 AngelScript 脚本路径
        for script_path in config.get("script_paths", ["Script"]):
            script_items = self._scan_angelscript_ability_classes(script_path, prefixes)
            items.extend(script_items)
        
        return self._update_options_list("gameplay_abilities", items)
    
    def _scan_angelscript_ability_classes(self, relative_path: str, prefixes: tuple) -> List[Dict[str, str]]:
        """
        扫描 AngelScript 技能类
        
        AngelScript 类的特点:
        1. 类名通常带 U 前缀 (如 UGA_CastStone)
        2. 继承自 UGameplayAbility 或其子类 (如 UDJ01GameplayAbility)
        3. 使用 UFUNCTION(BlueprintOverride) 覆盖 ActivateAbility 等事件
        
        重要说明:
        - AngelScript 类在运行时由 AngelScript 插件动态生成 UASClass
        - 类路径格式为 /Script/AngelscriptCode.ClassName (不含 U 前缀)
        - 在 AbilitySet 中引用时，需使用正确的类路径
        """
        import re
        items = []
        
        full_path = os.path.join(self.project_root, relative_path)
        if not os.path.exists(full_path):
            return items
        
        # 匹配 AngelScript 类定义: class ClassName : ParentClass
        # 支持多行和各种空白字符
        class_pattern = re.compile(
            r'class\s+(U?\w+)\s*:\s*(U?\w+)',
            re.MULTILINE
        )
        
        # 检查是否是技能类的父类关键字
        ability_parent_keywords = [
            'GameplayAbility',
            'DJ01GameplayAbility', 
            'LyraGameplayAbility',
            'Ability'
        ]
        
        for root, dirs, files in os.walk(full_path):
            for filename in files:
                if not filename.endswith('.as'):
                    continue
                
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    for match in class_pattern.finditer(content):
                        class_name = match.group(1)
                        parent_class = match.group(2)
                        
                        # 检查是否是技能类（通过父类名判断）
                        is_ability_class = any(
                            kw in parent_class for kw in ability_parent_keywords
                        )
                        if not is_ability_class:
                            continue
                        
                        # 检查前缀（支持带 U 前缀和不带 U 前缀）
                        # UGA_xxx 匹配 GA_ 前缀，GA_xxx 也匹配 GA_ 前缀
                        check_name = class_name
                        if class_name.startswith('U'):
                            check_name = class_name[1:]  # 去掉 U 前缀再检查
                        
                        if prefixes and not check_name.startswith(prefixes):
                            continue
                        
                        # 计算相对路径（用于显示）
                        rel_file_path = os.path.relpath(file_path, self.project_root)
                        script_display_path = rel_file_path.replace('\\', '/')
                        
                        # AngelScript 类路径格式:
                        # 实际加载路径: /Script/Angelscript.ClassName
                        # 软引用格式: /Script/AngelscriptCode.ASClass'/Script/Angelscript.ClassName'
                        # 
                        # 为了兼容性，我们存储软引用格式，load_class_from_path 会自动提取内部路径
                        class_name_without_u = class_name[1:] if class_name.startswith('U') else class_name
                        as_class_path = f"/Script/AngelscriptCode.ASClass'/Script/Angelscript.{class_name_without_u}'"
                        
                        items.append({
                            "name": as_class_path,
                            "display_name": f"{class_name} (AngelScript)",
                            "description": f"继承自 {parent_class} | 脚本: {script_display_path}",
                            "script_path": script_display_path,
                            "class_name": class_name,
                            "parent_class": parent_class,
                            "source_type": "angelscript"
                        })
                except Exception as e:
                    print(f"扫描 AngelScript 文件失败: {file_path}, 错误: {e}")
        
        return items
    
    def _scan_angelscript_classes(self, relative_path: str, prefixes: tuple, base_class: str) -> List[Dict[str, str]]:
        """
        通用 AngelScript 类扫描方法
        
        Args:
            relative_path: 相对于项目根目录的脚本路径
            prefixes: 类名前缀过滤
            base_class: 基类名称关键字（用于过滤）
        """
        import re
        items = []
        
        full_path = os.path.join(self.project_root, relative_path)
        if not os.path.exists(full_path):
            return items
        
        # 匹配 AngelScript 类定义: class ClassName : ParentClass
        class_pattern = re.compile(
            r'class\s+(U?\w+)\s*:\s*(U?\w+)',
            re.MULTILINE
        )
        
        for root, dirs, files in os.walk(full_path):
            for filename in files:
                if not filename.endswith('.as'):
                    continue
                
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    for match in class_pattern.finditer(content):
                        class_name = match.group(1)
                        parent_class = match.group(2)
                        
                        # 检查是否匹配基类
                        if base_class and base_class not in parent_class:
                            continue
                        
                        # 检查前缀
                        check_name = class_name
                        if class_name.startswith('U'):
                            check_name = class_name[1:]
                        
                        if prefixes and not check_name.startswith(prefixes):
                            continue
                        
                        # 计算相对路径
                        rel_file_path = os.path.relpath(file_path, self.project_root)
                        script_path = rel_file_path.replace('\\', '/')
                        
                        # AngelScript 类路径格式:
                        # 软引用: /Script/AngelscriptCode.ASClass'/Script/Angelscript.ClassName'
                        class_name_without_u = class_name[1:] if class_name.startswith('U') else class_name
                        as_class_path = f"/Script/AngelscriptCode.ASClass'/Script/Angelscript.{class_name_without_u}'"
                        
                        items.append({
                            "name": as_class_path,
                            "display_name": f"{class_name} (AngelScript)",
                            "description": f"继承自 {parent_class}",
                            "script_path": script_path,
                            "source_type": "angelscript"
                        })
                except Exception as e:
                    pass
        
        return items
    
    def _scan_cpp_ability_classes(self, relative_path: str) -> List[Dict[str, str]]:
        """
        扫描 C++ 技能类
        
        C++ 类的特点:
        1. 类名带 U 前缀 (如 UDJ01GameplayAbility)
        2. UE 类引用路径不含 U 前缀: /Script/DJ01.DJ01GameplayAbility
        """
        import re
        items = []
        
        full_path = os.path.join(self.project_root, relative_path)
        if not os.path.exists(full_path):
            return items
        
        # 匹配 UGameplayAbility 子类
        class_pattern = re.compile(
            r'class\s+\w*_API\s+(U\w+)\s*:\s*public\s+(U\w*(?:Gameplay)?Ability\w*)'
        )
        
        for root, dirs, files in os.walk(full_path):
            for filename in files:
                if not filename.endswith('.h'):
                    continue
                
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    for match in class_pattern.finditer(content):
                        class_name = match.group(1)  # e.g., UDJ01GameplayAbility
                        parent_class = match.group(2)
                        
                        # UE 类引用路径不含 U 前缀
                        class_path_name = class_name[1:] if class_name.startswith('U') else class_name
                        
                        items.append({
                            "name": f"/Script/DJ01.{class_path_name}",
                            "display_name": f"{class_name} (C++)",
                            "description": f"继承自 {parent_class}",
                            "source_type": "cpp"
                        })
                except Exception as e:
                    pass
        
        return items
    
    def get_gameplay_ability_options(self) -> List[Dict[str, str]]:
        """获取所有 GameplayAbility 选项"""
        return self.options_data.get("gameplay_abilities", {}).get("items", [])
    
    def _update_attribute_sets(self) -> int:
        """扫描并更新 AttributeSet 选项"""
        import re
        import csv
        items = []
        config = self.get_scan_config("attribute_sets")
        
        # 1. 从 AttributeDefinitions.csv 读取 SetName 列表
        csv_config = config.get("csv_config")
        if csv_config:
            csv_path = os.path.join(self.project_root, csv_config)
            if os.path.exists(csv_path):
                try:
                    set_names = set()
                    with open(csv_path, 'r', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            set_name = row.get('SetName', '').strip()
                            if set_name:
                                set_names.add(set_name)
                    
                    for set_name in sorted(set_names):
                        # 生成类名：SetName -> DJ01{SetName}
                        # 注意：UE 类路径不包含 U 前缀，但实际 C++ 类名是 UDJ01{SetName}
                        class_path_name = f"DJ01{set_name}"
                        display_name = f"UDJ01{set_name}"
                        items.append({
                            "name": f"/Script/DJ01.{class_path_name}",
                            "display_name": display_name,
                            "description": f"属性集 (来自 AttributeDefinitions.csv)"
                        })
                except Exception as e:
                    print(f"读取 AttributeDefinitions.csv 失败: {e}")
        
        # 2. 扫描 C++ 路径（作为补充）
        for cpp_path in config.get("cpp_paths", []):
            full_path = os.path.join(self.project_root, cpp_path)
            if not os.path.exists(full_path):
                continue
            
            # 匹配 UAttributeSet 子类
            class_pattern = re.compile(
                r'class\s+\w*_API\s+(U\w+AttributeSet\w*)\s*:\s*public\s+(UAttributeSet|U\w+AttributeSet)'
            )
            
            for root, dirs, files in os.walk(full_path):
                for filename in files:
                    if not filename.endswith('.h'):
                        continue
                    
                    file_path = os.path.join(root, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        
                        for match in class_pattern.finditer(content):
                            class_name = match.group(1)  # e.g., UDJ01StatSet
                            
                            # UE 类路径不包含 U 前缀
                            class_path_name = class_name[1:] if class_name.startswith('U') else class_name
                            
                            # 避免重复添加
                            existing_names = {item["name"] for item in items}
                            item_name = f"/Script/DJ01.{class_path_name}"
                            if item_name not in existing_names:
                                items.append({
                                    "name": item_name,
                                    "display_name": class_name,
                                    "description": "属性集 (C++)"
                                })
                    except Exception as e:
                        pass
        
        return self._update_options_list("attribute_sets", items)
    
    def get_attribute_set_options(self) -> List[Dict[str, str]]:
        """获取所有 AttributeSet 选项"""
        return self.options_data.get("attribute_sets", {}).get("items", [])
    
    def _update_gameplay_effects(self) -> int:
        """扫描并更新 GameplayEffect 选项"""
        items = []
        config = self.get_scan_config("gameplay_effects")
        prefixes = tuple(config.get("prefixes", ["GE_", "Effect_"]))
        
        # 扫描蓝图路径
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_blueprint_assets_recursive(full_path, content_path, prefixes, items, "GameplayEffect")
        
        return self._update_options_list("gameplay_effects", items)
    
    def get_gameplay_effect_options(self) -> List[Dict[str, str]]:
        """获取所有 GameplayEffect 选项"""
        return self.options_data.get("gameplay_effects", {}).get("items", [])
    
    def _update_gameplay_effects(self) -> int:
        """扫描并更新 GameplayEffect 选项"""
        items = []
        config = self.get_scan_config("gameplay_effects")
        prefixes = tuple(config.get("prefixes", ["GE_", "Effect_"]))
        
        # 扫描蓝图路径
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_blueprint_assets_recursive(full_path, content_path, prefixes, items, "GameplayEffect")
        
        return self._update_options_list("gameplay_effects", items)
    
    def get_gameplay_effect_options(self) -> List[Dict[str, str]]:
        """获取所有 GameplayEffect 选项"""
        return self.options_data.get("gameplay_effects", {}).get("items", [])
    
    def _update_widget_classes(self) -> int:
        """扫描并更新 Widget 类选项"""
        items = []
        config = self.get_scan_config("widget_classes")
        prefixes = tuple(config.get("prefixes", ["W_", "WBP_", "UI_"]))
        
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_blueprint_assets_recursive(full_path, content_path, prefixes, items, "Widget")
        
        return self._update_options_list("widget_classes", items)
    
    def get_widget_class_options(self) -> List[Dict[str, str]]:
        """获取所有 Widget 类选项"""
        return self.options_data.get("widget_classes", {}).get("items", [])
    
    def _update_activatable_widgets(self) -> int:
        """扫描并更新 ActivatableWidget 类选项"""
        items = []
        config = self.get_scan_config("activatable_widgets")
        prefixes = tuple(config.get("prefixes", ["W_", "WBP_", "Layout_"]))
        
        for bp_path in config.get("blueprint_paths", []):
            content_path = bp_path.replace("Content/", "") if bp_path.startswith("Content/") else bp_path
            full_path = os.path.join(self.project_root, "Content", content_path)
            
            if not os.path.exists(full_path):
                continue
            
            self._scan_blueprint_assets_recursive(full_path, content_path, prefixes, items, "Layout Widget")
        
        return self._update_options_list("activatable_widgets", items)
    
    def get_activatable_widget_options(self) -> List[Dict[str, str]]:
        """获取所有 ActivatableWidget 类选项"""
        return self.options_data.get("activatable_widgets", {}).get("items", [])
    
    def _update_ui_layer_tags(self) -> int:
        """更新 UI 层级标签选项"""
        config = self.get_scan_config("ui_layer_tags")
        tag_category = config.get("tag_category", "UI.Layer")
        
        # 从 gameplay tags 中获取 UI.Layer 分类的标签
        items = []
        for category, tags in self._gameplay_tags_cache.items():
            for tag_info in tags:
                tag = tag_info.get("tag", "")
                if tag.startswith(tag_category):
                    items.append({
                        "name": tag,
                        "display_name": tag,
                        "description": tag_info.get("description", "")
                    })
        
        return self._update_options_list("ui_layer_tags", items)
    
    def get_ui_layer_tag_options(self) -> List[Dict[str, str]]:
        """获取所有 UI 层级标签选项"""
        return self.options_data.get("ui_layer_tags", {}).get("items", [])
    
    def _update_ui_slot_tags(self) -> int:
        """更新 UI 插槽标签选项"""
        config = self.get_scan_config("ui_slot_tags")
        tag_category = config.get("tag_category", "UI.Slot")
        
        # 从 gameplay tags 中获取 UI.Slot 分类的标签
        items = []
        for category, tags in self._gameplay_tags_cache.items():
            for tag_info in tags:
                tag = tag_info.get("tag", "")
                if tag.startswith(tag_category):
                    items.append({
                        "name": tag,
                        "display_name": tag,
                        "description": tag_info.get("description", "")
                    })
        
        return self._update_options_list("ui_slot_tags", items)
    
    def get_ui_slot_tag_options(self) -> List[Dict[str, str]]:
        """获取所有 UI 插槽标签选项"""
        return self.options_data.get("ui_slot_tags", {}).get("items", [])
    
    def _scan_blueprint_assets_recursive(self, full_path: str, content_path: str, 
                                          prefixes: tuple, items: List[Dict], 
                                          asset_type: str):
        """递归扫描蓝图资产"""
        if not os.path.exists(full_path):
            return
        
        for entry in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry)
            
            if os.path.isdir(entry_path):
                # 递归子目录
                sub_content_path = f"{content_path}/{entry}"
                self._scan_blueprint_assets_recursive(entry_path, sub_content_path, 
                                                       prefixes, items, asset_type)
            elif entry.endswith('.uasset'):
                name = entry[:-7]
                # 检查前缀（如果有指定）
                if not prefixes or name.startswith(prefixes):
                    asset_path = f"/Game/{content_path}/{name}.{name}_C"
                    items.append({
                        "name": asset_path,
                        "display_name": f"{name}",
                        "description": f"{asset_type}: {content_path}"
                    })
    
    def _scan_blueprint_classes(self, content_path: str, prefix: str = "") -> List[Dict[str, str]]:
        """扫描指定目录下的蓝图类"""
        full_path = os.path.join(self.project_root, "Content", content_path)
        items = []
        
        if not os.path.exists(full_path):
            return items
        
        for entry in os.listdir(full_path):
            if entry.endswith('.uasset'):
                name = entry[:-7]  # 去掉 .uasset
                if prefix and not name.startswith(prefix):
                    continue
                
                # 蓝图类路径格式
                asset_path = f"/Game/{content_path}/{name}.{name}_C"
                items.append({
                    "name": asset_path,
                    "display_name": f"{name} (Blueprint)",
                    "description": f"蓝图类: {content_path}"
                })
        
        return items
    
    def _update_options_list(self, option_key: str, items: List[Dict[str, str]]) -> int:
        """更新选项列表（直接替换）"""
        if option_key not in self.options_data:
            self.options_data[option_key] = {}
        
        self.options_data[option_key]["items"] = items
        self.save_options()
        return len(items)
    
    def get_pawn_class_options(self) -> List[Dict[str, str]]:
        """获取所有 Pawn 类选项"""
        return self.options_data.get("pawn_classes", {}).get("items", [])
    
    def get_camera_mode_options(self) -> List[Dict[str, str]]:
        """获取所有相机模式选项"""
        return self.options_data.get("camera_modes", {}).get("items", [])
    
    def _update_input_tags(self) -> int:
        """将 InputTag 分类的标签同步到选项配置"""
        input_tags = self._gameplay_tags_cache.get("InputTag", [])
        
        if "input_tags" not in self.options_data:
            self.options_data["input_tags"] = {"items": []}
        
        # 直接替换为最新的标签列表
        self.options_data["input_tags"]["items"] = [
            {
                "name": tag["tag"],
                "display_name": tag["tag"],
                "description": tag.get("description", "")
            }
            for tag in input_tags
        ]
        
        self.save_options()
        return len(input_tags)
    
    def get_input_tags(self) -> List[Dict[str, str]]:
        """获取 InputTag 选项"""
        return self.options_data.get("input_tags", {}).get("items", [])
    
    def update_game_features(self) -> int:
        """扫描并更新 GameFeature 选项，返回新增数量"""
        scanned = self.scan_game_features()
        
        if "game_features" not in self.options_data:
            self.options_data["game_features"] = {"items": []}
        
        existing_names = {item["name"] for item in self.options_data["game_features"].get("items", [])}
        new_count = 0
        
        for item in scanned:
            if item.name not in existing_names:
                self.options_data["game_features"]["items"].append({
                    "name": item.name,
                    "display_name": item.display_name,
                    "description": item.description,
                    "plugin_path": item.path
                })
                new_count += 1
        
        if new_count > 0:
            self.save_options()
        
        return new_count
    
    def get_game_features(self) -> List[Dict[str, str]]:
        """获取所有 GameFeature 选项"""
        return self.options_data.get("game_features", {}).get("items", [])
    
    def get_pawn_data_options(self) -> List[Dict[str, str]]:
        """获取所有 PawnData 选项"""
        return self.options_data.get("pawn_data", {}).get("items", [])
    
    def get_ability_set_options(self) -> List[Dict[str, str]]:
        """获取所有 AbilitySet 选项"""
        return self.options_data.get("ability_sets", {}).get("items", [])
    
    def get_action_set_options(self) -> List[Dict[str, str]]:
        """获取所有 ActionSet 选项"""
        return self.options_data.get("action_sets", {}).get("items", [])
    
    def get_input_config_options(self) -> List[Dict[str, str]]:
        """获取所有 InputConfig 选项"""
        return self.options_data.get("input_configs", {}).get("items", [])
    
    def get_pawn_class_options(self) -> List[Dict[str, str]]:
        """获取所有 Pawn 类选项"""
        return self.options_data.get("pawn_classes", {}).get("items", [])
    
    def get_camera_mode_options(self) -> List[Dict[str, str]]:
        """获取所有相机模式选项"""
        return self.options_data.get("camera_modes", {}).get("items", [])
    
    def get_gameplay_tags(self, category: str = None) -> List[str]:
        """
        获取 Gameplay 标签列表
        优先从 GameplayTagDefinitions.json 获取，否则使用配置文件
        """
        # 优先使用从 JSON 文件加载的标签
        if self._gameplay_tags_cache:
            if category:
                tags = self._gameplay_tags_cache.get(category, [])
                return [t["tag"] for t in tags]
            
            # 返回所有标签
            all_tags = []
            for tags in self._gameplay_tags_cache.values():
                all_tags.extend([t["tag"] for t in tags])
            return all_tags
        
        # 回退到配置文件中的标签
        tags_data = self.options_data.get("gameplay_tags", {}).get("categories", {})
        
        if category:
            return tags_data.get(category, {}).get("tags", [])
        
        all_tags = []
        for cat_data in tags_data.values():
            all_tags.extend(cat_data.get("tags", []))
        return all_tags
    
    def get_gameplay_tags_with_info(self, category: str = None) -> List[Dict[str, str]]:
        """获取带描述信息的 Gameplay 标签列表"""
        if not self._gameplay_tags_cache:
            return []
        
        if category:
            return self._gameplay_tags_cache.get(category, [])
        
        all_tags = []
        for tags in self._gameplay_tags_cache.values():
            all_tags.extend(tags)
        return all_tags
    
    def get_gameplay_tag_categories(self) -> List[str]:
        """获取所有标签分类"""
        return list(self._gameplay_tags_cache.keys())
    
    def get_input_action_options(self) -> List[Dict[str, str]]:
        """获取所有 InputAction 选项"""
        return self.options_data.get("input_actions", {}).get("items", [])
    
    def sync_from_config(self, config_type: str, config_data: Dict[str, Any]):
        """从配置数据同步选项（如已创建的 PawnData 等）"""
        option_key = {
            "PawnData": "pawn_data",
            "AbilitySet": "ability_sets",
            "ActionSet": "action_sets",
            "InputConfig": "input_configs",
        }.get(config_type)
        
        if not option_key:
            return
        
        if option_key not in self.options_data:
            self.options_data[option_key] = {"items": []}
        
        existing_names = {item["name"] for item in self.options_data[option_key].get("items", [])}
        
        for name, data in config_data.items():
            if name not in existing_names:
                self.options_data[option_key]["items"].append({
                    "name": name,
                    "display_name": data.get("display_name", name),
                    "description": data.get("description", ""),
                    "asset_path": data.get("asset_path", "")
                })
        
        self.save_options()
"""
DJ01 DataAsset 生成器 - 公共工具函数
"""

import unreal
import json
import os

# 配置文件路径 - 使用 UE 项目路径
PROJECT_DIR = unreal.Paths.project_dir().rstrip('/')
CONFIG_DIR = os.path.join(PROJECT_DIR, "Tools", "DataAssetManager", "configs")

# 资产路径配置
ASSET_PATHS = {
    "experience": "/Game/System/Experiences",
    "pawn_data": "/Game/Characters/PawnData",
    "ability_set": "/Game/Gameplay/Abilities/AbilitySets",
    "input_config": "/Game/Input/InputConfig",
    "action_set": "/Game/System/ActionSets",
}


def load_config(config_name: str) -> dict:
    """加载 JSON 配置"""
    config_path = os.path.join(CONFIG_DIR, f"{config_name}.json")
    unreal.log(f"加载配置: {config_path}")
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    unreal.log_warning(f"配置文件不存在: {config_path}")
    return {}


def get_config_data(config: dict, *keys) -> dict:
    """从配置中获取数据，尝试多个可能的 key"""
    for key in keys:
        if key in config:
            return config[key]
    return {}


def resolve_asset_path(name_or_path: str, asset_type: str) -> str:
    """解析资产路径，如果只是名称则构造完整路径"""
    if not name_or_path:
        return ""
    
    # 已经是完整路径
    if name_or_path.startswith("/Game") or name_or_path.startswith("/Script"):
        return name_or_path
    
    # 移除显示后缀如 "(Blueprint)", "(C++)" 等
    clean_name = name_or_path.split(" (")[0].strip()
    
    # 根据类型构造路径
    base_path = ASSET_PATHS.get(asset_type, "/Game")
    return f"{base_path}/{clean_name}"


def resolve_class_path(name_or_path: str) -> str:
    """解析类路径"""
    if not name_or_path:
        return ""
    
    # 已经是脚本路径
    if name_or_path.startswith("/Script"):
        return name_or_path
    
    # 蓝图类 - 移除后缀
    clean_name = name_or_path.split(" (")[0].strip()
    
    # 如果以 BP_ 开头，可能是蓝图
    if clean_name.startswith("BP_"):
        possible_paths = [
            f"/Game/Characters/Heroes/{clean_name}.{clean_name}_C",
            f"/Game/Characters/{clean_name}.{clean_name}_C",
            f"/Game/Blueprints/{clean_name}.{clean_name}_C",
        ]
        for path in possible_paths:
            if unreal.EditorAssetLibrary.does_asset_exist(path.rsplit(".", 1)[0]):
                return path
    
    # 如果以 CM_ 开头，是相机模式
    if clean_name.startswith("CM_"):
        possible_paths = [
            f"/Game/Characters/Cameras/{clean_name}.{clean_name}_C",
            f"/Game/System/Cameras/{clean_name}.{clean_name}_C",
        ]
        for path in possible_paths:
            if unreal.EditorAssetLibrary.does_asset_exist(path.rsplit(".", 1)[0]):
                return path
    
    return name_or_path


def resolve_input_action_path(name_or_path: str) -> str:
    """解析 InputAction 资产路径"""
    if not name_or_path:
        return ""
    
    # 已经是完整路径
    if name_or_path.startswith("/Game"):
        return name_or_path
    
    # 移除显示后缀
    clean_name = name_or_path.split(" (")[0].strip()
    
    # 从名称构造路径
    return f"/Game/Input/Actions/{clean_name}"


def extract_class_path_for_import(class_path: str) -> str:
    """
    从类路径中提取用于 import_text 的路径格式
    
    输入格式:
    - C++: /Script/DJ01.DJ01GameplayAbility
    - Blueprint: /Game/.../BP_xxx.BP_xxx_C
    - AngelScript 软引用: /Script/AngelscriptCode.ASClass'/Script/Angelscript.GA_xxx'
    
    输出格式:
    - C++: /Script/DJ01.DJ01GameplayAbility
    - Blueprint: /Game/.../BP_xxx.BP_xxx_C
    - AngelScript: /Script/Angelscript.GA_xxx (提取内部路径)
    """
    if not class_path:
        return ""
    
    # AngelScript 软引用格式: 提取单引号内的路径
    if "ASClass'" in class_path and "'" in class_path:
        parts = class_path.split("'")
        if len(parts) >= 2:
            return parts[1]
    
    return class_path


def load_class_from_path(class_path: str):
    """
    从路径加载类，支持多种格式
    """
    if not class_path:
        return None
    
    actual_path = extract_class_path_for_import(class_path)
    
    try:
        loaded_class = unreal.load_class(None, actual_path)
        if loaded_class:
            return loaded_class
    except Exception as e:
        unreal.log_warning(f"  加载类失败: {actual_path}, {e}")
    
    return None


def set_struct_gameplay_tag(struct_instance, property_name: str, tag_name: str) -> bool:
    """
    在结构体实例上设置 GameplayTag 属性
    """
    if not tag_name:
        unreal.log_warning(f"  {property_name}: tag_name 为空")
        return False
    
    try:
        tag = struct_instance.get_editor_property(property_name)
        tag.import_text(tag_name)
        struct_instance.set_editor_property(property_name, tag)
        return True
    except Exception as e:
        unreal.log_warning(f"  设置 {property_name} = '{tag_name}' 失败: {e}")
        return False
"""
DJ01 DataAsset 生成器 - 入口脚本

在 UE Editor 中执行此脚本来创建各类 DataAsset

使用方法：
1. 在 UE Editor 中打开 Output Log
2. 执行: ExecutePythonScript D:/UnrealProjects/DJ01/Tools/DataAssetManager/ue_scripts/generate_all.py
"""

import sys
import os

# 将当前脚本目录添加到 Python 路径，确保能找到 generators 包
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import unreal

from generators.base import (
    ASSET_PATHS, CONFIG_DIR,
    load_config, get_config_data
)
from generators import (
    create_pawn_data, delete_pawn_data,
    create_ability_set, delete_ability_set,
    create_input_config, delete_input_config,
    create_action_set,
    create_experience_blueprint, delete_experience,
)


def sync_deletions():
    """同步删除 - 删除 UE 中存在但配置中不存在的资产"""
    unreal.log("\n🗑️ 检查需要删除的资产...")
    
    deleted_count = 0
    
    # 检查 Experience
    exp_config = load_config("experiences")
    exp_data = get_config_data(exp_config, "experience", "experiences", "Experience")
    config_exp_names = set(k for k in exp_data.keys() if not k.startswith("_") and k != "version")
    
    exp_path = ASSET_PATHS["experience"]
    ue_exp_assets = unreal.EditorAssetLibrary.list_assets(exp_path, recursive=False)
    
    for asset_path in ue_exp_assets:
        asset_name = asset_path.split("/")[-1].split(".")[0]
        if asset_name not in config_exp_names:
            if delete_experience(asset_name):
                deleted_count += 1
    
    # 检查 PawnData
    pawn_config = load_config("pawn_data")
    pawn_data = get_config_data(pawn_config, "pawndata", "pawn_data", "PawnData")
    config_pawn_names = set(k for k in pawn_data.keys() if not k.startswith("_") and k != "version")
    
    pawn_path = ASSET_PATHS["pawn_data"]
    ue_pawn_assets = unreal.EditorAssetLibrary.list_assets(pawn_path, recursive=False)
    
    for asset_path in ue_pawn_assets:
        asset_name = asset_path.split("/")[-1].split(".")[0]
        if asset_name not in config_pawn_names:
            if delete_pawn_data(asset_name):
                deleted_count += 1
    
    return deleted_count


def generate_all_from_config():
    """从配置文件生成所有资产"""
    
    unreal.log("=" * 60)
    unreal.log("[DataAssetManager] 开始生成资产...")
    unreal.log(f"配置目录: {CONFIG_DIR}")
    unreal.log("=" * 60)
    
    created_count = 0
    updated_count = 0
    
    # 1. 生成 AbilitySets（被其他资产依赖，先创建）
    unreal.log("\n📦 处理 AbilitySet...")
    ability_config = load_config("ability_sets")
    ability_data = get_config_data(ability_config, "abilityset", "ability_sets", "AbilitySet")
    
    for name, data in ability_data.items():
        if name.startswith("_") or name == "version":
            continue
        result = create_ability_set(name, data)
        if result:
            created_count += 1
    
    # 2. 生成 InputConfigs（被 PawnData 依赖）
    unreal.log("\n🎮 处理 InputConfig...")
    input_config = load_config("input_configs")
    input_data = get_config_data(input_config, "inputconfig", "input_configs", "InputConfig")
    
    for name, data in input_data.items():
        if name.startswith("_") or name == "version":
            continue
        result = create_input_config(name, data)
        if result:
            created_count += 1
    
    # 3. 生成 PawnData（被 Experience 依赖）
    unreal.log("\n👤 处理 PawnData...")
    pawn_config = load_config("pawn_data")
    pawn_data = get_config_data(pawn_config, "pawndata", "pawn_data", "PawnData")
    
    for name, data in pawn_data.items():
        if name.startswith("_") or name == "version":
            continue
        result = create_pawn_data(name, data)
        if result:
            created_count += 1
    
    # 4. 生成 ActionSets（被 Experience 依赖）
    unreal.log("\n📋 处理 ActionSet...")
    action_set_config = load_config("action_sets")
    action_set_data = get_config_data(action_set_config, "actionset", "action_sets", "ActionSet")
    
    for name, data in action_set_data.items():
        if name.startswith("_") or name == "version":
            continue
        
        base_path = ASSET_PATHS["action_set"]
        package_path = f"{base_path}/{name}"
        existed = unreal.EditorAssetLibrary.does_asset_exist(package_path)
        
        result = create_action_set(name, data)
        if result:
            if existed:
                updated_count += 1
            else:
                created_count += 1
    
    # 5. 生成 Experiences（依赖其他资产，最后处理）
    unreal.log("\n🎯 处理 Experience...")
    exp_config = load_config("experiences")
    exp_data = get_config_data(exp_config, "experience", "experiences", "Experience")
    
    for name, data in exp_data.items():
        if name.startswith("_") or name == "version":
            continue
        
        base_path = ASSET_PATHS["experience"]
        package_path = f"{base_path}/{name}"
        existed = unreal.EditorAssetLibrary.does_asset_exist(package_path)
        
        result = create_experience_blueprint(name, data)
        if result:
            if existed:
                updated_count += 1
            else:
                created_count += 1
    
    # 6. 同步删除
    deleted_count = sync_deletions()
    
    unreal.log("\n" + "=" * 60)
    unreal.log(f"[DataAssetManager] 生成完成!")
    unreal.log(f"  ✅ 新建: {created_count} 个")
    unreal.log(f"  🔄 更新: {updated_count} 个")
    unreal.log(f"  🗑️ 删除: {deleted_count} 个")
    unreal.log("=" * 60)


# 入口点
if __name__ == "__main__":
    generate_all_from_config()
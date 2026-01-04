"""
DJ01 DataAsset 生成器 - PawnData
"""

import unreal
from .base import ASSET_PATHS, resolve_asset_path, resolve_class_path


def create_pawn_data(name: str, config: dict):
    """创建或更新 PawnData DataAsset"""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["pawn_data"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    pawn_data = None
    
    if editor_asset_lib.does_asset_exist(package_path):
        pawn_data = unreal.load_asset(package_path)
        unreal.log(f"PawnData '{name}' 已存在，进行更新")
    else:
        is_new = True
    
    if is_new:
        pawn_data_class = unreal.load_class(None, "/Script/DJ01.DJ01PawnData")
        if not pawn_data_class:
            unreal.log_error("无法加载 DJ01PawnData 类!")
            return None
        
        factory = unreal.DataAssetFactory()
        factory.set_editor_property("data_asset_class", pawn_data_class)
        
        pawn_data = asset_tools.create_asset(
            asset_name=name,
            package_path=base_path,
            asset_class=None,
            factory=factory
        )
        
        if not pawn_data:
            unreal.log_error(f"创建 PawnData 失败: {name}")
            return None
    
    # 设置 PawnClass
    pawn_class_name = config.get("PawnClass") or config.get("pawn_class")
    if pawn_class_name:
        pawn_class_path = resolve_class_path(pawn_class_name)
        pawn_class = unreal.load_class(None, pawn_class_path)
        if pawn_class:
            pawn_data.set_editor_property("PawnClass", pawn_class)
            unreal.log(f"  设置 PawnClass: {pawn_class_path}")
        else:
            unreal.log_warning(f"  无法加载 PawnClass: {pawn_class_path}")
    else:
        # 清空 PawnClass
        pawn_data.set_editor_property("PawnClass", None)
        unreal.log(f"  清空 PawnClass")
    
    # 设置 InputConfig（支持清空）
    input_config_name = config.get("InputConfig") or config.get("input_config")
    if input_config_name:
        input_config_path = resolve_asset_path(input_config_name, "input_config")
        input_config = unreal.load_asset(input_config_path)
        if input_config:
            pawn_data.set_editor_property("InputConfig", input_config)
            unreal.log(f"  设置 InputConfig: {input_config_path}")
        else:
            unreal.log_warning(f"  无法加载 InputConfig: {input_config_path}")
    else:
        # 清空 InputConfig
        pawn_data.set_editor_property("InputConfig", None)
        unreal.log(f"  清空 InputConfig")
    
    # 设置 AbilitySets（始终设置，包括空数组以支持清空）
    ability_set_names = config.get("AbilitySets") or config.get("ability_sets", [])
    ability_sets = []
    for set_name in ability_set_names:
        set_path = resolve_asset_path(set_name, "ability_set")
        ability_set = unreal.load_asset(set_path)
        if ability_set:
            ability_sets.append(ability_set)
    try:
        pawn_data.set_editor_property("AbilitySets", ability_sets)
        unreal.log(f"  设置 AbilitySets: {len(ability_sets)} 个")
    except Exception as e:
        unreal.log_warning(f"  设置 AbilitySets 失败: {e}")
    
    # 设置 DefaultCameraMode（支持清空）
    camera_mode_name = config.get("DefaultCameraMode") or config.get("default_camera_mode")
    if camera_mode_name:
        camera_mode_path = resolve_class_path(camera_mode_name)
        if camera_mode_path:
            camera_mode = unreal.load_class(None, camera_mode_path)
            if camera_mode:
                pawn_data.set_editor_property("DefaultCameraMode", camera_mode)
                unreal.log(f"  设置 DefaultCameraMode: {camera_mode_path}")
    else:
        # 清空 DefaultCameraMode
        pawn_data.set_editor_property("DefaultCameraMode", None)
        unreal.log(f"  清空 DefaultCameraMode")
    
    # 保存
    unreal.EditorAssetLibrary.save_asset(package_path)
    
    action = "创建" if is_new else "更新"
    unreal.log(f"✅ 成功{action} PawnData: {name} -> {package_path}")
    return pawn_data


def delete_pawn_data(name: str) -> bool:
    """删除 PawnData 资产"""
    package_path = f"{ASSET_PATHS['pawn_data']}/{name}"
    
    if unreal.EditorAssetLibrary.does_asset_exist(package_path):
        result = unreal.EditorAssetLibrary.delete_asset(package_path)
        if result:
            unreal.log(f"✅ 已删除 PawnData: {name}")
        else:
            unreal.log_error(f"删除 PawnData 失败: {name}")
        return result
    else:
        unreal.log_warning(f"PawnData 不存在: {name}")
        return True
"""
DJ01 DataAsset 生成器 - ActionSet
"""

import unreal
from .base import ASSET_PATHS


def create_action_set(name: str, config: dict):
    """创建或更新 ActionSet DataAsset"""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["action_set"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    action_set = None
    
    if editor_asset_lib.does_asset_exist(package_path):
        action_set = unreal.load_asset(package_path)
        unreal.log(f"ActionSet '{name}' 已存在，进行更新")
    else:
        action_set_class = unreal.load_class(None, "/Script/DJ01.DJ01ExperienceActionSet")
        if not action_set_class:
            unreal.log_error("无法加载 DJ01ExperienceActionSet 类!")
            return None
        
        factory = unreal.DataAssetFactory()
        factory.set_editor_property("data_asset_class", action_set_class)
        
        action_set = asset_tools.create_asset(
            asset_name=name,
            package_path=base_path,
            asset_class=None,
            factory=factory
        )
        is_new = True
    
    if not action_set:
        unreal.log_error(f"创建/加载 ActionSet 失败: {name}")
        return None
    
    # 设置 GameFeaturesToEnable（始终设置，包括空数组以支持清空）
    game_features = config.get("GameFeaturesToEnable") or config.get("game_features", [])
    try:
        action_set.set_editor_property("GameFeaturesToEnable", game_features)
        unreal.log(f"  设置 GameFeatures: {len(game_features)} 个")
    except Exception as e:
        unreal.log_warning(f"  设置 GameFeatures 失败: {e}")
    
    # 提示：Actions 需要手动配置
    actions_config = config.get("Actions", [])
    if actions_config:
        unreal.log(f"  ⚠️ 配置中包含 {len(actions_config)} 个 Actions，请在 UE 编辑器中手动配置")
    
    # 保存资产
    unreal.EditorAssetLibrary.save_asset(package_path)
    
    action = "创建" if is_new else "更新"
    unreal.log(f"✅ 成功{action} ActionSet: {name} -> {package_path}")
    return action_set


def delete_action_set(name: str) -> bool:
    """删除 ActionSet 资产"""
    package_path = f"{ASSET_PATHS['action_set']}/{name}"
    
    if unreal.EditorAssetLibrary.does_asset_exist(package_path):
        result = unreal.EditorAssetLibrary.delete_asset(package_path)
        if result:
            unreal.log(f"✅ 已删除 ActionSet: {name}")
        else:
            unreal.log_error(f"删除 ActionSet 失败: {name}")
        return result
    else:
        unreal.log_warning(f"ActionSet 不存在: {name}")
        return True
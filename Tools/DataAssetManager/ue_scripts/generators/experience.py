"""
DJ01 DataAsset 生成器 - Experience
"""

import unreal
from .base import ASSET_PATHS, resolve_asset_path


def get_or_create_experience_blueprint(name: str):
    """
    获取或创建 Experience 蓝图
    
    Returns:
        (blueprint, cdo, is_new) 元组
    """
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["experience"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    blueprint = None
    
    if editor_asset_lib.does_asset_exist(package_path):
        blueprint = unreal.load_asset(package_path)
        unreal.log(f"Experience '{name}' 已存在，进行更新")
    else:
        parent_class = unreal.load_class(None, "/Script/DJ01.DJ01ExperienceDefinition")
        if not parent_class:
            unreal.log_error("无法加载 DJ01ExperienceDefinition 类!")
            return None, None, False
        
        factory = unreal.BlueprintFactory()
        factory.set_editor_property("parent_class", parent_class)
        
        blueprint = asset_tools.create_asset(
            asset_name=name,
            package_path=base_path,
            asset_class=unreal.Blueprint,
            factory=factory
        )
        is_new = True
    
    if not blueprint:
        unreal.log_error(f"创建/加载 Experience 蓝图失败: {name}")
        return None, None, False
    
    # 获取 CDO
    try:
        generated_class = unreal.BlueprintEditorLibrary.generated_class(blueprint)
    except:
        try:
            generated_class = blueprint.get_editor_property("GeneratedClass")
        except:
            unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
            try:
                generated_class = blueprint.get_editor_property("GeneratedClass")
            except Exception as e:
                unreal.log_warning(f"  无法获取 GeneratedClass: {e}")
                return blueprint, None, is_new
    
    if not generated_class:
        return blueprint, None, is_new
    
    cdo = unreal.get_default_object(generated_class)
    return blueprint, cdo, is_new


def create_experience_blueprint(name: str, config: dict):
    """创建或更新 Experience 蓝图类"""
    base_path = ASSET_PATHS["experience"]
    package_path = f"{base_path}/{name}"
    
    blueprint, cdo, is_new = get_or_create_experience_blueprint(name)
    
    if not blueprint:
        return None
    
    if not cdo:
        unreal.log_warning(f"  无法获取 CDO，跳过属性设置")
        unreal.EditorAssetLibrary.save_asset(package_path)
        return blueprint
    
    # 设置 DefaultPawnData
    pawn_data_name = config.get("DefaultPawnData") or config.get("default_pawn_data")
    if pawn_data_name:
        pawn_data_path = resolve_asset_path(pawn_data_name, "pawn_data")
        pawn_data = unreal.load_asset(pawn_data_path)
        if pawn_data:
            try:
                cdo.set_editor_property("DefaultPawnData", pawn_data)
                unreal.log(f"  设置 DefaultPawnData: {pawn_data_path}")
            except Exception as e:
                unreal.log_warning(f"  设置 DefaultPawnData 失败: {e}")
        else:
            unreal.log_warning(f"  无法加载 PawnData: {pawn_data_path}")
    else:
        # 清空 DefaultPawnData
        try:
            cdo.set_editor_property("DefaultPawnData", None)
            unreal.log(f"  清空 DefaultPawnData")
        except Exception as e:
            unreal.log_warning(f"  清空 DefaultPawnData 失败: {e}")
    
    # 设置 GameFeaturesToEnable（始终设置）
    game_features = config.get("GameFeaturesToEnable") or config.get("game_features", [])
    try:
        cdo.set_editor_property("GameFeaturesToEnable", game_features)
        unreal.log(f"  设置 GameFeatures: {len(game_features)} 个")
    except Exception as e:
        unreal.log_warning(f"  设置 GameFeatures 失败: {e}")
    
    # 设置 ActionSets（始终设置）
    action_set_names = config.get("ActionSets") or config.get("action_sets", [])
    action_sets = []
    for set_name in action_set_names:
        set_path = resolve_asset_path(set_name, "action_set")
        action_set = unreal.load_asset(set_path)
        if action_set:
            action_sets.append(action_set)
    try:
        cdo.set_editor_property("ActionSets", action_sets)
        unreal.log(f"  设置 ActionSets: {len(action_sets)} 个")
    except Exception as e:
        unreal.log_warning(f"  设置 ActionSets 失败: {e}")
    
    # 编译蓝图
    unreal.BlueprintEditorLibrary.compile_blueprint(blueprint)
    
    # 提示：Actions 需要手动配置
    actions_config = config.get("Actions", [])
    if actions_config:
        unreal.log(f"  ⚠️ 配置中包含 {len(actions_config)} 个 Actions，请在 UE 编辑器中手动配置")
    
    # 保存资产
    unreal.EditorAssetLibrary.save_asset(package_path)
    
    action = "创建" if is_new else "更新"
    unreal.log(f"✅ 成功{action} Experience: {name} -> {package_path}")
    return blueprint


def delete_experience(name: str) -> bool:
    """删除 Experience 蓝图"""
    package_path = f"{ASSET_PATHS['experience']}/{name}"
    
    if unreal.EditorAssetLibrary.does_asset_exist(package_path):
        result = unreal.EditorAssetLibrary.delete_asset(package_path)
        if result:
            unreal.log(f"✅ 已删除 Experience: {name}")
        else:
            unreal.log_error(f"删除 Experience 失败: {name}")
        return result
    else:
        unreal.log_warning(f"Experience 不存在: {name}")
        return True
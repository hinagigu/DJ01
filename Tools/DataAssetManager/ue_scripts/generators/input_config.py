"""
DJ01 DataAsset 生成器 - InputConfig
"""

import unreal
from .base import ASSET_PATHS, resolve_input_action_path, set_struct_gameplay_tag


def create_input_config(name: str, config: dict):
    """创建或更新 InputConfig DataAsset"""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["input_config"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    input_config = None
    
    if editor_asset_lib.does_asset_exist(package_path):
        input_config = unreal.load_asset(package_path)
        unreal.log(f"InputConfig '{name}' 已存在，进行更新")
    else:
        is_new = True
        input_config_class = unreal.load_class(None, "/Script/DJ01.DJ01InputConfig")
        if not input_config_class:
            unreal.log_error("无法加载 DJ01InputConfig 类!")
            return None
        
        factory = unreal.DataAssetFactory()
        factory.set_editor_property("data_asset_class", input_config_class)
        
        input_config = asset_tools.create_asset(
            asset_name=name,
            package_path=base_path,
            asset_class=None,
            factory=factory
        )
    
    if not input_config:
        unreal.log_error(f"创建/加载 InputConfig 失败: {name}")
        return None
    
    # 设置 NativeInputActions
    native_actions = config.get("NativeInputActions", [])
    native_array = []
    
    for action_entry in native_actions:
        input_action_name = action_entry.get("InputAction", "")
        input_tag_str = action_entry.get("InputTag", "")
        
        if not input_action_name or not input_tag_str:
            continue
        
        input_action_path = resolve_input_action_path(input_action_name)
        input_action = unreal.load_asset(input_action_path)
        
        if not input_action:
            unreal.log_warning(f"  无法加载 InputAction: {input_action_path}")
            continue
        
        try:
            struct_instance = unreal.DJ01InputAction()
            struct_instance.set_editor_property("InputAction", input_action)
            
            if set_struct_gameplay_tag(struct_instance, "InputTag", input_tag_str):
                native_array.append(struct_instance)
                unreal.log(f"  添加 NativeInputAction: {input_action_name} -> {input_tag_str}")
            else:
                unreal.log_warning(f"  跳过 NativeInputAction（Tag设置失败）: {input_action_name}")
        except Exception as e:
            unreal.log_warning(f"  创建 NativeInputAction 失败: {e}")
    
    try:
        input_config.set_editor_property("NativeInputActions", native_array)
        unreal.log(f"  NativeInputActions 已设置: {len(native_array)} 项")
    except Exception as e:
        unreal.log_warning(f"  设置 NativeInputActions 失败: {e}")
    
    # 设置 AbilityInputActions
    ability_actions = config.get("AbilityInputActions", [])
    ability_array = []
    
    for action_entry in ability_actions:
        input_action_name = action_entry.get("InputAction", "")
        input_tag_str = action_entry.get("InputTag", "")
        
        if not input_action_name or not input_tag_str:
            continue
        
        input_action_path = resolve_input_action_path(input_action_name)
        input_action = unreal.load_asset(input_action_path)
        
        if not input_action:
            unreal.log_warning(f"  无法加载 InputAction: {input_action_path}")
            continue
        
        try:
            struct_instance = unreal.DJ01InputAction()
            struct_instance.set_editor_property("InputAction", input_action)
            
            if set_struct_gameplay_tag(struct_instance, "InputTag", input_tag_str):
                ability_array.append(struct_instance)
                unreal.log(f"  添加 AbilityInputAction: {input_action_name} -> {input_tag_str}")
            else:
                unreal.log_warning(f"  跳过 AbilityInputAction（Tag设置失败）: {input_action_name}")
        except Exception as e:
            unreal.log_warning(f"  创建 DJ01InputAction 失败: {e}")
    
    try:
        input_config.set_editor_property("AbilityInputActions", ability_array)
        unreal.log(f"  AbilityInputActions 已设置: {len(ability_array)} 项")
    except Exception as e:
        unreal.log_warning(f"  设置 AbilityInputActions 失败: {e}")
    
    # 保存资产
    unreal.EditorAssetLibrary.save_asset(package_path, only_if_is_dirty=False)
    
    action = "创建" if is_new else "更新"
    unreal.log(f"✅ 成功{action} InputConfig: {name} -> {package_path}")
    return input_config


def delete_input_config(name: str) -> bool:
    """删除 InputConfig 资产"""
    package_path = f"{ASSET_PATHS['input_config']}/{name}"
    
    if unreal.EditorAssetLibrary.does_asset_exist(package_path):
        result = unreal.EditorAssetLibrary.delete_asset(package_path)
        if result:
            unreal.log(f"✅ 已删除 InputConfig: {name}")
        else:
            unreal.log_error(f"删除 InputConfig 失败: {name}")
        return result
    else:
        unreal.log_warning(f"InputConfig 不存在: {name}")
        return True
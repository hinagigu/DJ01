"""
DJ01 DataAsset 生成器 - AbilitySet
"""

import unreal
from .base import ASSET_PATHS, extract_class_path_for_import, load_class_from_path


def create_ability_set(name: str, config: dict):
    """
    创建或更新 AbilitySet DataAsset
    """
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["ability_set"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    ability_set = None
    
    if editor_asset_lib.does_asset_exist(package_path):
        ability_set = unreal.load_asset(package_path)
        unreal.log(f"AbilitySet '{name}' 已存在，进行更新")
    else:
        is_new = True
        ability_set_class = unreal.load_class(None, "/Script/DJ01.DJ01AbilitySet")
        if not ability_set_class:
            unreal.log_error("无法加载 DJ01AbilitySet 类!")
            return None
        
        factory = unreal.DataAssetFactory()
        factory.set_editor_property("data_asset_class", ability_set_class)
        
        ability_set = asset_tools.create_asset(
            asset_name=name,
            package_path=base_path,
            asset_class=None,
            factory=factory
        )
    
    if not ability_set:
        unreal.log_error(f"创建/加载 AbilitySet 失败: {name}")
        return None
    
    # ========== 设置 GrantedGameplayAbilities ==========
    granted_abilities_config = config.get("GrantedGameplayAbilities", [])
    abilities_array = []
    
    for ability_entry in granted_abilities_config:
        ability_path = ability_entry.get("Ability", "")
        ability_level = ability_entry.get("AbilityLevel", 1)
        input_tag_str = ability_entry.get("InputTag", "")
        
        if not ability_path:
            unreal.log_warning("  跳过空的 Ability 配置")
            continue
        
        import_path = extract_class_path_for_import(ability_path)
        tag_part = f',InputTag=(TagName="{input_tag_str}")' if input_tag_str else ',InputTag=(TagName="")'
        import_str = f'(Ability={import_path},AbilityLevel={int(ability_level)}{tag_part})'
        
        try:
            struct_instance = unreal.DJ01AbilitySet_GameplayAbility()
            struct_instance.import_text(import_str)
            abilities_array.append(struct_instance)
            
            ability_class = load_class_from_path(ability_path)
            class_name = ability_class.get_name() if ability_class else import_path
            unreal.log(f"  添加技能: {class_name} (Lv.{ability_level})")
            
        except Exception as e:
            unreal.log_warning(f"  创建技能结构体失败: {ability_path}")
            unreal.log_warning(f"    import_text: {import_str}")
            unreal.log_warning(f"    错误: {e}")
            continue
    
    try:
        ability_set.set_editor_property("GrantedGameplayAbilities", abilities_array)
        unreal.log(f"  GrantedGameplayAbilities: {len(abilities_array)} 个技能")
    except Exception as e:
        unreal.log_error(f"  设置 GrantedGameplayAbilities 失败: {e}")
    
    # ========== 设置 GrantedGameplayEffects ==========
    granted_effects_config = config.get("GrantedGameplayEffects", [])
    effects_array = []
    
    for effect_entry in granted_effects_config:
        effect_path = effect_entry.get("GameplayEffect", "")
        effect_level = effect_entry.get("EffectLevel", 1.0)
        
        if not effect_path:
            continue
        
        import_path = extract_class_path_for_import(effect_path)
        import_str = f'(GameplayEffect={import_path},EffectLevel={float(effect_level)})'
        
        try:
            struct_instance = unreal.DJ01AbilitySet_GameplayEffect()
            struct_instance.import_text(import_str)
            effects_array.append(struct_instance)
            
            effect_class = load_class_from_path(effect_path)
            class_name = effect_class.get_name() if effect_class else import_path
            unreal.log(f"  添加效果: {class_name} (Lv.{effect_level})")
            
        except Exception as e:
            unreal.log_warning(f"  创建效果结构体失败: {effect_path}, {e}")
            continue
    
    try:
        ability_set.set_editor_property("GrantedGameplayEffects", effects_array)
        unreal.log(f"  GrantedGameplayEffects: {len(effects_array)} 个效果")
    except Exception as e:
        unreal.log_error(f"  设置 GrantedGameplayEffects 失败: {e}")
    
    # ========== 设置 GrantedAttributes ==========
    granted_attributes_config = config.get("GrantedAttributes", [])
    attributes_array = []
    
    for attr_entry in granted_attributes_config:
        attr_path = attr_entry.get("AttributeSet", "")
        
        if not attr_path:
            continue
        
        import_path = extract_class_path_for_import(attr_path)
        import_str = f'(AttributeSet={import_path})'
        
        try:
            struct_instance = unreal.DJ01AbilitySet_AttributeSet()
            struct_instance.import_text(import_str)
            attributes_array.append(struct_instance)
            
            attr_class = load_class_from_path(attr_path)
            class_name = attr_class.get_name() if attr_class else import_path
            unreal.log(f"  添加属性集: {class_name}")
            
        except Exception as e:
            unreal.log_warning(f"  创建属性集结构体失败: {attr_path}, {e}")
            continue
    
    try:
        ability_set.set_editor_property("GrantedAttributes", attributes_array)
        unreal.log(f"  GrantedAttributes: {len(attributes_array)} 个属性集")
    except Exception as e:
        unreal.log_error(f"  设置 GrantedAttributes 失败: {e}")
    
    # 保存资产
    unreal.EditorAssetLibrary.save_asset(package_path)
    action = "创建" if is_new else "更新"
    unreal.log(f"✅ 成功{action} AbilitySet: {name} -> {package_path}")
    return ability_set


def delete_ability_set(name: str) -> bool:
    """删除 AbilitySet 资产"""
    package_path = f"{ASSET_PATHS['ability_set']}/{name}"
    
    if unreal.EditorAssetLibrary.does_asset_exist(package_path):
        result = unreal.EditorAssetLibrary.delete_asset(package_path)
        if result:
            unreal.log(f"✅ 已删除 AbilitySet: {name}")
        else:
            unreal.log_error(f"删除 AbilitySet 失败: {name}")
        return result
    else:
        unreal.log_warning(f"AbilitySet 不存在: {name}")
        return True
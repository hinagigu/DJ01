"""
DJ01 DataAsset 生成器 - UE Python 脚本
在 UE Editor 中执行此脚本来创建各类 DataAsset

使用方法：
1. 在 UE Editor 中打开 Output Log
2. 执行: ExecutePythonScript D:/UnrealProjects/DJ01/Tools/DataAssetManager/ue_scripts/generate_experience.py

注意：
- Experience 的 Actions 需要在 UE 编辑器中手动配置
- 此脚本只处理简单的 DataAsset 属性设置
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
        # 尝试常见的蓝图路径
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
    
    # 检查是否已存在
    if editor_asset_lib.does_asset_exist(package_path):
        blueprint = unreal.load_asset(package_path)
        unreal.log(f"Experience '{name}' 已存在，进行更新")
    else:
        # 获取父类
        parent_class = unreal.load_class(None, "/Script/DJ01.DJ01ExperienceDefinition")
        if not parent_class:
            unreal.log_error("无法加载 DJ01ExperienceDefinition 类!")
            return None, None, False
        
        # 创建蓝图
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
    """
    创建或更新 Experience 蓝图类
    
    Args:
        name: Experience 名称
        config: 配置字典
    """
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
    
    # 设置 GameFeaturesToEnable（始终设置，包括空数组以支持清空）
    game_features = config.get("GameFeaturesToEnable") or config.get("game_features", [])
    try:
        cdo.set_editor_property("GameFeaturesToEnable", game_features)
        unreal.log(f"  设置 GameFeatures: {len(game_features)} 个")
    except Exception as e:
        unreal.log_warning(f"  设置 GameFeatures 失败: {e}")
    
    # 设置 ActionSets（始终设置，包括空数组以支持清空）
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
        # 获取 PawnData 类
        pawn_data_class = unreal.load_class(None, "/Script/DJ01.DJ01PawnData")
        if not pawn_data_class:
            unreal.log_error("无法加载 DJ01PawnData 类!")
            return None
        
        # 创建 DataAsset
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
    
    # 设置 InputConfig
    input_config_name = config.get("InputConfig") or config.get("input_config")
    if input_config_name:
        input_config_path = resolve_asset_path(input_config_name, "input_config")
        input_config = unreal.load_asset(input_config_path)
        if input_config:
            pawn_data.set_editor_property("InputConfig", input_config)
            unreal.log(f"  设置 InputConfig: {input_config_path}")
        else:
            unreal.log_warning(f"  无法加载 InputConfig: {input_config_path}")
    
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
    
    # 设置 DefaultCameraMode
    camera_mode_name = config.get("DefaultCameraMode") or config.get("default_camera_mode")
    if camera_mode_name:
        camera_mode_path = resolve_class_path(camera_mode_name)
        if camera_mode_path:
            camera_mode = unreal.load_class(None, camera_mode_path)
            if camera_mode:
                pawn_data.set_editor_property("DefaultCameraMode", camera_mode)
                unreal.log(f"  设置 DefaultCameraMode: {camera_mode_path}")
    
    # 保存
    unreal.EditorAssetLibrary.save_asset(package_path)
    
    action = "创建" if is_new else "更新"
    unreal.log(f"✅ 成功{action} PawnData: {name} -> {package_path}")
    return pawn_data


def extract_class_path_for_import(class_path: str) -> str:
    """
    从类路径中提取用于 import_text 的路径格式
    
    输入格式:
    - C++: /Script/DJ01.DJ01GameplayAbility
    - Blueprint: /Game/.../BP_xxx.BP_xxx_C
    - AngelScript 软引用: /Script/AngelscriptCode.ASClass'/Script/Angelscript.GA_xxx'
    
    输出格式 (用于 import_text):
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
            return parts[1]  # 返回 /Script/Angelscript.ClassName
    
    return class_path


def load_class_from_path(class_path: str):
    """
    从路径加载类，支持多种格式：
    - C++: /Script/DJ01.DJ01GameplayAbility
    - Blueprint: /Game/.../BP_xxx.BP_xxx_C
    - AngelScript: /Script/AngelscriptCode.ASClass'/Script/Angelscript.GA_xxx'
                   或直接 /Script/Angelscript.GA_xxx
    """
    if not class_path:
        return None
    
    # 提取实际路径
    actual_path = extract_class_path_for_import(class_path)
    
    try:
        loaded_class = unreal.load_class(None, actual_path)
        if loaded_class:
            return loaded_class
    except Exception as e:
        unreal.log_warning(f"  加载类失败: {actual_path}, {e}")
    
    return None


def create_ability_set(name: str, config: dict):
    """
    创建或更新 AbilitySet DataAsset
    
    支持配置结构:
    {
        "GrantedGameplayAbilities": [
            {"Ability": "/Script/AngelscriptCode.ASClass'/Script/Angelscript.GA_xxx'", "AbilityLevel": 1, "InputTag": "InputTag.xxx"},
            ...
        ],
        "GrantedGameplayEffects": [
            {"GameplayEffect": "/Script/DJ01.GE_xxx", "EffectLevel": 1.0},
            ...
        ],
        "GrantedAttributes": [
            {"AttributeSet": "/Script/DJ01.DJ01StatSet"},
            ...
        ]
    }
    """
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["ability_set"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    ability_set = None
    
    # 检查是否已存在
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
        
        # 提取用于 import_text 的路径
        import_path = extract_class_path_for_import(ability_path)
        
        # 构建 import_text 字符串
        # 格式: (Ability=/Script/xxx.ClassName,AbilityLevel=1,InputTag=(TagName="xxx"))
        tag_part = f',InputTag=(TagName="{input_tag_str}")' if input_tag_str else ',InputTag=(TagName="")'
        import_str = f'(Ability={import_path},AbilityLevel={int(ability_level)}{tag_part})'
        
        try:
            struct_instance = unreal.DJ01AbilitySet_GameplayAbility()
            struct_instance.import_text(import_str)
            abilities_array.append(struct_instance)
            
            # 获取类名用于日志
            ability_class = load_class_from_path(ability_path)
            class_name = ability_class.get_name() if ability_class else import_path
            unreal.log(f"  添加技能: {class_name} (Lv.{ability_level})")
            
        except Exception as e:
            unreal.log_warning(f"  创建技能结构体失败: {ability_path}")
            unreal.log_warning(f"    import_text: {import_str}")
            unreal.log_warning(f"    错误: {e}")
            continue
    
    # 始终设置数组（包括空数组，以支持清空操作）
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
        
        # 提取用于 import_text 的路径
        import_path = extract_class_path_for_import(effect_path)
        
        # 构建 import_text 字符串
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
    
    # 始终设置数组（包括空数组，以支持清空操作）
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
        
        # 提取用于 import_text 的路径
        import_path = extract_class_path_for_import(attr_path)
        
        # 构建 import_text 字符串
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
    
    # 始终设置数组（包括空数组，以支持清空操作）
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


def resolve_input_action_path(name_or_path: str) -> str:
    """解析 InputAction 资产路径"""
    if not name_or_path:
        return ""
    
    # 已经是完整路径
    if name_or_path.startswith("/Game"):
        return name_or_path
    
    # 移除显示后缀如 "(InputAction)" 等
    clean_name = name_or_path.split(" (")[0].strip()
    
    # 从名称构造路径 (格式: /Game/Input/Actions/IA_xxx)
    return f"/Game/Input/Actions/{clean_name}"


def set_struct_gameplay_tag(struct_instance, property_name: str, tag_name: str) -> bool:
    """
    在结构体实例上设置 GameplayTag 属性
    使用 import_text 方法正确设置 GameplayTag 值
    """
    if not tag_name:
        unreal.log_warning(f"  {property_name}: tag_name 为空")
        return False
    
    try:
        # 获取结构体上的 GameplayTag 属性
        tag = struct_instance.get_editor_property(property_name)
        
        # 使用 import_text 设置 tag 值
        tag.import_text(tag_name)
        
        # 将修改后的 tag 设置回结构体
        struct_instance.set_editor_property(property_name, tag)
        
        return True
    except Exception as e:
        unreal.log_warning(f"  设置 {property_name} = '{tag_name}' 失败: {e}")
        return False


def create_input_config(name: str, config: dict):
    """创建或更新 InputConfig DataAsset"""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["input_config"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    input_config = None
    
    # 检查是否已存在
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
        
        # 加载 InputAction 资产
        input_action_path = resolve_input_action_path(input_action_name)
        input_action = unreal.load_asset(input_action_path)
        
        if not input_action:
            unreal.log_warning(f"  无法加载 InputAction: {input_action_path}")
            continue
        
        # 创建结构体实例并设置属性
        try:
            struct_instance = unreal.DJ01InputAction()
            struct_instance.set_editor_property("InputAction", input_action)
                
            # 设置 GameplayTag
            if set_struct_gameplay_tag(struct_instance, "InputTag", input_tag_str):
                native_array.append(struct_instance)
                unreal.log(f"  添加 NativeInputAction: {input_action_name} -> {input_tag_str}")
            else:
                unreal.log_warning(f"  跳过 NativeInputAction（Tag设置失败）: {input_action_name}")
        except Exception as e:
            unreal.log_warning(f"  创建 NativeInputAction 失败: {e}")
    
    # 设置属性（始终设置，包括空数组以支持清空）
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
        
        # 加载 InputAction 资产
        input_action_path = resolve_input_action_path(input_action_name)
        input_action = unreal.load_asset(input_action_path)
        
        if not input_action:
            unreal.log_warning(f"  无法加载 InputAction: {input_action_path}")
            continue
        
        # 创建结构体实例并设置属性
        try:
            struct_instance = unreal.DJ01InputAction()
            struct_instance.set_editor_property("InputAction", input_action)
                
            # 设置 GameplayTag
            if set_struct_gameplay_tag(struct_instance, "InputTag", input_tag_str):
                ability_array.append(struct_instance)
                unreal.log(f"  添加 AbilityInputAction: {input_action_name} -> {input_tag_str}")
            else:
                unreal.log_warning(f"  跳过 AbilityInputAction（Tag设置失败）: {input_action_name}")
        except Exception as e:
            unreal.log_warning(f"  创建 DJ01InputAction 失败: {e}")
    
    # 设置属性（始终设置，包括空数组以支持清空）
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


def create_action_set(name: str, config: dict):
    """创建或更新 ActionSet DataAsset"""
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    editor_asset_lib = unreal.EditorAssetLibrary
    
    base_path = ASSET_PATHS["action_set"]
    package_path = f"{base_path}/{name}"
    
    is_new = False
    action_set = None
    
    # 检查是否已存在
    if editor_asset_lib.does_asset_exist(package_path):
        action_set = unreal.load_asset(package_path)
        unreal.log(f"ActionSet '{name}' 已存在，进行更新")
    else:
        # 获取 ActionSet 类
        action_set_class = unreal.load_class(None, "/Script/DJ01.DJ01ExperienceActionSet")
        if not action_set_class:
            unreal.log_error("无法加载 DJ01ExperienceActionSet 类!")
            return None
        
        # 创建 DataAsset
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
    
    # 5. 生成 Experiences（依赖其他资产，并支持更新）
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
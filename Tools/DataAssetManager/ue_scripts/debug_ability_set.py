"""
调试 AbilitySet 创建的脚本
在 UE Editor 中执行：py D:/UnrealProjects/DJ01/Tools/DataAssetManager/ue_scripts/debug_ability_set.py
"""

import unreal


def load_class_from_path(class_path: str):
    """从路径加载类"""
    if not class_path:
        return None
    
    # AngelScript 软引用格式: /Script/AngelscriptCode.ASClass'/Script/Angelscript.ClassName'
    if "ASClass'" in class_path and "'" in class_path:
        try:
            parts = class_path.split("'")
            if len(parts) >= 2:
                inner_path = parts[1]
                loaded_class = unreal.load_class(None, inner_path)
                if loaded_class:
                    return loaded_class
        except Exception as e:
            unreal.log_warning(f"  加载 AngelScript 类失败: {class_path}, {e}")
    
    try:
        loaded_class = unreal.load_class(None, class_path)
        if loaded_class:
            return loaded_class
    except Exception as e:
        unreal.log_warning(f"  加载类失败: {class_path}, {e}")
    
    return None


def test_struct_methods():
    """测试结构体的各种方法"""
    unreal.log("=" * 60)
    unreal.log("[DEBUG] 测试结构体方法")
    unreal.log("=" * 60)
    
    # 1. 查看现有资产中结构体的 export_text
    unreal.log("\n[1] 检查现有结构体的 export_text 格式...")
    test_asset_path = "/Game/Gameplay/Abilities/AbilitySets/TestSets"
    
    if unreal.EditorAssetLibrary.does_asset_exist(test_asset_path):
        asset = unreal.load_asset(test_asset_path)
        if asset:
            abilities = asset.get_editor_property("GrantedGameplayAbilities")
            if len(abilities) > 0:
                existing_struct = abilities[0]
                try:
                    exported = existing_struct.export_text()
                    unreal.log(f"  现有结构体 export_text:")
                    unreal.log(f"  {exported}")
                except Exception as e:
                    unreal.log(f"  export_text 失败: {e}")
    
    # 2. 测试使用 import_text 设置结构体
    unreal.log("\n[2] 测试 import_text 设置结构体...")
    
    struct = unreal.DJ01AbilitySet_GameplayAbility()
    
    # 尝试不同的 import_text 格式
    test_formats = [
        # 格式1: 简单格式
        '(Ability=/Script/DJ01.DJ01GameplayAbility,AbilityLevel=1)',
        # 格式2: 带类路径格式
        '(Ability=Class\'/Script/DJ01.DJ01GameplayAbility\',AbilityLevel=1)',
        # 格式3: BlueprintGeneratedClass 格式
        '(Ability=BlueprintGeneratedClass\'/Script/DJ01.DJ01GameplayAbility\',AbilityLevel=1)',
    ]
    
    for fmt in test_formats:
        try:
            struct.import_text(fmt)
            unreal.log(f"  ✅ import_text 成功: {fmt[:60]}...")
            # 验证
            exported = struct.export_text()
            unreal.log(f"     导出验证: {exported}")
            break
        except Exception as e:
            unreal.log(f"  ❌ import_text 失败: {fmt[:40]}...")
            unreal.log(f"     错误: {e}")
    
    # 3. 测试 AngelScript 类的 import_text
    unreal.log("\n[3] 测试 AngelScript 类 import_text...")
    
    # 先获取正确的类路径格式
    as_class = load_class_from_path("/Script/AngelscriptCode.ASClass'/Script/Angelscript.GA_CastStone'")
    if as_class:
        unreal.log(f"  AS 类对象: {as_class}")
        unreal.log(f"  AS 类路径: {as_class.get_path_name()}")
        
        # 尝试用获取到的路径
        as_formats = [
            f'(Ability={as_class.get_path_name()},AbilityLevel=1,InputTag=(TagName="InputTag.Test.CastStone"))',
            f'(Ability=Class\'{as_class.get_path_name()}\',AbilityLevel=1)',
            f'(Ability=/Script/Angelscript.GA_CastStone,AbilityLevel=1)',
        ]
        
        for fmt in as_formats:
            try:
                struct2 = unreal.DJ01AbilitySet_GameplayAbility()
                struct2.import_text(fmt)
                unreal.log(f"  ✅ AS import_text 成功!")
                unreal.log(f"     格式: {fmt[:80]}...")
                exported = struct2.export_text()
                unreal.log(f"     导出: {exported}")
                break
            except Exception as e:
                unreal.log(f"  ❌ AS import_text 失败: {fmt[:50]}...")
                unreal.log(f"     错误: {e}")
    
    # 4. 测试直接修改资产数组
    unreal.log("\n[4] 测试直接操作资产数组...")
    test_asset_path2 = "/Game/Gameplay/Abilities/AbilitySets/HealthySets"
    
    if unreal.EditorAssetLibrary.does_asset_exist(test_asset_path2):
        ability_set = unreal.load_asset(test_asset_path2)
        if ability_set:
            unreal.log(f"  加载资产: {test_asset_path2}")
            
            # 获取当前数组
            current = ability_set.get_editor_property("GrantedGameplayAbilities")
            unreal.log(f"  当前数组长度: {len(current)}")
            
            # 创建新结构体并使用 import_text
            new_struct = unreal.DJ01AbilitySet_GameplayAbility()
            try:
                # 使用从现有结构体获取的格式
                as_class = load_class_from_path("/Script/AngelscriptCode.ASClass'/Script/Angelscript.GA_CastStone'")
                if as_class:
                    import_str = f'(Ability={as_class.get_path_name()},AbilityLevel=1,InputTag=(TagName="InputTag.Test.CastStone"))'
                    unreal.log(f"  尝试 import: {import_str}")
                    new_struct.import_text(import_str)
                    
                    # 添加到数组
                    new_array = list(current) + [new_struct]
                    ability_set.set_editor_property("GrantedGameplayAbilities", new_array)
                    
                    # 保存
                    unreal.EditorAssetLibrary.save_asset(test_asset_path2)
                    unreal.log(f"  ✅ 资产已保存")
                    
                    # 重新加载验证
                    ability_set2 = unreal.load_asset(test_asset_path2)
                    new_len = len(ability_set2.get_editor_property("GrantedGameplayAbilities"))
                    unreal.log(f"  验证: 新数组长度 = {new_len}")
                    
            except Exception as e:
                unreal.log(f"  ❌ 操作失败: {e}")
    
    unreal.log("\n" + "=" * 60)
    unreal.log("[DEBUG] 测试完成")
    unreal.log("=" * 60)


# 执行测试
test_struct_methods()
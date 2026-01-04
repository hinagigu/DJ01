"""
DJ01 PawnData API 测试脚本

创建临时 PawnData 资产进行测试，测试完成后自动删除

使用方法：
在 UE Editor 中执行:
ExecutePythonScript D:/UnrealProjects/DJ01/Tools/DataAssetManager/ue_scripts/test_pawn_data_api.py
"""

import unreal

# 测试用临时资产
TEST_ASSET_NAME = "_API_Test_PawnData_Temp"
TEST_ASSET_PATH = f"/Game/Characters/PawnData/{TEST_ASSET_NAME}"


def log_separator(title: str):
    unreal.log("=" * 60)
    unreal.log(f"  {title}")
    unreal.log("=" * 60)


def log_result(test_name: str, success: bool, message: str = ""):
    status = "✅ PASS" if success else "❌ FAIL"
    unreal.log(f"  {status}: {test_name}")
    if message:
        unreal.log(f"         {message}")


def create_test_pawn_data():
    """创建测试用的临时 PawnData"""
    log_separator("准备: 创建临时测试资产")
    
    # 如果已存在则先删除
    if unreal.EditorAssetLibrary.does_asset_exist(TEST_ASSET_PATH):
        unreal.EditorAssetLibrary.delete_asset(TEST_ASSET_PATH)
        unreal.log(f"  已删除旧的测试资产")
    
    # 加载 PawnData 类
    pawn_data_class = unreal.load_class(None, "/Script/DJ01.DJ01PawnData")
    if not pawn_data_class:
        log_result("加载 DJ01PawnData 类", False, "无法加载类")
        return None
    
    log_result("加载 DJ01PawnData 类", True)
    
    # 创建资产
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    factory = unreal.DataAssetFactory()
    factory.set_editor_property("data_asset_class", pawn_data_class)
    
    pawn_data = asset_tools.create_asset(
        asset_name=TEST_ASSET_NAME,
        package_path="/Game/Characters/PawnData",
        asset_class=None,
        factory=factory
    )
    
    if pawn_data:
        log_result("创建测试 PawnData", True, TEST_ASSET_PATH)
        return pawn_data
    else:
        log_result("创建测试 PawnData", False)
        return None


def delete_test_pawn_data():
    """删除测试用的临时 PawnData"""
    log_separator("清理: 删除临时测试资产")
    
    if unreal.EditorAssetLibrary.does_asset_exist(TEST_ASSET_PATH):
        result = unreal.EditorAssetLibrary.delete_asset(TEST_ASSET_PATH)
        log_result("删除测试资产", result)
        return result
    else:
        unreal.log("  测试资产不存在，无需删除")
        return True


def test_get_properties(pawn_data):
    """测试1: 读取 PawnData 的各属性"""
    log_separator("测试1: 读取属性 (初始状态应为空)")
    
    if not pawn_data:
        log_result("读取属性", False, "pawn_data 为 None")
        return
    
    properties = ["PawnClass", "InputConfig", "AbilitySets", "DefaultCameraMode"]
    
    for prop in properties:
        try:
            value = pawn_data.get_editor_property(prop)
            if prop == "AbilitySets":
                log_result(f"get_editor_property('{prop}')", True, f"数量: {len(value) if value else 0}")
            else:
                log_result(f"get_editor_property('{prop}')", True, f"值: {value}")
        except Exception as e:
            log_result(f"get_editor_property('{prop}')", False, str(e))


def test_set_none_values(pawn_data):
    """测试2: 设置属性为 None"""
    log_separator("测试2: 设置属性为 None")
    
    if not pawn_data:
        return
    
    # 测试 InputConfig = None
    try:
        pawn_data.set_editor_property("InputConfig", None)
        value = pawn_data.get_editor_property("InputConfig")
        log_result("InputConfig = None", value is None, f"当前值: {value}")
    except Exception as e:
        log_result("InputConfig = None", False, str(e))
    
    # 测试 DefaultCameraMode = None
    try:
        pawn_data.set_editor_property("DefaultCameraMode", None)
        value = pawn_data.get_editor_property("DefaultCameraMode")
        log_result("DefaultCameraMode = None", value is None, f"当前值: {value}")
    except Exception as e:
        log_result("DefaultCameraMode = None", False, str(e))
    
    # 测试 PawnClass = None
    try:
        pawn_data.set_editor_property("PawnClass", None)
        value = pawn_data.get_editor_property("PawnClass")
        log_result("PawnClass = None", value is None, f"当前值: {value}")
    except Exception as e:
        log_result("PawnClass = None", False, str(e))
    
    # 测试 AbilitySets = []
    try:
        pawn_data.set_editor_property("AbilitySets", [])
        value = pawn_data.get_editor_property("AbilitySets")
        log_result("AbilitySets = []", len(value) == 0 if value is not None else False, 
                   f"长度: {len(value) if value else 'None'}")
    except Exception as e:
        log_result("AbilitySets = []", False, str(e))


def test_set_input_config(pawn_data):
    """测试3: 设置 InputConfig"""
    log_separator("测试3: 设置 InputConfig")
    
    if not pawn_data:
        return None
    
    # 查找可用的 InputConfig
    input_config_path = "/Game/Input/InputConfig"
    assets = unreal.EditorAssetLibrary.list_assets(input_config_path, recursive=False)
    
    unreal.log(f"  可用 InputConfig: {len(assets)} 个")
    
    if not assets:
        log_result("查找 InputConfig", False, "目录为空")
        return None
    
    # 加载第一个
    first_path = assets[0].split(".")[0]
    input_config = unreal.load_asset(first_path)
    
    if not input_config:
        log_result("加载 InputConfig", False)
        return None
    
    unreal.log(f"  使用: {input_config.get_name()}")
    
    # 设置
    try:
        pawn_data.set_editor_property("InputConfig", input_config)
        value = pawn_data.get_editor_property("InputConfig")
        log_result("设置 InputConfig", value == input_config)
        return input_config
    except Exception as e:
        log_result("设置 InputConfig", False, str(e))
        return None


def test_set_ability_sets(pawn_data):
    """测试4: 设置 AbilitySets"""
    log_separator("测试4: 设置 AbilitySets")
    
    if not pawn_data:
        return
    
    # 查找可用的 AbilitySet
    ability_set_path = "/Game/Gameplay/Abilities/AbilitySets"
    assets = unreal.EditorAssetLibrary.list_assets(ability_set_path, recursive=False)
    
    unreal.log(f"  可用 AbilitySet: {len(assets)} 个")
    
    if not assets:
        log_result("查找 AbilitySet", False, "目录为空")
        return
    
    # 加载前2个
    ability_sets = []
    for asset_path in assets[:2]:
        path = asset_path.split(".")[0]
        asset = unreal.load_asset(path)
        if asset:
            ability_sets.append(asset)
            unreal.log(f"    加载: {asset.get_name()}")
    
    if not ability_sets:
        log_result("加载 AbilitySet", False)
        return
    
    # 设置
    try:
        pawn_data.set_editor_property("AbilitySets", ability_sets)
        value = pawn_data.get_editor_property("AbilitySets")
        log_result("设置 AbilitySets", len(value) == len(ability_sets), 
                   f"期望: {len(ability_sets)}, 实际: {len(value)}")
    except Exception as e:
        log_result("设置 AbilitySets", False, str(e))


def test_set_pawn_class(pawn_data):
    """测试5: 设置 PawnClass"""
    log_separator("测试5: 设置 PawnClass (蓝图类)")
    
    if not pawn_data:
        return
    
    # 查找 BP_ 开头的蓝图
    unreal.log("  查找 Pawn 蓝图类...")
    
    search_paths = ["/Game/Characters/Heroes", "/Game/Characters"]
    found_class = None
    
    for search_path in search_paths:
        try:
            assets = unreal.EditorAssetLibrary.list_assets(search_path, recursive=True)
            bp_assets = [a for a in assets if "/BP_" in a and not a.endswith("_C")]
            
            for asset_path in bp_assets[:5]:
                clean_path = asset_path.split(".")[0]
                unreal.log(f"    尝试: {clean_path}")
                
                # 构造类路径
                asset_name = clean_path.split("/")[-1]
                class_path = f"{clean_path}.{asset_name}_C"
                
                try:
                    loaded_class = unreal.load_class(None, class_path)
                    if loaded_class:
                        unreal.log(f"    ✓ 加载成功: {loaded_class.get_name()}")
                        found_class = loaded_class
                        break
                except:
                    pass
            
            if found_class:
                break
        except:
            pass
    
    if not found_class:
        log_result("查找 Pawn 蓝图类", False, "未找到可用的蓝图")
        return
    
    # 设置
    try:
        pawn_data.set_editor_property("PawnClass", found_class)
        value = pawn_data.get_editor_property("PawnClass")
        log_result("设置 PawnClass", value == found_class)
    except Exception as e:
        log_result("设置 PawnClass", False, str(e))


def test_set_camera_mode(pawn_data):
    """测试6: 设置 DefaultCameraMode"""
    log_separator("测试6: 设置 DefaultCameraMode (蓝图类)")
    
    if not pawn_data:
        return
    
    unreal.log("  查找 CameraMode 蓝图类...")
    
    search_paths = ["/Game/Characters", "/Game/System"]
    found_class = None
    
    for search_path in search_paths:
        try:
            assets = unreal.EditorAssetLibrary.list_assets(search_path, recursive=True)
            cm_assets = [a for a in assets if "/CM_" in a and not a.endswith("_C")]
            
            for asset_path in cm_assets[:5]:
                clean_path = asset_path.split(".")[0]
                unreal.log(f"    尝试: {clean_path}")
                
                asset_name = clean_path.split("/")[-1]
                class_path = f"{clean_path}.{asset_name}_C"
                
                try:
                    loaded_class = unreal.load_class(None, class_path)
                    if loaded_class:
                        unreal.log(f"    ✓ 加载成功: {loaded_class.get_name()}")
                        found_class = loaded_class
                        break
                except:
                    pass
            
            if found_class:
                break
        except:
            pass
    
    if not found_class:
        log_result("查找 CameraMode 蓝图类", False, "未找到可用的蓝图")
        return
    
    # 设置
    try:
        pawn_data.set_editor_property("DefaultCameraMode", found_class)
        value = pawn_data.get_editor_property("DefaultCameraMode")
        log_result("设置 DefaultCameraMode", value == found_class)
    except Exception as e:
        log_result("设置 DefaultCameraMode", False, str(e))


def test_save_and_reload(pawn_data):
    """测试7: 保存并重新加载验证"""
    log_separator("测试7: 保存并重新加载")
    
    if not pawn_data:
        return
    
    # 保存
    try:
        unreal.EditorAssetLibrary.save_asset(TEST_ASSET_PATH)
        log_result("保存资产", True)
    except Exception as e:
        log_result("保存资产", False, str(e))
        return
    
    # 重新加载
    try:
        reloaded = unreal.load_asset(TEST_ASSET_PATH)
        if reloaded:
            log_result("重新加载资产", True)
            
            # 验证属性
            input_config = reloaded.get_editor_property("InputConfig")
            ability_sets = reloaded.get_editor_property("AbilitySets")
            pawn_class = reloaded.get_editor_property("PawnClass")
            camera_mode = reloaded.get_editor_property("DefaultCameraMode")
            
            unreal.log(f"  InputConfig: {input_config}")
            unreal.log(f"  AbilitySets: {len(ability_sets) if ability_sets else 0} 项")
            unreal.log(f"  PawnClass: {pawn_class}")
            unreal.log(f"  DefaultCameraMode: {camera_mode}")
        else:
            log_result("重新加载资产", False)
    except Exception as e:
        log_result("重新加载资产", False, str(e))


def test_clear_after_set(pawn_data):
    """测试8: 设置值后再清空"""
    log_separator("测试8: 设置值后再清空")
    
    if not pawn_data:
        return
    
    # 清空 InputConfig
    try:
        pawn_data.set_editor_property("InputConfig", None)
        value = pawn_data.get_editor_property("InputConfig")
        log_result("清空 InputConfig (设置后)", value is None, f"值: {value}")
    except Exception as e:
        log_result("清空 InputConfig (设置后)", False, str(e))
    
    # 清空 DefaultCameraMode
    try:
        pawn_data.set_editor_property("DefaultCameraMode", None)
        value = pawn_data.get_editor_property("DefaultCameraMode")
        log_result("清空 DefaultCameraMode (设置后)", value is None, f"值: {value}")
    except Exception as e:
        log_result("清空 DefaultCameraMode (设置后)", False, str(e))
    
    # 清空 AbilitySets
    try:
        pawn_data.set_editor_property("AbilitySets", [])
        value = pawn_data.get_editor_property("AbilitySets")
        log_result("清空 AbilitySets (设置后)", len(value) == 0 if value else False)
    except Exception as e:
        log_result("清空 AbilitySets (设置后)", False, str(e))
    
    # 保存清空后的状态
    try:
        unreal.EditorAssetLibrary.save_asset(TEST_ASSET_PATH)
        log_result("保存清空后状态", True)
    except Exception as e:
        log_result("保存清空后状态", False, str(e))


def run_all_tests():
    """运行所有测试"""
    unreal.log("\n")
    unreal.log("*" * 60)
    unreal.log("*  DJ01 PawnData API 测试")
    unreal.log("*  临时资产保留用于检查: " + TEST_ASSET_PATH)
    unreal.log("*" * 60)
    
    # 创建测试资产
    pawn_data = create_test_pawn_data()
    
    if not pawn_data:
        unreal.log("\n❌ 无法创建测试资产，测试终止")
        return
    
    # 运行测试
    test_get_properties(pawn_data)
    test_set_none_values(pawn_data)
    test_set_input_config(pawn_data)
    test_set_ability_sets(pawn_data)
    test_set_pawn_class(pawn_data)
    test_set_camera_mode(pawn_data)
    test_save_and_reload(pawn_data)
    # 注释掉清空测试，保留最后设置的值
    # test_clear_after_set(pawn_data)
    
    # 不删除，保留资产用于检查
    # delete_test_pawn_data()
    
    unreal.log("\n")
    unreal.log("*" * 60)
    unreal.log("*  测试完成！")
    unreal.log("*  请在 Content Browser 检查: " + TEST_ASSET_PATH)
    unreal.log("*  手动删除: 右键 -> Delete")
    unreal.log("*" * 60)


# 入口
if __name__ == "__main__":
    run_all_tests()
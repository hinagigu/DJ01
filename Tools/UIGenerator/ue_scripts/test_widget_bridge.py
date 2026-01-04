#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Widget Bridge 测试脚本
测试 UDJ01WidgetBlueprintLibrary C++ Bridge 是否正常工作

使用方式：
1. 确保 DJ01Editor 模块已编译成功
2. 在 UE 编辑器中打开 Output Log (Window -> Developer Tools -> Output Log)
3. 执行: py "D:/UnrealProjects/DJ01/Tools/UIGenerator/ue_scripts/test_widget_bridge.py"
"""

import unreal

def log(msg):
    """打印日志"""
    unreal.log(f"[WidgetBridge] {msg}")

def log_error(msg):
    """打印错误"""
    unreal.log_error(f"[WidgetBridge] {msg}")

def log_warning(msg):
    """打印警告"""
    unreal.log_warning(f"[WidgetBridge] {msg}")

def test_bridge_available():
    """测试 1: 检查 Bridge 是否可用"""
    log("=" * 60)
    log("测试 1: 检查 DJ01WidgetBlueprintLibrary 是否可用")
    log("=" * 60)
    
    try:
        lib = unreal.DJ01WidgetBlueprintLibrary
        log(f"  ✓ DJ01WidgetBlueprintLibrary 可用: {lib}")
        
        # 列出所有方法
        methods = [m for m in dir(lib) if not m.startswith('_') and callable(getattr(lib, m, None))]
        log(f"  可用方法:")
        for m in methods:
            log(f"    - {m}()")
        
        return lib
    except AttributeError as e:
        log_error(f"  ✗ DJ01WidgetBlueprintLibrary 不可用!")
        log_error(f"    错误: {e}")
        log_error(f"    请确保 DJ01Editor 模块已正确编译")
        return None

def test_load_widget_bp():
    """测试 2: 加载 Widget Blueprint"""
    log("=" * 60)
    log("测试 2: 加载 Widget Blueprint")
    log("=" * 60)
    
    bp_path = "/Game/UI/Generated/WBP_DJ01HealthBar"
    
    # 检查资产是否存在
    if not unreal.EditorAssetLibrary.does_asset_exist(bp_path):
        log_warning(f"  资产不存在: {bp_path}")
        log("  尝试创建新的 Widget Blueprint...")
        
        # 创建新的
        factory = unreal.WidgetBlueprintFactory()
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        
        widget_bp = asset_tools.create_asset(
            "WBP_TestBridge",
            "/Game/UI/Generated",
            unreal.WidgetBlueprint,
            factory
        )
        
        if widget_bp:
            log(f"  ✓ 创建成功: {widget_bp.get_path_name()}")
            return widget_bp
        else:
            log_error("  ✗ 创建失败")
            return None
    
    # 加载现有资产
    asset = unreal.EditorAssetLibrary.load_asset(bp_path)
    if asset:
        log(f"  ✓ 成功加载: {bp_path}")
        log(f"    类型: {type(asset)}")
        return asset
    else:
        log_error(f"  ✗ 无法加载: {bp_path}")
        return None

def test_get_widget_tree(lib, widget_bp):
    """测试 3: 通过 Bridge 获取 WidgetTree"""
    log("=" * 60)
    log("测试 3: 通过 Bridge 获取 WidgetTree")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return None
    
    try:
        widget_tree = lib.get_widget_tree(widget_bp)
        if widget_tree:
            log(f"  ✓ 获取 WidgetTree 成功!")
            log(f"    类型: {type(widget_tree)}")
            return widget_tree
        else:
            log_warning("  WidgetTree 为 None（可能是新创建的空 BP）")
            return None
    except Exception as e:
        log_error(f"  ✗ 获取失败: {e}")
        return None

def test_get_root_widget(lib, widget_bp):
    """测试 4: 获取根 Widget"""
    log("=" * 60)
    log("测试 4: 获取根 Widget")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return None
    
    try:
        root = lib.get_root_widget(widget_bp)
        if root:
            log(f"  ✓ 根 Widget: {root}")
            log(f"    类型: {type(root)}")
            log(f"    名称: {root.get_name()}")
            return root
        else:
            log("  根 Widget 为空（正常，表示还没有添加控件）")
            return None
    except Exception as e:
        log_error(f"  ✗ 获取失败: {e}")
        return None

def test_create_widgets(lib, widget_bp):
    """测试 5: 创建控件"""
    log("=" * 60)
    log("测试 5: 通过 Bridge 创建控件")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return None, None, None
    
    canvas = None
    progress = None
    text = None
    
    # 创建 CanvasPanel
    log("  创建 CanvasPanel...")
    try:
        canvas = lib.create_canvas_panel(widget_bp, "TestCanvas")
        if canvas:
            log(f"    ✓ CanvasPanel 创建成功: {canvas}")
        else:
            log_error("    ✗ 返回 None")
    except Exception as e:
        log_error(f"    ✗ 失败: {e}")
    
    # 创建 ProgressBar
    log("  创建 ProgressBar...")
    try:
        progress = lib.create_progress_bar(widget_bp, "TestProgressBar")
        if progress:
            log(f"    ✓ ProgressBar 创建成功: {progress}")
        else:
            log_error("    ✗ 返回 None")
    except Exception as e:
        log_error(f"    ✗ 失败: {e}")
    
    # 创建 TextBlock
    log("  创建 TextBlock...")
    try:
        text = lib.create_text_block(widget_bp, "TestTextBlock")
        if text:
            log(f"    ✓ TextBlock 创建成功: {text}")
        else:
            log_error("    ✗ 返回 None")
    except Exception as e:
        log_error(f"    ✗ 失败: {e}")
    
    return canvas, progress, text

def test_set_root_and_hierarchy(lib, widget_bp, canvas, progress, text):
    """测试 6: 设置层级结构"""
    log("=" * 60)
    log("测试 6: 设置层级结构")
    log("=" * 60)
    
    if not lib or not widget_bp or not canvas:
        log_error("  缺少必要参数")
        return False
    
    # 设置根 Widget
    log("  设置 CanvasPanel 为根控件...")
    try:
        result = lib.set_root_widget(widget_bp, canvas)
        if result:
            log("    ✓ 设置成功")
        else:
            log_error("    ✗ 设置失败")
            return False
    except Exception as e:
        log_error(f"    ✗ 异常: {e}")
        return False
    
    # 添加 ProgressBar 到 Canvas
    if progress:
        log("  添加 ProgressBar 到 Canvas...")
        try:
            result = lib.add_child_to_canvas(
                canvas, 
                progress, 
                unreal.Vector2D(50, 50),     # Position
                unreal.Vector2D(200, 30)     # Size
            )
            if result:
                log("    ✓ 添加成功")
            else:
                log_error("    ✗ 添加失败")
        except Exception as e:
            log_error(f"    ✗ 异常: {e}")
    
    # 添加 TextBlock 到 Canvas
    if text:
        log("  添加 TextBlock 到 Canvas...")
        try:
            result = lib.add_child_to_canvas(
                canvas, 
                text, 
                unreal.Vector2D(50, 100),    # Position
                unreal.Vector2D(150, 25)     # Size
            )
            if result:
                log("    ✓ 添加成功")
            else:
                log_error("    ✗ 添加失败")
        except Exception as e:
            log_error(f"    ✗ 异常: {e}")
    
    return True

def test_find_widget(lib, widget_bp):
    """测试 7: 查找控件"""
    log("=" * 60)
    log("测试 7: 查找控件")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return
    
    widgets_to_find = ["TestCanvas", "TestProgressBar", "TestTextBlock"]
    
    for name in widgets_to_find:
        try:
            widget = lib.find_widget_by_name(widget_bp, name)
            if widget:
                log(f"  ✓ 找到 {name}: {widget}")
            else:
                log_warning(f"  ✗ 未找到 {name}")
        except Exception as e:
            log_error(f"  ✗ 查找 {name} 失败: {e}")

def test_get_all_widgets(lib, widget_bp):
    """测试 8: 获取所有控件"""
    log("=" * 60)
    log("测试 8: 获取所有控件")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return
    
    try:
        all_widgets = lib.get_all_widgets(widget_bp)
        log(f"  共 {len(all_widgets)} 个控件:")
        for w in all_widgets:
            log(f"    - {w.get_name()} ({type(w).__name__})")
    except Exception as e:
        log_error(f"  ✗ 获取失败: {e}")

def test_save(lib, widget_bp):
    """测试 9: 保存"""
    log("=" * 60)
    log("测试 9: 保存 Widget Blueprint")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return False
    
    try:
        # 先标记为脏
        lib.mark_dirty(widget_bp)
        log("  ✓ 标记为已修改")
        
        # 保存
        result = lib.save_widget_blueprint(widget_bp)
        if result:
            log("  ✓ 保存成功!")
            return True
        else:
            log_error("  ✗ 保存失败")
            return False
    except Exception as e:
        log_error(f"  ✗ 保存异常: {e}")
        return False

def test_json_creation(lib, widget_bp):
    """测试 10: 通过 JSON 批量创建"""
    log("=" * 60)
    log("测试 10: 通过 JSON 批量创建控件")
    log("=" * 60)
    
    if not lib or not widget_bp:
        log_error("  缺少必要参数")
        return False
    
    import json
    
    schema = {
        "components": [
            {
                "name": "RootCanvas",
                "type": "CanvasPanel",
                "children": [
                    {"name": "HealthBar", "type": "ProgressBar"},
                    {"name": "HealthText", "type": "TextBlock"},
                    {"name": "ManaBar", "type": "ProgressBar"},
                    {"name": "ManaText", "type": "TextBlock"}
                ]
            }
        ]
    }
    
    schema_json = json.dumps(schema)
    log(f"  Schema JSON: {schema_json[:100]}...")
    
    try:
        result = lib.create_widgets_from_json(widget_bp, schema_json)
        if result:
            log("  ✓ JSON 批量创建成功!")
            return True
        else:
            log_error("  ✗ JSON 批量创建失败")
            return False
    except Exception as e:
        log_error(f"  ✗ 异常: {e}")
        return False

def run_all_tests():
    """运行所有测试"""
    log("")
    log("*" * 60)
    log("Widget Bridge 测试开始")
    log("*" * 60)
    log("")
    
    # 测试 1: 检查 Bridge 是否可用
    lib = test_bridge_available()
    if not lib:
        log_error("Bridge 不可用，测试终止")
        return
    log("")
    
    # 测试 2: 加载/创建 Widget Blueprint
    widget_bp = test_load_widget_bp()
    if not widget_bp:
        log_error("无法获取 Widget Blueprint，测试终止")
        return
    log("")
    
    # 测试 3: 获取 WidgetTree
    widget_tree = test_get_widget_tree(lib, widget_bp)
    log("")
    
    # 测试 4: 获取现有根 Widget
    existing_root = test_get_root_widget(lib, widget_bp)
    log("")
    
    # 如果已有根控件，跳过创建测试
    if existing_root:
        log("已有根 Widget，跳过创建测试")
        test_get_all_widgets(lib, widget_bp)
    else:
        # 测试 5: 创建控件
        canvas, progress, text = test_create_widgets(lib, widget_bp)
        log("")
        
        # 测试 6: 设置层级
        if canvas:
            test_set_root_and_hierarchy(lib, widget_bp, canvas, progress, text)
            log("")
        
        # 测试 7: 查找控件
        test_find_widget(lib, widget_bp)
        log("")
        
        # 测试 8: 获取所有控件
        test_get_all_widgets(lib, widget_bp)
        log("")
        
        # 测试 9: 保存
        test_save(lib, widget_bp)
    
    log("")
    log("*" * 60)
    log("测试完成！请在 UMG Designer 中打开 Widget Blueprint 验证")
    log("*" * 60)
    log("")

# 运行测试
if __name__ == "__main__":
    run_all_tests()
else:
    run_all_tests()
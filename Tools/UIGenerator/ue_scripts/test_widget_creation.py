#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Widget 创建测试脚本
在 UE 编辑器的 Python 控制台中运行此脚本，测试各种创建 Widget 的方法

使用方式：
1. 在 UE 编辑器中打开 Output Log (Window -> Developer Tools -> Output Log)
2. 打开 Python 控制台 (Window -> Developer Tools -> Python Console) 或者直接在 Output Log 的 Cmd 输入
3. 执行: py "D:/UnrealProjects/DJ01/Tools/UIGenerator/ue_scripts/test_widget_creation.py"
"""

import unreal

def log(msg):
    """打印日志"""
    unreal.log(f"[WidgetTest] {msg}")

def log_error(msg):
    """打印错误"""
    unreal.log_error(f"[WidgetTest] {msg}")

def log_warning(msg):
    """打印警告"""
    unreal.log_warning(f"[WidgetTest] {msg}")

def test_find_widget_classes():
    """测试 1: 查找 Widget 类"""
    log("=" * 60)
    log("测试 1: 查找 Widget 类")
    log("=" * 60)
    
    # 直接从 unreal 模块获取类
    classes_to_find = [
        ("CanvasPanel", "CanvasPanel"),
        ("ProgressBar", "ProgressBar"),
        ("TextBlock", "TextBlock"),
        ("Image", "Image"),
        ("Button", "Button"),
        ("HorizontalBox", "HorizontalBox"),
        ("VerticalBox", "VerticalBox"),
        ("Overlay", "Overlay"),
        ("SizeBox", "SizeBox"),
    ]
    
    found_classes = {}
    for name, class_name in classes_to_find:
        try:
            widget_class = getattr(unreal, class_name, None)
            if widget_class:
                log(f"  ✓ {name}: unreal.{class_name}")
                found_classes[name] = widget_class
            else:
                log_warning(f"  ✗ {name}: unreal.{class_name} 不存在")
        except Exception as e:
            log_warning(f"  ✗ {name}: 获取失败 - {e}")
    
    # 列出所有可用的 Widget 相关类
    log("")
    log("  所有 UMG 相关类:")
    umg_classes = [c for c in dir(unreal) if 'panel' in c.lower() or 'box' in c.lower() 
                   or 'text' in c.lower() or 'image' in c.lower() or 'button' in c.lower()
                   or 'progress' in c.lower() or 'widget' in c.lower()]
    for c in sorted(umg_classes)[:30]:
        log(f"    - unreal.{c}")
    
    return found_classes

def test_load_existing_widget_bp():
    """测试 2: 加载现有的 Widget Blueprint"""
    log("=" * 60)
    log("测试 2: 加载现有 Widget Blueprint")
    log("=" * 60)
    
    # 尝试加载 WBP_DJ01HealthBar
    bp_path = "/Game/UI/Generated/WBP_DJ01HealthBar"
    
    asset = unreal.EditorAssetLibrary.load_asset(bp_path)
    if asset:
        log(f"  ✓ 成功加载: {bp_path}")
        log(f"    类型: {type(asset)}")
        log(f"    类名: {asset.get_class().get_name()}")
        
        # 检查是否是 WidgetBlueprint
        if isinstance(asset, unreal.WidgetBlueprint):
            log(f"    ✓ 是 WidgetBlueprint")
            return asset
        else:
            log_warning(f"    ✗ 不是 WidgetBlueprint，是 {type(asset)}")
    else:
        log_warning(f"  ✗ 无法加载: {bp_path}")
    
    return None

def test_get_widget_tree(widget_bp):
    """测试 3: 获取 WidgetTree"""
    log("=" * 60)
    log("测试 3: 获取 WidgetTree")
    log("=" * 60)
    
    if not widget_bp:
        log_error("  没有 Widget Blueprint")
        return None
    
    # 方法 1: get_editor_property
    try:
        widget_tree = widget_bp.get_editor_property("widget_tree")
        if widget_tree:
            log(f"  ✓ 方法1 (get_editor_property): {widget_tree}")
            log(f"    类型: {type(widget_tree)}")
            return widget_tree
    except Exception as e:
        log_warning(f"  ✗ 方法1 失败: {e}")
    
    # 方法 2: 直接属性访问
    try:
        if hasattr(widget_bp, 'widget_tree'):
            widget_tree = widget_bp.widget_tree
            if widget_tree:
                log(f"  ✓ 方法2 (直接属性): {widget_tree}")
                return widget_tree
    except Exception as e:
        log_warning(f"  ✗ 方法2 失败: {e}")
    
    # 列出所有可用属性
    log("  可用属性:")
    try:
        for prop in dir(widget_bp):
            if not prop.startswith('_'):
                log(f"    - {prop}")
    except:
        pass
    
    return None

def test_get_root_widget(widget_tree):
    """测试 4: 获取根 Widget"""
    log("=" * 60)
    log("测试 4: 获取根 Widget")
    log("=" * 60)
    
    if not widget_tree:
        log_error("  没有 WidgetTree")
        return None
    
    try:
        root = widget_tree.get_editor_property("root_widget")
        if root:
            log(f"  ✓ 根 Widget: {root}")
            log(f"    类型: {type(root)}")
            log(f"    名称: {root.get_name()}")
            return root
        else:
            log("  根 Widget 为空（正常，表示还没有添加控件）")
    except Exception as e:
        log_warning(f"  获取根 Widget 失败: {e}")
    
    return None

def test_construct_widget(widget_tree, widget_classes):
    """测试 5: 使用 construct_widget 创建控件"""
    log("=" * 60)
    log("测试 5: 使用各种方法创建控件")
    log("=" * 60)
    
    if not widget_tree:
        log_error("  没有 WidgetTree")
        return None
    
    canvas = None
    
    # 方法 1: 使用 construct_widget
    log("  方法 1: widget_tree.construct_widget()")
    if hasattr(widget_tree, 'construct_widget'):
        try:
            canvas_class = widget_classes.get("CanvasPanel")
            if canvas_class:
                canvas = widget_tree.construct_widget(canvas_class, "TestCanvas")
                if canvas:
                    log(f"    ✓ 成功: {canvas}")
                    return canvas
                else:
                    log_warning("    ✗ 返回 None")
        except Exception as e:
            log_error(f"    ✗ 失败: {e}")
    else:
        log_warning("    ✗ construct_widget 方法不存在")
    
    # 方法 2: 直接实例化
    log("  方法 2: 直接实例化 unreal.CanvasPanel()")
    try:
        canvas = unreal.CanvasPanel()
        if canvas:
            log(f"    ✓ 成功: {canvas}")
            # 尝试设置名称
            try:
                canvas.rename("TestCanvas")
            except:
                pass
            return canvas
    except Exception as e:
        log_error(f"    ✗ 失败: {e}")
    
    # 方法 3: 使用 new_object
    log("  方法 3: unreal.new_object()")
    if hasattr(unreal, 'new_object'):
        try:
            canvas = unreal.new_object(unreal.CanvasPanel)
            if canvas:
                log(f"    ✓ 成功: {canvas}")
                return canvas
        except Exception as e:
            log_error(f"    ✗ 失败: {e}")
    else:
        log_warning("    ✗ new_object 不存在")
    
    return canvas

def test_set_root_widget(widget_tree, root_widget):
    """测试 6: 设置根 Widget"""
    log("=" * 60)
    log("测试 6: 设置根 Widget")
    log("=" * 60)
    
    if not widget_tree or not root_widget:
        log_error("  缺少 WidgetTree 或 root_widget")
        return False
    
    try:
        widget_tree.set_editor_property("root_widget", root_widget)
        log(f"  ✓ 设置根 Widget 成功")
        
        # 验证
        verify_root = widget_tree.get_editor_property("root_widget")
        if verify_root == root_widget:
            log(f"  ✓ 验证成功")
            return True
        else:
            log_warning(f"  ✗ 验证失败，root 不匹配")
    except Exception as e:
        log_error(f"  ✗ 设置根 Widget 失败: {e}")
    
    return False

def test_add_child_widgets(widget_tree, parent_widget, widget_classes):
    """测试 7: 添加子控件"""
    log("=" * 60)
    log("测试 7: 添加子控件到父控件")
    log("=" * 60)
    
    if not parent_widget:
        log_error("  缺少 parent_widget")
        return
    
    # 列出父控件的所有 add 相关方法
    log(f"  父控件类型: {type(parent_widget)}")
    add_methods = [m for m in dir(parent_widget) if 'add' in m.lower() or 'child' in m.lower()]
    log(f"  add/child 相关方法: {add_methods}")
    
    # 创建 ProgressBar
    log("")
    log("  创建 ProgressBar:")
    progress_bar = None
    
    # 先尝试通过 widget_tree
    if widget_tree and hasattr(widget_tree, 'construct_widget'):
        try:
            progress_bar = widget_tree.construct_widget(unreal.ProgressBar, "TestProgressBar")
            if progress_bar:
                log(f"    ✓ widget_tree.construct_widget 成功")
        except Exception as e:
            log_warning(f"    ✗ widget_tree.construct_widget 失败: {e}")
    
    # 如果失败，直接实例化
    if not progress_bar:
        try:
            progress_bar = unreal.ProgressBar()
            log(f"    ✓ 直接实例化成功: {progress_bar}")
        except Exception as e:
            log_error(f"    ✗ 直接实例化失败: {e}")
    
    # 尝试添加到父控件
    if progress_bar:
        log("    尝试添加到父控件:")
        added = False
        
        # 方法 1: add_child_to_canvas (CanvasPanel)
        if hasattr(parent_widget, 'add_child_to_canvas'):
            try:
                slot = parent_widget.add_child_to_canvas(progress_bar)
                log(f"      add_child_to_canvas: slot={slot}")
                added = True
            except Exception as e:
                log_warning(f"      add_child_to_canvas 失败: {e}")
        
        # 方法 2: add_child (PanelWidget)
        if not added and hasattr(parent_widget, 'add_child'):
            try:
                slot = parent_widget.add_child(progress_bar)
                log(f"      add_child: slot={slot}")
                added = True
            except Exception as e:
                log_warning(f"      add_child 失败: {e}")
        
        # 方法 3: add_child_to_overlay
        if not added and hasattr(parent_widget, 'add_child_to_overlay'):
            try:
                slot = parent_widget.add_child_to_overlay(progress_bar)
                log(f"      add_child_to_overlay: slot={slot}")
                added = True
            except Exception as e:
                log_warning(f"      add_child_to_overlay 失败: {e}")
        
        if not added:
            log_warning("      所有添加方法都失败了")
    
    # 创建 TextBlock
    log("")
    log("  创建 TextBlock:")
    text_block = None
    
    if widget_tree and hasattr(widget_tree, 'construct_widget'):
        try:
            text_block = widget_tree.construct_widget(unreal.TextBlock, "TestTextBlock")
            if text_block:
                log(f"    ✓ widget_tree.construct_widget 成功")
        except Exception as e:
            log_warning(f"    ✗ widget_tree.construct_widget 失败: {e}")
    
    if not text_block:
        try:
            text_block = unreal.TextBlock()
            log(f"    ✓ 直接实例化成功: {text_block}")
        except Exception as e:
            log_error(f"    ✗ 直接实例化失败: {e}")
    
    if text_block and parent_widget:
        try:
            if hasattr(parent_widget, 'add_child_to_canvas'):
                slot = parent_widget.add_child_to_canvas(text_block)
                log(f"    添加到 Canvas: slot={slot}")
            elif hasattr(parent_widget, 'add_child'):
                slot = parent_widget.add_child(text_block)
                log(f"    添加子控件: slot={slot}")
        except Exception as e:
            log_error(f"    添加失败: {e}")

def test_list_widget_tree_methods(widget_tree):
    """列出 WidgetTree 的所有方法"""
    log("=" * 60)
    log("WidgetTree 可用方法和属性")
    log("=" * 60)
    
    if not widget_tree:
        return
    
    methods = []
    properties = []
    
    for attr in dir(widget_tree):
        if attr.startswith('_'):
            continue
        try:
            val = getattr(widget_tree, attr)
            if callable(val):
                methods.append(attr)
            else:
                properties.append(f"{attr} = {val}")
        except:
            properties.append(f"{attr} (无法访问)")
    
    log("  方法:")
    for m in sorted(methods):
        log(f"    - {m}()")
    
    log("  属性:")
    for p in sorted(properties):
        log(f"    - {p}")

def test_alternative_creation():
    """测试 8: 替代方案"""
    log("=" * 60)
    log("测试 8: 替代方案")
    log("=" * 60)
    
    # 检查 WidgetBlueprintFactory
    log("  检查 WidgetBlueprintFactory:")
    try:
        factory = unreal.WidgetBlueprintFactory()
        log(f"    ✓ WidgetBlueprintFactory 可用: {factory}")
        log(f"    方法: {[m for m in dir(factory) if not m.startswith('_')]}")
    except Exception as e:
        log_warning(f"    ✗ WidgetBlueprintFactory: {e}")
    
    # 检查 UMGEditor 相关
    log("")
    log("  检查 UMG Editor 相关类:")
    umg_editor_classes = [c for c in dir(unreal) if 'widget' in c.lower() and 'edit' in c.lower()]
    for c in umg_editor_classes:
        log(f"    - {c}")
    
    # 检查 WidgetTree 类是否存在
    log("")
    log("  检查 WidgetTree 类:")
    try:
        wt = unreal.WidgetTree
        log(f"    ✓ WidgetTree 类存在: {wt}")
        log(f"    方法: {[m for m in dir(wt) if not m.startswith('_')]}")
    except Exception as e:
        log_warning(f"    ✗ WidgetTree: {e}")
    
    # 检查 EditorUtilityWidget
    log("")
    log("  检查 EditorUtilityWidget:")
    try:
        euw = unreal.EditorUtilityWidget
        log(f"    ✓ EditorUtilityWidget 可用: {euw}")
    except Exception as e:
        log_warning(f"    ✗ EditorUtilityWidget: {e}")
    
    # 检查 WidgetBlueprintEditorUtils
    log("")
    log("  检查 WidgetBlueprint Editor 工具:")
    editor_utils = [c for c in dir(unreal) if 'blueprint' in c.lower() and ('util' in c.lower() or 'edit' in c.lower() or 'lib' in c.lower())]
    for c in editor_utils[:15]:
        log(f"    - {c}")

def test_subsystem_approach():
    """测试 9: 通过 Subsystem 访问"""
    log("=" * 60)
    log("测试 9: 通过 Subsystem / EditorSubsystem 访问")
    log("=" * 60)
    
    # 获取 Editor Subsystem
    try:
        eas = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
        if eas:
            log(f"  ✓ AssetEditorSubsystem: {eas}")
            log(f"    方法: {[m for m in dir(eas) if not m.startswith('_')]}")
    except Exception as e:
        log_warning(f"  ✗ AssetEditorSubsystem: {e}")
    
    # UnrealEditorSubsystem
    try:
        ues = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem)
        if ues:
            log(f"  ✓ UnrealEditorSubsystem: {ues}")
    except Exception as e:
        log_warning(f"  ✗ UnrealEditorSubsystem: {e}")
    
    # 列出所有 Subsystem
    log("")
    log("  所有可用 Subsystem:")
    subsystems = [c for c in dir(unreal) if 'subsystem' in c.lower()]
    for s in subsystems[:20]:
        log(f"    - {s}")

def test_widget_blueprint_generated_class(widget_bp):
    """测试 10: 通过 GeneratedClass 访问"""
    log("=" * 60)
    log("测试 10: 通过 GeneratedClass 访问 Widget 默认对象")
    log("=" * 60)
    
    if not widget_bp:
        log_error("  没有 Widget Blueprint")
        return
    
    try:
        gen_class = widget_bp.generated_class()
        if gen_class:
            log(f"  ✓ GeneratedClass: {gen_class}")
            log(f"    类名: {gen_class.get_name()}")
            
            # 获取 CDO (Class Default Object)
            try:
                cdo = gen_class.get_default_object()
                if cdo:
                    log(f"    ✓ CDO: {cdo}")
                    log(f"      类型: {type(cdo)}")
                    
                    # 列出 CDO 的属性
                    cdo_props = [p for p in dir(cdo) if not p.startswith('_')]
                    widget_props = [p for p in cdo_props if 'widget' in p.lower() or 'root' in p.lower() or 'canvas' in p.lower()]
                    log(f"      Widget 相关属性: {widget_props}")
            except Exception as e:
                log_warning(f"    ✗ 获取 CDO 失败: {e}")
    except Exception as e:
        log_error(f"  ✗ 获取 GeneratedClass 失败: {e}")

def test_editor_scripting():
    """测试 11: Editor Scripting Utilities"""
    log("=" * 60)
    log("测试 11: Editor Scripting Utilities")
    log("=" * 60)
    
    # AssetEditorSubsystem - 打开资产编辑器
    log("  检查 AssetEditorSubsystem:")
    try:
        aes = unreal.get_editor_subsystem(unreal.AssetEditorSubsystem)
        if aes:
            log(f"    ✓ AssetEditorSubsystem 获取成功")
            # 打开 Widget Blueprint 编辑器
            bp_path = "/Game/UI/Generated/WBP_DJ01HealthBar"
            asset = unreal.EditorAssetLibrary.load_asset(bp_path)
            if asset:
                aes.open_editor_for_assets([asset])
                log(f"    ✓ 已尝试打开编辑器: {bp_path}")
    except Exception as e:
        log_warning(f"    ✗ AssetEditorSubsystem 失败: {e}")
    
    # 检查是否有 UMG Editor 模块
    log("")
    log("  检查 UMGEditor 模块类:")
    umg_editor = [c for c in dir(unreal) if 'umgeditor' in c.lower() or 'widgeteditor' in c.lower()]
    log(f"    找到: {umg_editor}")
    
    # WidgetBlueprintEditor
    log("")
    log("  检查 WidgetBlueprintEditor:")
    wbe_classes = [c for c in dir(unreal) if 'widgetblueprint' in c.lower()]
    for c in wbe_classes:
        log(f"    - {c}")
        try:
            cls = getattr(unreal, c)
            methods = [m for m in dir(cls) if not m.startswith('_') and callable(getattr(cls, m, None))]
            if methods:
                log(f"      方法: {methods[:10]}")
        except:
            pass

def test_create_widget_in_world():
    """测试 12: 在 World 中创建 Widget (运行时方式)"""
    log("=" * 60)
    log("测试 12: 运行时方式创建 Widget")
    log("=" * 60)
    
    # 这种方式只在运行时有效，编辑器中可能不行
    log("  注意: 此方法通常只在运行时有效")
    
    try:
        # 获取 Editor World
        world = unreal.EditorLevelLibrary.get_editor_world()
        if world:
            log(f"  ✓ Editor World: {world}")
            
            # 尝试创建 Widget
            try:
                canvas = unreal.WidgetBlueprintLibrary.create(world, unreal.CanvasPanel)
                log(f"    WidgetBlueprintLibrary.create: {canvas}")
            except Exception as e:
                log_warning(f"    WidgetBlueprintLibrary.create 失败: {e}")
        else:
            log_warning("  ✗ 无法获取 Editor World")
    except Exception as e:
        log_warning(f"  ✗ EditorLevelLibrary: {e}")

def save_widget_bp(widget_bp):
    """保存 Widget Blueprint"""
    log("=" * 60)
    log("保存 Widget Blueprint")
    log("=" * 60)
    
    if not widget_bp:
        log_error("  没有 Widget Blueprint")
        return False
    
    try:
        # 标记为脏
        widget_bp.modify()
        log("  ✓ 标记为已修改")
        
        # 保存
        result = unreal.EditorAssetLibrary.save_asset(widget_bp.get_path_name())
        if result:
            log("  ✓ 保存成功")
            return True
        else:
            log_warning("  ✗ 保存失败")
    except Exception as e:
        log_error(f"  ✗ 保存异常: {e}")
    
    return False

def run_all_tests():
    """运行所有测试"""
    log("")
    log("*" * 60)
    log("Widget 创建测试开始")
    log("*" * 60)
    log("")
    
    # 测试 1: 查找类
    widget_classes = test_find_widget_classes()
    log("")
    
    # 测试 2: 加载 Widget BP
    widget_bp = test_load_existing_widget_bp()
    log("")
    
    # 测试 3: 获取 WidgetTree
    widget_tree = test_get_widget_tree(widget_bp)
    log("")
    
    # 列出 WidgetTree 方法
    if widget_tree:
        test_list_widget_tree_methods(widget_tree)
        log("")
    
    # 测试 4: 获取根 Widget
    existing_root = test_get_root_widget(widget_tree)
    log("")
    
    # 测试 5: 创建控件
    new_canvas = test_construct_widget(widget_tree, widget_classes)
    log("")
    
    # 测试 6: 设置根 Widget（如果还没有根）
    if new_canvas and not existing_root:
        test_set_root_widget(widget_tree, new_canvas)
        log("")
        
        # 测试 7: 添加子控件
        test_add_child_widgets(widget_tree, new_canvas, widget_classes)
        log("")
        
        # 保存
        save_widget_bp(widget_bp)
    elif existing_root:
        log("已有根 Widget，跳过创建测试")
        # 仍然尝试添加子控件到现有根
        test_add_child_widgets(widget_tree, existing_root, widget_classes)
        save_widget_bp(widget_bp)
    
    # 测试 8: 替代方案
    test_alternative_creation()
    log("")
    
    # 测试 9: Subsystem 方式
    test_subsystem_approach()
    log("")
    
    # 测试 10: GeneratedClass
    test_widget_blueprint_generated_class(widget_bp)
    log("")
    
    # 测试 11: Editor Scripting
    test_editor_scripting()
    log("")
    
    # 测试 12: 运行时创建
    test_create_widget_in_world()
    
    log("")
    log("*" * 60)
    log("测试完成！请查看上方日志")
    log("*" * 60)
    log("")
    
    # 最终结论
    log("")
    log("=" * 60)
    log("结论与建议")
    log("=" * 60)
    log("  UE Python API 限制:")
    log("    - WidgetBlueprint.widget_tree 未暴露给 Python")
    log("    - 无法通过 Python 直接操作 UMG Designer 中的控件层级")
    log("")
    log("  可行的替代方案:")
    log("    1. 使用 C++ Editor Module 自定义命令")
    log("    2. 使用 Editor Utility Widget + Blueprintable 方法")
    log("    3. 手动在 UMG Designer 中添加控件（最简单）")
    log("    4. 生成代码时使用 BindWidgetOptional 避免编译错误")
    log("")

# 运行测试
if __name__ == "__main__":
    run_all_tests()
else:
    # 如果通过 py 命令执行
    run_all_tests()
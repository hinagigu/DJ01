"""
在 UE 内运行的蓝图生成脚本
根据 Schema 创建 Widget Blueprint 并添加组件
"""

import unreal
import json
import os


def create_widget_blueprint(schema_path: str):
    """
    根据 Schema 创建 Widget Blueprint
    
    Args:
        schema_path: Schema JSON 文件路径
    """
    # 加载 Schema
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = json.load(f)
    
    name = schema['name']
    blueprint_path = schema.get('blueprint_path', '/Game/UI/Generated')
    base_class_name = f"{name}Base"
    
    unreal.log(f"[UIGenerator] 开始创建 Widget Blueprint: {name}")
    
    # 查找基类
    base_class = unreal.find_object(None, f"/Script/DJ01.{base_class_name}")
    if not base_class:
        unreal.log_error(f"[UIGenerator] 找不到基类: {base_class_name}")
        unreal.log_error("[UIGenerator] 请先编译 C++ 代码")
        return False
    
    # 创建 Widget Blueprint
    asset_path = f"{blueprint_path}/WBP_{name}"
    
    # 检查是否已存在
    if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
        unreal.log_warning(f"[UIGenerator] 资产已存在: {asset_path}")
        return False
    
    # 创建 Blueprint
    factory = unreal.WidgetBlueprintFactory()
    factory.set_editor_property("parent_class", base_class)
    
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    
    # 分离路径和名称
    package_path = blueprint_path
    asset_name = f"WBP_{name}"
    
    widget_bp = asset_tools.create_asset(
        asset_name,
        package_path,
        unreal.WidgetBlueprint,
        factory
    )
    
    if not widget_bp:
        unreal.log_error("[UIGenerator] 创建 Widget Blueprint 失败")
        return False
    
    unreal.log(f"[UIGenerator] ✅ 创建成功: {asset_path}")
    
    # 注意：通过 Python API 向 Widget Blueprint 添加组件是非常复杂的
    # UE 的 WidgetBlueprint 编辑器 API 不完全暴露给 Python
    # 最实际的方案是：
    # 1. 创建一个空的继承正确基类的 Blueprint
    # 2. 用户在编辑器中手动添加组件（名称必须匹配）
    
    # 打印需要添加的组件列表
    unreal.log("=" * 50)
    unreal.log("[UIGenerator] 请在编辑器中添加以下组件：")
    unreal.log("=" * 50)
    
    _print_required_components(schema.get('components', []), indent=0)
    
    unreal.log("=" * 50)
    unreal.log("[UIGenerator] 组件名称必须完全匹配！")
    unreal.log("=" * 50)
    
    # 保存
    unreal.EditorAssetLibrary.save_asset(asset_path)
    
    return True


def _print_required_components(components: list, indent: int):
    """打印需要的组件层级"""
    prefix = "  " * indent
    for comp in components:
        name = comp['name']
        comp_type = comp['type']
        comment = comp.get('comment', '')
        
        info = f"{prefix}├── [{comp_type}] Name=\"{name}\""
        if comment:
            info += f"  // {comment}"
        
        unreal.log(info)
        
        if 'children' in comp:
            _print_required_components(comp['children'], indent + 1)


def generate_from_schema(schema_path: str):
    """
    外部调用入口
    """
    try:
        return create_widget_blueprint(schema_path)
    except Exception as e:
        import traceback
        unreal.log_error(f"[UIGenerator] 生成失败: {e}")
        unreal.log_error(traceback.format_exc())
        return False


# 测试用
if __name__ == "__main__":
    # 测试路径
    test_schema = "D:/UnrealProjects/DJ01/Tools/UIGenerator/schemas/examples/health_bar.json"
    generate_from_schema(test_schema)
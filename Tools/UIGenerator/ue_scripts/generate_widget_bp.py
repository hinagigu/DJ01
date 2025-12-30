"""
在 UE 内运行的蓝图生成脚本
根据 Schema 创建 Widget Blueprint 并添加组件

核心功能：
1. 创建继承 C++ 基类的 Widget Blueprint
2. 通过 WidgetTree 操作自动添加组件
3. 设置组件层级关系和基本属性
"""

import unreal
import json
import os
from typing import Dict, List, Optional, Any


# =============== 组件类型映射 ===============
WIDGET_CLASS_MAP = {
    # 容器组件
    "CanvasPanel": "CanvasPanel",
    "VerticalBox": "VerticalBox",
    "HorizontalBox": "HorizontalBox",
    "Overlay": "Overlay",
    "SizeBox": "SizeBox",
    "ScaleBox": "ScaleBox",
    "ScrollBox": "ScrollBox",
    "WidgetSwitcher": "WidgetSwitcher",
    "Border": "Border",
    "GridPanel": "GridPanel",
    "UniformGridPanel": "UniformGridPanel",
    "WrapBox": "WrapBox",
    
    # 基础组件
    "TextBlock": "TextBlock",
    "RichTextBlock": "RichTextBlock",
    "Image": "Image",
    "ProgressBar": "ProgressBar",
    "Slider": "Slider",
    "Button": "Button",
    "CheckBox": "CheckBox",
    "EditableText": "EditableText",
    "EditableTextBox": "EditableTextBox",
    "MultiLineEditableText": "MultiLineEditableText",
    "ComboBox": "ComboBoxString",
    "SpinBox": "SpinBox",
    "Spacer": "Spacer",
    "Throbber": "Throbber",
    "CircularThrobber": "CircularThrobber",
    
    # CommonUI 组件
    "CommonTextBlock": "CommonTextBlock",
    "CommonRichTextBlock": "CommonRichTextBlock",
    "CommonButtonBase": "CommonButtonBase",
    "CommonActionWidget": "CommonActionWidget",
    "CommonBorder": "CommonBorder",
    "CommonVisibilitySwitcher": "CommonVisibilitySwitcher",
    "CommonLazyImage": "CommonLazyImage",
    "CommonNumericTextBlock": "CommonNumericTextBlock",
}


class WidgetBlueprintGenerator:
    """Widget Blueprint 生成器"""
    
    def __init__(self, schema: Dict):
        self.schema = schema
        self.name = schema['name']
        self.blueprint_path = schema.get('blueprint_path', '/Game/UI/Generated')
        self.base_class_name = f"{self.name}Base"
        self.widget_bp = None
        self.created_widgets = {}  # name -> widget 映射
        
    def generate(self) -> bool:
        """执行生成流程"""
        unreal.log(f"[UIGenerator] ========================================")
        unreal.log(f"[UIGenerator] 开始创建 Widget Blueprint: {self.name}")
        unreal.log(f"[UIGenerator] ========================================")
        
        # 步骤 1: 查找基类
        if not self._find_base_class():
            return False
        
        # 步骤 2: 创建或获取 Widget Blueprint
        if not self._create_or_get_blueprint():
            return False
        
        # 步骤 3: 添加组件树
        if not self._add_component_tree():
            return False
        
        # 步骤 4: 编译并保存
        if not self._compile_and_save():
            return False
        
        unreal.log(f"[UIGenerator] ========================================")
        unreal.log(f"[UIGenerator] ✅ Widget Blueprint 生成完成!")
        unreal.log(f"[UIGenerator] 路径: {self.blueprint_path}/WBP_{self.name}")
        unreal.log(f"[UIGenerator] ========================================")
        
        return True
    
    def _find_base_class(self) -> bool:
        """查找 C++ 基类"""
        # 首先尝试在主模块查找
        self.base_class = unreal.find_object(None, f"/Script/DJ01.{self.base_class_name}")
        
        if not self.base_class:
            # 尝试查找 U 前缀版本
            self.base_class = unreal.find_object(None, f"/Script/DJ01.U{self.base_class_name}")
        
        if not self.base_class:
            unreal.log_error(f"[UIGenerator] ❌ 找不到基类: {self.base_class_name}")
            unreal.log_error("[UIGenerator] 请确保：")
            unreal.log_error("  1. 已执行 C++ 代码生成")
            unreal.log_error("  2. 已重新编译项目")
            return False
        
        unreal.log(f"[UIGenerator] ✓ 找到基类: {self.base_class_name}")
        return True
    
    def _create_or_get_blueprint(self) -> bool:
        """创建或获取现有的 Widget Blueprint"""
        asset_path = f"{self.blueprint_path}/WBP_{self.name}"
        
        # 确保目录存在
        if not unreal.EditorAssetLibrary.does_directory_exist(self.blueprint_path):
            unreal.EditorAssetLibrary.make_directory(self.blueprint_path)
        
        # 检查是否已存在
        if unreal.EditorAssetLibrary.does_asset_exist(asset_path):
            unreal.log_warning(f"[UIGenerator] ⚠️ 资产已存在，将更新组件: {asset_path}")
            self.widget_bp = unreal.EditorAssetLibrary.load_asset(asset_path)
            if self.widget_bp:
                return True
            unreal.log_error("[UIGenerator] ❌ 加载现有资产失败")
            return False
        
        # 创建新的 Widget Blueprint
        try:
            factory = unreal.WidgetBlueprintFactory()
            factory.set_editor_property("parent_class", self.base_class)
            
            asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
            
            self.widget_bp = asset_tools.create_asset(
                f"WBP_{self.name}",
                self.blueprint_path,
                unreal.WidgetBlueprint,
                factory
            )
            
            if not self.widget_bp:
                unreal.log_error("[UIGenerator] ❌ 创建 Widget Blueprint 失败")
                return False
            
            unreal.log(f"[UIGenerator] ✓ 创建 Widget Blueprint 成功")
            return True
            
        except Exception as e:
            unreal.log_error(f"[UIGenerator] ❌ 创建失败: {e}")
            return False
    
    def _add_component_tree(self) -> bool:
        """添加组件树到 Widget Blueprint"""
        components = self.schema.get('components', [])
        if not components:
            unreal.log_warning("[UIGenerator] ⚠️ Schema 中没有定义组件")
            return True
        
        try:
            # 获取 WidgetTree
            widget_tree = self.widget_bp.get_editor_property("widget_tree")
            if not widget_tree:
                unreal.log_error("[UIGenerator] ❌ 无法获取 WidgetTree")
                return False
            
            unreal.log("[UIGenerator] 开始添加组件...")
            
            # 递归添加组件
            for comp in components:
                self._add_widget_recursive(widget_tree, comp, None)
            
            # 设置根组件
            if components and components[0]['name'] in self.created_widgets:
                root_widget = self.created_widgets[components[0]['name']]
                widget_tree.set_editor_property("root_widget", root_widget)
                unreal.log(f"[UIGenerator] ✓ 设置根组件: {components[0]['name']}")
            
            return True
            
        except Exception as e:
            unreal.log_error(f"[UIGenerator] ❌ 添加组件失败: {e}")
            import traceback
            unreal.log_error(traceback.format_exc())
            
            # 如果自动添加失败，打印手动添加指南
            self._print_manual_guide()
            return True  # 仍返回 True，允许手动完成
    
    def _add_widget_recursive(self, widget_tree, comp_def: Dict, parent_widget) -> Optional[Any]:
        """递归添加 Widget"""
        comp_name = comp_def['name']
        comp_type = comp_def['type']
        
        # 获取 UE Widget 类名
        ue_class_name = WIDGET_CLASS_MAP.get(comp_type)
        if not ue_class_name:
            unreal.log_warning(f"[UIGenerator] ⚠️ 未知组件类型: {comp_type}，跳过 {comp_name}")
            return None
        
        try:
            # 查找 Widget 类
            widget_class = unreal.find_class(f"/Script/UMG.{ue_class_name}")
            if not widget_class:
                # 尝试 CommonUI
                widget_class = unreal.find_class(f"/Script/CommonUI.{ue_class_name}")
            
            if not widget_class:
                unreal.log_warning(f"[UIGenerator] ⚠️ 找不到 Widget 类: {ue_class_name}")
                return None
            
            # 创建 Widget
            widget = widget_tree.construct_widget(widget_class, comp_name)
            if not widget:
                unreal.log_warning(f"[UIGenerator] ⚠️ 创建 Widget 失败: {comp_name}")
                return None
            
            self.created_widgets[comp_name] = widget
            unreal.log(f"[UIGenerator]   ├── [{comp_type}] {comp_name}")
            
            # 如果有父组件，添加到父组件
            if parent_widget:
                try:
                    # 尝试作为子组件添加
                    if hasattr(parent_widget, 'add_child'):
                        parent_widget.add_child(widget)
                    elif hasattr(parent_widget, 'add_child_to_overlay'):
                        parent_widget.add_child_to_overlay(widget)
                    elif hasattr(parent_widget, 'add_child_to_canvas'):
                        slot = parent_widget.add_child_to_canvas(widget)
                        if slot:
                            # 设置 Canvas 默认布局
                            slot.set_editor_property("anchors", unreal.Anchors(
                                minimum=unreal.Vector2D(0.5, 0.5),
                                maximum=unreal.Vector2D(0.5, 0.5)
                            ))
                except Exception as add_e:
                    unreal.log_warning(f"[UIGenerator] ⚠️ 添加到父组件失败: {add_e}")
            
            # 递归处理子组件
            if 'children' in comp_def:
                for child_def in comp_def['children']:
                    self._add_widget_recursive(widget_tree, child_def, widget)
            
            return widget
            
        except Exception as e:
            unreal.log_warning(f"[UIGenerator] ⚠️ 处理组件 {comp_name} 时出错: {e}")
            return None
    
    def _compile_and_save(self) -> bool:
        """编译并保存 Blueprint"""
        try:
            asset_path = f"{self.blueprint_path}/WBP_{self.name}"
            
            # 标记为脏
            self.widget_bp.modify()
            
            # 编译 Blueprint
            unreal.BlueprintEditorLibrary.compile_blueprint(self.widget_bp)
            unreal.log("[UIGenerator] ✓ Blueprint 编译完成")
            
            # 保存
            unreal.EditorAssetLibrary.save_asset(asset_path)
            unreal.log("[UIGenerator] ✓ 资产已保存")
            
            return True
            
        except Exception as e:
            unreal.log_error(f"[UIGenerator] ❌ 编译/保存失败: {e}")
            return False
    
    def _print_manual_guide(self):
        """打印手动添加组件指南"""
        unreal.log("")
        unreal.log("=" * 60)
        unreal.log("[UIGenerator] 📋 自动添加组件受限，请手动添加以下组件：")
        unreal.log("=" * 60)
        unreal.log("")
        
        def print_tree(components: list, indent: int = 0):
            prefix = "    " * indent
            for comp in components:
                optional = " (可选)" if comp.get('optional', False) else ""
                comment = f"  // {comp.get('comment', '')}" if comp.get('comment') else ""
                unreal.log(f"{prefix}├── [{comp['type']}] Name=\"{comp['name']}\"{optional}{comment}")
                if 'children' in comp:
                    print_tree(comp['children'], indent + 1)
        
        print_tree(self.schema.get('components', []))
        
        unreal.log("")
        unreal.log("⚠️ 注意：组件变量名必须与 Schema 定义完全一致！")
        unreal.log("=" * 60)
        unreal.log("")


def create_widget_blueprint(schema_path: str) -> bool:
    """
    根据 Schema 创建 Widget Blueprint
    
    Args:
        schema_path: Schema JSON 文件路径
        
    Returns:
        是否成功
    """
    # 加载 Schema
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except Exception as e:
        unreal.log_error(f"[UIGenerator] ❌ 加载 Schema 失败: {e}")
        return False
    
    # 创建生成器并执行
    generator = WidgetBlueprintGenerator(schema)
    return generator.generate()


def generate_from_schema(schema_path: str) -> bool:
    """
    外部调用入口
    
    Args:
        schema_path: Schema JSON 文件路径
    """
    try:
        return create_widget_blueprint(schema_path)
    except Exception as e:
        import traceback
        unreal.log_error(f"[UIGenerator] ❌ 生成失败: {e}")
        unreal.log_error(traceback.format_exc())
        return False


def generate_all_from_directory(schemas_dir: str) -> dict:
    """
    批量生成目录下所有 Schema 的 Widget Blueprint
    
    Args:
        schemas_dir: Schema 文件目录
        
    Returns:
        {'success': [...], 'failed': [...]}
    """
    result = {'success': [], 'failed': []}
    
    if not os.path.exists(schemas_dir):
        unreal.log_error(f"[UIGenerator] ❌ 目录不存在: {schemas_dir}")
        return result
    
    unreal.log(f"[UIGenerator] 扫描目录: {schemas_dir}")
    
    for filename in os.listdir(schemas_dir):
        if not filename.endswith('.json'):
            continue
        
        schema_path = os.path.join(schemas_dir, filename)
        
        try:
            success = create_widget_blueprint(schema_path)
            if success:
                result['success'].append(filename)
            else:
                result['failed'].append(filename)
        except Exception as e:
            unreal.log_error(f"[UIGenerator] ❌ {filename} 失败: {e}")
            result['failed'].append(filename)
    
    unreal.log(f"[UIGenerator] 批量生成完成: 成功 {len(result['success'])}, 失败 {len(result['failed'])}")
    return result


# =============== 测试入口 ===============
if __name__ == "__main__":
    test_schema = "D:/UnrealProjects/DJ01/Tools/UIGenerator/schemas/widgets/HealthBar.json"
    generate_from_schema(test_schema)
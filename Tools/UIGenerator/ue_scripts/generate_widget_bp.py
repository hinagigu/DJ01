"""
在 UE 内运行的蓝图生成脚本
根据 Schema 创建 Widget Blueprint 并添加组件

核心功能：
1. 创建继承 C++ 基类的 Widget Blueprint
2. 通过 DJ01WidgetBlueprintLibrary C++ Bridge 操作 WidgetTree
3. 设置组件层级关系和基本属性

使用方式：
    py "D:/UnrealProjects/DJ01/Tools/UIGenerator/ue_scripts/generate_widget_bp.py"
    
或者在 Python 中：
    from generate_widget_bp import generate_from_schema
    generate_from_schema("path/to/schema.json")
"""

import unreal
import json
import os
from typing import Dict, List, Optional, Any


# =============== 获取 C++ Bridge ===============
def get_widget_lib():
    """获取 DJ01WidgetBlueprintLibrary C++ Bridge"""
    try:
        return unreal.DJ01WidgetBlueprintLibrary
    except AttributeError:
        unreal.log_error("[UIGenerator] ❌ DJ01WidgetBlueprintLibrary 不可用!")
        unreal.log_error("[UIGenerator] 请确保 DJ01Editor 模块已正确编译")
        return None


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
    """Widget Blueprint 生成器 - 使用 DJ01WidgetBlueprintLibrary C++ Bridge"""
    
    def __init__(self, schema: Dict):
        self.schema = schema
        self.name = schema['name']
        self.blueprint_path = schema.get('blueprint_path', '/Game/UI/Generated')
        self.base_class_name = f"{self.name}Base"
        self.widget_bp = None
        self.created_widgets = {}  # name -> widget 映射
        self.lib = None  # C++ Bridge
        
    def generate(self) -> bool:
        """执行生成流程"""
        unreal.log(f"[UIGenerator] ========================================")
        unreal.log(f"[UIGenerator] 开始创建 Widget Blueprint: {self.name}")
        unreal.log(f"[UIGenerator] ========================================")
        
        # 步骤 0: 获取 C++ Bridge
        self.lib = get_widget_lib()
        if not self.lib:
            return False
        unreal.log(f"[UIGenerator] ✓ C++ Bridge 已就绪")
        
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
        """添加组件树到 Widget Blueprint（使用 C++ Bridge）"""
        components = self.schema.get('components', [])
        if not components:
            unreal.log_warning("[UIGenerator] ⚠️ Schema 中没有定义组件")
            return True
        
        try:
            # 通过 C++ Bridge 获取 WidgetTree
            widget_tree = self.lib.get_widget_tree(self.widget_bp)
            if not widget_tree:
                unreal.log_error("[UIGenerator] ❌ 无法获取 WidgetTree")
                return False
            
            unreal.log("[UIGenerator] 开始添加组件...")
            
            # 清除现有控件（如果是更新模式）
            existing_root = self.lib.get_root_widget(self.widget_bp)
            if existing_root:
                unreal.log("[UIGenerator] ⚠️ 检测到现有根控件，将重新创建")
                # 注意：这里可能需要先删除现有控件，暂时跳过
            
            # 递归添加组件
            root_widget = None
            for idx, comp in enumerate(components):
                widget = self._add_widget_recursive(comp, None)
                if idx == 0 and widget:
                    root_widget = widget
            
            # 设置根组件
            if root_widget:
                success = self.lib.set_root_widget(self.widget_bp, root_widget)
                if success:
                    unreal.log(f"[UIGenerator] ✓ 设置根组件: {components[0]['name']}")
                else:
                    unreal.log_error("[UIGenerator] ❌ 设置根组件失败")
                    return False
            
            return True
            
        except Exception as e:
            unreal.log_error(f"[UIGenerator] ❌ 添加组件失败: {e}")
            import traceback
            unreal.log_error(traceback.format_exc())
            
            # 如果自动添加失败，打印手动添加指南
            self._print_manual_guide()
            return True  # 仍返回 True，允许手动完成
    
    def _add_widget_recursive(self, comp_def: Dict, parent_widget) -> Optional[Any]:
        """递归添加 Widget（使用 C++ Bridge）"""
        comp_name = comp_def['name']
        comp_type = comp_def['type']
        
        # 获取 UE Widget 类名
        ue_class_name = WIDGET_CLASS_MAP.get(comp_type)
        if not ue_class_name:
            unreal.log_warning(f"[UIGenerator] ⚠️ 未知组件类型: {comp_type}，跳过 {comp_name}")
            return None
        
        try:
            # 使用 C++ Bridge 创建特定类型的 Widget
            widget = None
            
            if comp_type == "CanvasPanel":
                widget = self.lib.create_canvas_panel(self.widget_bp, comp_name)
            elif comp_type == "ProgressBar":
                widget = self.lib.create_progress_bar(self.widget_bp, comp_name)
            elif comp_type == "TextBlock":
                widget = self.lib.create_text_block(self.widget_bp, comp_name)
            elif comp_type == "Image":
                widget = self.lib.create_image(self.widget_bp, comp_name)
            else:
                # 使用通用创建方法
                widget_class = self._find_widget_class(ue_class_name)
                if widget_class:
                    widget = self.lib.create_widget(self.widget_bp, widget_class, comp_name)
            
            if not widget:
                unreal.log_warning(f"[UIGenerator] ⚠️ 创建 Widget 失败: {comp_name} ({comp_type})")
                return None
            
            self.created_widgets[comp_name] = widget
            unreal.log(f"[UIGenerator]   ├── [{comp_type}] {comp_name}")
            
            # 如果有父组件，添加到父组件
            if parent_widget:
                self._add_to_parent(parent_widget, widget, comp_def)
            
            # 递归处理子组件
            if 'children' in comp_def:
                for child_def in comp_def['children']:
                    self._add_widget_recursive(child_def, widget)
            
            return widget
            
        except Exception as e:
            unreal.log_warning(f"[UIGenerator] ⚠️ 处理组件 {comp_name} 时出错: {e}")
            import traceback
            unreal.log_warning(traceback.format_exc())
            return None
    
    def _find_widget_class(self, class_name: str):
        """查找 Widget 类"""
        # 尝试 UMG 模块
        widget_class = getattr(unreal, class_name, None)
        if widget_class:
            return widget_class
        
        # 尝试 CommonUI 模块
        common_class_name = f"Common{class_name}"
        widget_class = getattr(unreal, common_class_name, None)
        if widget_class:
            return widget_class
        
        return None
    
    def _add_to_parent(self, parent_widget, child_widget, comp_def: Dict):
        """将子控件添加到父控件"""
        # 获取布局属性
        position = comp_def.get('position', {'x': 0, 'y': 0})
        size = comp_def.get('size', {'width': 100, 'height': 32})
        
        pos_vec = unreal.Vector2D(position.get('x', 0), position.get('y', 0))
        size_vec = unreal.Vector2D(size.get('width', 100), size.get('height', 32))
        
        # 检查父控件类型
        parent_type = type(parent_widget).__name__
        
        try:
            if parent_type == "CanvasPanel":
                # 使用 C++ Bridge 添加到 Canvas
                success = self.lib.add_child_to_canvas(parent_widget, child_widget, pos_vec, size_vec)
                if not success:
                    # 回退到直接方法
                    self.lib.add_child_to_panel(parent_widget, child_widget)
            else:
                # 其他面板类型
                self.lib.add_child_to_panel(parent_widget, child_widget)
        except Exception as e:
            unreal.log_warning(f"[UIGenerator] ⚠️ 添加子控件失败: {e}")
    
    def _compile_and_save(self) -> bool:
        """编译并保存 Blueprint（使用 C++ Bridge）"""
        try:
            # 标记为脏
            self.lib.mark_dirty(self.widget_bp)
            
            # 编译 Blueprint
            try:
                unreal.BlueprintEditorLibrary.compile_blueprint(self.widget_bp)
                unreal.log("[UIGenerator] ✓ Blueprint 编译完成")
            except Exception as compile_e:
                unreal.log_warning(f"[UIGenerator] ⚠️ 编译警告: {compile_e}")
            
            # 使用 C++ Bridge 保存
            success = self.lib.save_widget_blueprint(self.widget_bp)
            if success:
                unreal.log("[UIGenerator] ✓ 资产已保存")
                return True
            else:
                unreal.log_error("[UIGenerator] ❌ 保存失败")
                return False
            
        except Exception as e:
            unreal.log_error(f"[UIGenerator] ❌ 编译/保存失败: {e}")
            import traceback
            unreal.log_error(traceback.format_exc())
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
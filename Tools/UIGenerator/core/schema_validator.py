"""
Schema 校验器
验证 UI Schema 的合法性
"""

import json
import os
from typing import Dict, List, Tuple, Optional, Any


class SchemaValidator:
    """UI Schema 校验器"""
    
    def __init__(self, widget_types_path: str):
        """
        初始化校验器
        
        Args:
            widget_types_path: widget_types.json 的路径
        """
        with open(widget_types_path, 'r', encoding='utf-8') as f:
            self.widget_types = json.load(f)
        
        self.valid_widget_types = set(self.widget_types['widget_types'].keys())
        self.valid_base_classes = set(self.widget_types['common_base_classes'].keys())
        self.valid_property_types = set(self.widget_types['property_types'].keys())
        
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def validate(self, schema: Dict) -> Tuple[bool, List[str], List[str]]:
        """
        校验 Schema
        
        Args:
            schema: 解析后的 schema 字典
            
        Returns:
            (是否有效, 错误列表, 警告列表)
        """
        self.errors = []
        self.warnings = []
        
        # 必需字段
        self._check_required_fields(schema)
        
        # 名称规范
        self._check_naming(schema)
        
        # 父类
        self._check_parent_class(schema)
        
        # 组件
        if 'components' in schema:
            self._check_components(schema['components'], path='components')
        
        # 属性
        if 'properties' in schema:
            self._check_properties(schema['properties'])
        
        # 函数
        if 'functions' in schema:
            self._check_functions(schema['functions'])
        
        # 事件
        if 'events' in schema:
            self._check_events(schema['events'])
        
        # 绑定引用检查
        self._check_binding_references(schema)
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _check_required_fields(self, schema: Dict):
        """检查必需字段"""
        required = ['name', 'components']
        for field in required:
            if field not in schema:
                self.errors.append(f"缺少必需字段: {field}")
    
    def _check_naming(self, schema: Dict):
        """检查命名规范"""
        name = schema.get('name', '')
        if name:
            if not name[0].isupper():
                self.errors.append(f"类名必须以大写字母开头: {name}")
            if not name.replace('_', '').isalnum():
                self.errors.append(f"类名只能包含字母、数字和下划线: {name}")
    
    def _check_parent_class(self, schema: Dict):
        """检查父类"""
        parent = schema.get('parent_class', 'CommonUserWidget')
        if parent not in self.valid_base_classes:
            self.errors.append(
                f"无效的父类: {parent}，有效值: {self.valid_base_classes}"
            )
        
        # 检查 ActivatableWidget 特有配置
        is_activatable = parent in ['CommonActivatableWidget', 'CommonActivatableStackWidget']
        
        if 'input_config' in schema and not is_activatable:
            self.warnings.append(
                "input_config 仅对 CommonActivatableWidget 有效"
            )
        
        if 'activation' in schema and not is_activatable:
            self.warnings.append(
                "activation 配置仅对 CommonActivatableWidget 有效"
            )
        
        if 'layer' in schema and not is_activatable:
            self.warnings.append(
                "layer 配置仅对 CommonActivatableWidget 有效"
            )
        
        # 验证 input_config
        if 'input_config' in schema:
            input_config = schema['input_config']
            valid_modes = ['Game', 'Menu', 'All']
            if input_config.get('mode') and input_config['mode'] not in valid_modes:
                self.errors.append(
                    f"无效的 input_config.mode: {input_config['mode']}，有效值: {valid_modes}"
                )
            
            valid_captures = [
                'NoCapture', 'CapturePermanently', 
                'CapturePermanentlyIncludingInitialMouseDown',
                'CaptureDuringMouseDown', 'CaptureDuringRightMouseDown'
            ]
            if input_config.get('mouse_capture') and input_config['mouse_capture'] not in valid_captures:
                self.errors.append(
                    f"无效的 input_config.mouse_capture: {input_config['mouse_capture']}"
                )
    
    def _check_components(self, components: List[Dict], path: str):
        """递归检查组件"""
        names_seen = set()
        
        for i, comp in enumerate(components):
            comp_path = f"{path}[{i}]"
            
            # 必需字段
            if 'name' not in comp:
                self.errors.append(f"{comp_path}: 缺少 name")
                continue
            if 'type' not in comp:
                self.errors.append(f"{comp_path}: 缺少 type")
                continue
            
            name = comp['name']
            comp_type = comp['type']
            
            # 名称唯一性
            if name in names_seen:
                self.errors.append(f"{comp_path}: 组件名重复: {name}")
            names_seen.add(name)
            
            # 类型有效性
            if comp_type not in self.valid_widget_types:
                self.errors.append(
                    f"{comp_path}: 无效的组件类型: {comp_type}"
                )
            
            # 检查子组件
            if 'children' in comp:
                widget_info = self.widget_types['widget_types'].get(comp_type, {})
                if not widget_info.get('is_panel', False):
                    self.warnings.append(
                        f"{comp_path}: {comp_type} 通常不作为容器使用"
                    )
                self._check_components(comp['children'], f"{comp_path}.children")
    
    def _check_properties(self, properties: List[Dict]):
        """检查属性定义"""
        names_seen = set()
        
        for i, prop in enumerate(properties):
            if 'name' not in prop:
                self.errors.append(f"properties[{i}]: 缺少 name")
                continue
            if 'type' not in prop:
                self.errors.append(f"properties[{i}]: 缺少 type")
                continue
            
            name = prop['name']
            prop_type = prop['type']
            
            if name in names_seen:
                self.errors.append(f"properties[{i}]: 属性名重复: {name}")
            names_seen.add(name)
            
            if prop_type not in self.valid_property_types:
                self.errors.append(
                    f"properties[{i}]: 无效的属性类型: {prop_type}"
                )
    
    def _check_functions(self, functions: List[Dict]):
        """检查函数定义"""
        names_seen = set()
        
        for i, func in enumerate(functions):
            if 'name' not in func:
                self.errors.append(f"functions[{i}]: 缺少 name")
                continue
            
            name = func['name']
            if name in names_seen:
                self.errors.append(f"functions[{i}]: 函数名重复: {name}")
            names_seen.add(name)
    
    def _check_events(self, events: List[Dict]):
        """检查事件定义"""
        for i, event in enumerate(events):
            if 'name' not in event:
                self.errors.append(f"events[{i}]: 缺少 name")
                continue
            
            name = event['name']
            if not name.startswith('On'):
                self.warnings.append(
                    f"events[{i}]: 事件名建议以 'On' 开头: {name}"
                )
    
    def _check_binding_references(self, schema: Dict):
        """检查绑定引用是否存在对应的属性或 BindingSet 变量"""
        # 收集所有属性名
        valid_bindings = set()
        
        # 1. Schema 中定义的 properties
        for prop in schema.get('properties', []):
            valid_bindings.add(prop.get('name', ''))
        
        # 2. BindingSet 提供的变量（从项目配置加载）
        binding_set = schema.get('binding_set', {})
        binding_set_name = binding_set.get('name', '') if binding_set else ''
        
        if binding_set_name:
            # 尝试加载 BindingSet 定义
            binding_set_vars = self._get_binding_set_variables(binding_set_name)
            valid_bindings.update(binding_set_vars)
        
        # 检查组件中的绑定
        def check_component_bindings(components: List[Dict]):
            for comp in components:
                for key in ['bind_percent', 'bind_text', 'bind_image']:
                    if key in comp:
                        bind_target = comp[key]
                        if bind_target and bind_target not in valid_bindings:
                            # 只显示警告而非错误，因为可能是自定义绑定
                            self.warnings.append(
                                f"组件 {comp['name']} 的 {key} 引用了 '{bind_target}'，"
                                f"不在已知属性或 BindingSet 变量中"
                            )
                if 'children' in comp:
                    check_component_bindings(comp['children'])
        
        check_component_bindings(schema.get('components', []))
    
    def _get_binding_set_variables(self, binding_set_name: str) -> set:
        """获取 BindingSet 提供的变量名列表"""
        variables = set()
        
        # 尝试查找 BindingSetDefinitions.json
        try:
            # 从 widget_types_path 推算项目根目录
            # widget_types.json 在 Tools/UIGenerator/configs/
            import os
            config_dir = os.path.dirname(os.path.abspath(__file__))  # core/
            ui_generator_dir = os.path.dirname(config_dir)           # UIGenerator/
            tools_dir = os.path.dirname(ui_generator_dir)            # Tools/
            project_root = os.path.dirname(tools_dir)                # DJ01/
            
            binding_defs_path = os.path.join(
                project_root, "Source", "DJ01", "AbilitySystem", "Attributes",
                "BindingSets", "Config", "BindingSetDefinitions.json"
            )
            
            if os.path.exists(binding_defs_path):
                with open(binding_defs_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                for bs in data.get("BindingSets", []):
                    if bs.get("Name") == binding_set_name:
                        # 提取属性绑定变量
                        for attr in bs.get("AttributeBindings", []):
                            var_name = attr.get("VariableName", attr.get("AttributeName", ""))
                            for vt in attr.get("ValueTypes", ["Current"]):
                                if vt == "Current":
                                    variables.add(f"Current{var_name}")
                                elif vt == "Max":
                                    variables.add(f"Max{var_name}")
                                else:
                                    variables.add(f"{vt}{var_name}")
                        
                        # 提取 Tag 绑定变量
                        for tag in bs.get("TagBindings", []):
                            var_name = tag.get("VariableName", "")
                            if var_name:
                                variables.add(var_name)
                        break
        except Exception as e:
            # 静默失败，不影响验证
            pass
        
        return variables


def load_and_validate(schema_path: str, widget_types_path: str) -> Tuple[Optional[Dict], List[str], List[str]]:
    """
    加载并校验 Schema 文件
    
    Args:
        schema_path: Schema JSON 文件路径
        widget_types_path: widget_types.json 路径
        
    Returns:
        (schema 或 None, 错误列表, 警告列表)
    """
    try:
        with open(schema_path, 'r', encoding='utf-8') as f:
            schema = json.load(f)
    except json.JSONDecodeError as e:
        return None, [f"JSON 解析错误: {e}"], []
    except FileNotFoundError:
        return None, [f"文件不存在: {schema_path}"], []
    
    validator = SchemaValidator(widget_types_path)
    is_valid, errors, warnings = validator.validate(schema)
    
    if is_valid:
        return schema, errors, warnings
    else:
        return None, errors, warnings
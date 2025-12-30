"""
C++ 代码生成器
根据 Schema 生成 Widget 的 C++ 头文件和实现文件

支持特性：
- 基础 UserWidget
- CommonUI 的 CommonUserWidget
- CommonUI 的 CommonActivatableWidget（含 InputConfig、生命周期）
"""

import json
import os
from typing import Dict, List, Set, Optional
from datetime import datetime
from pathlib import Path


class CppGenerator:
    """C++ Widget 代码生成器"""
    
    def __init__(self, widget_types_path: str, project_name: str = "DJ01", 
                 bindingset_config_path: str = None):
        """
        初始化生成器
        
        Args:
            widget_types_path: widget_types.json 路径
            project_name: 项目名称（用于 API 宏）
            bindingset_config_path: BindingSetDefinitions.json 路径
        """
        with open(widget_types_path, 'r', encoding='utf-8') as f:
            self.widget_types = json.load(f)
        
        self.project_name = project_name
        self.api_macro = f"{project_name.upper()}_API"
        
        # 加载 BindingSet 配置
        self.binding_sets = {}
        if bindingset_config_path and os.path.exists(bindingset_config_path):
            with open(bindingset_config_path, 'r', encoding='utf-8') as f:
                bs_config = json.load(f)
                for bs in bs_config.get('BindingSets', []):
                    self.binding_sets[bs['Name']] = bs
    
    def get_binding_set_vars(self, bs_name: str) -> List[Dict]:
        """获取 BindingSet 定义的变量列表（支持多值类型）"""
        if bs_name not in self.binding_sets:
            return []
        
        bs = self.binding_sets[bs_name]
        vars_list = []
        
        # Tag 绑定 -> bool 变量
        for tag_binding in bs.get('TagBindings', []):
            event_type = tag_binding.get('EventType', 'NewOrRemoved')
            var_type = 'bool' if event_type == 'NewOrRemoved' else 'int32'
            vars_list.append({
                'name': tag_binding['VariableName'],
                'type': var_type,
                'source': 'Tag',
                'description': tag_binding.get('Description', '')
            })
        
        # Attribute 绑定 -> float/int 变量（支持多值类型）
        for attr_binding in bs.get('AttributeBindings', []):
            var_type = attr_binding.get('VarType', 'float')
            base_var_name = attr_binding.get('VariableName', '')
            description = attr_binding.get('Description', '')
            
            # 新格式：value_types 是列表
            value_types = attr_binding.get('ValueTypes', [])
            if value_types:
                for vt in value_types:
                    # 根据值类型生成变量名（与 data.py 逻辑一致）
                    if vt == 'Current' and len(value_types) == 1:
                        var_name = base_var_name
                    elif vt == 'Current':
                        var_name = f"Current{base_var_name}"
                    else:
                        var_name = f"{vt}{base_var_name}"
                    
                    vars_list.append({
                        'name': var_name,
                        'type': var_type,
                        'source': 'Attribute',
                        'value_type': vt,
                        'description': f"{description} ({vt})"
                    })
            else:
                # 旧格式兼容：单个 ValueType
                value_type = attr_binding.get('ValueType', 'Current')
                vars_list.append({
                    'name': base_var_name,
                    'type': var_type,
                    'source': 'Attribute',
                    'value_type': value_type,
                    'description': description
                })
        
        return vars_list
    
    def is_activatable_widget(self, schema: Dict) -> bool:
        """判断是否是可激活 Widget"""
        parent = schema.get('parent_class', 'CommonUserWidget')
        return parent in ['CommonActivatableWidget', 'CommonActivatableStackWidget']
    
    def generate(self, schema: Dict, output_dir: str) -> Dict[str, str]:
        """
        生成 C++ 代码
        
        Args:
            schema: 验证过的 schema
            output_dir: 输出目录
            
        Returns:
            生成的文件路径字典 {'header': path, 'source': path}
        """
        class_name = f"U{schema['name']}Base"
        header_content = self._generate_header(schema, class_name)
        source_content = self._generate_source(schema, class_name)
        
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        header_path = os.path.join(output_dir, f"{schema['name']}Base.h")
        source_path = os.path.join(output_dir, f"{schema['name']}Base.cpp")
        
        with open(header_path, 'w', encoding='utf-8') as f:
            f.write(header_content)
        
        with open(source_path, 'w', encoding='utf-8') as f:
            f.write(source_content)
        
        return {
            'header': header_path,
            'source': source_path
        }
    
    def _generate_header(self, schema: Dict, class_name: str) -> str:
        """生成头文件"""
        lines = []
        is_activatable = self.is_activatable_widget(schema)
        
        # 文件头
        lines.append(self._generate_file_header(schema))
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        
        # Includes
        includes = self._collect_includes(schema)
        for inc in sorted(includes):
            lines.append(f'#include "{inc}"')
        
        # ActivatableWidget 需要额外的 include
        if is_activatable:
            lines.append('#include "Input/CommonUIInputTypes.h"')
        
        lines.append("")
        lines.append(f'#include "{schema["name"]}Base.generated.h"')
        lines.append("")
        
        # ViewModel 头文件
        viewmodel = schema.get('viewmodel')
        if viewmodel and viewmodel.get('header'):
            lines.append(f'#include "{viewmodel["header"]}"')
            lines.append("")
        
        # 前向声明
        forward_decls = self._collect_forward_declarations(schema)
        if forward_decls:
            for decl in sorted(forward_decls):
                lines.append(f"class {decl};")
            lines.append("")
        
        # 委托声明
        delegates = self._generate_delegates(schema)
        if delegates:
            lines.extend(delegates)
            lines.append("")
        
        # 类定义
        lines.append(self._generate_class_doc(schema))
        lines.append("UCLASS(Abstract, Blueprintable)")
        
        parent_class = self._get_parent_class(schema)
        lines.append(f"class {self.api_macro} {class_name} : public {parent_class}")
        lines.append("{")
        lines.append("\tGENERATED_BODY()")
        lines.append("")
        
        # Public
        lines.append("public:")
        lines.append(f"\t{class_name}(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get());")
        lines.append("")
        
        # Protected
        lines.append("protected:")
        lines.append("\t//~ Begin UUserWidget Interface")
        lines.append("\tvirtual void NativeConstruct() override;")
        lines.append("\tvirtual void NativeDestruct() override;")
        lines.append("\t//~ End UUserWidget Interface")
        lines.append("")
        
        # BindingSet 集成
        binding_set = schema.get('binding_set')
        if binding_set:
            bs_name = binding_set.get('name', '')
            lines.append(f"\t// ===== BindingSet: {bs_name} =====")
            lines.append(f"\t// 以下变量和函数由 DJ01_DECLARE_BINDING_SET({bs_name}) 自动生成")
            lines.append(f"\tDJ01_DECLARE_BINDING_SET({bs_name})")
            lines.append("")
            
            lines.append("\t/** ASC 弱引用 */")
            lines.append("\tTWeakObjectPtr<UAbilitySystemComponent> BoundASC;")
            lines.append("")
            
            lines.append("public:")
            lines.append("\t/** 绑定到 AbilitySystemComponent */")
            lines.append("\tUFUNCTION(BlueprintCallable, Category = \"Binding\")")
            lines.append("\tvoid BindToASC(UAbilitySystemComponent* InASC);")
            lines.append("")
            lines.append("\t/** 解除绑定 */")
            lines.append("\tUFUNCTION(BlueprintCallable, Category = \"Binding\")")
            lines.append("\tvoid UnbindFromASC();")
            lines.append("")
            
            # 生成转换函数声明
            component_bindings = binding_set.get('component_bindings', [])
            transforms_needed = set()
            for cb in component_bindings:
                transform = cb.get('transform', 'Direct')
                if transform != 'Direct':
                    transforms_needed.add(transform)
            
            if transforms_needed:
                lines.append("protected:")
                lines.append("\t// ===== 值转换函数 =====")
                for t in sorted(transforms_needed):
                    if t == 'HealthToPercent':
                        lines.append("\tfloat TransformHealthToPercent(float Health) const;")
                    elif t == 'HealthToText':
                        lines.append("\tFText TransformHealthToText(float Health) const;")
                    elif t == 'BoolToVisibility':
                        lines.append("\tESlateVisibility TransformBoolToVisibility(bool bValue) const;")
                lines.append("")
        
        # CommonActivatableWidget 特有接口
        if is_activatable:
            lines.append("\t//~ Begin UCommonActivatableWidget Interface")
            lines.append("\tvirtual TOptional<FUIInputConfig> GetDesiredInputConfig() const override;")
            lines.append("\tvirtual void NativeOnActivated() override;")
            lines.append("\tvirtual void NativeOnDeactivated() override;")
            lines.append("\t//~ End UCommonActivatableWidget Interface")
            lines.append("")
            
            # 蓝图可重写的激活/停用事件
            lines.append("\t/** 蓝图可实现：Widget 被激活时调用 */")
            lines.append("\tUFUNCTION(BlueprintImplementableEvent, Category = \"Activation\")")
            lines.append("\tvoid BP_OnActivated();")
            lines.append("")
            lines.append("\t/** 蓝图可实现：Widget 被停用时调用 */")
            lines.append("\tUFUNCTION(BlueprintImplementableEvent, Category = \"Activation\")")
            lines.append("\tvoid BP_OnDeactivated();")
            lines.append("")
        
        # CommonUI Activatable 相关方法 (如果父类是 CommonActivatableWidget)
        if schema.get('parent_class', '') in ['CommonActivatableWidget', 'CommonActivatableStackWidget']:
            lines.append("\t//~ Begin UCommonActivatableWidget Interface")
            lines.append("\tvirtual TOptional<FUIInputConfig> GetDesiredInputConfig() const override;")
            lines.append("\tvirtual void NativeOnActivated() override;")
            lines.append("\tvirtual void NativeOnDeactivated() override;")
            lines.append("\t//~ End UCommonActivatableWidget Interface")
        lines.append("")
        
        # ViewModel
        viewmodel = schema.get('viewmodel')
        if viewmodel:
            vm_class = viewmodel.get('class', 'UObject')
            lines.append("\t// ===== ViewModel =====")
            lines.append(f"\t/** 绑定的 ViewModel */")
            lines.append(f"\tUPROPERTY(BlueprintReadOnly, Category = \"ViewModel\")")
            lines.append(f"\tTObjectPtr<{vm_class}> ViewModel;")
            lines.append("")
            lines.append(f"\t/** 设置 ViewModel 并初始化绑定 */")
            lines.append(f"\tUFUNCTION(BlueprintCallable, Category = \"ViewModel\")")
            lines.append(f"\tvoid SetViewModel({vm_class}* InViewModel);")
            lines.append("")
        
        # 绑定组件
        components = self._collect_all_components(schema.get('components', []))
        if components:
            lines.append("\t// ===== UI 组件 (BindWidget) =====")
            for comp in components:
                lines.append(self._generate_component_declaration(comp))
            lines.append("")
        
        # 属性
        properties = schema.get('properties', [])
        if properties:
            lines.append("\t// ===== 属性 =====")
            for prop in properties:
                lines.append(self._generate_property_declaration(prop))
            lines.append("")
        
        # 事件
        events = schema.get('events', [])
        if events:
            lines.append("\t// ===== 事件 =====")
            for event in events:
                lines.append(self._generate_event_declaration(event))
            lines.append("")
        
        # 函数
        functions = schema.get('functions', [])
        if functions:
            lines.append("public:")
            lines.append("\t// ===== 函数 =====")
            for func in functions:
                lines.append(self._generate_function_declaration(func))
            lines.append("")
        
        # Private
        lines.append("private:")
        lines.append("\t/** 更新所有 UI 绑定 */")
        lines.append("\tvoid UpdateBindings();")
        lines.append("")
        
        lines.append("};")
        
        return "\n".join(lines)
    
    def _generate_source(self, schema: Dict, class_name: str) -> str:
        """生成源文件"""
        lines = []
        is_activatable = self.is_activatable_widget(schema)
        
        # 文件头
        lines.append(self._generate_file_header(schema))
        lines.append("")
        lines.append(f'#include "{schema["name"]}Base.h"')
        lines.append("")
        
        # 额外 includes
        lines.append('#include "Components/ProgressBar.h"')
        lines.append('#include "Components/TextBlock.h"')
        lines.append('#include "Components/Image.h"')
        lines.append("")
        
        # 构造函数
        lines.append(f"{class_name}::{class_name}(const FObjectInitializer& ObjectInitializer)")
        lines.append("\t: Super(ObjectInitializer)")
        lines.append("{")
        # 如果是 ActivatableWidget，设置默认激活行为
        if is_activatable:
            activation = schema.get('activation', {})
            if activation.get('is_back_handler', True):
                lines.append("\tbIsBackHandler = true;")
            if activation.get('is_back_action_displayed_in_action_bar', True):
                lines.append("\tbIsBackActionDisplayedInActionBar = true;")
        lines.append("}")
        lines.append("")
        
        # NativeConstruct
        lines.append(f"void {class_name}::NativeConstruct()")
        lines.append("{")
        lines.append("\tSuper::NativeConstruct();")
        lines.append("\t")
        lines.append("\t// 初始化绑定")
        lines.append("\tUpdateBindings();")
        lines.append("}")
        lines.append("")
        
        # NativeDestruct
        binding_set = schema.get('binding_set')
        lines.append(f"void {class_name}::NativeDestruct()")
        lines.append("{")
        if binding_set:
            bs_name = binding_set.get('name', '')
            lines.append("\tUnbindFromASC();")
        lines.append("\tSuper::NativeDestruct();")
        lines.append("}")
        lines.append("")
        
        # BindingSet 绑定/解绑函数
        if binding_set:
            bs_name = binding_set.get('name', '')
            
            # BindToASC
            lines.append(f"void {class_name}::BindToASC(UAbilitySystemComponent* InASC)")
            lines.append("{")
            lines.append("\tif (!InASC || BoundASC.Get() == InASC)")
            lines.append("\t{")
            lines.append("\t\treturn;")
            lines.append("\t}")
            lines.append("\t")
            lines.append("\t// 先解除旧绑定")
            lines.append("\tUnbindFromASC();")
            lines.append("\t")
            lines.append("\tBoundASC = InASC;")
            lines.append(f"\tInitBindingSet_{bs_name}(InASC);")
            lines.append("\t")
            lines.append("\t// 初始化 UI")
            lines.append("\tUpdateBindings();")
            lines.append("}")
            lines.append("")
            
            # UnbindFromASC
            lines.append(f"void {class_name}::UnbindFromASC()")
            lines.append("{")
            lines.append("\tif (BoundASC.IsValid())")
            lines.append("\t{")
            lines.append(f"\t\tCleanupBindingSet_{bs_name}(BoundASC.Get());")
            lines.append("\t\tBoundASC.Reset();")
            lines.append("\t}")
            lines.append("}")
            lines.append("")
            
            # 转换函数实现
            component_bindings = binding_set.get('component_bindings', [])
            transforms_needed = set()
            for cb in component_bindings:
                transform = cb.get('transform', 'Direct')
                if transform != 'Direct':
                    transforms_needed.add(transform)
            
            for t in sorted(transforms_needed):
                if t == 'HealthToPercent':
                    lines.append(f"float {class_name}::TransformHealthToPercent(float Health) const")
                    lines.append("{")
                    lines.append("\t// MaxHealth 来自 BindingSet 自动生成的变量")
                    lines.append("\treturn MaxHealth > 0.0f ? FMath::Clamp(Health / MaxHealth, 0.0f, 1.0f) : 0.0f;")
                    lines.append("}")
                    lines.append("")
                elif t == 'HealthToText':
                    lines.append(f"FText {class_name}::TransformHealthToText(float Health) const")
                    lines.append("{")
                    lines.append("\t// MaxHealth 来自 BindingSet 自动生成的变量")
                    lines.append("\treturn FText::Format(NSLOCTEXT(\"Health\", \"HealthFormat\", \"{0}/{1}\"),")
                    lines.append("\t\tFMath::RoundToInt(Health), FMath::RoundToInt(MaxHealth));")
                    lines.append("}")
                    lines.append("")
                elif t == 'BoolToVisibility':
                    lines.append(f"ESlateVisibility {class_name}::TransformBoolToVisibility(bool bValue) const")
                    lines.append("{")
                    lines.append("\treturn bValue ? ESlateVisibility::Visible : ESlateVisibility::Collapsed;")
                    lines.append("}")
                    lines.append("")
        
        # ActivatableWidget 特有方法实现
        if is_activatable:
            # GetDesiredInputConfig
            lines.append(f"TOptional<FUIInputConfig> {class_name}::GetDesiredInputConfig() const")
            lines.append("{")
            
            input_config = schema.get('input_config', {})
            input_mode = input_config.get('mode', 'Menu')
            mouse_capture = input_config.get('mouse_capture', 'NoCapture')
            hide_cursor = input_config.get('hide_cursor_during_capture', False)
            
            # 获取枚举值
            input_modes = self.widget_types.get('input_modes', {})
            mouse_captures = self.widget_types.get('mouse_capture_modes', {})
            
            input_mode_enum = input_modes.get(input_mode, {}).get('enum_value', 'ECommonInputMode::Menu')
            mouse_capture_enum = mouse_captures.get(mouse_capture, {}).get('enum_value', 'EMouseCaptureMode::NoCapture')
            
            lines.append(f"\treturn FUIInputConfig({input_mode_enum}, {mouse_capture_enum}, {'true' if hide_cursor else 'false'});")
            lines.append("}")
            lines.append("")
            
            # NativeOnActivated
            lines.append(f"void {class_name}::NativeOnActivated()")
            lines.append("{")
            lines.append("\tSuper::NativeOnActivated();")
            lines.append("\tBP_OnActivated();")
            lines.append("}")
            lines.append("")
            
            # NativeOnDeactivated
            lines.append(f"void {class_name}::NativeOnDeactivated()")
            lines.append("{")
            lines.append("\tSuper::NativeOnDeactivated();")
            lines.append("\tBP_OnDeactivated();")
            lines.append("}")
            lines.append("")
        
        # UpdateBindings
        lines.append(f"void {class_name}::UpdateBindings()")
        lines.append("{")
        bindings = self._generate_binding_updates(schema)
        for binding in bindings:
            lines.append(f"\t{binding}")
        lines.append("}")
        lines.append("")
        
        # 函数实现
        for func in schema.get('functions', []):
            if not func.get('blueprint_implementable', False):
                lines.extend(self._generate_function_implementation(schema, class_name, func))
                lines.append("")
        
        return "\n".join(lines)
    
    def _generate_file_header(self, schema: Dict) -> str:
        """生成文件头注释"""
        return f"""// =============================================================================
// {schema['name']}Base - 自动生成的 Widget 基类
// 
// 描述: {schema.get('description', 'UI Widget')}
// 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
// 
// ⚠️ 此文件由 UI Generator 自动生成，请勿手动修改
// ============================================================================="""
    
    def _collect_includes(self, schema: Dict) -> Set[str]:
        """收集需要的 include"""
        includes = set()
        
        # 父类
        parent = schema.get('parent_class', 'CommonUserWidget')
        parent_info = self.widget_types['common_base_classes'].get(parent, {})
        if 'header' in parent_info:
            includes.add(parent_info['header'])
        
        # 组件类型
        for comp in self._collect_all_components(schema.get('components', [])):
            comp_type = comp['type']
            type_info = self.widget_types['widget_types'].get(comp_type, {})
            if 'header' in type_info:
                includes.add(type_info['header'])
        
        # BindingSet 头文件
        if schema.get('binding_set'):
            includes.add('DJ01/AbilitySystem/Attributes/BindingSets/Generated/BindingSets.h')
        
        return includes
    
    def _collect_forward_declarations(self, schema: Dict) -> Set[str]:
        """收集前向声明"""
        decls = set()
        for comp in self._collect_all_components(schema.get('components', [])):
            comp_type = comp['type']
            type_info = self.widget_types['widget_types'].get(comp_type, {})
            if 'ue_class' in type_info:
                decls.add(type_info['ue_class'])
        return decls
    
    def _collect_all_components(self, components: List[Dict], result: List[Dict] = None) -> List[Dict]:
        """递归收集所有组件"""
        if result is None:
            result = []
        
        for comp in components:
            result.append(comp)
            if 'children' in comp:
                self._collect_all_components(comp['children'], result)
        
        return result
    
    def _get_parent_class(self, schema: Dict) -> str:
        """获取父类的 UE 类名"""
        parent = schema.get('parent_class', 'CommonUserWidget')
        parent_info = self.widget_types['common_base_classes'].get(parent, {})
        return parent_info.get('ue_class', 'UUserWidget')
    
    def _generate_class_doc(self, schema: Dict) -> str:
        """生成类文档注释"""
        desc = schema.get('description', '')
        return f"""/**
 * {schema['name']} 基类
 * 
 * {desc}
 * 
 * 使用方式：
 * 1. 创建继承此类的 Widget Blueprint
 * 2. 在 Designer 中添加对应名称的控件
 * 3. 调整布局和样式
 */"""
    
    def _generate_component_declaration(self, comp: Dict) -> str:
        """生成组件声明"""
        comp_type = comp['type']
        type_info = self.widget_types['widget_types'].get(comp_type, {})
        ue_class = type_info.get('ue_class', 'UWidget')
        
        meta = "BindWidget"
        if comp.get('optional', False):
            meta = "BindWidgetOptional"
        
        comment = comp.get('comment', '')
        comment_str = f"  // {comment}" if comment else ""
        
        return f"\tUPROPERTY(BlueprintReadWrite, meta = ({meta}))\n\tTObjectPtr<{ue_class}> {comp['name']};{comment_str}"
    
    def _generate_property_declaration(self, prop: Dict) -> str:
        """生成属性声明"""
        prop_type = prop['type']
        type_info = self.widget_types['property_types'].get(prop_type, {})
        cpp_type = type_info.get('cpp_type', prop_type)
        
        # UPROPERTY 说明符
        specifiers = ["EditAnywhere", "BlueprintReadWrite"]
        if prop.get('blueprint_read_only', False):
            specifiers = ["VisibleAnywhere", "BlueprintReadOnly"]
        
        category = prop.get('category', 'Default')
        specifiers.append(f'Category = "{category}"')
        
        specifier_str = ", ".join(specifiers)
        
        # 默认值
        default = prop.get('default')
        default_str = ""
        if default is not None:
            if isinstance(default, bool):
                default_str = f" = {'true' if default else 'false'}"
            elif isinstance(default, (int, float)):
                default_str = f" = {default}f" if isinstance(default, float) else f" = {default}"
        
        # 注释
        desc = prop.get('description', '')
        comment = f"\t/** {desc} */\n" if desc else ""
        
        return f"{comment}\tUPROPERTY({specifier_str})\n\t{cpp_type} {prop['name']}{default_str};"
    
    def _generate_delegates(self, schema: Dict) -> List[str]:
        """生成委托声明"""
        lines = []
        for event in schema.get('events', []):
            params = event.get('parameters', [])
            
            if params:
                param_str = ', '.join([f"{p['type']}, {p['name']}" for p in params])
                lines.append(f"DECLARE_DYNAMIC_MULTICAST_DELEGATE_{len(params)}Param(F{event['name']}Delegate, {param_str});")
            else:
                lines.append(f"DECLARE_DYNAMIC_MULTICAST_DELEGATE(F{event['name']}Delegate);")
        
        return lines
    
    def _generate_event_declaration(self, event: Dict) -> str:
        """生成事件属性声明"""
        desc = event.get('description', '')
        comment = f"\t/** {desc} */\n" if desc else ""
        
        return f"{comment}\tUPROPERTY(BlueprintAssignable, Category = \"Events\")\n\tF{event['name']}Delegate {event['name']};"
    
    def _generate_function_declaration(self, func: Dict) -> str:
        """生成函数声明"""
        return_type = func.get('return_type', 'void')
        params = func.get('parameters', [])
        param_str = ", ".join([f"{p['type']} {p['name']}" for p in params])
        
        # UFUNCTION 说明符
        specifiers = []
        if func.get('blueprint_callable', True):
            specifiers.append("BlueprintCallable")
        if func.get('blueprint_implementable', False):
            specifiers.append("BlueprintImplementableEvent")
        specifiers.append('Category = "UI"')
        
        specifier_str = ", ".join(specifiers)
        
        desc = func.get('description', '')
        comment = f"\t/** {desc} */\n" if desc else ""
        
        return f"{comment}\tUFUNCTION({specifier_str})\n\t{return_type} {func['name']}({param_str});"
    
    def _generate_binding_updates(self, schema: Dict) -> List[str]:
        """生成绑定更新代码"""
        lines = []
        
        # 来自 BindingSet 的组件绑定
        binding_set = schema.get('binding_set')
        if binding_set:
            component_bindings = binding_set.get('component_bindings', [])
            for cb in component_bindings:
                comp_name = cb['component']
                prop = cb['property']
                source = cb['source']
                transform = cb.get('transform', 'Direct')
                
                lines.append(f"if ({comp_name})")
                lines.append("{")
                
                # 应用转换
                if transform == 'Direct':
                    value_expr = source
                elif transform == 'HealthToPercent':
                    value_expr = f"TransformHealthToPercent({source})"
                elif transform == 'HealthToText':
                    value_expr = f"TransformHealthToText({source})"
                elif transform == 'BoolToVisibility':
                    value_expr = f"TransformBoolToVisibility({source})"
                else:
                    value_expr = source
                
                # 设置属性
                if prop == 'Percent':
                    lines.append(f"\t{comp_name}->SetPercent({value_expr});")
                elif prop == 'Text':
                    lines.append(f"\t{comp_name}->SetText({value_expr});")
                elif prop == 'Visibility':
                    lines.append(f"\t{comp_name}->SetVisibility({value_expr});")
                elif prop == 'ColorAndOpacity':
                    lines.append(f"\t{comp_name}->SetColorAndOpacity({value_expr});")
                
                lines.append("}")
        
        # 兼容旧的 bind_percent/bind_text 语法
        for comp in self._collect_all_components(schema.get('components', [])):
            if 'bind_percent' in comp:
                prop_name = comp['bind_percent']
                lines.append(f"if ({comp['name']})")
                lines.append("{")
                lines.append(f"\t{comp['name']}->SetPercent({prop_name});")
                lines.append("}")
            
            if 'bind_text' in comp:
                prop_name = comp['bind_text']
                lines.append(f"if ({comp['name']})")
                lines.append("{")
                lines.append(f"\t{comp['name']}->SetText({prop_name});")
                lines.append("}")
        
        if not lines:
            lines.append("// 在此添加绑定更新逻辑")
        
        return lines
    
    def _generate_viewmodel_setter(self, schema: Dict, class_name: str) -> List[str]:
        """生成 SetViewModel 函数实现"""
        lines = []
        viewmodel = schema.get('viewmodel')
        if not viewmodel:
            return lines
        
        vm_class = viewmodel.get('class', 'UObject')
        
        lines.append(f"void {class_name}::SetViewModel({vm_class}* InViewModel)")
        lines.append("{")
        lines.append("\tViewModel = InViewModel;")
        lines.append("\tif (!ViewModel)")
        lines.append("\t{")
        lines.append("\t\treturn;")
        lines.append("\t}")
        lines.append("")
        lines.append("\t// 绑定 ViewModel 属性变化到 UI 更新")
        
        # 生成每个绑定
        for binding in viewmodel.get('bindings', []):
            source = binding.get('source', '')
            target = binding.get('target', '')
            if not target:
                continue
            
            # 解析 target: "ComponentName.Property"
            parts = target.split('.')
            if len(parts) == 2:
                comp_name, prop = parts
                lines.append(f"\t// {source} -> {target}")
                # 这里可以使用 FieldNotify 的委托绑定
        
        lines.append("")
        lines.append("\t// 初始化更新")
        lines.append("\tUpdateBindings();")
        lines.append("}")
        lines.append("")
        
        return lines
    
    def _generate_function_implementation(self, schema: Dict, class_name: str, func: Dict) -> List[str]:
        """生成函数实现"""
        lines = []
        
        return_type = func.get('return_type', 'void')
        params = func.get('parameters', [])
        param_str = ", ".join([f"{p['type']} {p['name']}" for p in params])
        
        lines.append(f"{return_type} {class_name}::{func['name']}({param_str})")
        lines.append("{")
        
        # 根据 body_hint 生成基本实现
        body_hint = func.get('body_hint', '')
        if body_hint:
            lines.append(f"\t// TODO: {body_hint}")
        
        lines.append("\tUpdateBindings();")
        lines.append("}")
        
        return lines
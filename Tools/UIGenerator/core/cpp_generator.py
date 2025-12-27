"""
C++ 代码生成器
根据 Schema 生成 Widget 的 C++ 头文件和实现文件
"""

import json
import os
from typing import Dict, List, Set, Optional
from datetime import datetime


class CppGenerator:
    """C++ Widget 代码生成器"""
    
    def __init__(self, widget_types_path: str, project_name: str = "DJ01"):
        """
        初始化生成器
        
        Args:
            widget_types_path: widget_types.json 路径
            project_name: 项目名称（用于 API 宏）
        """
        with open(widget_types_path, 'r', encoding='utf-8') as f:
            self.widget_types = json.load(f)
        
        self.project_name = project_name
        self.api_macro = f"{project_name.upper()}_API"
    
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
        
        # 文件头
        lines.append(self._generate_file_header(schema))
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        
        # Includes
        includes = self._collect_includes(schema)
        for inc in sorted(includes):
            lines.append(f'#include "{inc}"')
        lines.append("")
        lines.append(f'#include "{schema["name"]}Base.generated.h"')
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
        lines.append(f"void {class_name}::NativeDestruct()")
        lines.append("{")
        lines.append("\tSuper::NativeDestruct();")
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
            param_types = ", ".join([p['type'] for p in params])
            
            if params:
                lines.append(f"DECLARE_DYNAMIC_MULTICAST_DELEGATE_{len(params)}Param(F{event['name']}Delegate, {', '.join([f'{p[\"type\"]}, {p[\"name\"]}' for p in params])});")
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
        
        for comp in self._collect_all_components(schema.get('components', [])):
            # ProgressBar 百分比绑定
            if 'bind_percent' in comp:
                prop_name = comp['bind_percent']
                lines.append(f"if ({comp['name']})")
                lines.append("{")
                lines.append(f"\t{comp['name']}->SetPercent({prop_name});")
                lines.append("}")
            
            # TextBlock 文本绑定
            if 'bind_text' in comp:
                prop_name = comp['bind_text']
                lines.append(f"if ({comp['name']})")
                lines.append("{")
                lines.append(f"\t{comp['name']}->SetText({prop_name});")
                lines.append("}")
        
        if not lines:
            lines.append("// 在此添加绑定更新逻辑")
        
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
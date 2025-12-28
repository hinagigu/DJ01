#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Execution 代码生成器
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import MODULE_NAME


class ExecutionCodeGenerator:
    """Execution 代码生成器"""
    
    @staticmethod
    def generate(execution, timestamp: str) -> tuple:
        class_name = f"UDJ01{execution.name}Execution"
        header = ExecutionCodeGenerator._generate_header(execution, class_name, timestamp)
        source = ExecutionCodeGenerator._generate_source(execution, class_name, timestamp)
        return header, source
    
    @staticmethod
    def _generate_header(exe, class_name: str, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append(f"// {class_name}")
        lines.append("// 自动生成，可根据需要修改计算逻辑")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "CoreMinimal.h"')
        lines.append('#include "GameplayEffectExecutionCalculation.h"')
        lines.append(f'#include "{class_name}.generated.h"')
        lines.append("")
        lines.append(f"/** {exe.description} */")
        lines.append("UCLASS()")
        lines.append(f"class {MODULE_NAME}_API {class_name} : public UGameplayEffectExecutionCalculation")
        lines.append("{")
        lines.append("    GENERATED_BODY()")
        lines.append("")
        lines.append("public:")
        lines.append(f"    {class_name}();")
        lines.append("")
        lines.append("    virtual void Execute_Implementation(")
        lines.append("        const FGameplayEffectCustomExecutionParameters& ExecutionParams,")
        lines.append("        FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const override;")
        lines.append("};")
        lines.append("")
        return "\n".join(lines)
    
    @staticmethod
    def _generate_source(exe, class_name: str, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append(f"// {class_name}")
        lines.append("// 自动生成，可根据需要修改计算逻辑")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append(f'#include "{class_name}.h"')
        lines.append('#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"')
        lines.append('#include "DJ01/System/Public/DJ01GameplayTags.h"')
        lines.append('#include "AbilitySystemComponent.h"')
        lines.append("")
        lines.append(f"#include UE_INLINE_GENERATED_CPP_BY_NAME({class_name})")
        lines.append("")
        
        # 分类捕获
        base_captures = []
        total_captures = []
        for cap in exe.captures:
            if cap.get('layer', 'Base') == 'Total':
                total_captures.append(cap)
            else:
                base_captures.append(cap)
        
        # 生成捕获结构体
        ExecutionCodeGenerator._generate_capture_struct(lines, total_captures, base_captures)
        
        # 生成构造函数
        ExecutionCodeGenerator._generate_constructor(lines, class_name, total_captures, base_captures)
        
        # 生成 Execute 函数
        ExecutionCodeGenerator._generate_execute(lines, exe, class_name, total_captures, base_captures)
        
        return "\n".join(lines)
    
    @staticmethod
    def _collect_captures(total_captures, base_captures):
        """收集所有需要的捕获定义
        
        Returns:
            list of (attr_class, actual_prop, member_name, source)
        """
        all_captures = []
        declared = set()
        
        for cap in total_captures:
            attr, attr_class = cap['attr'], f"UDJ01{cap['set']}"
            source = cap.get('source', 'Source')
            member_suffix = '_Target' if source == 'Target' else ''
            
            for layer in ['Base', 'Flat', 'Percent']:
                member_name = f"{layer}{attr}{member_suffix}"
                actual_prop = f"{layer}{attr}"
                if member_name not in declared:
                    declared.add(member_name)
                    all_captures.append((attr_class, actual_prop, member_name, source))
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr, attr_class = cap['attr'], f"UDJ01{cap['set']}"
            source = cap.get('source', 'Source')
            member_suffix = '_Target' if source == 'Target' else ''
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            member_name = f"{prop}{member_suffix}"
            actual_prop = prop
            
            if member_name not in declared:
                declared.add(member_name)
                all_captures.append((attr_class, actual_prop, member_name, source))
        
        return all_captures
    
    @staticmethod
    def _generate_capture_struct(lines, total_captures, base_captures):
        """生成捕获结构体 - 延迟初始化模式
        
        使用 bInitialized 标志确保只在首次调用 Execute 时初始化，
        避免静态初始化顺序问题。
        """
        all_captures = ExecutionCodeGenerator._collect_captures(total_captures, base_captures)
        
        lines.append("namespace")
        lines.append("{")
        lines.append("    struct FCapturedAttributes")
        lines.append("    {")
        lines.append("        bool bInitialized = false;")
        
        # 声明 Def 成员
        for attr_class, actual_prop, member_name, source in all_captures:
            lines.append(f"        FGameplayEffectAttributeCaptureDefinition {member_name}Def;")
        
        lines.append("")
        lines.append("        void Initialize()")
        lines.append("        {")
        lines.append("            if (bInitialized) return;")
        lines.append("            bInitialized = true;")
        lines.append("")
        
        # 在 Initialize() 中初始化，而不是构造函数
        for attr_class, actual_prop, member_name, source in all_captures:
            source_enum = f"EGameplayEffectAttributeCaptureSource::{source}"
            lines.append(f"            {member_name}Def = FGameplayEffectAttributeCaptureDefinition({attr_class}::Get{actual_prop}Attribute(), {source_enum}, false);")
        
        lines.append("        }")
        lines.append("    };")
        lines.append("")
        lines.append("    static FCapturedAttributes& GetCapturedAttributes()")
        lines.append("    {")
        lines.append("        static FCapturedAttributes Attributes;")
        lines.append("        return Attributes;")
        lines.append("    }")
        lines.append("}")
        lines.append("")
    
    @staticmethod
    def _generate_constructor(lines, class_name, total_captures, base_captures):
        """生成构造函数 - 空构造函数，捕获定义在 Execute 时添加"""
        lines.append(f"{class_name}::{class_name}()")
        lines.append("{")
        lines.append("    // 捕获定义延迟到 Execute_Implementation 首次调用时初始化")
        lines.append("    // 避免静态初始化顺序问题")
        lines.append("}")
        lines.append("")
    
    @staticmethod
    def _generate_execute(lines, exe, class_name, total_captures, base_captures):
        """生成 Execute 函数"""
        lines.append(f"void {class_name}::Execute_Implementation(")
        lines.append("    const FGameplayEffectCustomExecutionParameters& ExecutionParams,")
        lines.append("    FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const")
        lines.append("{")
        lines.append("    // 延迟初始化捕获定义（首次调用时）")
        lines.append("    FCapturedAttributes& Attrs = GetCapturedAttributes();")
        lines.append("    Attrs.Initialize();")
        lines.append("")
        lines.append("    const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();")
        lines.append("    FAggregatorEvaluateParameters EvalParams;")
        lines.append("    EvalParams.SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();")
        lines.append("    EvalParams.TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();")
        lines.append("")
        
        # Tag 捕获生成 bool 变量
        if exe.tag_conditions:
            ExecutionCodeGenerator._generate_tag_captures(lines, exe.tag_conditions)
        
        # SetByCaller 参数
        if exe.setbycaller_params:
            ExecutionCodeGenerator._generate_setbycaller_params(lines, exe.setbycaller_params)
        
        lines.append("    // ========== 获取属性值 ==========")
        
        processed = set()
        
        for cap in total_captures:
            attr = cap['attr']
            source = cap.get('source', 'Source')
            member_suffix = '_Target' if source == 'Target' else ''
            var_suffix = '_Target' if source == 'Target' else ''
            
            # 避免重复处理同名属性
            key = f"{attr}_{source}"
            if key in processed:
                continue
            processed.add(key)
            
            lines.append(f"    float Base{attr}{var_suffix} = 0.f, Flat{attr}{var_suffix} = 0.f, Percent{attr}{var_suffix} = 0.f;")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Base{attr}{member_suffix}Def, EvalParams, Base{attr}{var_suffix});")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Flat{attr}{member_suffix}Def, EvalParams, Flat{attr}{var_suffix});")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Percent{attr}{member_suffix}Def, EvalParams, Percent{attr}{var_suffix});")
            lines.append(f"    const float {attr}{var_suffix}Value = (Base{attr}{var_suffix} + Flat{attr}{var_suffix}) * (1.f + Percent{attr}{var_suffix});")
            lines.append("")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            source = cap.get('source', 'Source')
            member_suffix = '_Target' if source == 'Target' else ''
            var_suffix = '_Target' if source == 'Target' else ''
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            
            key = f"{attr}_{source}_{layer}"
            if key in processed:
                continue
            processed.add(key)
            
            lines.append(f"    float {attr}{var_suffix}Value = 0.f;")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.{prop}{member_suffix}Def, EvalParams, {attr}{var_suffix}Value);")
        
        lines.append("")
        lines.append("    // ========== 计算逻辑 ==========")
        
        if exe.formula:
            for line in exe.formula.split('\n'):
                lines.append(f"    {line}")
        else:
            lines.append("    float FinalValue = 0.f;")
        

        
        lines.append("")
        lines.append("    // ========== 输出结果 ==========")
        for out in exe.outputs:
            attr_class = f"UDJ01{out['set']}"
            op = out.get('op', 'Additive')
            lines.append(f"    if (FinalValue != 0.f)")
            lines.append(f"    {{")
            lines.append(f"        OutExecutionOutput.AddOutputModifier(FGameplayModifierEvaluatedData(")
            lines.append(f"            {attr_class}::Get{out['attr']}Attribute(), EGameplayModOp::{op}, FinalValue));")
            lines.append(f"    }}")
        lines.append("}")
        lines.append("")
    
    @staticmethod
    def _generate_setbycaller_params(lines, setbycaller_params):
        """生成 SetByCaller 参数读取代码"""
        lines.append("    // ========== SetByCaller 参数（技能传入） ==========")
        
        for param in setbycaller_params:
            tag = param.get('tag', '')
            var_name = param.get('var_name', '')
            default = param.get('default', 0.0)
            
            if not tag or not var_name:
                continue
            
            # 转换 Tag 为 C++ 变量名格式
            tag_native = tag.replace('.', '_')
            
            lines.append(f"    const float {var_name} = Spec.GetSetByCallerMagnitude(")
            lines.append(f"        DJ01GameplayTags::{tag_native}, false, {default}f);")
        
        lines.append("")
    
    @staticmethod
    def _generate_tag_captures(lines, tag_conditions):
        """生成 Tag 捕获 bool 变量"""
        lines.append("    // ========== Tag 状态捕获 ==========")
        
        for cond in tag_conditions:
            tag = cond.get('tag', '')
            source = cond.get('source', 'Target')
            
            if not tag:
                continue
            
            # 生成变量名
            tag_clean = tag.replace('.', '_').replace('-', '_')
            if source == 'Target':
                var_name = f"bTarget_{tag_clean}"
            else:
                var_name = f"bSource_{tag_clean}"
            
            tag_container = "EvalParams.SourceTags" if source == "Source" else "EvalParams.TargetTags"
            tag_native = tag.replace('.', '_')
            
            lines.append(f"    const bool {var_name} = {tag_container} && {tag_container}->HasTag(DJ01GameplayTags::{tag_native});")
        
        lines.append("")
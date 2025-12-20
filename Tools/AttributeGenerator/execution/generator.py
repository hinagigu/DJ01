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
        lines.append('#include "DJ01GeneratedAttributes.h"')
        lines.append('#include "DJ01GameplayTags.h"')
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
    def _generate_capture_struct(lines, total_captures, base_captures):
        """生成捕获结构体"""
        lines.append("namespace")
        lines.append("{")
        lines.append("    struct FCapturedAttributes")
        lines.append("    {")
        
        for cap in total_captures:
            attr = cap['attr']
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF(Base{attr}{suffix});")
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF(Flat{attr}{suffix});")
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF(Percent{attr}{suffix});")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"        DECLARE_ATTRIBUTE_CAPTUREDEF({prop}{suffix});")
        
        lines.append("")
        lines.append("        FCapturedAttributes()")
        lines.append("        {")
        
        for cap in total_captures:
            attr, attr_class = cap['attr'], f"UDJ01{cap['set']}"
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, Base{attr}, {source}, false);")
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, Flat{attr}, {source}, false);")
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, Percent{attr}, {source}, false);")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr, attr_class = cap['attr'], f"UDJ01{cap['set']}"
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"            DEFINE_ATTRIBUTE_CAPTUREDEF({attr_class}, {prop}, {source}, false);")
        
        lines.append("        }")
        lines.append("    };")
        lines.append("")
        lines.append("    static const FCapturedAttributes& GetCapturedAttributes()")
        lines.append("    {")
        lines.append("        static FCapturedAttributes Attributes;")
        lines.append("        return Attributes;")
        lines.append("    }")
        lines.append("}")
        lines.append("")
    
    @staticmethod
    def _generate_constructor(lines, class_name, total_captures, base_captures):
        """生成构造函数"""
        lines.append(f"{class_name}::{class_name}()")
        lines.append("{")
        lines.append("    const FCapturedAttributes& Attrs = GetCapturedAttributes();")
        
        for cap in total_captures:
            attr = cap['attr']
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.Base{attr}{suffix}Def);")
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.Flat{attr}{suffix}Def);")
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.Percent{attr}{suffix}Def);")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"    RelevantAttributesToCapture.Add(Attrs.{prop}{suffix}Def);")
        
        lines.append("}")
        lines.append("")
    
    @staticmethod
    def _generate_execute(lines, exe, class_name, total_captures, base_captures):
        """生成 Execute 函数"""
        lines.append(f"void {class_name}::Execute_Implementation(")
        lines.append("    const FGameplayEffectCustomExecutionParameters& ExecutionParams,")
        lines.append("    FGameplayEffectCustomExecutionOutput& OutExecutionOutput) const")
        lines.append("{")
        lines.append("    const FCapturedAttributes& Attrs = GetCapturedAttributes();")
        lines.append("")
        lines.append("    const FGameplayEffectSpec& Spec = ExecutionParams.GetOwningSpec();")
        lines.append("    FAggregatorEvaluateParameters EvalParams;")
        lines.append("    EvalParams.SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();")
        lines.append("    EvalParams.TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();")
        lines.append("")
        
        # Tag 条件生成
        if exe.tag_conditions:
            ExecutionCodeGenerator._generate_tag_conditions(lines, exe.tag_conditions)
        
        lines.append("    // ========== 获取属性值 ==========")
        
        for cap in total_captures:
            attr = cap['attr']
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            var_suffix = f"_{source}" if source == 'Target' else ''
            lines.append(f"    float Base{attr}{var_suffix} = 0.f, Flat{attr}{var_suffix} = 0.f, Percent{attr}{var_suffix} = 0.f;")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Base{attr}{suffix}Def, EvalParams, Base{attr}{var_suffix});")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Flat{attr}{suffix}Def, EvalParams, Flat{attr}{var_suffix});")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.Percent{attr}{suffix}Def, EvalParams, Percent{attr}{var_suffix});")
            lines.append(f"    const float {attr}{var_suffix}Value = (Base{attr}{var_suffix} + Flat{attr}{var_suffix}) * (1.f + Percent{attr}{var_suffix});")
            lines.append("")
        
        for cap in base_captures:
            layer = cap.get('layer', 'Base')
            attr = cap['attr']
            source = cap.get('source', 'Source')
            suffix = f"_{source}" if source == 'Target' else ''
            var_suffix = f"_{source}" if source == 'Target' else ''
            prop = f"{layer}{attr}" if layer in ['Base', 'Flat', 'Percent'] else attr
            lines.append(f"    float {attr}{var_suffix}Value = 0.f;")
            lines.append(f"    ExecutionParams.AttemptCalculateCapturedAttributeMagnitude(Attrs.{prop}{suffix}Def, EvalParams, {attr}{var_suffix}Value);")
        
        lines.append("")
        lines.append("    // ========== 计算逻辑 ==========")
        
        if exe.formula:
            for line in exe.formula.split('\n'):
                lines.append(f"    {line}")
        else:
            lines.append("    float FinalValue = 0.f;")
        
        # 如果有 Tag 条件，应用乘数和加成
        if exe.tag_conditions:
            lines.append("")
            lines.append("    // 应用 Tag 条件修正")
            lines.append("    FinalValue = (FinalValue + TagAdditive) * TagMultiplier;")
        
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
    def _generate_tag_conditions(lines, tag_conditions):
        """生成 Tag 条件检查代码"""
        lines.append("    // ========== Tag 条件检查 ==========")
        lines.append("    float TagMultiplier = 1.f;")
        lines.append("    float TagAdditive = 0.f;")
        lines.append("")
        
        for cond in tag_conditions:
            tag = cond.get('tag', '')
            source = cond.get('source', 'Target')
            effect = cond.get('effect', 'Skip')
            value = cond.get('value', 0)
            
            var_name = tag.replace('.', '_')
            tag_container = "EvalParams.SourceTags" if source == "Source" else "EvalParams.TargetTags"
            
            if effect == 'Skip':
                lines.append(f"    // {source} 有 {tag} 标签时跳过")
                lines.append(f"    if ({tag_container} && {tag_container}->HasTag(DJ01GameplayTags::{var_name}))")
                lines.append(f"    {{")
                lines.append(f"        return; // 免疫")
                lines.append(f"    }}")
            elif effect == 'Multiply':
                lines.append(f"    // {source} 有 {tag} 标签时乘以 {value}")
                lines.append(f"    if ({tag_container} && {tag_container}->HasTag(DJ01GameplayTags::{var_name}))")
                lines.append(f"    {{")
                lines.append(f"        TagMultiplier *= {value}f;")
                lines.append(f"    }}")
            elif effect == 'Add':
                lines.append(f"    // {source} 有 {tag} 标签时加 {value}")
                lines.append(f"    if ({tag_container} && {tag_container}->HasTag(DJ01GameplayTags::{var_name}))")
                lines.append(f"    {{")
                lines.append(f"        TagAdditive += {value}f;")
                lines.append(f"    }}")
            lines.append("")
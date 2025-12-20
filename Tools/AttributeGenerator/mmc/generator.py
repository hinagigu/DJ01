#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MMC 代码生成器
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from config import MODULE_NAME


class MMCCodeGenerator:
    """MMC C++ 代码生成器"""
    
    @staticmethod
    def generate_all(mmc_list: list, timestamp: str) -> tuple:
        """生成所有 MMC 的统一 .h 和 .cpp 文件"""
        header = MMCCodeGenerator._generate_header(mmc_list, timestamp)
        source = MMCCodeGenerator._generate_source(mmc_list, timestamp)
        return header, source
    
    @staticmethod
    def _generate_header(mmc_list: list, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated MMC (Modifier Magnitude Calculations)")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "CoreMinimal.h"')
        lines.append('#include "GameplayModMagnitudeCalculation.h"')
        lines.append('#include "DJ01GeneratedMMC.generated.h"')
        lines.append("")
        
        for mmc in mmc_list:
            if not mmc.name:
                continue
            class_name = f"UDJ01MMC_{mmc.name}"
            
            lines.append("")
            lines.append("// ============================================================")
            lines.append(f"// {class_name}")
            lines.append("// ============================================================")
            lines.append("")
            lines.append(f"/** {mmc.description} */")
            lines.append("UCLASS()")
            lines.append(f"class {MODULE_NAME}_API {class_name} : public UGameplayModMagnitudeCalculation")
            lines.append("{")
            lines.append("    GENERATED_BODY()")
            lines.append("")
            lines.append("public:")
            lines.append(f"    {class_name}();")
            lines.append("")
            lines.append("    virtual float CalculateBaseMagnitude_Implementation(const FGameplayEffectSpec& Spec) const override;")
            lines.append("")
            lines.append("private:")
            
            for cap in mmc.captures:
                attr = cap.get('attr', '')
                source = cap.get('source', 'Target')
                suffix = f"_{source}" if source == 'Target' else ''
                lines.append(f"    FGameplayEffectAttributeCaptureDefinition {attr}{suffix}Def;")
            
            lines.append("};")
            lines.append("")
        
        return "\n".join(lines)
    
    @staticmethod
    def _generate_source(mmc_list: list, timestamp: str) -> str:
        lines = []
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated MMC (Modifier Magnitude Calculations)")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append('#include "DJ01GeneratedMMC.h"')
        lines.append('#include "DJ01GeneratedAttributes.h"')
        lines.append('#include "AbilitySystemComponent.h"')
        lines.append('#include "GameplayTagContainer.h"')
        lines.append("")
        lines.append('#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GeneratedMMC)')
        lines.append("")
        
        for mmc in mmc_list:
            if not mmc.name:
                continue
            
            class_name = f"UDJ01MMC_{mmc.name}"
            
            lines.append("")
            lines.append("// ============================================================")
            lines.append(f"// {class_name}")
            lines.append("// ============================================================")
            lines.append("")
            
            # 构造函数
            lines.append(f"{class_name}::{class_name}()")
            lines.append("{")
            
            for cap in mmc.captures:
                attr = cap.get('attr', '')
                set_name = cap.get('set', '')
                source = cap.get('source', 'Target')
                layer = cap.get('layer', 'Total')
                suffix = f"_{source}" if source == 'Target' else ''
                attr_class = f"UDJ01{set_name}"
                
                if layer == 'Total':
                    attr_getter = f"Get{attr}Attribute"
                elif layer in ['Base', 'Flat', 'Percent']:
                    attr_getter = f"Get{layer}{attr}Attribute"
                else:
                    attr_getter = f"Get{attr}Attribute"
                
                lines.append(f"    // 捕获 {source} 的 {attr} ({layer})")
                lines.append(f"    {attr}{suffix}Def.AttributeToCapture = {attr_class}::{attr_getter}();")
                lines.append(f"    {attr}{suffix}Def.AttributeSource = EGameplayEffectAttributeCaptureSource::{source};")
                lines.append(f"    {attr}{suffix}Def.bSnapshot = false;")
                lines.append(f"    RelevantAttributesToCapture.Add({attr}{suffix}Def);")
                lines.append("")
            
            lines.append("}")
            lines.append("")
            
            # 计算函数
            lines.append(f"float {class_name}::CalculateBaseMagnitude_Implementation(const FGameplayEffectSpec& Spec) const")
            lines.append("{")
            lines.append("    const FGameplayTagContainer* SourceTags = Spec.CapturedSourceTags.GetAggregatedTags();")
            lines.append("    const FGameplayTagContainer* TargetTags = Spec.CapturedTargetTags.GetAggregatedTags();")
            lines.append("")
            lines.append("    FAggregatorEvaluateParameters EvalParams;")
            lines.append("    EvalParams.SourceTags = SourceTags;")
            lines.append("    EvalParams.TargetTags = TargetTags;")
            lines.append("")
            
            lines.append("    // ========== 获取捕获的属性值 ==========")
            for cap in mmc.captures:
                attr = cap.get('attr', '')
                source = cap.get('source', 'Target')
                suffix = f"_{source}" if source == 'Target' else ''
                var_name = f"{attr}{suffix}Value"
                
                lines.append(f"    float {var_name} = 0.f;")
                lines.append(f"    GetCapturedAttributeMagnitude({attr}{suffix}Def, Spec, EvalParams, {var_name});")
            lines.append("")
            
            if mmc.set_by_callers:
                lines.append("    // ========== 获取 SetByCaller 值 ==========")
                for sbc in mmc.set_by_callers:
                    tag = sbc.get('tag', '')
                    default = sbc.get('default', 0)
                    desc = sbc.get('description', '')
                    var_name = tag.replace('.', '_')
                    
                    lines.append(f"    // {desc}")
                    lines.append(f"    float {var_name} = Spec.GetSetByCallerMagnitude(")
                    lines.append(f'        FGameplayTag::RequestGameplayTag(FName("{tag}")),')
                    lines.append(f"        false,  // WarnIfNotFound")
                    lines.append(f"        {default}f  // DefaultValue")
                    lines.append(f"    );")
                lines.append("")
            
            lines.append("    // ========== 计算逻辑 ==========")
            if mmc.formula:
                for line in mmc.formula.strip().split('\n'):
                    lines.append(f"    {line}")
            else:
                lines.append("    float Result = 0.f;")
                lines.append("    // TODO: 在编辑器中配置计算公式")
                lines.append("    return Result;")
            
            lines.append("}")
            lines.append("")
        
        return "\n".join(lines)
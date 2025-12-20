#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
属性代码生成器 - 扩展版本
支持生成 Clamp、委托、事件、GameplayCue 代码
"""

import sys
from pathlib import Path
from collections import OrderedDict

sys.path.insert(0, str(Path(__file__).parent.parent))

from config import MODULE_NAME


class AttributeCodeGenerator:
    """属性代码生成器 - 扩展版本"""
    
    @staticmethod
    def generate_header(attribute_sets: dict, timestamp: str) -> str:
        """生成头文件"""
        lines = []
        
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated Attributes")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append("#pragma once")
        lines.append("")
        lines.append('#include "DJ01/AbilitySystem/Attributes/Public/DJ01AttributeSet.h"')
        lines.append('#include "DJ01/AbilitySystem/Attributes/Public/DJ01AttributeMacros.h"')
        lines.append('#include "AbilitySystemComponent.h"')
        lines.append('#include "DJ01GeneratedAttributes.generated.h"')
        lines.append("")
        
        for set_name, attributes in attribute_sets.items():
            lines.append("")
            lines.append(f"// ##########################################################")
            lines.append(f"// UDJ01{set_name}")
            lines.append(f"// ##########################################################")
            lines.extend(AttributeCodeGenerator._generate_class_header(set_name, attributes))
        
        return "\n".join(lines)
    
    @staticmethod
    def _generate_class_header(set_name: str, attributes: list) -> list:
        """生成单个类的头文件"""
        class_name = f"UDJ01{set_name}"
        
        layered = [a for a in attributes if a.type == 'Layered']
        simple = [a for a in attributes if a.type == 'Simple']
        resource = [a for a in attributes if a.type == 'Resource']
        meta = [a for a in attributes if a.type == 'Meta']
        
        # 检查是否需要行为回调
        # Resource 类型自动有 Clamp，所以也需要检查
        has_clamp = any(a.clamp.enabled or a.type == 'Resource' for a in attributes)
        has_delegate = any(a.delegate.on_change or a.delegate.on_increase or a.delegate.on_decrease for a in attributes)
        has_event = any(a.event.on_zero_tag or a.event.on_full_tag or a.event.threshold_low is not None for a in attributes)
        has_cue = any(a.cue.on_decrease_cue or a.cue.on_zero_cue or a.cue.on_increase_cue for a in attributes)
        needs_behavior = has_clamp or has_delegate or has_event or has_cue
        
        # 按分类组织
        categories = OrderedDict()
        for attr in attributes:
            if attr.category not in categories:
                categories[attr.category] = []
            categories[attr.category].append(attr)
        
        lines = []
        lines.append(f"/** {set_name} - 包含 {len(attributes)} 个属性 */")
        lines.append("UCLASS(BlueprintType)")
        lines.append(f"class {MODULE_NAME}_API {class_name} : public UDJ01AttributeSet")
        lines.append("{")
        lines.append("    GENERATED_BODY()")
        lines.append("")
        lines.append("public:")
        lines.append(f"    {class_name}();")
        lines.append("")
        
        # 生成属性声明
        for category, attrs in categories.items():
            lines.append(f"    // ---------- {category} ----------")
            for attr in attrs:
                lines.append(f"    /** {attr.description} */")
                if attr.type == 'Layered':
                    lines.append(f"    DECLARE_LAYERED_ATTRIBUTE({class_name}, {attr.name})")
                elif attr.type == 'Simple':
                    lines.append(f"    DECLARE_SIMPLE_ATTRIBUTE({class_name}, {attr.name})")
                elif attr.type == 'Resource':
                    lines.append(f"    DECLARE_RESOURCE_ATTRIBUTE({class_name}, {attr.name})")
                else:  # Meta
                    lines.append(f"    DECLARE_META_ATTRIBUTE({class_name}, {attr.name})")
                lines.append("")
        
        # 生成委托声明
        if has_delegate:
            lines.append("    // ---------- 属性变化委托 ----------")
            for attr in attributes:
                if attr.delegate.on_change:
                    lines.append(f"    /** {attr.name} 变化委托 */")
                    lines.append(f"    FDJ01AttributeEvent On{attr.name}Changed;")
                    lines.append("")
                if attr.delegate.on_increase:
                    lines.append(f"    /** {attr.name} 增加委托 */")
                    lines.append(f"    FDJ01AttributeEvent On{attr.name}Increased;")
                    lines.append("")
                if attr.delegate.on_decrease:
                    delegate_name = attr.delegate.decrease_alias if attr.delegate.decrease_alias else f"On{attr.name}Decreased"
                    lines.append(f"    /** {attr.name} 减少委托 */")
                    lines.append(f"    FDJ01AttributeEvent {delegate_name};")
                    lines.append("")
        
        lines.append("protected:")
        
        # OnRep 声明
        for attr in layered:
            lines.append(f"    DECLARE_LAYERED_ATTRIBUTE_ONREP({attr.name})")
        for attr in simple:
            lines.append(f"    DECLARE_SIMPLE_ATTRIBUTE_ONREP({attr.name})")
        for attr in resource:
            lines.append(f"    DECLARE_RESOURCE_ATTRIBUTE_ONREP({attr.name})")
        
        lines.append("")
        lines.append("    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;")
        
        # 如果需要行为回调，添加 override
        if has_clamp:
            lines.append("    virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;")
        if has_delegate or has_event or has_cue:
            lines.append("    virtual void PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue) override;")
        if has_cue:
            lines.append("    virtual void PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data) override;")
        
        lines.append("};")
        
        return lines
    
    @staticmethod
    def generate_source(attribute_sets: dict, timestamp: str) -> str:
        """生成源文件"""
        lines = []
        lines.append("// ============================================================")
        lines.append("// DJ01 Generated Attributes")
        lines.append("// 自动生成的文件，请勿手动修改！")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append("// ============================================================")
        lines.append("")
        lines.append('#include "DJ01/AbilitySystem/Attributes/Public/DJ01GeneratedAttributes.h"')
        lines.append('#include "Net/UnrealNetwork.h"')
        lines.append('#include "GameplayTagsManager.h"')
        lines.append('#include "AbilitySystemComponent.h"')
        lines.append("")
        lines.append("#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GeneratedAttributes)")
        lines.append("")
        
        for set_name, attributes in attribute_sets.items():
            lines.append("")
            lines.append(f"// ##########################################################")
            lines.append(f"// UDJ01{set_name}")
            lines.append(f"// ##########################################################")
            lines.append("")
            lines.extend(AttributeCodeGenerator._generate_class_source(set_name, attributes))
        
        return "\n".join(lines)
    
    @staticmethod
    def _generate_class_source(set_name: str, attributes: list) -> list:
        """生成单个类的源文件"""
        class_name = f"UDJ01{set_name}"
        
        layered = [a for a in attributes if a.type == 'Layered']
        simple = [a for a in attributes if a.type == 'Simple']
        resource = [a for a in attributes if a.type == 'Resource']
        
        # 检查是否需要行为回调
        # Resource 类型自动有 Clamp，所以也需要检查
        has_clamp = any(a.clamp.enabled or a.type == 'Resource' for a in attributes)
        has_delegate = any(a.delegate.on_change or a.delegate.on_increase or a.delegate.on_decrease for a in attributes)
        has_event = any(a.event.on_zero_tag or a.event.on_full_tag or a.event.threshold_low is not None for a in attributes)
        has_cue = any(a.cue.on_decrease_cue or a.cue.on_zero_cue or a.cue.on_increase_cue for a in attributes)
        
        lines = []
        
        # 构造函数
        lines.append(f"{class_name}::{class_name}()")
        lines.append("{")
        for attr in attributes:
            if attr.type == 'Layered':
                lines.append(f"    InitBase{attr.name}({attr.default_base}f);")
                lines.append(f"    InitFlat{attr.name}({attr.default_flat}f);")
                lines.append(f"    InitPercent{attr.name}({attr.default_percent}f);")
            elif attr.type == 'Simple':
                lines.append(f"    Init{attr.name}({attr.default_base}f);")
            elif attr.type == 'Resource':
                lines.append(f"    InitBaseMax{attr.name}({attr.default_base}f);")
                lines.append(f"    InitFlatMax{attr.name}({attr.default_flat}f);")
                lines.append(f"    InitPercentMax{attr.name}({attr.default_percent}f);")
                current_val = attr.default_current if attr.default_current else attr.default_base
                lines.append(f"    Init{attr.name}({current_val}f);")
        lines.append("}")
        lines.append("")
        
        # GetLifetimeReplicatedProps
        lines.append(f"void {class_name}::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const")
        lines.append("{")
        lines.append("    Super::GetLifetimeReplicatedProps(OutLifetimeProps);")
        for attr in layered:
            lines.append(f"    REGISTER_LAYERED_ATTRIBUTE_REPLICATION({class_name}, {attr.name})")
        for attr in simple:
            lines.append(f"    REGISTER_SIMPLE_ATTRIBUTE_REPLICATION({class_name}, {attr.name})")
        for attr in resource:
            lines.append(f"    REGISTER_RESOURCE_ATTRIBUTE_REPLICATION({class_name}, {attr.name})")
        lines.append("}")
        lines.append("")
        
        # OnRep 实现
        for attr in layered:
            lines.append(f"IMPLEMENT_LAYERED_ATTRIBUTE_ONREP({class_name}, {attr.name})")
        for attr in simple:
            lines.append(f"IMPLEMENT_SIMPLE_ATTRIBUTE_ONREP({class_name}, {attr.name})")
        for attr in resource:
            lines.append(f"IMPLEMENT_RESOURCE_ATTRIBUTE_ONREP({class_name}, {attr.name})")
        lines.append("")
        
        # ========== PreAttributeChange (Clamp) ==========
        if has_clamp:
            lines.extend(AttributeCodeGenerator._generate_pre_attribute_change(class_name, attributes))
        
        # ========== PostAttributeChange (委托 + 事件) ==========
        if has_delegate or has_event:
            lines.extend(AttributeCodeGenerator._generate_post_attribute_change(class_name, attributes))
        
        # ========== PostGameplayEffectExecute (Cue) ==========
        if has_cue:
            lines.extend(AttributeCodeGenerator._generate_post_ge_execute(class_name, attributes))
        
        return lines
    
    @staticmethod
    def _generate_pre_attribute_change(class_name: str, attributes: list) -> list:
        """生成 PreAttributeChange - Clamp 逻辑"""
        lines = []
        lines.append(f"void {class_name}::PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue)")
        lines.append("{")
        lines.append("    Super::PreAttributeChange(Attribute, NewValue);")
        lines.append("")
        
        for attr in attributes:
            # Resource 类型自动推断 Clamp：min=0, max=MaxXxx (通过 GetTotalMaxXxx)
            is_resource_auto_clamp = (attr.type == 'Resource')
            
            if not attr.clamp.enabled and not is_resource_auto_clamp:
                continue
            
            # 确定属性 getter
            if attr.type == 'Resource':
                attr_getter = f"Get{attr.name}Attribute"
            elif attr.type == 'Layered':
                attr_getter = f"GetBase{attr.name}Attribute"  # Clamp Base
            else:
                attr_getter = f"Get{attr.name}Attribute"
            
            lines.append(f"    // ===== {attr.name} Clamp =====")
            lines.append(f"    if (Attribute == {attr_getter}())")
            lines.append("    {")
            
            # 构建 Clamp 表达式
            if is_resource_auto_clamp and not attr.clamp.enabled:
                # Resource 自动 Clamp: [0, TotalMaxXxx]
                min_expr = "0.f"
                max_expr = f"GetTotalMax{attr.name}()"
                lines.append(f"        // Resource 自动 Clamp: [0, Max{attr.name}]")
            else:
                # 用户配置的 Clamp
                min_expr = str(attr.clamp.min_value) + "f" if attr.clamp.min_value is not None else None
                
                if attr.clamp.max_attribute:
                    # 最大值来自另一个属性
                    max_attr = attr.clamp.max_attribute
                    # 统一使用 GetTotal，因为这是计算后的最终值
                    max_expr = f"GetTotal{max_attr}()"
                elif attr.clamp.max_value is not None:
                    max_expr = str(attr.clamp.max_value) + "f"
                else:
                    max_expr = None
            
            if min_expr and max_expr:
                lines.append(f"        NewValue = FMath::Clamp(NewValue, {min_expr}, {max_expr});")
            elif min_expr:
                lines.append(f"        NewValue = FMath::Max(NewValue, {min_expr});")
            elif max_expr:
                lines.append(f"        NewValue = FMath::Min(NewValue, {max_expr});")
            
            lines.append("    }")
            lines.append("")
        
        lines.append("}")
        lines.append("")
        return lines
    
    @staticmethod
    def _generate_post_attribute_change(class_name: str, attributes: list) -> list:
        """生成 PostAttributeChange - 委托和事件逻辑"""
        lines = []
        lines.append(f"void {class_name}::PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue)")
        lines.append("{")
        lines.append("    Super::PostAttributeChange(Attribute, OldValue, NewValue);")
        lines.append("")
        
        for attr in attributes:
            has_any = (attr.delegate.on_change or attr.delegate.on_increase or attr.delegate.on_decrease or
                      attr.event.on_zero_tag or attr.event.on_full_tag or attr.event.threshold_low is not None)
            if not has_any:
                continue
            
            # 确定属性 getter
            if attr.type == 'Resource':
                attr_getter = f"Get{attr.name}Attribute"
            elif attr.type == 'Layered':
                attr_getter = f"GetBase{attr.name}Attribute"
            else:
                attr_getter = f"Get{attr.name}Attribute"
            
            lines.append(f"    // ===== {attr.name} 变化处理 =====")
            lines.append(f"    if (Attribute == {attr_getter}())")
            lines.append("    {")
            
            # 委托广播
            if attr.delegate.on_change:
                lines.append(f"        // 广播变化委托")
                lines.append(f"        On{attr.name}Changed.Broadcast(nullptr, nullptr, nullptr, NewValue - OldValue, OldValue, NewValue);")
                lines.append("")
            
            if attr.delegate.on_increase:
                lines.append(f"        // 增加时广播")
                lines.append(f"        if (NewValue > OldValue)")
                lines.append("        {")
                lines.append(f"            On{attr.name}Increased.Broadcast(nullptr, nullptr, nullptr, NewValue - OldValue, OldValue, NewValue);")
                lines.append("        }")
                lines.append("")
            
            if attr.delegate.on_decrease:
                delegate_name = attr.delegate.decrease_alias if attr.delegate.decrease_alias else f"On{attr.name}Decreased"
                lines.append(f"        // 减少时广播")
                lines.append(f"        if (NewValue < OldValue)")
                lines.append("        {")
                lines.append(f"            {delegate_name}.Broadcast(nullptr, nullptr, nullptr, OldValue - NewValue, OldValue, NewValue);")
                lines.append("        }")
                lines.append("")
            
            # 归零事件
            if attr.event.on_zero_tag:
                tag = attr.event.on_zero_tag.replace('.', '_')
                lines.append(f"        // 归零事件")
                lines.append(f"        if (NewValue <= 0.f && OldValue > 0.f)")
                lines.append("        {")
                lines.append(f"            if (UAbilitySystemComponent* ASC = GetAbilitySystemComponent())")
                lines.append("            {")
                lines.append(f'                FGameplayTag Tag = FGameplayTag::RequestGameplayTag(FName("{attr.event.on_zero_tag}"));')
                lines.append(f"                ASC->AddLooseGameplayTag(Tag);")
                lines.append("            }")
                lines.append("        }")
                lines.append("")
            
            # 满值事件
            if attr.event.on_full_tag:
                lines.append(f"        // 满值事件")
                if attr.type == 'Resource' and attr.clamp.max_attribute:
                    max_getter = f"GetTotal{attr.clamp.max_attribute}()"
                    lines.append(f"        if (NewValue >= {max_getter} && OldValue < {max_getter})")
                else:
                    lines.append(f"        // TODO: 需要配置最大值属性来检测满值")
                    lines.append(f"        // if (NewValue >= MaxValue && OldValue < MaxValue)")
                lines.append("        {")
                lines.append(f"            if (UAbilitySystemComponent* ASC = GetAbilitySystemComponent())")
                lines.append("            {")
                lines.append(f'                FGameplayTag Tag = FGameplayTag::RequestGameplayTag(FName("{attr.event.on_full_tag}"));')
                lines.append(f"                ASC->AddLooseGameplayTag(Tag);")
                lines.append("            }")
                lines.append("        }")
                lines.append("")
            
            # 低阈值事件
            if attr.event.threshold_low is not None and attr.event.threshold_low_tag:
                threshold = attr.event.threshold_low
                if attr.type == 'Resource' and attr.clamp.max_attribute:
                    max_getter = f"GetTotal{attr.clamp.max_attribute}()"
                    lines.append(f"        // 低阈值事件 ({threshold * 100:.0f}%)")
                    lines.append(f"        float ThresholdValue = {max_getter} * {threshold}f;")
                    lines.append(f"        if (NewValue <= ThresholdValue && OldValue > ThresholdValue)")
                    lines.append("        {")
                    lines.append(f"            if (UAbilitySystemComponent* ASC = GetAbilitySystemComponent())")
                    lines.append("            {")
                    lines.append(f'                FGameplayTag Tag = FGameplayTag::RequestGameplayTag(FName("{attr.event.threshold_low_tag}"));')
                    lines.append(f"                ASC->AddLooseGameplayTag(Tag);")
                    lines.append("            }")
                    lines.append("        }")
                    lines.append("")
            
            lines.append("    }")
            lines.append("")
        
        lines.append("}")
        lines.append("")
        return lines
    
    @staticmethod
    def _generate_post_ge_execute(class_name: str, attributes: list) -> list:
        """生成 PostGameplayEffectExecute - GameplayCue 逻辑"""
        lines = []
        lines.append(f"void {class_name}::PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data)")
        lines.append("{")
        lines.append("    Super::PostGameplayEffectExecute(Data);")
        lines.append("")
        
        for attr in attributes:
            if not (attr.cue.on_decrease_cue or attr.cue.on_zero_cue or attr.cue.on_increase_cue):
                continue
            
            # 确定属性 getter
            if attr.type == 'Resource':
                attr_getter = f"Get{attr.name}Attribute"
            elif attr.type == 'Layered':
                attr_getter = f"GetBase{attr.name}Attribute"
            else:
                attr_getter = f"Get{attr.name}Attribute"
            
            lines.append(f"    // ===== {attr.name} GameplayCue =====")
            lines.append(f"    if (Data.EvaluatedData.Attribute == {attr_getter}())")
            lines.append("    {")
            lines.append("        UAbilitySystemComponent* ASC = GetAbilitySystemComponent();")
            lines.append("        if (!ASC) return;")
            lines.append("")
            
            if attr.cue.on_decrease_cue:
                lines.append(f"        // 减少时触发 Cue")
                lines.append(f"        if (Data.EvaluatedData.Magnitude < 0)")
                lines.append("        {")
                lines.append(f"            FGameplayCueParameters CueParams;")
                lines.append(f"            CueParams.RawMagnitude = -Data.EvaluatedData.Magnitude;")
                lines.append(f'            FGameplayTag CueTag = FGameplayTag::RequestGameplayTag(FName("{attr.cue.on_decrease_cue}"));')
                lines.append(f"            ASC->ExecuteGameplayCue(CueTag, CueParams);")
                lines.append("        }")
                lines.append("")
            
            if attr.cue.on_increase_cue:
                lines.append(f"        // 增加时触发 Cue")
                lines.append(f"        if (Data.EvaluatedData.Magnitude > 0)")
                lines.append("        {")
                lines.append(f"            FGameplayCueParameters CueParams;")
                lines.append(f"            CueParams.RawMagnitude = Data.EvaluatedData.Magnitude;")
                lines.append(f'            FGameplayTag CueTag = FGameplayTag::RequestGameplayTag(FName("{attr.cue.on_increase_cue}"));')
                lines.append(f"            ASC->ExecuteGameplayCue(CueTag, CueParams);")
                lines.append("        }")
                lines.append("")
            
            if attr.cue.on_zero_cue:
                if attr.type == 'Resource':
                    current_getter = f"Get{attr.name}"
                else:
                    current_getter = f"Get{attr.name}"
                lines.append(f"        // 归零时触发 Cue")
                lines.append(f"        if ({current_getter}() <= 0.f)")
                lines.append("        {")
                lines.append(f"            FGameplayCueParameters CueParams;")
                lines.append(f'            FGameplayTag CueTag = FGameplayTag::RequestGameplayTag(FName("{attr.cue.on_zero_cue}"));')
                lines.append(f"            ASC->ExecuteGameplayCue(CueTag, CueParams);")
                lines.append("        }")
                lines.append("")
            
            lines.append("    }")
            lines.append("")
        
        lines.append("}")
        lines.append("")
        return lines
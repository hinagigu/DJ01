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
    
    # ============================================================
    # 头文件展开方法 - UHT 需要直接看到 UPROPERTY/UFUNCTION
    # ============================================================
    
    @staticmethod
    def _expand_layered_attribute_decl(class_name: str, attr_name: str) -> list:
        """展开三层属性声明 - UHT 需要直接看到 UPROPERTY"""
        lines = []
        for prefix in ['Base', 'Flat', 'Percent']:
            lines.append(f'    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_{prefix}{attr_name}, Category = "DJ01|{attr_name}", Meta = (AllowPrivateAccess = true))')
            lines.append(f"    FGameplayAttributeData {prefix}{attr_name};")
            lines.append(f"    ATTRIBUTE_ACCESSORS({class_name}, {prefix}{attr_name})")
            lines.append("")
        # GetTotal 计算函数
        lines.append(f'    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")')
        lines.append(f"    float GetTotal{attr_name}() const")
        lines.append("    {")
        lines.append(f"        return (GetBase{attr_name}() + GetFlat{attr_name}()) * (1.f + GetPercent{attr_name}());")
        lines.append("    }")
        lines.append("")
        # GetExtra 计算函数
        lines.append(f'    UFUNCTION(BlueprintPure, Category = "DJ01|Attributes")')
        lines.append(f"    float GetExtra{attr_name}() const")
        lines.append("    {")
        lines.append(f"        return GetTotal{attr_name}() - GetBase{attr_name}();")
        lines.append("    }")
        return lines
    
    @staticmethod
    def _expand_simple_attribute_decl(class_name: str, attr_name: str) -> list:
        """展开简单属性声明"""
        return [
            f'    UPROPERTY(BlueprintReadOnly, ReplicatedUsing = OnRep_{attr_name}, Category = "DJ01|Attributes", Meta = (AllowPrivateAccess = true))',
            f"    FGameplayAttributeData {attr_name};",
            f"    ATTRIBUTE_ACCESSORS({class_name}, {attr_name})"
        ]
    
    @staticmethod
    def _expand_resource_attribute_decl(class_name: str, attr_name: str) -> list:
        """展开资源属性声明 (Max + Current)"""
        lines = AttributeCodeGenerator._expand_layered_attribute_decl(class_name, f"Max{attr_name}")
        lines.append("")
        lines.extend(AttributeCodeGenerator._expand_simple_attribute_decl(class_name, attr_name))
        return lines
    
    @staticmethod
    def _expand_meta_attribute_decl(class_name: str, attr_name: str) -> list:
        """展开元属性声明 (不复制)"""
        return [
            f'    UPROPERTY(BlueprintReadOnly, Category = "DJ01|Meta", Meta = (HideFromModifiers, AllowPrivateAccess = true))',
            f"    FGameplayAttributeData {attr_name};",
            f"    ATTRIBUTE_ACCESSORS({class_name}, {attr_name})"
        ]
    
    @staticmethod
    def _expand_layered_onrep_decl(attr_name: str) -> list:
        """展开三层属性 OnRep 声明"""
        lines = []
        for prefix in ['Base', 'Flat', 'Percent']:
            lines.append("    UFUNCTION()")
            lines.append(f"    void OnRep_{prefix}{attr_name}(const FGameplayAttributeData& OldValue);")
        return lines
    
    @staticmethod
    def _expand_simple_onrep_decl(attr_name: str) -> list:
        """展开简单属性 OnRep 声明"""
        return [
            "    UFUNCTION()",
            f"    void OnRep_{attr_name}(const FGameplayAttributeData& OldValue);"
        ]
    
    @staticmethod
    def _expand_resource_onrep_decl(attr_name: str) -> list:
        """展开资源属性 OnRep 声明"""
        lines = AttributeCodeGenerator._expand_layered_onrep_decl(f"Max{attr_name}")
        lines.extend(AttributeCodeGenerator._expand_simple_onrep_decl(attr_name))
        return lines

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
        
        # 生成属性声明 - 完全展开以让 UHT 识别 UPROPERTY
        for category, attrs in categories.items():
            lines.append(f"    // ---------- {category} ----------")
            for attr in attrs:
                lines.append(f"    /** {attr.description} */")
                if attr.type == 'Layered':
                    lines.extend(AttributeCodeGenerator._expand_layered_attribute_decl(class_name, attr.name))
                elif attr.type == 'Simple':
                    lines.extend(AttributeCodeGenerator._expand_simple_attribute_decl(class_name, attr.name))
                elif attr.type == 'Resource':
                    lines.extend(AttributeCodeGenerator._expand_resource_attribute_decl(class_name, attr.name))
                else:  # Meta
                    lines.extend(AttributeCodeGenerator._expand_meta_attribute_decl(class_name, attr.name))
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
        
        # OnRep 声明 - 必须展开 UFUNCTION 让 UHT 识别
        for attr in layered:
            lines.extend(AttributeCodeGenerator._expand_layered_onrep_decl(attr.name))
        for attr in simple:
            lines.extend(AttributeCodeGenerator._expand_simple_onrep_decl(attr.name))
        for attr in resource:
            lines.extend(AttributeCodeGenerator._expand_resource_onrep_decl(attr.name))
        
        lines.append("")
        lines.append("    virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const override;")
        
        # Resource 类型需要监听 Max 变化来联动调整 Current
        has_resource_sync = any(a.type == 'Resource' for a in attributes)
        
        # 如果需要行为回调，添加 override
        if has_clamp:
            lines.append("    virtual void PreAttributeChange(const FGameplayAttribute& Attribute, float& NewValue) override;")
        if has_delegate or has_event or has_resource_sync:
            lines.append("    virtual void PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue) override;")
        # Meta 属性或 Cue 需要 PostGameplayEffectExecute
        has_meta = len(meta) > 0
        if has_cue or has_meta:
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
        lines.append('#include "GameplayEffectExtension.h"')
        lines.append("")
        lines.append("#include UE_INLINE_GENERATED_CPP_BY_NAME(DJ01GeneratedAttributes)")
        lines.append("")
        
        for set_name, attributes in attribute_sets.items():
            lines.append("")
            lines.append(f"// ##########################################################")
            lines.append(f"// UDJ01{set_name}")
            lines.append(f"// ##########################################################")
            lines.append("")
            # 传入所有属性集以支持跨集访问查找
            lines.extend(AttributeCodeGenerator._generate_class_source(set_name, attributes, attribute_sets))
        
        return "\n".join(lines)
    
    @staticmethod
    def _generate_class_source(set_name: str, attributes: list, all_attribute_sets: dict = None) -> list:
        """生成单个类的源文件
        
        Args:
            set_name: 当前属性集名称
            attributes: 当前属性集的属性列表
            all_attribute_sets: 所有属性集字典，用于跨集访问查找
        """
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
        # Meta 属性需要 PostGameplayEffectExecute 来处理
        has_meta = len(meta) > 0
        
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
            elif attr.type == 'Meta':
                # Meta 属性初始化为 0，每次使用后应该重置
                lines.append(f"    Init{attr.name}(0.0f);")
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
        
        # Resource 类型需要监听 Max 变化来联动调整 Current
        has_resource_sync = any(a.type == 'Resource' for a in attributes)
        
        # ========== PostAttributeChange (委托 + 事件 + Resource联动) ==========
        if has_delegate or has_event or has_resource_sync:
            lines.extend(AttributeCodeGenerator._generate_post_attribute_change(class_name, attributes))
        
        # ========== PostGameplayEffectExecute (Cue + Meta) ==========
        if has_cue or has_meta:
            lines.extend(AttributeCodeGenerator._generate_post_ge_execute(class_name, attributes, meta, all_attribute_sets))
        
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
        """生成 PostAttributeChange - 委托、事件和 Resource 联动逻辑"""
        lines = []
        lines.append(f"void {class_name}::PostAttributeChange(const FGameplayAttribute& Attribute, float OldValue, float NewValue)")
        lines.append("{")
        lines.append("    Super::PostAttributeChange(Attribute, OldValue, NewValue);")
        lines.append("")
        
        # ========== Resource 类型 MaxXxx 变化联动 ==========
        resource_attrs = [a for a in attributes if a.type == 'Resource']
        for attr in resource_attrs:
            mode = attr.resource_config.max_change_mode
            
            # 监听 BaseMaxXxx, FlatMaxXxx, PercentMaxXxx 中任一变化
            lines.append(f"    // ===== Max{attr.name} 变化时联动调整 {attr.name} =====")
            lines.append(f"    if (Attribute == GetBaseMax{attr.name}Attribute() ||")
            lines.append(f"        Attribute == GetFlatMax{attr.name}Attribute() ||")
            lines.append(f"        Attribute == GetPercentMax{attr.name}Attribute())")
            lines.append("    {")
            
            if mode == "KeepRatio":
                # 保持百分比: 计算旧的百分比，乘以新的最大值
                lines.append(f"        // KeepRatio: 保持当前值占最大值的百分比")
                lines.append(f"        const float OldMax = GetTotalMax{attr.name}() - (NewValue - OldValue);")
                lines.append(f"        const float NewMax = GetTotalMax{attr.name}();")
                lines.append(f"        if (OldMax > 0.f && NewMax > 0.f)")
                lines.append("        {")
                lines.append(f"            const float Ratio = Get{attr.name}() / OldMax;")
                lines.append(f"            Set{attr.name}(FMath::Clamp(Ratio * NewMax, 0.f, NewMax));")
                lines.append("        }")
            elif mode == "AddDifference":
                # 增加差值: 当前值 += (新最大值 - 旧最大值)
                lines.append(f"        // AddDifference: 当前值同步增减差值")
                lines.append(f"        const float MaxDelta = NewValue - OldValue;")
                lines.append(f"        const float NewCurrent = Get{attr.name}() + MaxDelta;")
                lines.append(f"        Set{attr.name}(FMath::Clamp(NewCurrent, 0.f, GetTotalMax{attr.name}()));")
            else:
                # KeepCurrent (默认): 只做 Clamp，确保不超过新上限
                lines.append(f"        // KeepCurrent: 保持当前值，超限时 Clamp")
                lines.append(f"        const float CurrentValue = Get{attr.name}();")
                lines.append(f"        const float NewMax = GetTotalMax{attr.name}();")
                lines.append(f"        if (CurrentValue > NewMax)")
                lines.append("        {")
                lines.append(f"            Set{attr.name}(NewMax);")
                lines.append("        }")
            
            lines.append("    }")
            lines.append("")
        
        # ========== 委托和事件处理 ==========
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
                lines.append(f"            if (UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent())")
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
                lines.append(f"            if (UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent())")
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
                    lines.append(f"            if (UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent())")
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
    def _generate_post_ge_execute(class_name: str, attributes: list, meta_attrs: list = None, 
                                   all_attribute_sets: dict = None) -> list:
        """生成 PostGameplayEffectExecute - GameplayCue 和 Meta 属性处理逻辑
        
        Args:
            class_name: 当前类名
            attributes: 当前类的所有属性
            meta_attrs: 当前类的 Meta 属性
            all_attribute_sets: 所有属性集字典，用于跨集访问查找
        """
        lines = []
        lines.append(f"void {class_name}::PostGameplayEffectExecute(const FGameplayEffectModCallbackData& Data)")
        lines.append("{")
        lines.append("    Super::PostGameplayEffectExecute(Data);")
        lines.append("")
        
        # ========== Meta 属性处理 ==========
        if meta_attrs:
            for attr in meta_attrs:
                lines.append(f"    // ===== Meta 属性: {attr.name} =====")
                lines.append(f"    if (Data.EvaluatedData.Attribute == Get{attr.name}Attribute())")
                lines.append("    {")
                lines.append(f"        // 获取 Meta 属性的值")
                lines.append(f"        const float LocalValue = Get{attr.name}();")
                lines.append("")
                
                # 根据 Meta 属性的配置生成处理逻辑
                if attr.meta_config and attr.meta_config.target_attribute:
                    target_full = attr.meta_config.target_attribute
                    target_set_name = None
                    target = None
                    target_attr_obj = None
                    
                    # 解析 "SetName.AttributeName" 格式
                    if '.' in target_full:
                        target_set_name, target = target_full.split('.', 1)
                        # 验证并查找目标属性对象
                        if all_attribute_sets and target_set_name in all_attribute_sets:
                            for a in all_attribute_sets[target_set_name]:
                                if a.name == target:
                                    target_attr_obj = a
                                    break
                    else:
                        # 兼容旧格式：只有属性名，需要查找属于哪个 AttributeSet
                        target = target_full
                        if all_attribute_sets:
                            for set_name, attrs in all_attribute_sets.items():
                                for a in attrs:
                                    if a.name == target:
                                        target_set_name = set_name
                                        target_attr_obj = a
                                        break
                                if target_set_name:
                                    break
                    
                    # 判断是否跨集访问
                    current_set_name = class_name.replace("UDJ01", "")
                    is_cross_set = target_set_name and target_set_name != current_set_name
                    
                    if is_cross_set:
                        # 跨 AttributeSet 访问
                        target_class = f"UDJ01{target_set_name}"
                        lines.append(f"        // 跨 AttributeSet 访问: 将 Meta 值转发到 {target_class}::{target}")
                        lines.append(f"        if (LocalValue != 0.0f)")
                        lines.append("        {")
                        lines.append(f"            if (UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent())")
                        lines.append("            {")
                        lines.append(f"                if ({target_class}* TargetSet = const_cast<{target_class}*>(ASC->GetSet<{target_class}>()))")
                        lines.append("                {")
                        lines.append(f"                    const float NewValue = TargetSet->Get{target}() + LocalValue;")
                        lines.append(f"                    TargetSet->Set{target}(NewValue);")
                        
                        # 广播事件（如果配置了）
                        if attr.meta_config.broadcast_event and attr.meta_config.event_tag:
                            lines.append("")
                            lines.append(f"                    // 广播事件")
                            lines.append(f"                    FGameplayEventData EventData;")
                            lines.append(f"                    EventData.EventMagnitude = FMath::Abs(LocalValue);")
                            lines.append(f'                    FGameplayTag EventTag = FGameplayTag::RequestGameplayTag(FName("{attr.meta_config.event_tag}"));')
                            lines.append(f"                    ASC->HandleGameplayEvent(EventTag, &EventData);")
                        
                        lines.append("                }")
                        lines.append("            }")
                        lines.append("        }")
                    else:
                        # 同一 AttributeSet 内访问
                        lines.append(f"        // 将 Meta 值转发到目标属性: {target}")
                        lines.append(f"        if (LocalValue != 0.0f)")
                        lines.append("        {")
                        lines.append(f"            const float NewValue = Get{target}() + LocalValue;")
                        lines.append(f"            Set{target}(NewValue);")
                        
                        # 广播事件（如果配置了）
                        if attr.meta_config.broadcast_event and attr.meta_config.event_tag:
                            lines.append("")
                            lines.append(f"            // 广播事件")
                            lines.append(f"            if (UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent())")
                            lines.append("            {")
                            lines.append(f"                FGameplayEventData EventData;")
                            lines.append(f"                EventData.EventMagnitude = FMath::Abs(LocalValue);")
                            lines.append(f'                FGameplayTag EventTag = FGameplayTag::RequestGameplayTag(FName("{attr.meta_config.event_tag}"));')
                            lines.append(f"                ASC->HandleGameplayEvent(EventTag, &EventData);")
                            lines.append("            }")
                        
                        lines.append("        }")
                else:
                    # 无配置，生成注释模板
                    lines.append(f"        // TODO: 在这里处理 {attr.name} 的逻辑")
                    lines.append(f"        // 示例: 将伤害应用到 Health")
                    lines.append(f"        // if (LocalValue != 0.0f)")
                    lines.append(f"        // {{")
                    lines.append(f"        //     SetHealth(GetHealth() + LocalValue);")
                    lines.append(f"        // }}")
                
                lines.append("")
                lines.append(f"        // 重置 Meta 属性")
                lines.append(f"        Set{attr.name}(0.0f);")
                lines.append("    }")
                lines.append("")
        
        # ========== Cue 处理 ==========
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
            lines.append("        UAbilitySystemComponent* ASC = GetOwningAbilitySystemComponent();")
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
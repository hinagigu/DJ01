#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AngelScript 技能代码生成器
"""

from datetime import datetime
from typing import List, Set
from .data import (
    AbilityDefinition, EffectDefinition, ConditionDefinition,
    DamageConfig, HealConfig, AttributeCapture, TagCondition
)


class AbilityScriptGenerator:
    """AngelScript 技能代码生成器"""
    
    # 伤害类型映射
    DAMAGE_TYPE_MAP = {
        "Physical": 0,
        "Magical": 1,
        "Pure": 2
    }
    
    # 属性到 AttributeSet 的映射
    ATTRIBUTE_SET_MAP = {
        # UDJ01ResourceSet 中的属性
        "Health": ("UDJ01ResourceSet", "Health"),
        "MaxHealth": ("UDJ01ResourceSet", "TotalMaxHealth"),  # 使用 GetTotalMaxHealth() 方法
        "Mana": ("UDJ01ResourceSet", "Mana"),
        "MaxMana": ("UDJ01ResourceSet", "TotalMaxMana"),
        
        # UDJ01StatSet 中的属性 - 使用 GetTotal* 方法
        "AttackDamage": ("UDJ01StatSet", "TotalAttackPower"),
        "AttackPower": ("UDJ01StatSet", "TotalAttackPower"),
        "AbilityPower": ("UDJ01StatSet", "TotalMagicPower"),
        "MagicPower": ("UDJ01StatSet", "TotalMagicPower"),
        "Defense": ("UDJ01StatSet", "TotalDefense"),
        "MagicDefense": ("UDJ01StatSet", "TotalMagicDefense"),
        "CriticalRate": ("UDJ01StatSet", "TotalCriticalRate"),
        "CriticalDamage": ("UDJ01StatSet", "TotalCriticalDamage"),
        "AttackSpeed": ("UDJ01StatSet", "TotalAttackSpeed"),
    }
    
    @staticmethod
    def generate(ability: AbilityDefinition) -> str:
        """生成完整的 AngelScript 技能类"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lines = []
        
        # 文件头注释
        lines.append(f"// ============================================================")
        lines.append(f"// UGA_{ability.name}")
        lines.append(f"// {ability.display_name}")
        lines.append(f"// 自动生成 - 请勿手动修改")
        lines.append(f"// 生成时间: {timestamp}")
        lines.append(f"// ============================================================")
        lines.append("")
        
        # 类定义
        lines.append(f"class UGA_{ability.name} : UDJ01GameplayAbility")
        lines.append("{")
        
        # 生成属性配置
        AbilityScriptGenerator._generate_properties(lines, ability)
        
        # 生成 ActivateAbility
        AbilityScriptGenerator._generate_activate_ability(lines, ability)
        
        # 生成各阶段处理函数
        AbilityScriptGenerator._generate_phase_handlers(lines, ability)
        
        # 生成效果执行函数
        AbilityScriptGenerator._generate_effect_executors(lines, ability)
        
        # 生成辅助函数
        AbilityScriptGenerator._generate_helpers(lines, ability)
        
        lines.append("}")
        lines.append("")
        
        return "\n".join(lines)
    
    @staticmethod
    def _generate_properties(lines: List[str], ability: AbilityDefinition):
        """生成技能属性"""
        lines.append("    // ==================== 配置属性 ====================")
        lines.append("")
        
        # 通用 GE 类引用
        lines.append("    // 伤害 GameplayEffect")
        lines.append("    UPROPERTY(EditDefaultsOnly, Category = \"Effects\")")
        lines.append("    TSubclassOf<UGameplayEffect> DamageEffectClass;")
        lines.append("")
        lines.append("    // 治疗 GameplayEffect")
        lines.append("    UPROPERTY(EditDefaultsOnly, Category = \"Effects\")")
        lines.append("    TSubclassOf<UGameplayEffect> HealEffectClass;")
        lines.append("")
        
        # 收集需要的 ApplyEffect GE 类
        apply_effects = set()
        for effect in ability.effects:
            if effect.apply_effect_config:
                apply_effects.add(effect.apply_effect_config.effect_class)
        
        # 为每个需要应用的效果生成 GE 类属性
        for ge_name in apply_effects:
            lines.append(f"    // {ge_name} GameplayEffect")
            lines.append(f"    UPROPERTY(EditDefaultsOnly, Category = \"Effects\")")
            lines.append(f"    TSubclassOf<UGameplayEffect> {ge_name}Class;")
            lines.append("")
        
        # 为每个效果生成可配置数值
        for effect in ability.effects:
            lines.append(f"    // ---------- {effect.name} 配置 ----------")
            
            if effect.damage_config:
                prefix = f"{effect.name}_"
                lines.append(f"    UPROPERTY(EditDefaultsOnly, Category = \"Effects|{effect.name}\")")
                lines.append(f"    float {prefix}BaseDamage = {effect.damage_config.base_damage}f;")
                
                for scaling in effect.damage_config.scaling_ratios:
                    lines.append(f"    UPROPERTY(EditDefaultsOnly, Category = \"Effects|{effect.name}\")")
                    lines.append(f"    float {prefix}{scaling.attr}Ratio = {scaling.ratio}f;")
                lines.append("")
            
            if effect.heal_config:
                prefix = f"{effect.name}_"
                lines.append(f"    UPROPERTY(EditDefaultsOnly, Category = \"Effects|{effect.name}\")")
                lines.append(f"    float {prefix}BaseHeal = {effect.heal_config.base_heal}f;")
                
                for scaling in effect.heal_config.scaling_ratios:
                    lines.append(f"    UPROPERTY(EditDefaultsOnly, Category = \"Effects|{effect.name}\")")
                    lines.append(f"    float {prefix}{scaling.attr}Ratio = {scaling.ratio}f;")
                lines.append("")
        
        lines.append("")
    
    @staticmethod
    def _generate_activate_ability(lines: List[str], ability: AbilityDefinition):
        """生成 ActivateAbility 函数"""
        lines.append("    // ==================== 技能激活 ====================")
        lines.append("")
        lines.append("    UFUNCTION(BlueprintOverride)")
        lines.append("    void ActivateAbility()")
        lines.append("    {")
        
        # 基础检查
        lines.append("        // 检查是否可以激活")
        lines.append("        if (!CommitAbility())")
        lines.append("        {")
        lines.append("            EndAbility();")
        lines.append("            return;")
        lines.append("        }")
        lines.append("")
        
        # OnActivate 阶段
        on_activate_effects = [e for e in ability.effects if e.phase == "OnActivate"]
        if on_activate_effects:
            lines.append("        // OnActivate 阶段效果")
            lines.append("        ExecuteOnActivateEffects();")
            lines.append("")
        
        # OnCommit 阶段
        on_commit_effects = [e for e in ability.effects if e.phase == "OnCommit"]
        if on_commit_effects:
            lines.append("        // OnCommit 阶段效果")
            lines.append("        ExecuteOnCommitEffects();")
            lines.append("")
        
        # 检查是否有 OnAnimEvent 效果
        on_anim_effects = [e for e in ability.effects if e.phase == "OnAnimEvent"]
        if on_anim_effects:
            lines.append("        // 有动画事件效果，等待动画完成")
            lines.append("        // TODO: 播放动画并绑定事件")
        else:
            # 没有动画事件，直接结束
            on_end_effects = [e for e in ability.effects if e.phase == "OnEnd"]
            if on_end_effects:
                lines.append("        // OnEnd 阶段效果")
                lines.append("        ExecuteOnEndEffects();")
            lines.append("        EndAbility();")
        
        lines.append("    }")
        lines.append("")
    
    @staticmethod
    def _generate_phase_handlers(lines: List[str], ability: AbilityDefinition):
        """生成各阶段处理函数"""
        
        # OnActivate
        on_activate_effects = [e for e in ability.effects if e.phase == "OnActivate"]
        if on_activate_effects:
            lines.append("    // OnActivate 阶段")
            lines.append("    void ExecuteOnActivateEffects()")
            lines.append("    {")
            for effect in on_activate_effects:
                lines.append(f"        Execute_{effect.name}();")
            lines.append("    }")
            lines.append("")
        
        # OnCommit
        on_commit_effects = [e for e in ability.effects if e.phase == "OnCommit"]
        if on_commit_effects:
            lines.append("    // OnCommit 阶段")
            lines.append("    void ExecuteOnCommitEffects()")
            lines.append("    {")
            for effect in on_commit_effects:
                lines.append(f"        Execute_{effect.name}();")
            lines.append("    }")
            lines.append("")
        
        # OnAnimEvent - 按 EventTag 分组
        on_anim_effects = [e for e in ability.effects if e.phase == "OnAnimEvent"]
        if on_anim_effects:
            # 收集所有唯一的 EventTag
            event_tags: Set[str] = set()
            for effect in on_anim_effects:
                if effect.event_tag:
                    event_tags.add(effect.event_tag)
            
            lines.append("    // OnAnimEvent 处理")
            lines.append("    void HandleAnimEvent(FGameplayTag EventTag)")
            lines.append("    {")
            
            for tag in event_tags:
                tag_var = tag.replace(".", "_")
                effects_for_tag = [e for e in on_anim_effects if e.event_tag == tag]
                lines.append(f"        if (EventTag.MatchesTag(FGameplayTag::RequestGameplayTag(n\"{tag}\")))")
                lines.append("        {")
                for effect in effects_for_tag:
                    lines.append(f"            Execute_{effect.name}();")
                lines.append("        }")
            
            lines.append("    }")
            lines.append("")
        
        # OnEnd
        on_end_effects = [e for e in ability.effects if e.phase == "OnEnd"]
        if on_end_effects:
            lines.append("    // OnEnd 阶段")
            lines.append("    void ExecuteOnEndEffects()")
            lines.append("    {")
            for effect in on_end_effects:
                lines.append(f"        Execute_{effect.name}();")
            lines.append("    }")
            lines.append("")
            
            lines.append("    UFUNCTION(BlueprintOverride)")
            lines.append("    void OnEndAbility(bool bWasCancelled)")
            lines.append("    {")
            lines.append("        if (!bWasCancelled)")
            lines.append("        {")
            lines.append("            ExecuteOnEndEffects();")
            lines.append("        }")
            lines.append("    }")
            lines.append("")
    
    @staticmethod
    def _generate_effect_executors(lines: List[str], ability: AbilityDefinition):
        """生成效果执行函数"""
        lines.append("    // ==================== 效果执行器 ====================")
        lines.append("")
        
        for effect in ability.effects:
            lines.append(f"    // {effect.name}")
            lines.append(f"    void Execute_{effect.name}()")
            lines.append("    {")
            
            # 获取 ASC
            lines.append("        UAbilitySystemComponent ASC = GetAbilitySystemComponentFromActorInfo();")
            lines.append("        if (!IsValid(ASC)) return;")
            lines.append("")
            
            # 生成条件检查和变量
            AbilityScriptGenerator._generate_condition_code(lines, effect)
            
            # 根据效果类型生成执行代码
            if effect.effect_type == "Damage" and effect.damage_config:
                AbilityScriptGenerator._generate_damage_execution(lines, effect)
            elif effect.effect_type == "Heal" and effect.heal_config:
                AbilityScriptGenerator._generate_heal_execution(lines, effect)
            elif effect.effect_type == "ApplyEffect" and effect.apply_effect_config:
                AbilityScriptGenerator._generate_apply_effect_execution(lines, effect)
            
            lines.append("    }")
            lines.append("")
    
    @staticmethod
    def _generate_condition_code(lines: List[str], effect: EffectDefinition):
        """生成条件检查代码"""
        condition = effect.condition
        
        # 隐式变量初始化
        if effect.effect_type == "Damage":
            lines.append("        float DamageMultiplier = 1.0f;")
        elif effect.effect_type == "Heal":
            lines.append("        float HealMultiplier = 1.0f;")
        
        # 属性捕获
        if condition.captures:
            lines.append("")
            lines.append("        // 捕获属性")
            for cap in condition.captures:
                var_name = f"{cap.attr}_{cap.source}Value"
                AbilityScriptGenerator._generate_attribute_capture(lines, cap, var_name)
        
        # Tag 检查
        if condition.tag_conditions:
            lines.append("")
            lines.append("        // Tag 状态检查")
            for tag_cond in condition.tag_conditions:
                var_name = f"b{tag_cond.source}_{tag_cond.tag.replace('.', '_')}"
                AbilityScriptGenerator._generate_tag_check(lines, tag_cond, var_name)
        
        # 自定义条件代码 - 需要做语法转换
        if condition.code:
            lines.append("")
            lines.append("        // 条件逻辑")
            # 将 JSON 中的代码转换为 AngelScript 格式
            code_lines = condition.code.strip().split('\n')
            for code_line in code_lines:
                stripped = code_line.strip()
                if stripped:
                    # 替换 FMath:: 为 Math::
                    stripped = stripped.replace("FMath::", "Math::")
                    lines.append(f"        {stripped}")
        
        lines.append("")
    
    @staticmethod
    def _generate_attribute_capture(lines: List[str], cap: AttributeCapture, var_name: str):
        """生成属性捕获代码"""
        # 查找正确的 AttributeSet 和方法名
        attr_key = cap.attr
        if attr_key in AbilityScriptGenerator.ATTRIBUTE_SET_MAP:
            attr_class, method_name = AbilityScriptGenerator.ATTRIBUTE_SET_MAP[attr_key]
        else:
            # 默认使用 StatSet，直接使用属性名
            attr_class = "UDJ01StatSet"
            method_name = f"Total{cap.attr}"
        
        lines.append(f"        float {var_name} = 0.f;")
        
        if cap.layer == "Total" or cap.layer == "Current":
            # 使用 GetAttributeSet 和 GetTotal* 方法
            lines.append(f"        {{")
            if cap.source == "Source":
                # 从自身 ASC 获取
                lines.append(f"            const {attr_class} AttrSet = Cast<{attr_class}>(ASC.GetAttributeSet({attr_class}::StaticClass()));")
                lines.append(f"            if (IsValid(AttrSet))")
                lines.append(f"            {{")
                lines.append(f"                {var_name} = AttrSet.Get{method_name}();")
                lines.append(f"            }}")
            else:
                # TODO: 从目标获取属性 - 需要目标系统实现
                lines.append(f"            // TODO: 从目标获取属性值")
                lines.append(f"            // 需要获取目标的 ASC 并读取属性")
            lines.append(f"        }}")
        else:
            lines.append(f"        // TODO: Capture {cap.layer} layer (Base, Flat, or Percent)")
    
    @staticmethod
    def _generate_tag_check(lines: List[str], tag_cond: TagCondition, var_name: str):
        """生成 Tag 检查代码"""
        # 使用 FGameplayTag::RequestGameplayTag 获取 Tag
        tag_literal = tag_cond.tag
        if tag_cond.source == "Source":
            lines.append(f"        bool {var_name} = ASC.GetGameplayTagCount(FGameplayTag::RequestGameplayTag(n\"{tag_literal}\")) > 0;")
        else:
            lines.append(f"        bool {var_name} = false; // TODO: 检查目标的 {tag_literal} Tag")
    
    @staticmethod
    def _generate_damage_execution(lines: List[str], effect: EffectDefinition):
        """生成伤害执行代码"""
        config = effect.damage_config
        prefix = f"{effect.name}_"
        damage_type = AbilityScriptGenerator.DAMAGE_TYPE_MAP.get(config.damage_type, 0)
        
        lines.append("        // 计算原始伤害")
        lines.append(f"        float RawDamage = {prefix}BaseDamage;")
        
        # 添加属性缩放 - 使用 GetAttributeSet 获取正确的值
        for scaling in config.scaling_ratios:
            attr_key = scaling.attr
            if attr_key in AbilityScriptGenerator.ATTRIBUTE_SET_MAP:
                attr_class, method_name = AbilityScriptGenerator.ATTRIBUTE_SET_MAP[attr_key]
            else:
                attr_class = "UDJ01StatSet"
                method_name = f"Total{scaling.attr}"
            
            lines.append(f"        // + {scaling.attr} * {scaling.ratio}")
            lines.append(f"        {{")
            lines.append(f"            const {attr_class} StatSet = Cast<{attr_class}>(ASC.GetAttributeSet({attr_class}::StaticClass()));")
            lines.append(f"            if (IsValid(StatSet))")
            lines.append(f"            {{")
            lines.append(f"                RawDamage += StatSet.Get{method_name}() * {prefix}{scaling.attr}Ratio;")
            lines.append(f"            }}")
            lines.append(f"        }}")
        
        lines.append("")
        lines.append("        // 应用伤害倍率")
        lines.append("        RawDamage *= DamageMultiplier;")
        lines.append("")
        lines.append("        // 创建 GE Spec 并设置 SetByCaller")
        lines.append("        if (IsValid(DamageEffectClass) && RawDamage > 0.f)")
        lines.append("        {")
        lines.append("            FGameplayEffectSpecHandle SpecHandle = MakeOutgoingGameplayEffectSpec(DamageEffectClass, GetAbilityLevel());")
        lines.append("")
        lines.append("            // 使用 AbilitySystem 命名空间设置 SetByCaller")
        lines.append("            FGameplayTag DamageRawTag = FGameplayTag::RequestGameplayTag(n\"SetByCaller.Damage.Raw\");")
        lines.append("            FGameplayTag DamageTypeTag = FGameplayTag::RequestGameplayTag(n\"SetByCaller.Damage.Type\");")
        lines.append("            SpecHandle = AbilitySystem::AssignTagSetByCallerMagnitude(SpecHandle, DamageRawTag, RawDamage);")
        lines.append(f"            SpecHandle = AbilitySystem::AssignTagSetByCallerMagnitude(SpecHandle, DamageTypeTag, {damage_type}.f);")
        lines.append("")
        lines.append("            // 应用到自身 (TODO: 改为应用到目标)")
        lines.append("            ApplyGameplayEffectSpecToOwner(SpecHandle);")
        lines.append("        }")
    
    @staticmethod
    def _generate_heal_execution(lines: List[str], effect: EffectDefinition):
        """生成治疗执行代码"""
        config = effect.heal_config
        prefix = f"{effect.name}_"
        
        lines.append("        // 计算原始治疗量")
        lines.append(f"        float RawHeal = {prefix}BaseHeal;")
        
        # 添加属性缩放 - 使用 GetAttributeSet 获取正确的值
        for scaling in config.scaling_ratios:
            attr_key = scaling.attr
            if attr_key in AbilityScriptGenerator.ATTRIBUTE_SET_MAP:
                attr_class, method_name = AbilityScriptGenerator.ATTRIBUTE_SET_MAP[attr_key]
            else:
                attr_class = "UDJ01StatSet"
                method_name = f"Total{scaling.attr}"
            
            lines.append(f"        // + {scaling.attr} * {scaling.ratio}")
            lines.append(f"        {{")
            lines.append(f"            const {attr_class} StatSet = Cast<{attr_class}>(ASC.GetAttributeSet({attr_class}::StaticClass()));")
            lines.append(f"            if (IsValid(StatSet))")
            lines.append(f"            {{")
            lines.append(f"                RawHeal += StatSet.Get{method_name}() * {prefix}{scaling.attr}Ratio;")
            lines.append(f"            }}")
            lines.append(f"        }}")
        
        lines.append("")
        lines.append("        // 应用治疗倍率")
        lines.append("        RawHeal *= HealMultiplier;")
        lines.append("")
        lines.append("        // 创建 GE Spec 并设置 SetByCaller")
        lines.append("        if (IsValid(HealEffectClass) && RawHeal > 0.f)")
        lines.append("        {")
        lines.append("            FGameplayEffectSpecHandle SpecHandle = MakeOutgoingGameplayEffectSpec(HealEffectClass, GetAbilityLevel());")
        lines.append("")
        lines.append("            // 使用 AbilitySystem 命名空间设置 SetByCaller")
        lines.append("            FGameplayTag HealRawTag = FGameplayTag::RequestGameplayTag(n\"SetByCaller.Heal.Raw\");")
        lines.append("            SpecHandle = AbilitySystem::AssignTagSetByCallerMagnitude(SpecHandle, HealRawTag, RawHeal);")
        lines.append("")
        lines.append("            // 应用到自身")
        lines.append("            ApplyGameplayEffectSpecToOwner(SpecHandle);")
        lines.append("        }")
    
    @staticmethod
    def _generate_apply_effect_execution(lines: List[str], effect: EffectDefinition):
        """生成应用效果代码"""
        config = effect.apply_effect_config
        ge_var_name = f"{config.effect_class}Class"
        
        lines.append(f"        // 应用效果: {config.effect_class}")
        lines.append(f"        if (IsValid({ge_var_name}))")
        lines.append("        {")
        lines.append(f"            FGameplayEffectSpecHandle SpecHandle = MakeOutgoingGameplayEffectSpec({ge_var_name}, GetAbilityLevel());")
        lines.append(f"            ApplyGameplayEffectSpecToOwner(SpecHandle);")
        lines.append("        }")
    
    @staticmethod
    def _generate_helpers(lines: List[str], ability: AbilityDefinition):
        """生成辅助函数"""
        lines.append("    // ==================== 辅助函数 ====================")
        lines.append("")
        
        # 获取目标的辅助函数
        lines.append("    // 获取当前目标 (需要根据项目实际情况实现)")
        lines.append("    AActor GetCurrentTarget()")
        lines.append("    {")
        lines.append("        // TODO: 实现目标获取逻辑")
        lines.append("        return nullptr;")
        lines.append("    }")
        lines.append("")
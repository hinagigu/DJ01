# UDJ01HealEffect

**继承自**: `UDJ01AbilityEffect`

UDJ01HealEffect

治疗效果 - 计算并应用治疗
支持基础治疗 + 属性缩放

## 属性

### BaseHeal
- **类型**: `float32`

### AttributeScalings
- **类型**: `TArray<FDJ01AttributeScaling>`

### bHealSelf
- **类型**: `bool`

### HealGameplayEffect
- **类型**: `TSubclassOf<UGameplayEffect>`

## 方法

### CalculateRawHeal
```angelscript
float32 CalculateRawHeal(FDJ01EffectContext Context)
```
计算最终的原始治疗量


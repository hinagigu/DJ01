# UDJ01DamageEffect

**继承自**: `UDJ01AbilityEffect`

UDJ01DamageEffect

伤害效果 - 计算并应用伤害
支持基础伤害 + 属性缩放

## 属性

### BaseDamage
- **类型**: `float32`

### DamageType
- **类型**: `EDJ01DamageType`

### AttributeScalings
- **类型**: `TArray<FDJ01AttributeScaling>`

### DamageGameplayEffect
- **类型**: `TSubclassOf<UGameplayEffect>`

## 方法

### CalculateRawDamage
```angelscript
float32 CalculateRawDamage(FDJ01EffectContext Context)
```
计算最终的原始伤害


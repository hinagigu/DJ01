# FDJ01EffectContext

效果执行上下文
包含效果执行所需的所有信息

## 属性

### InstigatorASC
- **类型**: `UAbilitySystemComponent`
- **描述**: 拥有此技能的 ASC（施法者）

### TargetASCs
- **类型**: `TArray<TObjectPtr<UAbilitySystemComponent>>`
- **描述**: 目标 ASC 列表

### EventTag
- **类型**: `FGameplayTag`
- **描述**: 触发此效果的事件 Tag

### AbilityLevel
- **类型**: `int`
- **描述**: 技能等级

### EventMagnitude
- **类型**: `float32`
- **描述**: 事件附加数值（可选）

### SourceAbility
- **类型**: `UGameplayAbility`
- **描述**: 技能实例（可选，用于访问技能数据）

## 方法

### opAssign
```angelscript
FDJ01EffectContext& opAssign(FDJ01EffectContext Other)
```


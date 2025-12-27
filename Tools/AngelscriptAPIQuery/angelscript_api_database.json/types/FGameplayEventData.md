# FGameplayEventData

Metadata for a tag-based Gameplay Event, that can activate other abilities or run ability-specific logic

## 属性

### EventTag
- **类型**: `FGameplayTag`

### Instigator
- **类型**: `const AActor`

### Target
- **类型**: `const AActor`

### OptionalObject
- **类型**: `const UObject`

### OptionalObject2
- **类型**: `const UObject`

### ContextHandle
- **类型**: `FGameplayEffectContextHandle`

### InstigatorTags
- **类型**: `FGameplayTagContainer`

### TargetTags
- **类型**: `FGameplayTagContainer`

### EventMagnitude
- **类型**: `float32`

### TargetData
- **类型**: `FGameplayAbilityTargetDataHandle`

## 方法

### opAssign
```angelscript
FGameplayEventData& opAssign(FGameplayEventData Other)
```


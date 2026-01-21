# FComboGraphGameplayEffectContainer

Struct defining a list of gameplay effects, a tag, and targeting info

These containers are defined statically in blueprints or assets and then turn into Specs at runtime

## 属性

### TargetGameplayEffectClasses
- **类型**: `TArray<TSubclassOf<UGameplayEffect>>`

### bUseSetByCallerMagnitude
- **类型**: `bool`

### SetByCallerDataTag
- **类型**: `FGameplayTag`

### SetByCallerMagnitude
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FComboGraphGameplayEffectContainer& opAssign(FComboGraphGameplayEffectContainer Other)
```


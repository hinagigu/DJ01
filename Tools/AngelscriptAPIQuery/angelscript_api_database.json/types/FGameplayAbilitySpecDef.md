# FGameplayAbilitySpecDef

This is data that can be used to create an FGameplayAbilitySpec. Has some data that is only relevant when granted by a GameplayEffect

## 属性

### Ability
- **类型**: `TSubclassOf<UGameplayAbility>`
- **描述**: What ability to grant

### LevelScalableFloat
- **类型**: `FScalableFloat`
- **描述**: What level to grant this ability at

### InputID
- **类型**: `int`
- **描述**: Input ID to bind this ability to

### RemovalPolicy
- **类型**: `EGameplayEffectGrantedAbilityRemovePolicy`
- **描述**: What will remove this ability later

## 方法

### opAssign
```angelscript
FGameplayAbilitySpecDef& opAssign(FGameplayAbilitySpecDef Other)
```


# FGameplayAbilitySpecConfig

Options on how to configure a GameplayAbilitySpec to grant an Actor

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
FGameplayAbilitySpecConfig& opAssign(FGameplayAbilitySpecConfig Other)
```


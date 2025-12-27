# FGameplayEffectRemovalInfo

Data struct for containing information pertinent to GameplayEffects as they are removed

## 属性

### bPrematureRemoval
- **类型**: `bool`
- **描述**: True when the gameplay effect's duration has not expired, meaning the gameplay effect is being forcefully removed.

### StackCount
- **类型**: `int`
- **描述**: Number of Stacks this gameplay effect had before it was removed.

### EffectContext
- **类型**: `FGameplayEffectContextHandle`
- **描述**: Actor this gameplay effect was targeting.

## 方法

### opAssign
```angelscript
FGameplayEffectRemovalInfo& opAssign(FGameplayEffectRemovalInfo Other)
```


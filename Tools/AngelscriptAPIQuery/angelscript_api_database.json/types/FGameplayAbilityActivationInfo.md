# FGameplayAbilityActivationInfo

FGameplayAbilityActivationInfo

Data tied to a specific activation of an ability.
        -Tell us whether we are the authority, if we are predicting, confirmed, etc.
        -Holds current and previous PredictionKey
        -Generally not meant to be subclassed in projects.
        -Passed around by value since the struct is small.

## 属性

### ActivationMode
- **类型**: `EGameplayAbilityActivationMode`
- **描述**: Activation status of this ability

## 方法

### opAssign
```angelscript
FGameplayAbilityActivationInfo& opAssign(FGameplayAbilityActivationInfo Other)
```


# FGameplayEffectSpec

GameplayEffect Specification. Tells us:
    -What UGameplayEffect (const data)
    -What Level
 -Who instigated

FGameplayEffectSpec is modifiable. We start with initial conditions and modifications be applied to it. In this sense, it is stateful/mutable but it
is still distinct from an FActiveGameplayEffect which in an applied instance of an FGameplayEffectSpec.

## 方法

### opAssign
```angelscript
FGameplayEffectSpec& opAssign(FGameplayEffectSpec Other)
```


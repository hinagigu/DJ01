# FGameplayEffectSpecHandle

Allows blueprints to generate a GameplayEffectSpec once and then reference it by handle, to apply it multiple times/multiple targets.

## 方法

### GetSpec
```angelscript
FGameplayEffectSpec& GetSpec()
```

### IsValid
```angelscript
bool IsValid()
```

### opAssign
```angelscript
FGameplayEffectSpecHandle& opAssign(FGameplayEffectSpecHandle Other)
```


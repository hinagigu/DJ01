# FGameplayEffectCreationData

## 属性

### MenuPath
- **类型**: `FString`
- **描述**: Where to show this in the menu. Use "|" for sub categories. E.g, "Status|Hard|Stun|Root".

### BaseName
- **类型**: `FString`
- **描述**: The default BaseName of the new asset. E.g "Damage" -> GE_Damage or GE_HeroName_AbilityName_Damage

### ParentGameplayEffect
- **类型**: `TSubclassOf<UGameplayEffect>`

## 方法

### opAssign
```angelscript
FGameplayEffectCreationData& opAssign(FGameplayEffectCreationData Other)
```


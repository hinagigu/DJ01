# FGameplayModifierEvaluatedData

Data that describes what happened in an attribute modification. This is passed to ability set callbacks

## 方法

### GetAttribute
```angelscript
FGameplayAttribute GetAttribute()
```

### GetHandle
```angelscript
FActiveGameplayEffectHandle GetHandle()
```

### GetIsValid
```angelscript
bool GetIsValid()
```

### GetMagnitude
```angelscript
float32 GetMagnitude()
```

### GetModifierOp
```angelscript
EGameplayModOp GetModifierOp()
```

### SetAttribute
```angelscript
void SetAttribute(FGameplayAttribute NewValue)
```

### SetHandle
```angelscript
void SetHandle(FActiveGameplayEffectHandle NewValue)
```

### SetIsValid
```angelscript
void SetIsValid(bool NewValue)
```

### SetMagnitude
```angelscript
void SetMagnitude(float32 NewValue)
```

### SetModifierOp
```angelscript
void SetModifierOp(EGameplayModOp NewValue)
```

### ToSimpleString
```angelscript
FString ToSimpleString()
```

### opAssign
```angelscript
FGameplayModifierEvaluatedData& opAssign(FGameplayModifierEvaluatedData Other)
```


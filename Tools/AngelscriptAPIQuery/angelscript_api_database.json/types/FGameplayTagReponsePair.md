# FGameplayTagReponsePair

## 属性

### Tag
- **类型**: `FGameplayTag`
- **描述**: Tag that triggers this response

### ResponseGameplayEffects
- **类型**: `TArray<TSubclassOf<UGameplayEffect>>`
- **描述**: The GameplayEffects to apply in reponse to the tag

### SoftCountCap
- **类型**: `int`
- **描述**: The max "count" this response can achieve. This will not prevent counts from being applied, but will be used when calculating the net count of a tag. 0=no cap.

## 方法

### opAssign
```angelscript
FGameplayTagReponsePair& opAssign(FGameplayTagReponsePair Other)
```


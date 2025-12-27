# FGameplayAbilityTargetData_ActorArray

Target data with a source location and a list of targeted actors, makes sense for AOE attacks

## 属性

### SourceLocation
- **类型**: `FGameplayAbilityTargetingLocationInfo`

### TargetActorArray
- **类型**: `TArray<TWeakObjectPtr<AActor>>`
- **描述**: Rather than targeting a single point, this type of targeting selects multiple actors.

## 方法

### opAssign
```angelscript
FGameplayAbilityTargetData_ActorArray& opAssign(FGameplayAbilityTargetData_ActorArray Other)
```


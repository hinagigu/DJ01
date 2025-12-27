# FGameplayAbilityTargetingLocationInfo

Structure that stores a location in one of several different formats

## 属性

### LocationType
- **类型**: `EGameplayAbilityTargetingLocationType`
- **描述**: Type of location used - will determine what data is transmitted over the network and what fields are used when calculating position.

### LiteralTransform
- **类型**: `FTransform`
- **描述**: A literal world transform can be used, if one has been calculated outside of the actor using the ability.

### SourceActor
- **类型**: `AActor`
- **描述**: A source actor is needed for Actor-based targeting, but not for Socket-based targeting.

### SourceComponent
- **类型**: `UMeshComponent`
- **描述**: Socket-based targeting requires a skeletal mesh component to check for the named socket.

### SourceAbility
- **类型**: `UGameplayAbility`
- **描述**: Ability that will be using the targeting data

### SourceSocketName
- **类型**: `FName`
- **描述**: If SourceComponent is valid, this is the name of the socket transform that will be used. If no Socket is provided, SourceComponent's transform will be used.

## 方法

### opAssign
```angelscript
FGameplayAbilityTargetingLocationInfo& opAssign(FGameplayAbilityTargetingLocationInfo Other)
```


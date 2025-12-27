# AGameplayAbilityWorldReticle

**继承自**: `AActor`

Reticles allow targeting to be visualized. Tasks can spawn these. Artists/designers can create BPs for these.

## 属性

### Parameters
- **类型**: `FWorldReticleParameters`

### bFaceOwnerFlat
- **类型**: `bool`

### bSnapToTargetedActor
- **类型**: `bool`

### bIsTargetValid
- **类型**: `bool`
- **描述**: This indicates whether or not the targeting actor considers the current target to be valid. Defaults to true.

### bIsTargetAnActor
- **类型**: `bool`
- **描述**: This indicates whether or not the targeting reticle is pointed at an actor. Defaults to false.

### PrimaryPC
- **类型**: `APlayerController`
- **描述**: This is used in the process of determining whether we should replicate to a specific client.

### TargetingActor
- **类型**: `AGameplayAbilityTargetActor`
- **描述**: In the future, we may want to grab things like sockets off of this.

## 方法

### FaceTowardSource
```angelscript
void FaceTowardSource(bool bFaceIn2D)
```

### OnParametersInitialized
```angelscript
void OnParametersInitialized()
```

### OnTargetingAnActor
```angelscript
void OnTargetingAnActor(bool bNewValue)
```
Called whenever bIsTargetAnActor changes value.

### OnValidTargetChanged
```angelscript
void OnValidTargetChanged(bool bNewValue)
```
Called whenever bIsTargetValid changes value.

### SetReticleMaterialParamFloat
```angelscript
void SetReticleMaterialParamFloat(FName ParamName, float value)
```

### SetReticleMaterialParamVector
```angelscript
void SetReticleMaterialParamVector(FName ParamName, FVector value)
```


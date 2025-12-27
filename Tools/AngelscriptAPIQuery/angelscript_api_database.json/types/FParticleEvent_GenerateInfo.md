# FParticleEvent_GenerateInfo

## 属性

### Type
- **类型**: `EParticleEventType`
- **描述**: The type of event.

### Frequency
- **类型**: `int`
- **描述**: How often to trigger the event (<= 1 means EVERY time).

### ParticleFrequency
- **类型**: `int`
- **描述**: Only fire the first time (collision only).

### CustomName
- **类型**: `FName`
- **描述**: Should the event tag with a custom name? Leave blank for the default.

### ParticleModuleEventsToSendToGame
- **类型**: `TArray<TObjectPtr<UParticleModuleEventSendToGame>>`
- **描述**: The events we want to fire off when this event has been generated

### FirstTimeOnly
- **类型**: `bool`

### LastTimeOnly
- **类型**: `bool`

### UseReflectedImpactVector
- **类型**: `bool`

### bUseOrbitOffset
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FParticleEvent_GenerateInfo& opAssign(FParticleEvent_GenerateInfo Other)
```


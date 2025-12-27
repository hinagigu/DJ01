# FRigUnit_SphereTraceByTraceChannel

Sweeps a sphere against the world and return the first blocking hit using a specific channel. Target objects can have different object types, but they need to have the same trace channel set to "block" in their collision response settings.
You can create custom trace channels in Project Setting - Collision.

## 属性

### Start
- **类型**: `FVector`

### End
- **类型**: `FVector`

### TraceChannel
- **类型**: `ETraceTypeQuery`

### Radius
- **类型**: `float32`

### bHit
- **类型**: `bool`
- **描述**: Returns true if there was a hit

### HitLocation
- **类型**: `FVector`
- **描述**: Hit location in rig / global Space

### HitNormal
- **类型**: `FVector`
- **描述**: Hit normal in rig / global Space

## 方法

### opAssign
```angelscript
FRigUnit_SphereTraceByTraceChannel& opAssign(FRigUnit_SphereTraceByTraceChannel Other)
```


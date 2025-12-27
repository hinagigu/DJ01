# FRigUnit_SphereTraceWorld

Sweeps a sphere against the world and return the first blocking hit using a specific channel

## 属性

### Start
- **类型**: `FVector`

### End
- **类型**: `FVector`

### Channel
- **类型**: `ECollisionChannel`

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
FRigUnit_SphereTraceWorld& opAssign(FRigUnit_SphereTraceWorld Other)
```


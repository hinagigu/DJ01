# FRigUnit_SphereTraceByObjectTypes

Sweeps a sphere against the world and return the first blocking hit. The trace is filtered by object types only, the collision response settings are ignored.
You can create custom object types in Project Setting - Collision

## 属性

### Start
- **类型**: `FVector`

### End
- **类型**: `FVector`

### ObjectTypes
- **类型**: `TArray<EObjectTypeQuery>`

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
FRigUnit_SphereTraceByObjectTypes& opAssign(FRigUnit_SphereTraceByObjectTypes Other)
```


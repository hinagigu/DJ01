# FHitResult

Structure containing information about one hit of a trace, such as point of impact and surface normal at that point.

## 属性

### FaceIndex
- **类型**: `int`

### PenetrationDepth
- **类型**: `float32`

### Distance
- **类型**: `float32`

### Time
- **类型**: `float32`

### TraceStart
- **类型**: `FVector`

### TraceEnd
- **类型**: `FVector`

### ImpactNormal
- **类型**: `FVector`

### ImpactPoint
- **类型**: `FVector`

### Location
- **类型**: `FVector`

### Normal
- **类型**: `FVector`

### BoneName
- **类型**: `FName`

## 方法

### GetActor
```angelscript
AActor GetActor()
```

### GetbBlockingHit
```angelscript
bool GetbBlockingHit()
```

### GetbStartPenetrating
```angelscript
bool GetbStartPenetrating()
```

### GetComponent
```angelscript
UPrimitiveComponent GetComponent()
```

### GetPhysMaterial
```angelscript
UPhysicalMaterial GetPhysMaterial()
```

### Reset
```angelscript
void Reset()
```

### SetActor
```angelscript
void SetActor(AActor Actor)
```

### SetbBlockingHit
```angelscript
void SetbBlockingHit(bool bIsBlocking)
```

### SetbStartPenetrating
```angelscript
void SetbStartPenetrating(bool bStartPenetrating)
```

### SetComponent
```angelscript
void SetComponent(UPrimitiveComponent Component)
```

### opAssign
```angelscript
FHitResult& opAssign(FHitResult Other)
```


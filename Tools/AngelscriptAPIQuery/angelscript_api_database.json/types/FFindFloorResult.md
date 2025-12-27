# FFindFloorResult

Data about the floor for walking movement, used by CharacterMovementComponent.

## 属性

### FloorDist
- **类型**: `float32`
- **描述**: The distance to the floor, computed from the swept capsule trace.

### LineDist
- **类型**: `float32`
- **描述**: The distance to the floor, computed from the trace. Only valid if bLineTrace is true.

### HitResult
- **类型**: `FHitResult`
- **描述**: Hit result of the test that found a floor. Includes more specific data about the point of impact and surface normal at that point.

### bBlockingHit
- **类型**: `bool`

### bWalkableFloor
- **类型**: `bool`

### bLineTrace
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FFindFloorResult& opAssign(FFindFloorResult Other)
```


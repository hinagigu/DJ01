# FEnvOverlapData

## 属性

### ExtentX
- **类型**: `float32`
- **描述**: shape parameter for overlap

### ExtentY
- **类型**: `float32`
- **描述**: shape parameter for overlap

### ExtentZ
- **类型**: `float32`
- **描述**: shape parameter for overlap

### ShapeOffset
- **类型**: `FVector`
- **描述**: Offset from the item location at which to test the overlap.  For example, you may need to offset vertically to avoid overlaps with flat ground.

### OverlapChannel
- **类型**: `ECollisionChannel`
- **描述**: geometry trace channel used for overlap

### OverlapShape
- **类型**: `EEnvOverlapShape`
- **描述**: shape used for geometry overlap

### bOnlyBlockingHits
- **类型**: `bool`

### bOverlapComplex
- **类型**: `bool`

### bSkipOverlapQuerier
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FEnvOverlapData& opAssign(FEnvOverlapData Other)
```


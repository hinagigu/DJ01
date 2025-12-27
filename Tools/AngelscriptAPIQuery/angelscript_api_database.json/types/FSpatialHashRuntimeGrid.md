# FSpatialHashRuntimeGrid

Represents a runtime grid (editing)

## 属性

### GridName
- **类型**: `FName`

### CellSize
- **类型**: `int`

### LoadingRange
- **类型**: `float32`

### bBlockOnSlowStreaming
- **类型**: `bool`
- **描述**: Should streaming block in situations where cells aren't getting loaded fast enough.

### Origin
- **类型**: `FVector2D`

### Priority
- **类型**: `int`

### DebugColor
- **类型**: `FLinearColor`

## 方法

### opAssign
```angelscript
FSpatialHashRuntimeGrid& opAssign(FSpatialHashRuntimeGrid Other)
```


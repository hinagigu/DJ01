# FBlendParameter

## 属性

### DisplayName
- **类型**: `FString`

### Min
- **类型**: `float32`
- **描述**: Minimum value for this axis range.

### Max
- **类型**: `float32`
- **描述**: Maximum value for this axis range.

### GridNum
- **类型**: `int`
- **描述**: The number of grid divisions along this axis.

### bSnapToGrid
- **类型**: `bool`
- **描述**: If true then samples will always be snapped to the grid on this axis when added, moved, or the axes are changed.

### bWrapInput
- **类型**: `bool`
- **描述**: If true then the input can go outside the min/max range and the blend space is treated as being cyclic on this axis. If false then input parameters are clamped to the min/max values on this axis.

## 方法

### opAssign
```angelscript
FBlendParameter& opAssign(FBlendParameter Other)
```


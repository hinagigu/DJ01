# FEFitDataflowNode

Fits a value from one range to another

Takes the value num from the range (oldmin, oldmax) and shifts it to the corresponding value in the new range (newmin, newmax). Unlike fit, this function does not clamp values in the given range.

## 属性

### Float
- **类型**: `float32`

### OldMin
- **类型**: `float32`

### OldMax
- **类型**: `float32`

### NewMin
- **类型**: `float32`

### NewMax
- **类型**: `float32`

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FEFitDataflowNode& opAssign(FEFitDataflowNode Other)
```


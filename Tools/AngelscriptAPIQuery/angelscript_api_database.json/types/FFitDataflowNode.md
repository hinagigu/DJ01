# FFitDataflowNode

Fits a value from one range to another
Returns a number between newmin and newmax that is relative to num in the range between oldmin and oldmax.
If the value is outside the old range, it will be clamped to the new range.

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
FFitDataflowNode& opAssign(FFitDataflowNode Other)
```


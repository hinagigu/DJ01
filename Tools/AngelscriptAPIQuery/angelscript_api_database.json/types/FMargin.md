# FMargin

Describes the space around a Widget.

## 属性

### Left
- **类型**: `float32`

### Top
- **类型**: `float32`

### Right
- **类型**: `float32`

### Bottom
- **类型**: `float32`

## 方法

### opMul
```angelscript
FMargin opMul(float32 Scale)
```

### opMul
```angelscript
FMargin opMul(FMargin InScale)
```

### opAdd
```angelscript
FMargin opAdd(FMargin Other)
```

### opSub
```angelscript
FMargin opSub(FMargin Other)
```

### opEquals
```angelscript
bool opEquals(FMargin Other)
```

### GetTopLeft
```angelscript
FVector2D GetTopLeft()
```

### GetDesiredSize
```angelscript
FVector2D GetDesiredSize()
```

### GetTotalSpaceAlongHorizontal
```angelscript
float32 GetTotalSpaceAlongHorizontal()
```

### GetTotalSpaceAlongVertical
```angelscript
float32 GetTotalSpaceAlongVertical()
```

### opAssign
```angelscript
FMargin& opAssign(FMargin Other)
```


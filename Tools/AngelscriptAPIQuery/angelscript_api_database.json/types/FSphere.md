# FSphere

## 属性

### W
- **类型**: `float`

### Center
- **类型**: `FVector`

## 方法

### opAdd
```angelscript
FSphere opAdd(FSphere Other)
```

### opAddAssign
```angelscript
FSphere& opAddAssign(FSphere Other)
```

### Equals
```angelscript
bool Equals(FSphere Sphere, float Tolerance)
```

### IsInside
```angelscript
bool IsInside(FSphere Other, float Tolerance)
```

### IsInside
```angelscript
bool IsInside(FVector In, float Tolerance)
```

### Intersects
```angelscript
bool Intersects(FSphere Other, float Tolerance)
```

### TransformBy
```angelscript
FSphere TransformBy(FTransform M)
```

### GetVolume
```angelscript
float32 GetVolume()
```


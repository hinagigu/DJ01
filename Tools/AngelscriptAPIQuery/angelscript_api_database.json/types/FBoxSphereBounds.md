# FBoxSphereBounds

## 属性

### Origin
- **类型**: `FVector`

### BoxExtent
- **类型**: `FVector`

### SphereRadius
- **类型**: `float`

## 方法

### opAdd
```angelscript
FBoxSphereBounds opAdd(FBoxSphereBounds Other)
```

### opEquals
```angelscript
bool opEquals(FBoxSphereBounds Other)
```

### ComputeSquaredDistanceFromBoxToPoint
```angelscript
float ComputeSquaredDistanceFromBoxToPoint(FVector Point)
```

### GetBox
```angelscript
FBox GetBox()
```

### GetBoxExtrema
```angelscript
FVector GetBoxExtrema(uint Extrema)
```

### GetSphere
```angelscript
FSphere GetSphere()
```

### ExpandBy
```angelscript
FBoxSphereBounds ExpandBy(float ExpandAmount)
```

### TransformBy
```angelscript
FBoxSphereBounds TransformBy(FTransform M)
```

### ToString
```angelscript
FString ToString()
```


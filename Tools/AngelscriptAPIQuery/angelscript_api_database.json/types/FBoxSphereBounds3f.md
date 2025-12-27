# FBoxSphereBounds3f

## 属性

### Origin
- **类型**: `FVector3f`

### BoxExtent
- **类型**: `FVector3f`

### SphereRadius
- **类型**: `float32`

## 方法

### opAdd
```angelscript
FBoxSphereBounds3f opAdd(FBoxSphereBounds3f Other)
```

### opEquals
```angelscript
bool opEquals(FBoxSphereBounds3f Other)
```

### ComputeSquaredDistanceFromBoxToPoint
```angelscript
float32 ComputeSquaredDistanceFromBoxToPoint(FVector3f Point)
```

### GetBox
```angelscript
FBox3f GetBox()
```

### GetBoxExtrema
```angelscript
FVector3f GetBoxExtrema(uint Extrema)
```

### GetSphere
```angelscript
FSphere3f GetSphere()
```

### ExpandBy
```angelscript
FBoxSphereBounds3f ExpandBy(float32 ExpandAmount)
```

### TransformBy
```angelscript
FBoxSphereBounds3f TransformBy(FTransform3f M)
```

### ToString
```angelscript
FString ToString()
```


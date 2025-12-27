# FBox3f

## 属性

### Min
- **类型**: `FVector3f`

### Max
- **类型**: `FVector3f`

## 方法

### opAdd
```angelscript
FBox3f opAdd(FBox3f Other)
```

### opAddAssign
```angelscript
FBox3f& opAddAssign(FBox3f Other)
```

### opEquals
```angelscript
bool opEquals(FBox3f Other)
```

### Intersect
```angelscript
bool Intersect(FBox3f other)
```

### opAdd
```angelscript
FBox3f opAdd(FVector3f Other)
```

### opAddAssign
```angelscript
FBox3f& opAddAssign(FVector3f Other)
```

### opIndex
```angelscript
FVector3f& opIndex(int Index)
```

### GetCenter
```angelscript
FVector3f GetCenter()
```

### GetExtent
```angelscript
FVector3f GetExtent()
```

### GetCenterAndExtents
```angelscript
void GetCenterAndExtents(FVector3f& Center, FVector3f& Extents)
```

### GetClosestPointTo
```angelscript
FVector3f GetClosestPointTo(FVector3f In)
```

### InverseTransformBy
```angelscript
FBox3f InverseTransformBy(FTransform M)
```

### TransformBy
```angelscript
FBox3f TransformBy(FTransform3f M)
```

### IsInside
```angelscript
bool IsInside(FVector3f In)
```

### IsInsideOrOn
```angelscript
bool IsInsideOrOn(FVector3f In)
```

### ToString
```angelscript
FString ToString()
```


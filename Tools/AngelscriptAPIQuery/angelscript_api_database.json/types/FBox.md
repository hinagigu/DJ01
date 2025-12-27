# FBox

## 属性

### Min
- **类型**: `FVector`

### Max
- **类型**: `FVector`

## 方法

### opAdd
```angelscript
FBox opAdd(FBox Other)
```

### opAddAssign
```angelscript
FBox& opAddAssign(FBox Other)
```

### opEquals
```angelscript
bool opEquals(FBox Other)
```

### opAdd
```angelscript
FBox opAdd(FVector Other)
```

### opAddAssign
```angelscript
FBox& opAddAssign(FVector Other)
```

### opIndex
```angelscript
FVector& opIndex(int Index)
```

### GetCenter
```angelscript
FVector GetCenter()
```

### GetExtent
```angelscript
FVector GetExtent()
```

### GetVolume
```angelscript
float GetVolume()
```

### GetCenterAndExtents
```angelscript
void GetCenterAndExtents(FVector& Center, FVector& Extents)
```

### GetClosestPointTo
```angelscript
FVector GetClosestPointTo(FVector In)
```

### InverseTransformBy
```angelscript
FBox InverseTransformBy(FTransform M)
```

### TransformBy
```angelscript
FBox TransformBy(FTransform M)
```

### Equals
```angelscript
bool Equals(FBox Other, float Tolerance)
```

### Intersect
```angelscript
bool Intersect(FBox Other)
```

### IntersectXY
```angelscript
bool IntersectXY(FBox Other)
```

### Overlap
```angelscript
FBox Overlap(FBox Other)
```

### ExpandBy
```angelscript
FBox ExpandBy(float W)
```

### ExpandBy
```angelscript
FBox ExpandBy(FVector V)
```

### ShiftBy
```angelscript
FBox ShiftBy(FVector Offset)
```

### MoveTo
```angelscript
FBox MoveTo(FVector Destination)
```

### IsInside
```angelscript
bool IsInside(FVector In)
```

### IsInsideOrOn
```angelscript
bool IsInsideOrOn(FVector In)
```

### IsInside
```angelscript
bool IsInside(FBox In)
```

### IsInsideXY
```angelscript
bool IsInsideXY(FVector In)
```

### IsInsideOrOnXY
```angelscript
bool IsInsideOrOnXY(FVector In)
```

### IsInsideXY
```angelscript
bool IsInsideXY(FBox In)
```

### ToString
```angelscript
FString ToString()
```


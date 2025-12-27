# FVector2D

## 属性

### X
- **类型**: `float`

### Y
- **类型**: `float`

## 方法

### opAssign
```angelscript
FVector2D& opAssign(FVector2D Other)
```

### opAdd
```angelscript
FVector2D opAdd(FVector2D Other)
```

### opSub
```angelscript
FVector2D opSub(FVector2D Other)
```

### opMul
```angelscript
FVector2D opMul(FVector2D Other)
```

### opDiv
```angelscript
FVector2D opDiv(FVector2D Other)
```

### opMul
```angelscript
FVector2D opMul(float Scale)
```

### opDiv
```angelscript
FVector2D opDiv(float Scale)
```

### opAdd
```angelscript
FVector2D opAdd(float Bias)
```

### opSub
```angelscript
FVector2D opSub(float Bias)
```

### opNeg
```angelscript
FVector2D opNeg()
```

### opMulAssign
```angelscript
FVector2D opMulAssign(float Scale)
```

### opDivAssign
```angelscript
FVector2D opDivAssign(float Scale)
```

### opMulAssign
```angelscript
FVector2D opMulAssign(FVector2D Other)
```

### opDivAssign
```angelscript
FVector2D opDivAssign(FVector2D Other)
```

### opAddAssign
```angelscript
FVector2D opAddAssign(FVector2D Other)
```

### opSubAssign
```angelscript
FVector2D opSubAssign(FVector2D Other)
```

### opIndex
```angelscript
float& opIndex(int Index)
```

### opIndex
```angelscript
float opIndex(int Index)
```

### opEquals
```angelscript
bool opEquals(FVector2D Other)
```

### Equals
```angelscript
bool Equals(FVector2D Other, float Tolerance)
```

### CrossProduct
```angelscript
float CrossProduct(FVector2D Other)
```

### DotProduct
```angelscript
float DotProduct(FVector2D Other)
```

### GetMax
```angelscript
float GetMax()
```

### GetAbsMax
```angelscript
float GetAbsMax()
```

### GetMin
```angelscript
float GetMin()
```

### GetAbs
```angelscript
FVector2D GetAbs()
```

### Size
```angelscript
float Size()
```

### SizeSquared
```angelscript
float SizeSquared()
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float Tolerance)
```

### IsZero
```angelscript
bool IsZero()
```

### Normalize
```angelscript
void Normalize(float Tolerance)
```

### GetSafeNormal
```angelscript
FVector2D GetSafeNormal(float Tolerance)
```

### ContainsNaN
```angelscript
bool ContainsNaN()
```

### GetSignVector
```angelscript
FVector2D GetSignVector()
```

### Distance
```angelscript
float Distance(FVector2D Other)
```

### DistSquared
```angelscript
float DistSquared(FVector2D Other)
```

### GetClampedToMaxSize
```angelscript
FVector2D GetClampedToMaxSize(float Max)
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```


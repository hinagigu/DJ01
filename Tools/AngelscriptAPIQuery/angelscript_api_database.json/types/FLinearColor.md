# FLinearColor

## 属性

### R
- **类型**: `float32`

### G
- **类型**: `float32`

### B
- **类型**: `float32`

### A
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FLinearColor& opAssign(FLinearColor Other)
```

### opAdd
```angelscript
FLinearColor opAdd(FLinearColor ColorB)
```

### opAddAssign
```angelscript
FLinearColor opAddAssign(FLinearColor ColorB)
```

### opSub
```angelscript
FLinearColor opSub(FLinearColor ColorB)
```

### opSubAssign
```angelscript
FLinearColor opSubAssign(FLinearColor ColorB)
```

### opMul
```angelscript
FLinearColor opMul(FLinearColor ColorB)
```

### opMulAssign
```angelscript
FLinearColor opMulAssign(FLinearColor ColorB)
```

### opMul
```angelscript
FLinearColor opMul(float32 Scalar)
```

### opMulAssign
```angelscript
FLinearColor opMulAssign(float32 Scalar)
```

### opDiv
```angelscript
FLinearColor opDiv(FLinearColor ColorB)
```

### opDivAssign
```angelscript
FLinearColor opDivAssign(FLinearColor ColorB)
```

### opDiv
```angelscript
FLinearColor opDiv(float32 Scalar)
```

### opDivAssign
```angelscript
FLinearColor opDivAssign(float32 Scalar)
```

### opEquals
```angelscript
bool opEquals(FLinearColor ColorB)
```

### GetClamped
```angelscript
FLinearColor GetClamped(float32 InMin, float32 InMax)
```

### Equals
```angelscript
bool Equals(FLinearColor ColorB, float32 Tolerance)
```

### IsAlmostBlack
```angelscript
bool IsAlmostBlack()
```

### GetMin
```angelscript
float32 GetMin()
```

### GetMax
```angelscript
float32 GetMax()
```

### GetLuminance
```angelscript
float32 GetLuminance()
```

### LinearRGBToHSV
```angelscript
FLinearColor LinearRGBToHSV()
```

### HSVToLinearRGB
```angelscript
FLinearColor HSVToLinearRGB()
```

### ToFColor
```angelscript
FColor ToFColor(bool bSRGB)
```

### ToString
```angelscript
FString ToString()
```


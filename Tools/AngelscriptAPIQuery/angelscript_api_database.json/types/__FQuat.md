# __FQuat

## 属性

### Identity
- **类型**: `const FQuat`

## 方法

### MakeFromEuler
```angelscript
FQuat MakeFromEuler(FVector Euler)
```

### MakeFromRotator
```angelscript
FQuat MakeFromRotator(FRotator Rotator)
```

### FindBetween
```angelscript
FQuat FindBetween(FVector Vector1, FVector Vector2)
```

### FindBetweenVectors
```angelscript
FQuat FindBetweenVectors(FVector Vector1, FVector Vector2)
```

### FindBetweenNormals
```angelscript
FQuat FindBetweenNormals(FVector Normal1, FVector Normal2)
```

### FastLerp
```angelscript
FQuat FastLerp(FQuat A, FQuat B, float Alpha)
```

### FastBilerp
```angelscript
FQuat FastBilerp(FQuat P00, FQuat P10, FQuat P01, FQuat P11, float FracX, float FracY)
```

### Slerp_NotNormalized
```angelscript
FQuat Slerp_NotNormalized(FQuat Quat1, FQuat Quat2, float Slerp)
```

### Slerp
```angelscript
FQuat Slerp(FQuat Quat1, FQuat Quat2, float Slerp)
```

### Error
```angelscript
float Error(FQuat Q1, FQuat Q2)
```

### ErrorAutoNormalize
```angelscript
float ErrorAutoNormalize(FQuat A, FQuat B)
```

### SlerpFullPath_NotNormalized
```angelscript
FQuat SlerpFullPath_NotNormalized(FQuat Quat1, FQuat Quat2, float Slerp)
```

### SlerpFullPath
```angelscript
FQuat SlerpFullPath(FQuat Quat1, FQuat Quat2, float Slerp)
```

### Squad
```angelscript
FQuat Squad(FQuat Quat1, FQuat Tang1, FQuat Quat2, FQuat Tang2, float Alpha)
```

### SquadFullPath
```angelscript
FQuat SquadFullPath(FQuat Quat1, FQuat Tang1, FQuat Quat2, FQuat Tang2, float Alpha)
```

### CalcTangents
```angelscript
void CalcTangents(FQuat PrevP, FQuat P, FQuat NextP, float Tension, FQuat& OutTan)
```

### MakeFromAxes
```angelscript
FQuat MakeFromAxes(FVector Forward, FVector Right, FVector Up)
```

### MakeFromX
```angelscript
FQuat MakeFromX(FVector XAxis)
```

### MakeFromXY
```angelscript
FQuat MakeFromXY(FVector XAxis, FVector YAxis)
```

### MakeFromXZ
```angelscript
FQuat MakeFromXZ(FVector XAxis, FVector ZAxis)
```

### MakeFromY
```angelscript
FQuat MakeFromY(FVector YAxis)
```

### MakeFromYX
```angelscript
FQuat MakeFromYX(FVector YAxis, FVector XAxis)
```

### MakeFromYZ
```angelscript
FQuat MakeFromYZ(FVector YAxis, FVector ZAxis)
```

### MakeFromZ
```angelscript
FQuat MakeFromZ(FVector ZAxis)
```

### MakeFromZX
```angelscript
FQuat MakeFromZX(FVector ZAxis, FVector XAxis)
```

### MakeFromZY
```angelscript
FQuat MakeFromZY(FVector ZAxis, FVector YAxis)
```


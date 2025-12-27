# __FQuat4f

## 属性

### Identity
- **类型**: `const FQuat4f`

## 方法

### MakeFromEuler
```angelscript
FQuat4f MakeFromEuler(FVector3f Euler)
```

### FindBetween
```angelscript
FQuat4f FindBetween(FVector3f Vector1, FVector3f Vector2)
```

### FindBetweenVectors
```angelscript
FQuat4f FindBetweenVectors(FVector3f Vector1, FVector3f Vector2)
```

### FindBetweenNormals
```angelscript
FQuat4f FindBetweenNormals(FVector3f Normal1, FVector3f Normal2)
```

### FastLerp
```angelscript
FQuat4f FastLerp(FQuat4f A, FQuat4f B, float32 Alpha)
```

### FastBilerp
```angelscript
FQuat4f FastBilerp(FQuat4f P00, FQuat4f P10, FQuat4f P01, FQuat4f P11, float32 FracX, float32 FracY)
```

### Slerp_NotNormalized
```angelscript
FQuat4f Slerp_NotNormalized(FQuat4f Quat1, FQuat4f Quat2, float32 Slerp)
```

### Slerp
```angelscript
FQuat4f Slerp(FQuat4f Quat1, FQuat4f Quat2, float32 Slerp)
```

### Error
```angelscript
float32 Error(FQuat4f Q1, FQuat4f Q2)
```

### ErrorAutoNormalize
```angelscript
float32 ErrorAutoNormalize(FQuat4f A, FQuat4f B)
```

### SlerpFullPath_NotNormalized
```angelscript
FQuat4f SlerpFullPath_NotNormalized(FQuat4f Quat1, FQuat4f Quat2, float32 Slerp)
```

### SlerpFullPath
```angelscript
FQuat4f SlerpFullPath(FQuat4f Quat1, FQuat4f Quat2, float32 Slerp)
```

### Squad
```angelscript
FQuat4f Squad(FQuat4f Quat1, FQuat4f Tang1, FQuat4f Quat2, FQuat4f Tang2, float32 Alpha)
```

### SquadFullPath
```angelscript
FQuat4f SquadFullPath(FQuat4f Quat1, FQuat4f Tang1, FQuat4f Quat2, FQuat4f Tang2, float32 Alpha)
```

### CalcTangents
```angelscript
void CalcTangents(FQuat4f PrevP, FQuat4f P, FQuat4f NextP, float32 Tension, FQuat4f& OutTan)
```

### MakeFromAxes
```angelscript
FQuat4f MakeFromAxes(FVector3f Forward, FVector3f Right, FVector3f Up)
```

### MakeFromX
```angelscript
FQuat4f MakeFromX(FVector3f XAxis)
```

### MakeFromXY
```angelscript
FQuat4f MakeFromXY(FVector3f XAxis, FVector3f YAxis)
```

### MakeFromXZ
```angelscript
FQuat4f MakeFromXZ(FVector3f XAxis, FVector3f ZAxis)
```

### MakeFromY
```angelscript
FQuat4f MakeFromY(FVector3f YAxis)
```

### MakeFromYX
```angelscript
FQuat4f MakeFromYX(FVector3f YAxis, FVector3f XAxis)
```

### MakeFromYZ
```angelscript
FQuat4f MakeFromYZ(FVector3f YAxis, FVector3f ZAxis)
```

### MakeFromZ
```angelscript
FQuat4f MakeFromZ(FVector3f ZAxis)
```

### MakeFromZX
```angelscript
FQuat4f MakeFromZX(FVector3f ZAxis, FVector3f XAxis)
```

### MakeFromZY
```angelscript
FQuat4f MakeFromZY(FVector3f ZAxis, FVector3f YAxis)
```


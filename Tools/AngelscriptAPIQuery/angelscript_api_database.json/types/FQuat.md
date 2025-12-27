# FQuat

## 属性

### X
- **类型**: `float`

### Y
- **类型**: `float`

### Z
- **类型**: `float`

### W
- **类型**: `float`

## 方法

### opAssign
```angelscript
FQuat& opAssign(FQuat Other)
```

### opAdd
```angelscript
FQuat opAdd(FQuat Other)
```

### opSub
```angelscript
FQuat opSub(FQuat Other)
```

### opAddAssign
```angelscript
FQuat opAddAssign(FQuat Other)
```

### opSubAssign
```angelscript
FQuat opSubAssign(FQuat Other)
```

### opEquals
```angelscript
bool opEquals(FQuat Other)
```

### Equals
```angelscript
bool Equals(FQuat Other, float Tolerance)
```

### IsIdentity
```angelscript
bool IsIdentity(float Tolerance)
```

### opMul
```angelscript
FQuat opMul(FQuat Other)
```

### opMulAssign
```angelscript
FQuat opMulAssign(FQuat Other)
```

### opMul
```angelscript
FQuat opMul(float Scale)
```

### opMulAssign
```angelscript
FQuat opMulAssign(float Scale)
```

### opDiv
```angelscript
FQuat opDiv(float Scale)
```

### opDivAssign
```angelscript
FQuat opDivAssign(float Scale)
```

### Normalize
```angelscript
void Normalize(float Tolerance)
```

### GetNormalized
```angelscript
FQuat GetNormalized(float Tolerance)
```

### IsNormalized
```angelscript
bool IsNormalized()
```

### Size
```angelscript
float Size()
```

### SizeSquared
```angelscript
float SizeSquared()
```

### GetAngle
```angelscript
float GetAngle()
```

### Log
```angelscript
FQuat Log()
```

### Exp
```angelscript
FQuat Exp()
```

### Inverse
```angelscript
FQuat Inverse()
```

### AngularDistance
```angelscript
float AngularDistance(FQuat Q)
```

### ContainsNaN
```angelscript
bool ContainsNaN()
```

### EnforceShortestArcWith
```angelscript
void EnforceShortestArcWith(FQuat Other)
```

### ToAxisAndAngle
```angelscript
void ToAxisAndAngle(FVector& Axis, float32& Angle)
```

### ToAxisAndAngle
```angelscript
void ToAxisAndAngle(FVector& Axis, float& Angle)
```

### opMul
```angelscript
FVector opMul(FVector Other)
```

### Euler
```angelscript
FVector Euler()
```

### RotateVector
```angelscript
FVector RotateVector(FVector V)
```

### UnrotateVector
```angelscript
FVector UnrotateVector(FVector V)
```

### GetAxisX
```angelscript
FVector GetAxisX()
```

### GetAxisY
```angelscript
FVector GetAxisY()
```

### GetAxisZ
```angelscript
FVector GetAxisZ()
```

### GetForwardVector
```angelscript
FVector GetForwardVector()
```

### GetRightVector
```angelscript
FVector GetRightVector()
```

### GetUpVector
```angelscript
FVector GetUpVector()
```

### Vector
```angelscript
FVector Vector()
```

### GetRotationAxis
```angelscript
FVector GetRotationAxis()
```

### Rotator
```angelscript
FRotator Rotator()
```

### ToSwingTwist
```angelscript
void ToSwingTwist(FVector InTwistAxis, FQuat& OutSwing, FQuat& OutTwist)
```

### GetTwistAngle
```angelscript
float GetTwistAngle(FVector InTwistAxis)
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```


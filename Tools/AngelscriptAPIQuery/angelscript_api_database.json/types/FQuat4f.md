# FQuat4f

## 属性

### X
- **类型**: `float32`

### Y
- **类型**: `float32`

### Z
- **类型**: `float32`

### W
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FQuat4f& opAssign(FQuat4f Other)
```

### opAdd
```angelscript
FQuat4f opAdd(FQuat4f Other)
```

### opSub
```angelscript
FQuat4f opSub(FQuat4f Other)
```

### opAddAssign
```angelscript
FQuat4f opAddAssign(FQuat4f Other)
```

### opSubAssign
```angelscript
FQuat4f opSubAssign(FQuat4f Other)
```

### opEquals
```angelscript
bool opEquals(FQuat4f Other)
```

### Equals
```angelscript
bool Equals(FQuat4f Other, float32 Tolerance)
```

### IsIdentity
```angelscript
bool IsIdentity(float32 Tolerance)
```

### opMul
```angelscript
FQuat4f opMul(FQuat4f Other)
```

### opMulAssign
```angelscript
FQuat4f opMulAssign(FQuat4f Other)
```

### opMul
```angelscript
FQuat4f opMul(float32 Scale)
```

### opMulAssign
```angelscript
FQuat4f opMulAssign(float32 Scale)
```

### opDiv
```angelscript
FQuat4f opDiv(float32 Scale)
```

### opDivAssign
```angelscript
FQuat4f opDivAssign(float32 Scale)
```

### Normalize
```angelscript
void Normalize(float32 Tolerance)
```

### GetNormalized
```angelscript
FQuat4f GetNormalized(float32 Tolerance)
```

### IsNormalized
```angelscript
bool IsNormalized()
```

### Size
```angelscript
float32 Size()
```

### SizeSquared
```angelscript
float32 SizeSquared()
```

### GetAngle
```angelscript
float32 GetAngle()
```

### Log
```angelscript
FQuat4f Log()
```

### Exp
```angelscript
FQuat4f Exp()
```

### Inverse
```angelscript
FQuat4f Inverse()
```

### AngularDistance
```angelscript
float32 AngularDistance(FQuat4f Q)
```

### ContainsNaN
```angelscript
bool ContainsNaN()
```

### EnforceShortestArcWith
```angelscript
void EnforceShortestArcWith(FQuat4f Other)
```

### ToAxisAndAngle
```angelscript
void ToAxisAndAngle(FVector3f& Axis, float32& Angle)
```

### opMul
```angelscript
FVector3f opMul(FVector3f Other)
```

### Euler
```angelscript
FVector3f Euler()
```

### RotateVector
```angelscript
FVector3f RotateVector(FVector3f V)
```

### UnrotateVector
```angelscript
FVector3f UnrotateVector(FVector3f V)
```

### GetAxisX
```angelscript
FVector3f GetAxisX()
```

### GetAxisY
```angelscript
FVector3f GetAxisY()
```

### GetAxisZ
```angelscript
FVector3f GetAxisZ()
```

### GetForwardVector
```angelscript
FVector3f GetForwardVector()
```

### GetRightVector
```angelscript
FVector3f GetRightVector()
```

### GetUpVector
```angelscript
FVector3f GetUpVector()
```

### Vector
```angelscript
FVector3f Vector()
```

### GetRotationAxis
```angelscript
FVector3f GetRotationAxis()
```

### Rotator
```angelscript
FRotator3f Rotator()
```

### ToSwingTwist
```angelscript
void ToSwingTwist(FVector3f InTwistAxis, FQuat4f& OutSwing, FQuat4f& OutTwist)
```

### GetTwistAngle
```angelscript
float32 GetTwistAngle(FVector3f InTwistAxis)
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```


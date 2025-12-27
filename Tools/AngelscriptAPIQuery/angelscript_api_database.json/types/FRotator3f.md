# FRotator3f

## 属性

### Pitch
- **类型**: `float32`

### Yaw
- **类型**: `float32`

### Roll
- **类型**: `float32`

## 方法

### opAssign
```angelscript
FRotator3f& opAssign(FRotator3f Other)
```

### opAdd
```angelscript
FRotator3f opAdd(FRotator3f R)
```

### opAddAssign
```angelscript
FRotator3f opAddAssign(FRotator3f R)
```

### opSub
```angelscript
FRotator3f opSub(FRotator3f R)
```

### opSubAssign
```angelscript
FRotator3f opSubAssign(FRotator3f R)
```

### opMul
```angelscript
FRotator3f opMul(float32 Scale)
```

### opMulAssign
```angelscript
FRotator3f opMulAssign(float32 Scale)
```

### opEquals
```angelscript
bool opEquals(FRotator3f R)
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float32 Tolerance)
```

### IsZero
```angelscript
bool IsZero()
```

### Equals
```angelscript
bool Equals(FRotator3f R, float32 Tolerance)
```

### GetInverse
```angelscript
FRotator3f GetInverse()
```

### Clamp
```angelscript
FRotator3f Clamp()
```

### GetNormalized
```angelscript
FRotator3f GetNormalized()
```

### GetDenormalized
```angelscript
FRotator3f GetDenormalized()
```

### GetWindingAndRemainder
```angelscript
void GetWindingAndRemainder(FRotator3f& Winding, FRotator3f& Remainder)
```

### GetManhattanDistance
```angelscript
float32 GetManhattanDistance(FRotator3f Rotator)
```

### Normalize
```angelscript
void Normalize()
```

### ContainsNaN
```angelscript
bool ContainsNaN()
```

### Vector
```angelscript
FVector3f Vector()
```

### Quaternion
```angelscript
FQuat4f Quaternion()
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

### ToColorString
```angelscript
FString ToColorString()
```

### InitFromString
```angelscript
bool InitFromString(FString SourceString)
```

### ToString
```angelscript
FString ToString()
```

### AngularDistance
```angelscript
float32 AngularDistance(FRotator3f B)
```
Get the angle in degrees between two rotators

### Compose
```angelscript
FRotator3f Compose(FRotator3f B)
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


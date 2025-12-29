# FRotator

## 属性

### Pitch
- **类型**: `float`

### Yaw
- **类型**: `float`

### Roll
- **类型**: `float`

## 方法

### opAssign
```angelscript
FRotator& opAssign(FRotator Other)
```

### opAdd
```angelscript
FRotator opAdd(FRotator R)
```

### opAddAssign
```angelscript
FRotator opAddAssign(FRotator R)
```

### opSub
```angelscript
FRotator opSub(FRotator R)
```

### opSubAssign
```angelscript
FRotator opSubAssign(FRotator R)
```

### opMul
```angelscript
FRotator opMul(float Scale)
```

### opMulAssign
```angelscript
FRotator opMulAssign(float Scale)
```

### opEquals
```angelscript
bool opEquals(FRotator R)
```

### IsNearlyZero
```angelscript
bool IsNearlyZero(float Tolerance)
```

### IsZero
```angelscript
bool IsZero()
```

### Equals
```angelscript
bool Equals(FRotator R, float Tolerance)
```

### GetInverse
```angelscript
FRotator GetInverse()
```

### Clamp
```angelscript
FRotator Clamp()
```

### GetNormalized
```angelscript
FRotator GetNormalized()
```

### GetDenormalized
```angelscript
FRotator GetDenormalized()
```

### GetWindingAndRemainder
```angelscript
void GetWindingAndRemainder(FRotator& Winding, FRotator& Remainder)
```

### GetManhattanDistance
```angelscript
float GetManhattanDistance(FRotator Rotator)
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
FVector Vector()
```

### Quaternion
```angelscript
FQuat Quaternion()
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
float AngularDistance(FRotator B)
```
Get the angle in degrees between two rotators

### Compose
```angelscript
FRotator Compose(FRotator B)
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


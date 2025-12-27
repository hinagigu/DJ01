# FTimespan

A time span value, which is the difference between two dates and times.
@note The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\Timespan.h

## 方法

### opAdd
```angelscript
FTimespan opAdd(FTimespan Other)
```

### opAddAssign
```angelscript
FTimespan& opAddAssign(FTimespan Other)
```

### opSub
```angelscript
FTimespan opSub()
```

### opSub
```angelscript
FTimespan opSub(FTimespan Other)
```

### opSubAssign
```angelscript
FTimespan& opSubAssign(FTimespan Other)
```

### opMul
```angelscript
FTimespan opMul(float Scalar)
```

### opMulAssign
```angelscript
FTimespan& opMulAssign(float Scalar)
```

### opDiv
```angelscript
FTimespan opDiv(float Scalar)
```

### opDivAssign
```angelscript
FTimespan& opDivAssign(float Scalar)
```

### opMod
```angelscript
FTimespan opMod(FTimespan Other)
```

### opModAssign
```angelscript
FTimespan& opModAssign(FTimespan Other)
```

### opCmp
```angelscript
int opCmp(FTimespan Other)
```

### opEquals
```angelscript
bool opEquals(FTimespan Other)
```

### GetDays
```angelscript
int GetDays()
```

### GetDuration
```angelscript
FTimespan GetDuration()
```

### GetFractionMicro
```angelscript
int GetFractionMicro()
```

### GetFractionMilli
```angelscript
int GetFractionMilli()
```

### GetFractionNano
```angelscript
int GetFractionNano()
```

### GetFractionTicks
```angelscript
int GetFractionTicks()
```

### GetHours
```angelscript
int GetHours()
```

### GetMinutes
```angelscript
int GetMinutes()
```

### GetSeconds
```angelscript
int GetSeconds()
```

### GetTicks
```angelscript
int64 GetTicks()
```

### GetTotalDays
```angelscript
float GetTotalDays()
```

### GetTotalHours
```angelscript
float GetTotalHours()
```

### GetTotalMicroseconds
```angelscript
float GetTotalMicroseconds()
```

### GetTotalMilliseconds
```angelscript
float GetTotalMilliseconds()
```

### GetTotalMinutes
```angelscript
float GetTotalMinutes()
```

### GetTotalSeconds
```angelscript
float GetTotalSeconds()
```

### IsZero
```angelscript
bool IsZero()
```

### ToString
```angelscript
FString ToString()
```

### ToString
```angelscript
FString ToString(FString Format)
```

### opAssign
```angelscript
FTimespan& opAssign(FTimespan Other)
```


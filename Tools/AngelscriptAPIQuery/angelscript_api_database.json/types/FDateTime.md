# FDateTime

A value representing a specific point date and time over a wide range of years.
@note The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\DateTime.h

## 方法

### opEquals
```angelscript
bool opEquals(FDateTime Other)
```

### GetDate
```angelscript
FDateTime GetDate()
```

### GetDate
```angelscript
void GetDate(int& OutYear, int& OutMonth, int& OutDay)
```

### GetDay
```angelscript
int GetDay()
```

### GetDayOfYear
```angelscript
int GetDayOfYear()
```

### GetHour
```angelscript
int GetHour()
```

### GetHour12
```angelscript
int GetHour12()
```

### GetMillisecond
```angelscript
int GetMillisecond()
```

### GetMinute
```angelscript
int GetMinute()
```

### GetMonth
```angelscript
int GetMonth()
```

### GetSecond
```angelscript
int GetSecond()
```

### GetYear
```angelscript
int GetYear()
```

### IsAfternoon
```angelscript
bool IsAfternoon()
```

### IsMorning
```angelscript
bool IsMorning()
```

### ToUnixTimestamp
```angelscript
int64 ToUnixTimestamp()
```

### ToHttpDate
```angelscript
FString ToHttpDate()
```

### ToIso8601
```angelscript
FString ToIso8601()
```

### ToString
```angelscript
FString ToString(FString Format)
```

### GetTicks
```angelscript
int64 GetTicks()
```

### opCmp
```angelscript
int opCmp(FDateTime Other)
```

### opAdd
```angelscript
FDateTime opAdd(FTimespan Other)
```

### opAddAssign
```angelscript
FDateTime& opAddAssign(FTimespan Other)
```

### opSub
```angelscript
FTimespan opSub(FDateTime Other)
```

### opSub
```angelscript
FDateTime opSub(FTimespan Other)
```

### opSubAssign
```angelscript
FDateTime& opSubAssign(FTimespan Other)
```

### ToString
```angelscript
FString ToString()
```

### opAssign
```angelscript
FDateTime& opAssign(FDateTime Other)
```


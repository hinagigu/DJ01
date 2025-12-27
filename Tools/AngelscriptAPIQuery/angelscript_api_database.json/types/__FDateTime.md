# __FDateTime

## 方法

### DaysInMonth
```angelscript
int DaysInMonth(int Year, int Month)
```

### DaysInYear
```angelscript
int DaysInYear(int Year)
```

### IsLeapYear
```angelscript
bool IsLeapYear(int Year)
```

### FromUnixTimestamp
```angelscript
FDateTime FromUnixTimestamp(int64 UnixTime)
```

### MinValue
```angelscript
FDateTime MinValue()
```

### MaxValue
```angelscript
FDateTime MaxValue()
```

### Now
```angelscript
FDateTime Now()
```

### UtcNow
```angelscript
FDateTime UtcNow()
```

### Today
```angelscript
FDateTime Today()
```

### Parse
```angelscript
bool Parse(FString DateTimeString, FDateTime& OutDateTime)
```

### ParseHttpDate
```angelscript
bool ParseHttpDate(FString HttpDate, FDateTime& OutDateTime)
```

### ParseIso8601
```angelscript
bool ParseIso8601(FString DateTimeString, FDateTime& OutDateTime)
```


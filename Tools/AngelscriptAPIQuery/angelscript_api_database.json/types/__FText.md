# __FText

## 方法

### FromStringTable
```angelscript
FText FromStringTable(FName InTableId, FString InKey, EStringTableLoadingPolicy InLoadingPolicy)
```

### FromName
```angelscript
FText FromName(FName Val)
```

### FromString
```angelscript
FText FromString(FString Val)
```

### AsCultureInvariant
```angelscript
FText AsCultureInvariant(FString Val)
```

### Join
```angelscript
FText Join(FText Delimiter, TArray<FFormatArgumentValue> Args)
```

### Join
```angelscript
FText Join(FText Delimiter, TArray<FText> Args)
```

### AsDate
```angelscript
FText AsDate(FDateTime DateTime, int DateStyle)
```

### AsDateTime
```angelscript
FText AsDateTime(FDateTime DateTime, int DateStyle, int TimeStyle)
```

### AsTime
```angelscript
FText AsTime(FDateTime DateTime, int TimeStyle)
```

### AsTimespan
```angelscript
FText AsTimespan(FTimespan Timespan)
```

### AsNumber
```angelscript
FText AsNumber(float32 Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(float Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(int8 Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(int16 Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(int Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(int64 Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(uint8 Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(uint16 Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(uint Val, FNumberFormattingOptions Options)
```

### AsNumber
```angelscript
FText AsNumber(uint64 Val, FNumberFormattingOptions Options)
```

### AsMemory
```angelscript
FText AsMemory(uint64 NumBytes)
```

### Format
```angelscript
FText Format(FText Format, ? Arg0)
```

### Format
```angelscript
FText Format(FText Format, ? Arg0, ? Arg1)
```

### Format
```angelscript
FText Format(FText Format, ? Arg0, ? Arg1, ? Arg2)
```

### Format
```angelscript
FText Format(FText Format, ? Arg0, ? Arg1, ? Arg2, ? Arg3)
```

### Format
```angelscript
FText Format(FText Format, ? Arg0, ? Arg1, ? Arg2, ? Arg3, ? Arg4)
```

### Format
```angelscript
FText Format(FText Format, TMap<FString,FFormatArgumentValue> Arguments)
```

### Format
```angelscript
FText Format(FText Format, TArray<FFormatArgumentValue> Arguments)
```

### GetFormatPatternParameters
```angelscript
void GetFormatPatternParameters(FText Fmt, TArray<FString>&out ParameterNames)
```


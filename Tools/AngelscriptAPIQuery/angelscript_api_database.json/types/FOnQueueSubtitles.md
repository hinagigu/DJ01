# FOnQueueSubtitles

## 方法

### opAssign
```angelscript
FOnQueueSubtitles& opAssign(FOnQueueSubtitles Other)
```

### IsBound
```angelscript
bool IsBound()
```

### GetUObject
```angelscript
UObject GetUObject()
```

### GetFunctionName
```angelscript
FName GetFunctionName()
```

### Clear
```angelscript
void Clear()
```

### BindUFunction
```angelscript
void BindUFunction(UObject Object, FName FunctionName)
```

### Execute
```angelscript
void Execute(const TArray<FSubtitleCue>&in Subtitles, float32 CueDuration)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(const TArray<FSubtitleCue>&in Subtitles, float32 CueDuration)
```


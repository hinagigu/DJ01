# FScriptTraceDelegate

## 方法

### opAssign
```angelscript
FScriptTraceDelegate& opAssign(FScriptTraceDelegate Other)
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
void Execute(uint64 TraceHandle, const TArray<FHitResult>&in OutHits, uint UserData)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(uint64 TraceHandle, const TArray<FHitResult>&in OutHits, uint UserData)
```


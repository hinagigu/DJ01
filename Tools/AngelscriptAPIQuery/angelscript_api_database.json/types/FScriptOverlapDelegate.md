# FScriptOverlapDelegate

## 方法

### opAssign
```angelscript
FScriptOverlapDelegate& opAssign(FScriptOverlapDelegate Other)
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
void Execute(uint64 TraceHandle, const TArray<FOverlapResult>&in OutOverlaps, uint UserData)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(uint64 TraceHandle, const TArray<FOverlapResult>&in OutOverlaps, uint UserData)
```


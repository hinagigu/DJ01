# FAsyncSaveGameToSlotDynamicDelegate

## 方法

### opAssign
```angelscript
FAsyncSaveGameToSlotDynamicDelegate& opAssign(FAsyncSaveGameToSlotDynamicDelegate Other)
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
void Execute(FString SlotName, int UserIndex, bool bSuccess)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(FString SlotName, int UserIndex, bool bSuccess)
```


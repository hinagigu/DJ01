# FAdvancedCopyCompletedEvent

## 方法

### opAssign
```angelscript
FAdvancedCopyCompletedEvent& opAssign(FAdvancedCopyCompletedEvent Other)
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
void Execute(bool bSuccess, const TArray<FAssetRenameData>&in AllCopiedAssets)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(bool bSuccess, const TArray<FAssetRenameData>&in AllCopiedAssets)
```


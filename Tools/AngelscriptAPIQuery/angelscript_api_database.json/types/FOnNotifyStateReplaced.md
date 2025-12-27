# FOnNotifyStateReplaced

## 方法

### opAssign
```angelscript
FOnNotifyStateReplaced& opAssign(FOnNotifyStateReplaced Other)
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
void Execute(const UAnimNotifyState OldNotifyState, const UAnimNotifyState NewNotifyState)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(const UAnimNotifyState OldNotifyState, const UAnimNotifyState NewNotifyState)
```


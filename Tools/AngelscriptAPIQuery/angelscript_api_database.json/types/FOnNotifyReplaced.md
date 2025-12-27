# FOnNotifyReplaced

## 方法

### opAssign
```angelscript
FOnNotifyReplaced& opAssign(FOnNotifyReplaced Other)
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
void Execute(const UAnimNotify OldNotify, const UAnimNotify NewNotify)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(const UAnimNotify OldNotify, const UAnimNotify NewNotify)
```


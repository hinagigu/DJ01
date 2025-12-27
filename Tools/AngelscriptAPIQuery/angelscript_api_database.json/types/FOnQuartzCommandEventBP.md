# FOnQuartzCommandEventBP

## 方法

### opAssign
```angelscript
FOnQuartzCommandEventBP& opAssign(FOnQuartzCommandEventBP Other)
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
void Execute(EQuartzCommandDelegateSubType EventType, FName Name)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(EQuartzCommandDelegateSubType EventType, FName Name)
```


# FCommonUserOnInitializeComplete

## 方法

### opAssign
```angelscript
FCommonUserOnInitializeComplete& opAssign(FCommonUserOnInitializeComplete Other)
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
void Execute(const UCommonUserInfo UserInfo, bool bSuccess, FText Error, ECommonUserPrivilege RequestedPrivilege, ECommonUserOnlineContext OnlineContext)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(const UCommonUserInfo UserInfo, bool bSuccess, FText Error, ECommonUserPrivilege RequestedPrivilege, ECommonUserOnlineContext OnlineContext)
```


# FCommonUserOnInitializeCompleteMulticast

## 方法

### opAssign
```angelscript
FCommonUserOnInitializeCompleteMulticast& opAssign(FCommonUserOnInitializeCompleteMulticast Other)
```

### IsBound
```angelscript
bool IsBound()
```

### Clear
```angelscript
void Clear()
```

### AddUFunction
```angelscript
void AddUFunction(const UObject Object, FName FunctionName)
```

### Unbind
```angelscript
void Unbind(UObject Object, FName FunctionName)
```

### UnbindObject
```angelscript
void UnbindObject(UObject Object)
```

### Broadcast
```angelscript
void Broadcast(const UCommonUserInfo UserInfo, bool bSuccess, FText Error, ECommonUserPrivilege RequestedPrivilege, ECommonUserOnlineContext OnlineContext)
```


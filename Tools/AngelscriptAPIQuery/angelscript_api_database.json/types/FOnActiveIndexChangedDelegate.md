# FOnActiveIndexChangedDelegate

## 方法

### opAssign
```angelscript
FOnActiveIndexChangedDelegate& opAssign(FOnActiveIndexChangedDelegate Other)
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
void Broadcast(UWidget ActiveWidget, int ActiveIndex)
```


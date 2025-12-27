# FDJ01TeamConfigChangedDelegate

## 方法

### opAssign
```angelscript
FDJ01TeamConfigChangedDelegate& opAssign(FDJ01TeamConfigChangedDelegate Other)
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
void Broadcast(UObject Agent, FDJ01TeamConfig OldConfig, FDJ01TeamConfig NewConfig)
```


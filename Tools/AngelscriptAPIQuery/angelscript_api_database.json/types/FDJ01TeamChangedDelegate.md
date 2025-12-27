# FDJ01TeamChangedDelegate

## 方法

### opAssign
```angelscript
FDJ01TeamChangedDelegate& opAssign(FDJ01TeamChangedDelegate Other)
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
void Broadcast(UObject TeamAgent, EDJ01Team OldTeam, EDJ01Team NewTeam)
```


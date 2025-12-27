# FAchievementWriteDelegate

## 方法

### opAssign
```angelscript
FAchievementWriteDelegate& opAssign(FAchievementWriteDelegate Other)
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
void Broadcast(FName WrittenAchievementName, float32 WrittenProgress, int WrittenUserTag)
```


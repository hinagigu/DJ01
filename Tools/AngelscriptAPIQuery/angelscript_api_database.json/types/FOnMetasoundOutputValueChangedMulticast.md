# FOnMetasoundOutputValueChangedMulticast

## 方法

### opAssign
```angelscript
FOnMetasoundOutputValueChangedMulticast& opAssign(FOnMetasoundOutputValueChangedMulticast Other)
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
void Broadcast(FName Name, const FMetaSoundOutput&in Output)
```


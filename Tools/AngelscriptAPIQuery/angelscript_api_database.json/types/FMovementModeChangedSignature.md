# FMovementModeChangedSignature

## 方法

### opAssign
```angelscript
FMovementModeChangedSignature& opAssign(FMovementModeChangedSignature Other)
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
void Broadcast(ACharacter Character, EMovementMode PrevMovementMode, uint8 PreviousCustomMode)
```


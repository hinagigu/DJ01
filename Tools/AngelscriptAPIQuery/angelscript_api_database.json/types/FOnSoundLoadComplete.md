# FOnSoundLoadComplete

## 方法

### opAssign
```angelscript
FOnSoundLoadComplete& opAssign(FOnSoundLoadComplete Other)
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
void Execute(const USoundWave LoadedSoundWave, bool WasCancelled)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(const USoundWave LoadedSoundWave, bool WasCancelled)
```


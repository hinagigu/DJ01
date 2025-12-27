# FOnMetasoundOutputValueChanged

## 方法

### opAssign
```angelscript
FOnMetasoundOutputValueChanged& opAssign(FOnMetasoundOutputValueChanged Other)
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
void Execute(FName OutputName, const FMetaSoundOutput&in Output)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(FName OutputName, const FMetaSoundOutput&in Output)
```


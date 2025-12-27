# FDataRegistryItemAcquiredBPCallback

## 方法

### opAssign
```angelscript
FDataRegistryItemAcquiredBPCallback& opAssign(FDataRegistryItemAcquiredBPCallback Other)
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
void Execute(FDataRegistryId ItemId, FDataRegistryLookup ResolvedLookup, EDataRegistryAcquireStatus Status)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(FDataRegistryId ItemId, FDataRegistryLookup ResolvedLookup, EDataRegistryAcquireStatus Status)
```


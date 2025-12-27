# FExtendExtensionPointDynamicDelegate

## 方法

### opAssign
```angelscript
FExtendExtensionPointDynamicDelegate& opAssign(FExtendExtensionPointDynamicDelegate Other)
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
void Execute(EUIExtensionAction Action, const FUIExtensionRequest&in ExtensionRequest)
```

### ExecuteIfBound
```angelscript
void ExecuteIfBound(EUIExtensionAction Action, const FUIExtensionRequest&in ExtensionRequest)
```


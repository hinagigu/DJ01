# FRigVMUserWorkflowProvider

## 方法

### opAssign
```angelscript
FRigVMUserWorkflowProvider& opAssign(FRigVMUserWorkflowProvider Other)
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
TArray<FRigVMUserWorkflow> Execute(const UObject InSubject)
```

### ExecuteIfBound
```angelscript
TArray<FRigVMUserWorkflow> ExecuteIfBound(const UObject InSubject)
```


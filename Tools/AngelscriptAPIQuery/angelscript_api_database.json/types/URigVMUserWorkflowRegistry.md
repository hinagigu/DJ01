# URigVMUserWorkflowRegistry

**继承自**: `UObject`

## 方法

### GetWorkflows
```angelscript
TArray<FRigVMUserWorkflow> GetWorkflows(ERigVMUserWorkflowType InType, const UScriptStruct InStruct, const UObject InSubject)
```

### RegisterProvider
```angelscript
int RegisterProvider(const UScriptStruct InStruct, FRigVMUserWorkflowProvider InProvider)
```

### UnregisterProvider
```angelscript
void UnregisterProvider(int InHandle)
```


# URigVMBlueprint

**继承自**: `UBlueprint`

## 属性

### RigGraphDisplaySettings
- **类型**: `FRigVMEdGraphDisplaySettings`

### VMRuntimeSettings
- **类型**: `FRigVMRuntimeSettings`

### VMCompileSettings
- **类型**: `FRigVMCompileSettings`

## 方法

### AddMemberVariable
```angelscript
FName AddMemberVariable(FName InName, FString InCPPType, bool bIsPublic, bool bIsReadOnly, FString InDefaultValue)
```

### AddModel
```angelscript
URigVMGraph AddModel(FString InName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### ChangeMemberVariableType
```angelscript
bool ChangeMemberVariableType(FName InName, FString InCPPType, bool bIsPublic, bool bIsReadOnly, FString InDefaultValue)
```

### CreateRigVMHost
```angelscript
URigVMHost CreateRigVMHost()
```

### GeneratePythonCommands
```angelscript
TArray<FString> GeneratePythonCommands(FString InNewBlueprintName)
```

### GetAllModels
```angelscript
TArray<URigVMGraph> GetAllModels()
```

### GetAutoVMRecompile
```angelscript
bool GetAutoVMRecompile()
```

### GetAvailableRigVMStructs
```angelscript
TArray<UStruct> GetAvailableRigVMStructs()
```

### GetController
```angelscript
URigVMController GetController(const URigVMGraph InGraph)
```

### GetControllerByName
```angelscript
URigVMController GetControllerByName(FString InGraphName)
```

### GetDebuggedRigVMHost
```angelscript
URigVMHost GetDebuggedRigVMHost()
```

### GetDefaultModel
```angelscript
URigVMGraph GetDefaultModel()
```

### GetFocusedModel
```angelscript
URigVMGraph GetFocusedModel()
```

### GetLocalFunctionLibrary
```angelscript
URigVMFunctionLibrary GetLocalFunctionLibrary()
```

### GetMemberVariables
```angelscript
TArray<FRigVMGraphVariableDescription> GetMemberVariables()
```

### GetModel
```angelscript
URigVMGraph GetModel(const UEdGraph InEdGraph)
```

### GetOrCreateController
```angelscript
URigVMController GetOrCreateController(URigVMGraph InGraph)
```

### GetRigVMHostClass
```angelscript
UClass GetRigVMHostClass()
```

### RecompileVM
```angelscript
void RecompileVM()
```

### RecompileVMIfRequired
```angelscript
void RecompileVMIfRequired()
```

### RemoveMemberVariable
```angelscript
bool RemoveMemberVariable(FName InName)
```

### RemoveModel
```angelscript
bool RemoveModel(FString InName, bool bSetupUndoRedo, bool bPrintPythonCommand)
```

### RenameMemberVariable
```angelscript
bool RenameMemberVariable(FName InOldName, FName InNewName)
```

### RequestAutoVMRecompilation
```angelscript
void RequestAutoVMRecompilation()
```

### RequestRigVMInit
```angelscript
void RequestRigVMInit()
```

### SetAutoVMRecompile
```angelscript
void SetAutoVMRecompile(bool bAutoRecompile)
```

### SuspendNotifications
```angelscript
void SuspendNotifications(bool bSuspendNotifs)
```


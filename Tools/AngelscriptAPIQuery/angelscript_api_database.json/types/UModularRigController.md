# UModularRigController

**继承自**: `UObject`

## 方法

### AddModule
```angelscript
FString AddModule(FName InModuleName, TSubclassOf<UControlRig> InClass, FString InParentModulePath, bool bSetupUndo)
```

### AutoConnectModules
```angelscript
bool AutoConnectModules(TArray<FString> InModulePaths, bool bReplaceExistingConnections, bool bSetupUndo)
```

### AutoConnectSecondaryConnectors
```angelscript
bool AutoConnectSecondaryConnectors(TArray<FRigElementKey> InConnectorKeys, bool bReplaceExistingConnections, bool bSetupUndo)
```

### BindModuleVariable
```angelscript
bool BindModuleVariable(FString InModulePath, FName InVariableName, FString InSourcePath, bool bSetupUndo)
```

### CanConnectConnectorToElement
```angelscript
bool CanConnectConnectorToElement(FRigElementKey InConnectorKey, FRigElementKey InTargetKey, FText& OutErrorMessage)
```

### ConnectConnectorToElement
```angelscript
bool ConnectConnectorToElement(FRigElementKey InConnectorKey, FRigElementKey InTargetKey, bool bSetupUndo, bool bAutoResolveOtherConnectors, bool bCheckValidConnection)
```

### DeleteModule
```angelscript
bool DeleteModule(FString InModulePath, bool bSetupUndo)
```

### DisconnectConnector
```angelscript
bool DisconnectConnector(FRigElementKey InConnectorKey, bool bDisconnectSubModules, bool bSetupUndo)
```

### DisconnectCyclicConnectors
```angelscript
TArray<FRigElementKey> DisconnectCyclicConnectors(bool bSetupUndo)
```

### MirrorModule
```angelscript
FString MirrorModule(FString InModulePath, FRigVMMirrorSettings InSettings, bool bSetupUndo)
```

### RenameModule
```angelscript
FString RenameModule(FString InModulePath, FName InNewName, bool bSetupUndo)
```

### ReparentModule
```angelscript
FString ReparentModule(FString InModulePath, FString InNewParentModulePath, bool bSetupUndo)
```

### SetConfigValueInModule
```angelscript
bool SetConfigValueInModule(FString InModulePath, FName InVariableName, FString InValue, bool bSetupUndo)
```

### SetModuleShortName
```angelscript
bool SetModuleShortName(FString InModulePath, FString InNewShortName, bool bSetupUndo)
```

### UnBindModuleVariable
```angelscript
bool UnBindModuleVariable(FString InModulePath, FName InVariableName, bool bSetupUndo)
```


# __ControlRig

## 方法

### CastToControlRigBlueprint
```angelscript
void CastToControlRigBlueprint(UObject Object, ECastToControlRigBlueprintCases& Branches, UControlRigBlueprint& AsControlRigBlueprint)
```

### GetAvailableRigModules
```angelscript
TArray<FRigModuleDescription> GetAvailableRigModules()
```

### GetAvailableRigUnits
```angelscript
TArray<UStruct> GetAvailableRigUnits()
```

### GetCurrentlyOpenRigBlueprints
```angelscript
TArray<UControlRigBlueprint> GetCurrentlyOpenRigBlueprints()
```

### GetHierarchy
```angelscript
URigHierarchy GetHierarchy(UControlRigBlueprint InRigBlueprint)
```

### GetHierarchyController
```angelscript
URigHierarchyController GetHierarchyController(UControlRigBlueprint InRigBlueprint)
```

### GetPreviewMesh
```angelscript
USkeletalMesh GetPreviewMesh(UControlRigBlueprint InRigBlueprint)
```

### RequestControlRigInit
```angelscript
void RequestControlRigInit(UControlRigBlueprint InRigBlueprint)
```

### SetPreviewMesh
```angelscript
void SetPreviewMesh(UControlRigBlueprint InRigBlueprint, USkeletalMesh PreviewMesh, bool bMarkAsDirty)
```

### SetupAllEditorMenus
```angelscript
void SetupAllEditorMenus()
```


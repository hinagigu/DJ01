# UControlRigBlueprint

**继承自**: `URigVMBlueprint`

## 属性

### ModularRigSettings
- **类型**: `FModularRigSettings`

### HierarchySettings
- **类型**: `FRigHierarchySettings`

### RigModuleSettings
- **类型**: `FRigModuleSettings`

### ShapeLibraries
- **类型**: `TArray<TSoftObjectPtr<UControlRigShapeLibrary>>`

### DrawContainer
- **类型**: `FRigVMDrawContainer`

### Influences
- **类型**: `FRigInfluenceMapPerEvent`

### Hierarchy
- **类型**: `URigHierarchy`

### ModularRigModel
- **类型**: `FModularRigModel`

### SourceHierarchyImport
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: The skeleton from import into a hierarchy

### SourceCurveImport
- **类型**: `TSoftObjectPtr<UObject>`
- **描述**: The skeleton from import into a curve

## 方法

### CanTurnIntoStandaloneRig
```angelscript
bool CanTurnIntoStandaloneRig()
```

### ConvertHierarchyElementsToSpawnerNodes
```angelscript
TArray<URigVMNode> ConvertHierarchyElementsToSpawnerNodes(URigHierarchy InHierarchy, TArray<FRigElementKey> InKeys, bool bRemoveElements)
```

### CreateControlRig
```angelscript
UControlRig CreateControlRig()
```

### GetControlRigClass
```angelscript
UClass GetControlRigClass()
```

### GetDebuggedControlRig
```angelscript
UControlRig GetDebuggedControlRig()
```

### GetHierarchyController
```angelscript
URigHierarchyController GetHierarchyController()
```

### GetModularRigController
```angelscript
UModularRigController GetModularRigController()
```

### GetPreviewMesh
```angelscript
USkeletalMesh GetPreviewMesh()
```

### GetRigModuleIcon
```angelscript
UTexture2D GetRigModuleIcon()
```

### IsControlRigModule
```angelscript
bool IsControlRigModule()
```

### RecompileModularRig
```angelscript
void RecompileModularRig()
```

### SetPreviewMesh
```angelscript
void SetPreviewMesh(USkeletalMesh PreviewMesh, bool bMarkAsDirty)
```
IInterface_PreviewMeshProvider interface

### TurnIntoControlRigModule
```angelscript
bool TurnIntoControlRigModule()
```

### TurnIntoStandaloneRig
```angelscript
bool TurnIntoStandaloneRig()
```


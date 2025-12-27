# FDynamicMeshChangeInfo

FDynamicMeshChangeInfo stores information about a change to a UDynamicMesh.
This struct is emitted by the UDynamicMesh OnPreMeshChanged() and OnMeshChanged() delegates.

## 属性

### Type
- **类型**: `EDynamicMeshChangeType`

### Flags
- **类型**: `EDynamicMeshAttributeChangeFlags`

### bIsRevertChange
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FDynamicMeshChangeInfo& opAssign(FDynamicMeshChangeInfo Other)
```


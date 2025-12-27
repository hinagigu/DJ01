# FInterchangeMeshGeometry

* A mesh geometry is a description of a translated mesh asset node that defines a geometry.

## 属性

### MeshUid
- **类型**: `FString`
- **描述**: The unique ID of the UInterchangeMeshNode represented by this structure.

### MeshNode
- **类型**: `const UInterchangeMeshNode`
- **描述**: The UInterchangeMeshNode pointer represented by this structure.

### ReferencingMeshInstanceUids
- **类型**: `TArray<FString>`
- **描述**: All mesh instances that refer to this UInterchangeMeshNode pointer.

### AttachedSocketUids
- **类型**: `TArray<FString>`
- **描述**: A list of all scene nodes that represent sockets attached to this mesh.

## 方法

### opAssign
```angelscript
FInterchangeMeshGeometry& opAssign(FInterchangeMeshGeometry Other)
```


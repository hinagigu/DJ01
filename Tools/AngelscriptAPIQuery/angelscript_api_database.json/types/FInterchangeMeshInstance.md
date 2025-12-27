# FInterchangeMeshInstance

* A mesh instance is a description of a translated scene node that points to a translated mesh asset.
* A mesh instance that points to an LOD group can have many LODs and many scene mesh nodes per LOD index.
* A mesh instance that points to a mesh node will have only LOD 0 and will point to one scene mesh node.

## 属性

### MeshInstanceUid
- **类型**: `FString`
- **描述**: This ID represents either a LOD group scene node UID or a mesh scene node UID.

### LodGroupNode
- **类型**: `const UInterchangeSceneNode`
- **描述**: This member is null unless the mesh instance represents a LOD group.

### bReferenceSkinnedMesh
- **类型**: `bool`

### bReferenceMorphTarget
- **类型**: `bool`

### bHasMorphTargets
- **类型**: `bool`

### SceneNodePerLodIndex
- **类型**: `TMap<int,FInterchangeLodSceneNodeContainer>`
- **描述**: Each scene node here represents a mesh scene node. If it represents a LOD group, there may be more then one mesh scene node for a specific LOD index.

### ReferencingMeshGeometryUids
- **类型**: `TArray<FString>`
- **描述**: All mesh geometry referenced by this MeshInstance.

## 方法

### opAssign
```angelscript
FInterchangeMeshInstance& opAssign(FInterchangeMeshInstance Other)
```


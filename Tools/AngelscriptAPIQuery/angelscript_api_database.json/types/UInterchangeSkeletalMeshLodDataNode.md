# UInterchangeSkeletalMeshLodDataNode

**继承自**: `UInterchangeFactoryBaseNode`

ns UE

## 方法

### AddMeshUid
```angelscript
bool AddMeshUid(FString MeshName)
```
Add a mesh geometry used to create this LOD geometry. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

### GetCustomSkeletonUid
```angelscript
bool GetCustomSkeletonUid(FString& AttributeValue)
```
Query the LOD skeletal mesh factory skeleton reference. Return false if the attribute was not set.

### GetMeshUids
```angelscript
void GetMeshUids(TArray<FString>& OutMeshNames)
```
Query all mesh geometry this LOD will be made from. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

### GetMeshUidsCount
```angelscript
int GetMeshUidsCount()
```
Return the number of mesh geometries this LOD will be made from. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

### RemoveAllMeshes
```angelscript
bool RemoveAllMeshes()
```
Remove all mesh geometry used to create this LOD geometry. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

### RemoveMeshUid
```angelscript
bool RemoveMeshUid(FString MeshName)
```
Remove a mesh geometry used to create this LOD geometry. A mesh UID can represent either a scene node or a mesh node. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

### SetCustomSkeletonUid
```angelscript
bool SetCustomSkeletonUid(FString AttributeValue)
```
Set the LOD skeletal mesh factory skeleton reference. Return false if the attribute could not be set.


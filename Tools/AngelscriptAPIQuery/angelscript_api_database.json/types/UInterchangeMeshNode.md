# UInterchangeMeshNode

**继承自**: `UInterchangeBaseNode`

## 方法

### GetCustomBoundingBox
```angelscript
bool GetCustomBoundingBox(FBox& AttributeValue)
```
Query the bounding box of this mesh. Return false if the attribute was not set.

### GetCustomHasSmoothGroup
```angelscript
bool GetCustomHasSmoothGroup(bool& AttributeValue)
```
Query whether this mesh has smoothing groups. Return false if the attribute was not set.

### GetCustomHasVertexBinormal
```angelscript
bool GetCustomHasVertexBinormal(bool& AttributeValue)
```
Query whether this mesh has vertex bi-normals. Return false if the attribute was not set.

### GetCustomHasVertexColor
```angelscript
bool GetCustomHasVertexColor(bool& AttributeValue)
```
Query whether this mesh has vertex colors. Return false if the attribute was not set.

### GetCustomHasVertexNormal
```angelscript
bool GetCustomHasVertexNormal(bool& AttributeValue)
```
Query whether this mesh has vertex normals. Return false if the attribute was not set.

### GetCustomHasVertexTangent
```angelscript
bool GetCustomHasVertexTangent(bool& AttributeValue)
```
Query whether this mesh has vertex tangents. Return false if the attribute was not set.

### GetCustomPolygonCount
```angelscript
bool GetCustomPolygonCount(int& AttributeValue)
```
Query the polygon count of this mesh. Return false if the attribute was not set.

### GetCustomUVCount
```angelscript
bool GetCustomUVCount(int& AttributeValue)
```
Query the UV count of this mesh. Return false if the attribute was not set.

### GetCustomVertexCount
```angelscript
bool GetCustomVertexCount(int& AttributeValue)
```
Query the vertex count of this mesh. Return false if the attribute was not set.

### GetMorphTargetDependeciesCount
```angelscript
int GetMorphTargetDependeciesCount()
```
Retrieve the number of morph target dependencies for this object.

### GetMorphTargetDependencies
```angelscript
void GetMorphTargetDependencies(TArray<FString>& OutDependencies)
```
Retrieve all morph target dependencies for this object.

### GetMorphTargetDependency
```angelscript
void GetMorphTargetDependency(int Index, FString& OutDependency)
```
Retrieve the specified morph target dependency for this object.

### GetMorphTargetName
```angelscript
bool GetMorphTargetName(FString& OutMorphTargetName)
```
Get the morph target name.
Return true if we successfully retrieved the MorphTargetName attribute.

### GetSceneInstanceUid
```angelscript
void GetSceneInstanceUid(int Index, FString& OutDependency)
```
Retrieve the asset instance this scene node refers to.

### GetSceneInstanceUids
```angelscript
void GetSceneInstanceUids(TArray<FString>& OutDependencies)
```
Retrieve the asset instances this scene node refers to.

### GetSceneInstanceUidsCount
```angelscript
int GetSceneInstanceUidsCount()
```
Retrieve the number of scene nodes instancing this mesh.

### GetSkeletonDependeciesCount
```angelscript
int GetSkeletonDependeciesCount()
```
Retrieve the number of skeleton dependencies for this object.

### GetSkeletonDependencies
```angelscript
void GetSkeletonDependencies(TArray<FString>& OutDependencies)
```
Retrieve the skeleton dependency for this object.

### GetSkeletonDependency
```angelscript
void GetSkeletonDependency(int Index, FString& OutDependency)
```
Retrieve the specified skeleton dependency for this object.

### GetSlotMaterialDependencies
```angelscript
void GetSlotMaterialDependencies(TMap<FString,FString>& OutMaterialDependencies)
```
Retrieve the correspondence table between slot names and assigned materials for this object.

### GetSlotMaterialDependencyUid
```angelscript
bool GetSlotMaterialDependencyUid(FString SlotName, FString& OutMaterialDependency)
```
Retrieve the specified Material dependency for a given slot of this object.

### IsMorphTarget
```angelscript
bool IsMorphTarget()
```
Return true if this node represents a morph target.

### IsSkinnedMesh
```angelscript
bool IsSkinnedMesh()
```
Return true if this node represents a skinned mesh.

### RemoveMorphTargetDependencyUid
```angelscript
bool RemoveMorphTargetDependencyUid(FString DependencyUid)
```
Remove the specified morph target dependency from this object.

### RemoveSceneInstanceUid
```angelscript
bool RemoveSceneInstanceUid(FString DependencyUid)
```
Remove the specified asset instance this scene node refers to.

### RemoveSkeletonDependencyUid
```angelscript
bool RemoveSkeletonDependencyUid(FString DependencyUid)
```
Remove the specified skeleton dependency from this object.

### RemoveSlotMaterialDependencyUid
```angelscript
bool RemoveSlotMaterialDependencyUid(FString SlotName)
```
Remove the Material dependency associated with the given slot name from this object.

### SetCustomBoundingBox
```angelscript
bool SetCustomBoundingBox(FBox AttributeValue)
```
Set the bounding box of this mesh. Return false if the attribute could not be set.

### SetCustomHasSmoothGroup
```angelscript
bool SetCustomHasSmoothGroup(bool AttributeValue)
```
Set the smoothing group attribute of this mesh. Return false if the attribute could not be set.

### SetCustomHasVertexBinormal
```angelscript
bool SetCustomHasVertexBinormal(bool AttributeValue)
```
Set the vertex bi-normal attribute of this mesh. Return false if the attribute could not be set.

### SetCustomHasVertexColor
```angelscript
bool SetCustomHasVertexColor(bool AttributeValue)
```
Set the vertex color attribute of this mesh. Return false if the attribute could not be set.

### SetCustomHasVertexNormal
```angelscript
bool SetCustomHasVertexNormal(bool AttributeValue)
```
Set the vertex normal attribute of this mesh. Return false if the attribute could not be set.

### SetCustomHasVertexTangent
```angelscript
bool SetCustomHasVertexTangent(bool AttributeValue)
```
Set the vertex tangent attribute of this mesh. Return false if the attribute could not be set.

### SetCustomPolygonCount
```angelscript
bool SetCustomPolygonCount(int AttributeValue)
```
Set the polygon count of this mesh. Return false if the attribute could not be set.

### SetCustomUVCount
```angelscript
bool SetCustomUVCount(int AttributeValue)
```
Set the UV count attribute of this mesh. Return false if the attribute could not be set.

### SetCustomVertexCount
```angelscript
bool SetCustomVertexCount(int AttributeValue)
```
Set the vertex count of this mesh. Return false if the attribute could not be set.

### SetMorphTarget
```angelscript
bool SetMorphTarget(bool bIsMorphTarget)
```
Set the IsMorphTarget attribute to determine whether this node represents a morph target.

### SetMorphTargetDependencyUid
```angelscript
bool SetMorphTargetDependencyUid(FString DependencyUid)
```
Add the specified morph target dependency to this object.

### SetMorphTargetName
```angelscript
bool SetMorphTargetName(FString MorphTargetName)
```
Set the MorphTargetName attribute to determine the name of the morph target.

### SetPayLoadKey
```angelscript
void SetPayLoadKey(FString PayLoadKey, EInterchangeMeshPayLoadType PayLoadType)
```

### SetSceneInstanceUid
```angelscript
bool SetSceneInstanceUid(FString DependencyUid)
```
Add the specified asset instance this scene node refers to.

### SetSkeletonDependencyUid
```angelscript
bool SetSkeletonDependencyUid(FString DependencyUid)
```
Add the specified skeleton dependency to this object.

### SetSkinnedMesh
```angelscript
bool SetSkinnedMesh(bool bIsSkinnedMesh)
```
Set the IsSkinnedMesh attribute to determine whether this node represents a skinned mesh.

### SetSlotMaterialDependencyUid
```angelscript
bool SetSlotMaterialDependencyUid(FString SlotName, FString MaterialDependencyUid)
```
Add the specified Material dependency to a specific slot name of this object.


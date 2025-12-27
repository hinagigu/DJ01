# UInterchangePipelineMeshesUtilities

**继承自**: `UObject`

## 方法

### GetAllMeshGeometry
```angelscript
void GetAllMeshGeometry(TArray<FString>& MeshGeometryUids)
```
Get the unique IDs of all mesh geometry.

### GetAllMeshGeometryNotInstanced
```angelscript
void GetAllMeshGeometryNotInstanced(TArray<FString>& MeshGeometryUids)
```
Get the unique IDs of all non-instanced mesh geometry.

### GetAllMeshInstanceUids
```angelscript
void GetAllMeshInstanceUids(TArray<FString>& MeshInstanceUids)
```
Get the unique IDs of all mesh instances.

### GetAllMeshInstanceUidsUsingMeshGeometryUid
```angelscript
void GetAllMeshInstanceUidsUsingMeshGeometryUid(FString MeshGeometryUid, TArray<FString>& MeshInstanceUids)
```
Get all instanced mesh UIDs that use the mesh geometry unique ID.

### GetAllSkinnedMeshGeometry
```angelscript
void GetAllSkinnedMeshGeometry(TArray<FString>& MeshGeometryUids)
```
Get the unique IDs of all skinned mesh geometry.

### GetAllSkinnedMeshInstance
```angelscript
void GetAllSkinnedMeshInstance(TArray<FString>& MeshInstanceUids)
```
Get the unique IDs of all skinned mesh instances.

### GetAllStaticMeshGeometry
```angelscript
void GetAllStaticMeshGeometry(TArray<FString>& MeshGeometryUids)
```
Get the unique IDs of all static mesh geometry.

### GetAllStaticMeshInstance
```angelscript
void GetAllStaticMeshInstance(TArray<FString>& MeshInstanceUids)
```
Get the unique IDs of all static mesh instances.

### GetMeshGeometryByUid
```angelscript
FInterchangeMeshGeometry GetMeshGeometryByUid(FString MeshGeometryUid)
```
Get the geometry mesh from the unique ID.

### GetMeshGeometrySkeletonRootUid
```angelscript
FString GetMeshGeometrySkeletonRootUid(FString MeshGeometryUid)
```
Return the skeleton root node UID. This is the UID for a UInterchangeSceneNode that has a "Joint" specialized type.
Return an empty string if the MeshGeometryUid parameter points to nothing.

### GetMeshInstanceByUid
```angelscript
FInterchangeMeshInstance GetMeshInstanceByUid(FString MeshInstanceUid)
```
Get the instanced mesh from the unique ID.

### GetMeshInstanceSkeletonRootUid
```angelscript
FString GetMeshInstanceSkeletonRootUid(FString MeshInstanceUid)
```
Return the skeleton root node UID. This is the UID for a UInterchangeSceneNode that has a "Joint" specialized type.
Return an empty string if the MeshInstanceUid parameter points to nothing.

### IsValidMeshGeometryUid
```angelscript
bool IsValidMeshGeometryUid(FString MeshGeometryUid)
```
Return true if there is an existing FInterchangeMeshGeometry that matches the MeshInstanceUid key.

### IsValidMeshInstanceUid
```angelscript
bool IsValidMeshInstanceUid(FString MeshInstanceUid)
```
Return true if there is an existing FInterchangeMeshInstance that matches the MeshInstanceUid key.

### SetContext
```angelscript
void SetContext(FInterchangePipelineMeshesUtilitiesContext Context)
```


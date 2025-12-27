# UInterchangeStaticMeshLodDataNode

**继承自**: `UInterchangeFactoryBaseNode`

namespace UE

## 方法

### AddBoxCollisionMeshUid
```angelscript
bool AddBoxCollisionMeshUid(FString MeshName)
```

### AddCapsuleCollisionMeshUid
```angelscript
bool AddCapsuleCollisionMeshUid(FString MeshName)
```

### AddConvexCollisionMeshUid
```angelscript
bool AddConvexCollisionMeshUid(FString MeshName)
```

### AddMeshUid
```angelscript
bool AddMeshUid(FString MeshName)
```

### AddSphereCollisionMeshUid
```angelscript
bool AddSphereCollisionMeshUid(FString MeshName)
```

### GetBoxCollisionMeshUids
```angelscript
void GetBoxCollisionMeshUids(TArray<FString>& OutMeshNames)
```

### GetBoxCollisionMeshUidsCount
```angelscript
int GetBoxCollisionMeshUidsCount()
```

### GetCapsuleCollisionMeshUids
```angelscript
void GetCapsuleCollisionMeshUids(TArray<FString>& OutMeshNames)
```

### GetCapsuleCollisionMeshUidsCount
```angelscript
int GetCapsuleCollisionMeshUidsCount()
```

### GetConvexCollisionMeshUids
```angelscript
void GetConvexCollisionMeshUids(TArray<FString>& OutMeshNames)
```

### GetConvexCollisionMeshUidsCount
```angelscript
int GetConvexCollisionMeshUidsCount()
```

### GetImportCollision
```angelscript
bool GetImportCollision(bool& AttributeValue)
```

### GetMeshUids
```angelscript
void GetMeshUids(TArray<FString>& OutMeshNames)
```

### GetMeshUidsCount
```angelscript
int GetMeshUidsCount()
```
Mesh UIDs can be either a scene node or a mesh node UID. If it is a scene node, the mesh factory bakes the geometry payload with the global transform of the scene node.

### GetOneConvexHullPerUCX
```angelscript
bool GetOneConvexHullPerUCX(bool& AttributeValue)
```

### GetSphereCollisionMeshUids
```angelscript
void GetSphereCollisionMeshUids(TArray<FString>& OutMeshNames)
```

### GetSphereCollisionMeshUidsCount
```angelscript
int GetSphereCollisionMeshUidsCount()
```

### RemoveAllBoxCollisionMeshes
```angelscript
bool RemoveAllBoxCollisionMeshes()
```

### RemoveAllCapsuleCollisionMeshes
```angelscript
bool RemoveAllCapsuleCollisionMeshes()
```

### RemoveAllConvexCollisionMeshes
```angelscript
bool RemoveAllConvexCollisionMeshes()
```

### RemoveAllMeshes
```angelscript
bool RemoveAllMeshes()
```

### RemoveAllSphereCollisionMeshes
```angelscript
bool RemoveAllSphereCollisionMeshes()
```

### RemoveBoxCollisionMeshUid
```angelscript
bool RemoveBoxCollisionMeshUid(FString MeshName)
```

### RemoveCapsuleCollisionMeshUid
```angelscript
bool RemoveCapsuleCollisionMeshUid(FString MeshName)
```

### RemoveConvexCollisionMeshUid
```angelscript
bool RemoveConvexCollisionMeshUid(FString MeshName)
```

### RemoveMeshUid
```angelscript
bool RemoveMeshUid(FString MeshName)
```

### RemoveSphereCollisionMeshUid
```angelscript
bool RemoveSphereCollisionMeshUid(FString MeshName)
```

### SetImportCollision
```angelscript
bool SetImportCollision(bool AttributeValue)
```

### SetOneConvexHullPerUCX
```angelscript
bool SetOneConvexHullPerUCX(bool AttributeValue)
```


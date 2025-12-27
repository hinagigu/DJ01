# UMRMeshComponent

**继承自**: `UPrimitiveComponent`

## 属性

### bCreateMeshProxySections
- **类型**: `bool`
- **描述**: If true, MRMesh will create a renderable mesh proxy.  If false it will not, but could still provide collision.

### bUpdateNavMeshOnMeshUpdate
- **类型**: `bool`
- **描述**: If true, MRMesh will automatically update its navmesh whenever any Mesh section is updated. This may be expensive. If this is disabled use ForceNavMeshUpdate to trigger a navmesh update when necessary.  Moving the component will also trigger a navmesh update.

### bNeverCreateCollisionMesh
- **类型**: `bool`
- **描述**: If true, MRMesh will not create a collidable ridgid body for each mesh section and can therefore never have collision.  Avoids the cost of generating collision.

## 方法

### Clear
```angelscript
void Clear()
```

### ForceNavMeshUpdate
```angelscript
void ForceNavMeshUpdate()
```
Force navmesh generation to run using the current collision data.  This will run even if the collision data has not been udpated! Unless you are changing navmesh settings or similar RequestNavMeshUpdate is reccomended.

### GetEnableMeshOcclusion
```angelscript
bool GetEnableMeshOcclusion()
```

### GetUseWireframe
```angelscript
bool GetUseWireframe()
```

### GetWireframeColor
```angelscript
FLinearColor GetWireframeColor()
```

### IsConnected
```angelscript
bool IsConnected()
```

### RequestNavMeshUpdate
```angelscript
void RequestNavMeshUpdate()
```
Generate nav mesh if collision data has changed since the last nav mesh generation.

### SetEnableMeshOcclusion
```angelscript
void SetEnableMeshOcclusion(bool bEnable)
```

### SetUseWireframe
```angelscript
void SetUseWireframe(bool bUseWireframe)
```

### SetWireframeColor
```angelscript
void SetWireframeColor(FLinearColor InColor)
```

### SetWireframeMaterial
```angelscript
void SetWireframeMaterial(UMaterialInterface InMaterial)
```
Set the wireframe material.


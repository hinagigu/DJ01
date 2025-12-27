# UStaticMeshDescription

**继承自**: `UMeshDescriptionBase`

A wrapper for MeshDescription, customized for static meshes

## 方法

### CreateCube
```angelscript
void CreateCube(FVector Center, FVector HalfExtents, FPolygonGroupID PolygonGroup, FPolygonID& PolygonID_PlusX, FPolygonID& PolygonID_MinusX, FPolygonID& PolygonID_PlusY, FPolygonID& PolygonID_MinusY, FPolygonID& PolygonID_PlusZ, FPolygonID& PolygonID_MinusZ)
```

### GetVertexInstanceUV
```angelscript
FVector2D GetVertexInstanceUV(FVertexInstanceID VertexInstanceID, int UVIndex)
```

### SetPolygonGroupMaterialSlotName
```angelscript
void SetPolygonGroupMaterialSlotName(FPolygonGroupID PolygonGroupID, FName SlotName)
```

### SetVertexInstanceUV
```angelscript
void SetVertexInstanceUV(FVertexInstanceID VertexInstanceID, FVector2D UV, int UVIndex)
```


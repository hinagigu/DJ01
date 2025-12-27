# UBakeInputMeshProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### TargetUVLayer
- **类型**: `FString`
- **描述**: UV channel to use for the target mesh

### bHideSourceMesh
- **类型**: `bool`
- **描述**: If true, hide the source mesh

### SourceNormalMap
- **类型**: `UTexture2D`
- **描述**: Source mesh normal map; if empty, the geometric normals will be used

### SourceNormalMapUVLayer
- **类型**: `FString`
- **描述**: UV channel to use for the source mesh normal map; only relevant if a source normal map is set

### SourceNormalSpace
- **类型**: `EBakeNormalSpace`
- **描述**: Normal space of the source mesh normal map.

### ProjectionDistance
- **类型**: `float32`
- **描述**: Maximum allowed distance for the projection from target mesh to source mesh for the sample to be considered valid.
This is only relevant if a separate source mesh is provided.

### bProjectionInWorldSpace
- **类型**: `bool`
- **描述**: If true, uses the world space positions for the projection from target mesh to source mesh, otherwise it uses their object space positions.
This is only relevant if a separate source mesh is provided.


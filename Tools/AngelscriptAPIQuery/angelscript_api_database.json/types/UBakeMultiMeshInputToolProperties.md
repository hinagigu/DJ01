# UBakeMultiMeshInputToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### TargetUVLayer
- **类型**: `FString`
- **描述**: UV channel to use for the target mesh

### SourceMeshes
- **类型**: `TArray<FBakeMultiMeshDetailProperties>`
- **描述**: Source meshes and textures to sample from

### ProjectionDistance
- **类型**: `float32`
- **描述**: Maximum allowed distance for the projection from target mesh to source mesh for the sample to be considered valid.
This is only relevant if a separate source mesh is provided.


# UFbxSceneImportOptionsStaticMesh

**继承自**: `UObject`

## 属性

### VertexColorImportOption
- **类型**: `EFbxSceneVertexColorImportOption`
- **描述**: Specify how vertex colors should be imported

### VertexOverrideColor
- **类型**: `FColor`
- **描述**: Specify override color in the case that VertexColorImportOption is set to Override

### NormalImportMethod
- **类型**: `EFBXSceneNormalImportMethod`
- **描述**: Enabling this option will read the tangents(tangent,binormal,normal) from FBX file instead of generating them automatically.

### NormalGenerationMethod
- **类型**: `EFBXSceneNormalGenerationMethod`
- **描述**: Use the MikkTSpace tangent space generator for generating normals and tangents on the mesh

### bAutoGenerateCollision
- **类型**: `bool`

### bRemoveDegenerates
- **类型**: `bool`

### bBuildReversedIndexBuffer
- **类型**: `bool`

### bGenerateLightmapUVs
- **类型**: `bool`

### bOneConvexHullPerUCX
- **类型**: `bool`


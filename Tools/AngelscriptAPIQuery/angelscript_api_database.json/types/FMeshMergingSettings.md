# FMeshMergingSettings

Mesh merging settings

## 属性

### TargetLightMapResolution
- **类型**: `int`

### OutputUVs
- **类型**: `EUVOutput`
- **描述**: Whether to output the specified UV channels into the merged mesh (only if the source meshes contain valid UVs for the specified channel)

### MaterialSettings
- **类型**: `FMaterialProxySettings`

### GutterSize
- **类型**: `int`
- **描述**: The gutter (in texels) to add to each sub-chart for our baked-out material for the top mip level

### LODSelectionType
- **类型**: `EMeshLODSelectionType`

### SpecificLOD
- **类型**: `int`

### NaniteSettings
- **类型**: `FMeshNaniteSettings`

### bGenerateLightMapUV
- **类型**: `bool`

### bComputedLightMapResolution
- **类型**: `bool`

### bPivotPointAtZero
- **类型**: `bool`

### bMergePhysicsData
- **类型**: `bool`

### bMergeMeshSockets
- **类型**: `bool`

### bMergeMaterials
- **类型**: `bool`

### bBakeVertexDataToMesh
- **类型**: `bool`

### bUseVertexDataForBakingMaterial
- **类型**: `bool`

### bUseTextureBinning
- **类型**: `bool`

### bReuseMeshLightmapUVs
- **类型**: `bool`

### bMergeEquivalentMaterials
- **类型**: `bool`

### bUseLandscapeCulling
- **类型**: `bool`

### bIncludeImposters
- **类型**: `bool`

### bSupportRayTracing
- **类型**: `bool`

### bAllowDistanceField
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMeshMergingSettings& opAssign(FMeshMergingSettings Other)
```


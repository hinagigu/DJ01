# FMeshReductionSettings

Settings used to reduce a mesh.

## 属性

### PercentTriangles
- **类型**: `float32`

### MaxNumOfTriangles
- **类型**: `uint`
- **描述**: The maximum number of triangles to retain when using percentage termination criterion. (Triangles criterion properties)

### PercentVertices
- **类型**: `float32`

### MaxNumOfVerts
- **类型**: `uint`
- **描述**: The maximum number of vertices to retain when using percentage termination criterion. (Vertices criterion properties)

### MaxDeviation
- **类型**: `float32`

### PixelError
- **类型**: `float32`

### WeldingThreshold
- **类型**: `float32`

### HardAngleThreshold
- **类型**: `float32`

### BaseLODModel
- **类型**: `int`

### SilhouetteImportance
- **类型**: `EMeshFeatureImportance`

### TextureImportance
- **类型**: `EMeshFeatureImportance`

### ShadingImportance
- **类型**: `EMeshFeatureImportance`

### TerminationCriterion
- **类型**: `EStaticMeshReductionTerimationCriterion`

### VisibilityAggressiveness
- **类型**: `EMeshFeatureImportance`

### VertexColorImportance
- **类型**: `EMeshFeatureImportance`

### bRecalculateNormals
- **类型**: `bool`

### bGenerateUniqueLightmapUVs
- **类型**: `bool`

### bKeepSymmetry
- **类型**: `bool`

### bVisibilityAided
- **类型**: `bool`

### bCullOccluded
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMeshReductionSettings& opAssign(FMeshReductionSettings Other)
```


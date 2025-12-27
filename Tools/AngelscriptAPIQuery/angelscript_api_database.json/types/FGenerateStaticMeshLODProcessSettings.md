# FGenerateStaticMeshLODProcessSettings

## 属性

### MeshGenerator
- **类型**: `EGenerateStaticMeshLODProcess_MeshGeneratorModes`
- **描述**: Method used to generate the initial mesh for AutoLOD processing

### SolidifyVoxelResolution
- **类型**: `int`
- **描述**: Target number of voxels along the maximum dimension for Solidify operation

### WindingThreshold
- **类型**: `float32`
- **描述**: Winding number threshold to determine what is considered inside the mesh during Solidify

### ClosureDistance
- **类型**: `float32`
- **描述**: Offset distance in the Morpohological Closure operation

### bPrefilterVertices
- **类型**: `bool`
- **描述**: Whether to subsample input vertices using a regular grid before computing the convex hull

### PrefilterGridResolution
- **类型**: `int`
- **描述**: Grid resolution (along the maximum-length axis) for subsampling before computing the convex hull

## 方法

### opAssign
```angelscript
FGenerateStaticMeshLODProcessSettings& opAssign(FGenerateStaticMeshLODProcessSettings Other)
```


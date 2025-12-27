# FGenerateStaticMeshLODProcess_UVSettings

## 属性

### UVMethod
- **类型**: `EGenerateStaticMeshLODProcess_AutoUVMethod`

### NumUVAtlasCharts
- **类型**: `int`
- **描述**: Maximum number of charts to create in UVAtlas

### NumInitialPatches
- **类型**: `int`
- **描述**: Number of initial patches mesh will be split into before computing island merging

### MergingThreshold
- **类型**: `float32`
- **描述**: Distortion/Stretching Threshold for island merging - larger values increase the allowable UV stretching

### MaxAngleDeviation
- **类型**: `float32`
- **描述**: UV islands will not be merged if their average face normals deviate by larger than this amount

### PatchBuilder
- **类型**: `FGenerateStaticMeshLODProcess_UVSettings_PatchBuilder`

## 方法

### opAssign
```angelscript
FGenerateStaticMeshLODProcess_UVSettings& opAssign(FGenerateStaticMeshLODProcess_UVSettings Other)
```


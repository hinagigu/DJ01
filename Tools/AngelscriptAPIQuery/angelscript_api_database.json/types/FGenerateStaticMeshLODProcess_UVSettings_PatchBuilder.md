# FGenerateStaticMeshLODProcess_UVSettings_PatchBuilder

## 属性

### CurvatureAlignment
- **类型**: `float32`
- **描述**: This parameter controls alignment of the initial patches to creases in the mesh

### SmoothingSteps
- **类型**: `int`
- **描述**: Number of smoothing steps to apply; this slightly increases distortion but produces more stable results.

### SmoothingAlpha
- **类型**: `float32`
- **描述**: Smoothing parameter; larger values result in faster smoothing in each step.

## 方法

### opAssign
```angelscript
FGenerateStaticMeshLODProcess_UVSettings_PatchBuilder& opAssign(FGenerateStaticMeshLODProcess_UVSettings_PatchBuilder Other)
```


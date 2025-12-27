# UParameterizeMeshToolPatchBuilderProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### InitialPatches
- **类型**: `int`
- **描述**: Number of initial patches the mesh will be split into before island merging.

### CurvatureAlignment
- **类型**: `float32`
- **描述**: Alignment of the initial patches to creases in the mesh.

### MergingDistortionThreshold
- **类型**: `float32`
- **描述**: Threshold for stretching and distortion below which island merging is allowed; larger values increase the allowable UV distortion.

### MergingAngleThreshold
- **类型**: `float32`
- **描述**: Threshold for the average face normal deviation below which island merging is allowed.

### SmoothingSteps
- **类型**: `int`
- **描述**: Number of smoothing steps to apply; this slightly increases distortion but produces more stable results.

### SmoothingAlpha
- **类型**: `float32`
- **描述**: Smoothing parameter; larger values result in faster smoothing in each step.

### bRepack
- **类型**: `bool`
- **描述**: Automatically pack result UVs into the unit square, i.e. fit between 0 and 1 with no overlap.

### TextureResolution
- **类型**: `int`
- **描述**: Expected resolution of the output textures; this controls spacing left between UV islands to avoid interpolation artifacts. This is only enabled when Repack is enabled.

### bUsePolygroups
- **类型**: `bool`
- **描述**: Generate new UVs based on polygroups from specified layer.

### bLayoutUDIMPerPolygroup
- **类型**: `bool`
- **描述**: Layout resulting islands on UDIMs based on polygroups.


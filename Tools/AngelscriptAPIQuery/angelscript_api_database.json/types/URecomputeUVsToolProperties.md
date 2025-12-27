# URecomputeUVsToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### IslandGeneration
- **类型**: `ERecomputeUVsPropertiesIslandMode`
- **描述**: Generation method for initial UV islands.

### UnwrapType
- **类型**: `ERecomputeUVsPropertiesUnwrapType`
- **描述**: Type of UV flattening algorithm to use

### AutoRotation
- **类型**: `ERecomputeUVsToolOrientationMode`
- **描述**: Type of automatic rotation applied to each UV island

### bPreserveIrregularity
- **类型**: `bool`
- **描述**: If enabled, reduces distortion for meshes with triangles of vastly different sizes, This is only enabled if the Unwrap Type is set to Spectral Conformal.

### SmoothingSteps
- **类型**: `int`
- **描述**: Number of smoothing steps to apply; this slightly increases distortion but produces more stable results. This is only enabled if the Unwrap Type is set to ExpMap or Island Merging.

### SmoothingAlpha
- **类型**: `float32`
- **描述**: Smoothing parameter; larger values result in faster smoothing in each step. This is only enabled if the Unwrap Type is set to ExpMap or Island Merging.

### MergingDistortionThreshold
- **类型**: `float32`
- **描述**: Threshold for stretching and distortion below which island merging is allowed; larger values increase the allowable UV distortion. This is only enabled if the Unwrap Type is set to Island Merging.

### MergingAngleThreshold
- **类型**: `float32`
- **描述**: Threshold for the average face normal deviation below  which island merging is allowed. This is only enabled if the Unwrap Type is set to Island Merging.

### LayoutType
- **类型**: `ERecomputeUVsPropertiesLayoutType`
- **描述**: Uniformly scale and translate UV islands collectively to pack them into the unit square, i.e. fit between 0 and 1 with no overlap.

### TextureResolution
- **类型**: `int`
- **描述**: Expected resolution of the output textures; this controls spacing left between UV islands to avoid interpolation artifacts. This is only enabled when the Layout Type is set to Repack.

### NormalizeScale
- **类型**: `float32`
- **描述**: Scaling factor used for UV island normalization/scaling. This is only enabled when the Layout Type is set to Normalize to Bounds or Normalize to World.

### bEnableUDIMLayout
- **类型**: `bool`
- **描述**: Enable UDIM aware layout and keep islands within their originating UDIM tiles when laying out.


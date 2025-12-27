# UDiffusionSmoothProperties

**继承自**: `UInteractiveToolPropertySet`

Properties for Diffusion Smoothing

## 属性

### SmoothingPerStep
- **类型**: `float32`
- **描述**: Amount of smoothing allowed per step. Smaller steps will avoid things like collapse of small/thin features.

### Steps
- **类型**: `int`
- **描述**: Number of Smoothing iterations

### bPreserveUVs
- **类型**: `bool`
- **描述**: If this is false, the smoother will try to reshape the triangles to be more regular, which will distort UVs


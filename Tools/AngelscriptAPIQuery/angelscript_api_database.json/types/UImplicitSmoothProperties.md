# UImplicitSmoothProperties

**继承自**: `UInteractiveToolPropertySet`

Properties for Implicit smoothing

## 属性

### Smoothness
- **类型**: `float32`
- **描述**: Desired Smoothness. This is not a linear quantity, but larger numbers produce smoother results

### bPreserveUVs
- **类型**: `bool`
- **描述**: If this is false, the smoother will try to reshape the triangles to be more regular, which will distort UVs

### VolumeCorrection
- **类型**: `float32`
- **描述**: Magic number that allows you to try to correct for shrinking caused by smoothing


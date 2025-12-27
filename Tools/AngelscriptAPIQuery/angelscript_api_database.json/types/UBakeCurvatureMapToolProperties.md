# UBakeCurvatureMapToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### CurvatureType
- **类型**: `EBakeCurvatureTypeMode`
- **描述**: Type of curvature

### ColorMapping
- **类型**: `EBakeCurvatureColorMode`
- **描述**: How to map calculated curvature values to colors

### ColorRangeMultiplier
- **类型**: `float32`
- **描述**: Multiplier for how the curvature values fill the available range in the selected Color Mapping; a larger value means that higher curvature is required to achieve the maximum color value.

### MinRangeMultiplier
- **类型**: `float32`
- **描述**: Minimum for the curvature values to not be clamped to zero relative to the curvature for the maximum color value; a larger value means that higher curvature is required to not be considered as no curvature.

### Clamping
- **类型**: `EBakeCurvatureClampMode`
- **描述**: Clamping applied to curvature values before color mapping


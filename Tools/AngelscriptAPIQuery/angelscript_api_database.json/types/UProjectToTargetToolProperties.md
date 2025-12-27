# UProjectToTargetToolProperties

**继承自**: `URemeshMeshToolProperties`

Subclass URemeshMeshToolProperties just so we can set default values for some properties. Setting these values in the
Setup function of UProjectToTargetTool turns out to be tricky to achieve with the property cache.

## 属性

### bWorldSpace
- **类型**: `bool`

### bParallel
- **类型**: `bool`

### FaceProjectionPassesPerRemeshIteration
- **类型**: `int`

### SurfaceProjectionSpeed
- **类型**: `float32`

### NormalAlignmentSpeed
- **类型**: `float32`

### bSmoothInFillAreas
- **类型**: `bool`

### FillAreaDistanceMultiplier
- **类型**: `float32`

### FillAreaSmoothMultiplier
- **类型**: `float32`


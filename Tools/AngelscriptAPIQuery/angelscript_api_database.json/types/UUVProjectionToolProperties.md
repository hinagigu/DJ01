# UUVProjectionToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties

## 属性

### ProjectionType
- **类型**: `EUVProjectionMethod`
- **描述**: Shape and/or algorithm to use for UV projection

### Dimensions
- **类型**: `FVector`
- **描述**: Width, length, and height of the projection shape before rotation

### bProportionalDimensions
- **类型**: `bool`
- **描述**: If true, changes to Dimensions result in all components be changed proportionally

### Initialization
- **类型**: `EUVProjectionToolInitializationMode`
- **描述**: Determines how projection settings will be initialized; this only takes effect if the projection shape dimensions or position are unchanged

### CylinderSplitAngle
- **类型**: `float32`
- **描述**: Angle in degrees to determine whether faces should be assigned to the cylinder or the flat end caps

### ExpMapNormalBlending
- **类型**: `float32`
- **描述**: Blend between surface normals and projection normal; ExpMap projection becomes Plane projection when this value is 1

### ExpMapSmoothingSteps
- **类型**: `int`
- **描述**: Number of smoothing steps to apply; this slightly increases distortion but produces more stable results.

### ExpMapSmoothingAlpha
- **类型**: `float32`
- **描述**: Smoothing parameter; larger values result in faster smoothing in each step.

### Rotation
- **类型**: `float32`
- **描述**: Rotation in degrees applied after computing projection

### Scale
- **类型**: `FVector2D`
- **描述**: Scaling applied after computing projection

### Translation
- **类型**: `FVector2D`
- **描述**: Translation applied after computing projection


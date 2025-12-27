# UBakeOcclusionMapToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### OcclusionRays
- **类型**: `int`
- **描述**: Number of occlusion rays per sample

### MaxDistance
- **类型**: `float32`
- **描述**: Maximum distance for occlusion rays to test for intersections; a value of 0 means infinity

### SpreadAngle
- **类型**: `float32`
- **描述**: Maximum spread angle in degrees for occlusion rays; for example, 180 degrees will cover the entire hemisphere whereas 90 degrees will only cover the center of the hemisphere down to 45 degrees from the horizon.

### BiasAngle
- **类型**: `float32`
- **描述**: Angle in degrees from the horizon for occlusion rays for which the contribution is attenuated to reduce faceting artifacts.


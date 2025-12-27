# UMaterialExpressionSpeedTree

**继承自**: `UMaterialExpression`

## 属性

### GeometryType
- **类型**: `ESpeedTreeGeometryType`
- **描述**: The type of SpeedTree geometry on which this material will be used

### WindType
- **类型**: `ESpeedTreeWindType`
- **描述**: The type of wind effect used on this tree. This can only go as high as it was in the SpeedTree Modeler, but you can set it to a lower option for lower quality wind and faster rendering.

### LODType
- **类型**: `ESpeedTreeLODType`
- **描述**: The type of LOD to use

### BillboardThreshold
- **类型**: `float32`
- **描述**: The threshold for triangles to be removed from the bilboard mesh when not facing the camera (0 = none pass, 1 = all pass).

### bAccurateWindVelocities
- **类型**: `bool`
- **描述**: Support accurate velocities from wind. This will incur extra cost per vertex.


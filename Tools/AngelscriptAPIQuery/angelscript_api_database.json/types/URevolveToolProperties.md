# URevolveToolProperties

**继承自**: `URevolveProperties`

## 属性

### CapFillMode
- **类型**: `ERevolvePropertiesCapFillMode`
- **描述**: Determines how end caps are created. This is not relevant if the end caps are not visible or if the path is not closed.

### bClosePathToAxis
- **类型**: `bool`
- **描述**: Connect the ends of an open path to the axis to add caps to the top and bottom of the revolved result.
This is not relevant for paths that are already closed.

### DrawPlaneOrigin
- **类型**: `FVector`
- **描述**: Sets the draw plane origin. The revolution axis is the X axis in the plane.

### DrawPlaneOrientation
- **类型**: `FRotator`
- **描述**: Sets the draw plane orientation. The revolution axis is the X axis in the plane.

### bEnableSnapping
- **类型**: `bool`
- **描述**: Enables snapping while editing the path.


# URevolveSplineToolProperties

**继承自**: `URevolveProperties`

## 属性

### SampleMode
- **类型**: `ERevolveSplineSampleMode`
- **描述**: Determines how points to revolve are actually picked from the spline.

### ErrorTolerance
- **类型**: `float`
- **描述**: How far to allow the triangulation boundary can deviate from the spline curve before we add more vertices.

### MaxSampleDistance
- **类型**: `float`
- **描述**: The maximal distance that the spacing should be allowed to be.

### CapFillMode
- **类型**: `ERevolvePropertiesCapFillMode`
- **描述**: Determines how end caps are created. This is not relevant if the end caps are not visible or if the path is not closed.

### bClosePathToAxis
- **类型**: `bool`
- **描述**: Connect the ends of an open path to the axis to add caps to the top and bottom of the revolved result.
This is not relevant for paths that are already closed.

### AxisOrigin
- **类型**: `FVector`
- **描述**: Sets the revolution axis origin.

### AxisOrientation
- **类型**: `FVector2D`
- **描述**: Sets the revolution axis pitch and yaw.

### bResetAxisOnStart
- **类型**: `bool`
- **描述**: If true, the revolution axis is re-fit to the input spline on each tool start. If false, the previous
revolution axis is kept.


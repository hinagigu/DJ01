# UMeshSpaceDeformerToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### SelectedOperationType
- **类型**: `ENonlinearOperationType`

### UpperBoundsInterval
- **类型**: `float32`
- **描述**: The upper bound to the region of space which the operation will affect. Measured along the gizmo Z axis from the gizmo center.

### LowerBoundsInterval
- **类型**: `float32`
- **描述**: The lower bound to the region of space which the operation will affect. Measured along the gizmo Z axis from the gizmo center.

### BendDegrees
- **类型**: `float32`
- **描述**: A line along the Z axis of the gizmo from lower bound to upper bound will be bent into a perfect arc of this
many degrees in the direction of the Y axis without changing length.

### TwistDegrees
- **类型**: `float32`
- **描述**: Degrees of twist to from the lower bound to the upper bound along the gizmo Z axis.

### FlareProfileType
- **类型**: `EFlareProfileType`
- **描述**: Determines the profile used as a displacement

### FlarePercentY
- **类型**: `float32`
- **描述**: Determines how much to flare perpendicular to the Z axis. When set to 100%, points are moved double the distance
away from the gizmo Z axis at the most extreme flare point. 0% does not flare at all, whereas -100% pinches all
the way to the gizmo Z axis at the most extreme flare point.

### bLockXAndYFlaring
- **类型**: `bool`
- **描述**: If true, flaring is applied along the gizmo X and Y axis the same amount.

### FlarePercentX
- **类型**: `float32`
- **描述**: Determines how much to flare perpendicular to the Z axis in the X direction if the flaring is not locked
to be the same in the X and Y directions.

### bLockBottom
- **类型**: `bool`
- **描述**: If true, the "bottom" of the mesh relative to the gizmo Z axis will stay in place while the rest bends or twists. If false, the bend
or twist will happen around the gizmo location.

### bShowOriginalMesh
- **类型**: `bool`

### bDrawVisualization
- **类型**: `bool`

### bAlignToNormalOnCtrlClick
- **类型**: `bool`
- **描述**: When true, Ctrl+click not only moves the gizmo to the clicked location, but also aligns the Z axis with the normal at that point.


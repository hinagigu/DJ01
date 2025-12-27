# UPolyEditOffsetProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### DistanceMode
- **类型**: `EPolyEditExtrudeDistanceMode`
- **描述**: How the offset distance is set.

### Distance
- **类型**: `float`
- **描述**: Offset distance.

### DirectionMode
- **类型**: `EPolyEditOffsetModeOptions`
- **描述**: Which way to move vertices during the offset

### MaxDistanceScaleFactor
- **类型**: `float`
- **描述**: Controls the maximum distance vertices can move from the target distance in order to stay parallel with their source triangles.

### bShellsToSolids
- **类型**: `bool`
- **描述**: Controls whether offsetting an entire open-border patch should create a solid or an open shell

### MeasureDirection
- **类型**: `EPolyEditExtrudeDirection`
- **描述**: What axis to measure the offset distance along.

### bUseColinearityForSettingBorderGroups
- **类型**: `bool`
- **描述**: When offsetting regions that touch the mesh border, assign the side groups (groups on the
stitched side of the offset) in a way that considers edge colinearity. For instance, when
true, extruding a flat rectangle will give four different groups on its sides rather than
one connected group.


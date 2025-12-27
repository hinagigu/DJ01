# UEdgeLoopInsertionProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### PositionMode
- **类型**: `EEdgeLoopPositioningMode`
- **描述**: Determines how edge loops position themselves vertically relative to loop direction.

### InsertionMode
- **类型**: `EEdgeLoopInsertionMode`
- **描述**: Determines how edge loops are added to the geometry

### NumLoops
- **类型**: `int`
- **描述**: How many loops to insert at a time. Only used with "even" positioning mode.

### ProportionOffset
- **类型**: `float`

### DistanceOffset
- **类型**: `float`

### bInteractive
- **类型**: `bool`
- **描述**: When false, the distance/proportion offset is numerically specified, and mouse clicks just choose the edge.

### bFlipOffsetDirection
- **类型**: `bool`
- **描述**: Measure the distance offset from the opposite side of the edges.

### bHighlightProblemGroups
- **类型**: `bool`
- **描述**: When true, non-quad-like groups that stop the loop will be highlighted, with X's marking the corners.

### VertexTolerance
- **类型**: `float`
- **描述**: How close a new loop edge needs to pass next to an existing vertex to use that vertex rather than creating a new one.


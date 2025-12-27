# UGroupEdgeInsertionProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### InsertionMode
- **类型**: `EGroupEdgeInsertionMode`
- **描述**: Determines how group edges are added to the geometry

### bContinuousInsertion
- **类型**: `bool`
- **描述**: If true, edge insertions are chained together so that each end point becomes the new start point

### VertexTolerance
- **类型**: `float`
- **描述**: How close a new loop edge needs to pass next to an existing vertex to use that vertex rather than creating a new one (used for plane cut).


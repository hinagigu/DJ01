# URevolveProperties

**继承自**: `UInteractiveToolPropertySet`

Common properties for revolving a PolyPath to create a mesh.

## 属性

### RevolveDegreesClamped
- **类型**: `float`
- **描述**: Revolution extent in degrees. Clamped to a maximum of 360 if Height Offset Per Degree is set to 0.

### RevolveDegrees
- **类型**: `float`
- **描述**: Revolution extent in degrees. Clamped to a maximum of 360 if Height Offset Per Degree is set to 0.

### RevolveDegreesOffset
- **类型**: `float`
- **描述**: The angle by which to rotate the path around the axis before beginning the revolve.

### StepsMaxDegrees
- **类型**: `float`
- **描述**: Implicitly defines the number of steps in the revolution such that each step moves the revolution no more than the given number of degrees. This is only available if Explicit Steps is disabled.

### bExplicitSteps
- **类型**: `bool`
- **描述**: If true, the number of steps can be specified explicitly via Steps. If false, the number of steps is adjusted automatically based on Steps Max Degrees.

### NumExplicitSteps
- **类型**: `int`
- **描述**: Number of steps in the revolution. This is only available if Explicit Steps is enabled.

### HeightOffsetPerDegree
- **类型**: `float`
- **描述**: How far to move each step along the revolution axis per degree. Non-zero values are useful for creating spirals.

### bReverseRevolutionDirection
- **类型**: `bool`
- **描述**: By default, revolution is done counterclockwise if looking down the revolution axis. This reverses the revolution direction to clockwise.

### bFlipMesh
- **类型**: `bool`
- **描述**: Flips the mesh inside out.

### bSharpNormals
- **类型**: `bool`
- **描述**: If true, normals are not averaged or shared between triangles beyond the Sharp Normals Degree Threshold.

### SharpNormalsDegreeThreshold
- **类型**: `float`
- **描述**: The threshold in degrees beyond which normals are not averaged or shared between triangles anymore. This is only available if Sharp Normals is enabled.

### bPathAtMidpointOfStep
- **类型**: `bool`
- **描述**: If true, the path is placed at the midpoint of each step instead of at the start and/or end of a step. For example, this is useful for creating square columns.

### PolygroupMode
- **类型**: `ERevolvePropertiesPolygroupMode`
- **描述**: How PolyGroups are assigned to shape primitives. If caps are generated, they will always be in separate groups.

### QuadSplitMode
- **类型**: `ERevolvePropertiesQuadSplit`
- **描述**: How generated quads are split into triangles.


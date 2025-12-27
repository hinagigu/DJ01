# UPatternToolSettings

**继承自**: `UInteractiveToolPropertySet`

Settings for the Pattern Tool

## 属性

### Seed
- **类型**: `int`
- **描述**: The seed used to introduce random transform variations when enabled

### bProjectElementsDown
- **类型**: `bool`
- **描述**: Whether or not the pattern items should be projected along the negative Z axis of the plane mechanic

### ProjectionOffset
- **类型**: `float32`
- **描述**: How much each pattern item should be moved along the negative Z axis of the plane mechanic if Project Elements Down is enabled

### bHideSources
- **类型**: `bool`
- **描述**: Hide the source meshes when enabled

### bUseRelativeTransforms
- **类型**: `bool`
- **描述**: If false, all pattern elements will be positioned at the origin of the first pattern element

### bRandomlyPickElements
- **类型**: `bool`
- **描述**: Whether to randomly pick which source mesh is scattered at each location, or to always use all source meshes

### Shape
- **类型**: `EPatternToolShape`
- **描述**: Shape of the underlying Pattern

### SingleAxis
- **类型**: `EPatternToolSingleAxis`
- **描述**: Axis direction used for the Pattern geometry

### SinglePlane
- **类型**: `EPatternToolSinglePlane`
- **描述**: Plane used for the Pattern geometry


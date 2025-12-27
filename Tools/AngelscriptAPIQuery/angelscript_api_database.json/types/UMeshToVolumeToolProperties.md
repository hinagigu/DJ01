# UMeshToVolumeToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### ConversionMode
- **类型**: `EMeshToVolumeMode`
- **描述**: Method for converting the input mesh to a set of Planar Polygonal Faces in the output Volume.

### bPreserveGroupBoundaries
- **类型**: `bool`
- **描述**: When true, adjacent coplanar groups will not be merged together into single faces. Not relevant if
conversion mode is set to emit all triangles separately.

### bAutoSimplify
- **类型**: `bool`
- **描述**: Determines whether mesh gets auto simplified when its triangle count is too high.

### SimplifyMaxTriangles
- **类型**: `int`
- **描述**: Target triangle count for auto simplification when Auto Simplify is true.

### NewVolumeType
- **类型**: `TSubclassOf<AVolume>`
- **描述**: Type of new Volume to create on Accept


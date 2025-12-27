# UVoxelSolidifyMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Properties of the solidify operation

## 属性

### WindingThreshold
- **类型**: `float`
- **描述**: Winding number threshold to determine what is consider inside the mesh

### ExtendBounds
- **类型**: `float`
- **描述**: How far we allow bounds of solid surface to go beyond the bounds of the original input surface before clamping / cutting the surface off

### SurfaceSearchSteps
- **类型**: `int`
- **描述**: How many binary search steps to take when placing vertices on the surface

### bSolidAtBoundaries
- **类型**: `bool`
- **描述**: Whether to fill at the border of the bounding box, if the surface extends beyond the voxel boundaries

### ThickenShells
- **类型**: `float`
- **描述**: Thicken open-boundary surfaces (extrude them inwards) to ensure they are captured in the VoxWrap output. Units are in world space.


# UVoxelProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### VoxelCount
- **类型**: `int`
- **描述**: The size of the geometry bounding box major axis measured in voxels

### bAutoSimplify
- **类型**: `bool`
- **描述**: Automatically simplify the result of voxel-based meshes.

### bRemoveInternalSurfaces
- **类型**: `bool`
- **描述**: Remove internal, occluded geometry

### SimplifyMaxErrorFactor
- **类型**: `float`
- **描述**: The max error (as a multiple of the voxel size) to accept when simplifying the output

### CubeRootMinComponentVolume
- **类型**: `float`
- **描述**: Automatically remove components smaller than this (to clean up any isolated floating bits)


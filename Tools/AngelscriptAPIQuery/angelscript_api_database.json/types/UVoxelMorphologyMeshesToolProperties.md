# UVoxelMorphologyMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Properties of the morphology tool

## 属性

### Operation
- **类型**: `EMorphologyOperation`
- **描述**: Which offset (or morphology) operation to apply

### Distance
- **类型**: `float`
- **描述**: Distance to offset the mesh

### bVoxWrap
- **类型**: `bool`
- **描述**: Apply a "VoxWrap" operation to input mesh(es) before computing the morphology.  Fixes results for inputs with holes and/or self-intersections.

### bRemoveInternalsAfterVoxWrap
- **类型**: `bool`
- **描述**: Remove internal surfaces from the VoxWrap output, before computing the morphology.

### ThickenShells
- **类型**: `float`
- **描述**: Thicken open-boundary surfaces (extrude them inwards) before VoxWrapping them. Units are in world space. If 0, no extrusion is applied.


# UVoxelBlendMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Properties of the blend operation

## 属性

### BlendPower
- **类型**: `float`
- **描述**: Blend power controls the shape of the blend between shapes

### BlendFalloff
- **类型**: `float`
- **描述**: Blend falloff controls the size of the blend region

### Operation
- **类型**: `EVoxelBlendOperation`
- **描述**: How to combine the shapes

### bVoxWrap
- **类型**: `bool`
- **描述**: Apply a "VoxWrap" operation to input mesh(es) before computing the blend.  Fixes results for inputs with holes and/or self-intersections.

### bRemoveInternalsAfterVoxWrap
- **类型**: `bool`
- **描述**: Remove internal surfaces from the VoxWrap output, before computing the blend.

### ThickenShells
- **类型**: `float`
- **描述**: Thicken open-boundary surfaces (extrude them inwards) before VoxWrapping them. Units are in world space. If 0 then no extrusion is applied.


# UNewMeshMaterialProperties

**继承自**: `UInteractiveToolPropertySet`

Standard material property settings for tools that generate new meshes

## 属性

### Material
- **类型**: `TWeakObjectPtr<UMaterialInterface>`
- **描述**: Material for new mesh

### UVScale
- **类型**: `float32`
- **描述**: Scale factor for generated UVs

### bWorldSpaceUVScale
- **类型**: `bool`
- **描述**: If true, UV scale will be relative to world space. This means objects of different sizes created with the same UV scale have the same average texel size.

### bShowWireframe
- **类型**: `bool`
- **描述**: If true, overlays preview with wireframe


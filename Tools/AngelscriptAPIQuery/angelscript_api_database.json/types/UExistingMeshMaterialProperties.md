# UExistingMeshMaterialProperties

**继承自**: `UInteractiveToolPropertySet`

Standard material property settings for tools that visualize materials on existing meshes (e.g. to help show UVs)

## 属性

### MaterialMode
- **类型**: `ESetMeshMaterialMode`
- **描述**: Material that will be used on the mesh

### CheckerDensity
- **类型**: `float32`
- **描述**: Number of checkerboard tiles within the 0 to 1 range; only available when Checkerboard is selected as material mode

### OverrideMaterial
- **类型**: `UMaterialInterface`
- **描述**: Material to use instead of the original material; only available when Override is selected as material mode

### UVChannel
- **类型**: `FString`
- **描述**: Which UV channel to use for visualizing the checkerboard material on the mesh; note that this does not affect the preview layout


# UTrimMeshesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Properties of the trim mode

## 属性

### WhichMesh
- **类型**: `ETrimOperation`
- **描述**: Which object to trim

### TrimSide
- **类型**: `ETrimSide`
- **描述**: Whether to remove the surface inside or outside of the trimming geometry

### WindingThreshold
- **类型**: `float32`
- **描述**: Threshold to determine whether a triangle in one mesh is inside or outside of the other

### bShowTrimmingMesh
- **类型**: `bool`
- **描述**: Whether to show a translucent version of the trimming mesh, to help visualize what is being cut

### OpacityOfTrimmingMesh
- **类型**: `float32`
- **描述**: Opacity of translucent version of the trimming mesh

### ColorOfTrimmingMesh
- **类型**: `FLinearColor`
- **描述**: Color of translucent version of the trimming mesh


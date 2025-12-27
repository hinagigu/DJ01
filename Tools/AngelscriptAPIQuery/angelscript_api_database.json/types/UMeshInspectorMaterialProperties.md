# UMeshInspectorMaterialProperties

**继承自**: `UInteractiveToolPropertySet`

material settings for mesh inspector tool

## 属性

### MaterialMode
- **类型**: `EMeshInspectorMaterialMode`
- **描述**: Material that will be used to render the mesh

### CheckerDensity
- **类型**: `float32`
- **描述**: Number of checkerboard tiles within the 0 to 1 range; only available when Checkerboard is selected as material mode

### OverrideMaterial
- **类型**: `UMaterialInterface`
- **描述**: Material to use instead of the original material; only available when Override is selected as material mode

### UVChannel
- **类型**: `FString`
- **描述**: Which UV channel to use for visualizing the checkerboard material on the mesh; note that this does not affect the preview layout

### bFlatShading
- **类型**: `bool`
- **描述**: Toggle flat shading on/off

### Color
- **类型**: `FLinearColor`
- **描述**: Main Color of Material

### Opacity
- **类型**: `float`
- **描述**: Opacity of transparent material

### TransparentMaterialColor
- **类型**: `FLinearColor`

### bTwoSided
- **类型**: `bool`
- **描述**: Although a two-sided transparent material causes rendering issues with overlapping faces, it is still frequently useful to see the shape when sculpting around other objects.


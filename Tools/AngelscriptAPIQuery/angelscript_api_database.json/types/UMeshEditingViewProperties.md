# UMeshEditingViewProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### bShowWireframe
- **类型**: `bool`
- **描述**: Toggle drawing of wireframe overlay on/off [Alt+W]

### MaterialMode
- **类型**: `EMeshEditingMaterialModes`
- **描述**: Set which material to use on object

### bFlatShading
- **类型**: `bool`
- **描述**: Toggle flat shading on/off

### Color
- **类型**: `FLinearColor`
- **描述**: Main Color of Material

### Image
- **类型**: `UTexture2D`
- **描述**: Image used in Image-Based Material

### Opacity
- **类型**: `float`
- **描述**: Opacity of transparent material

### TransparentMaterialColor
- **类型**: `FLinearColor`

### bTwoSided
- **类型**: `bool`
- **描述**: Although a two-sided transparent material causes rendering issues with overlapping faces, it is still frequently useful to see the shape when sculpting around other objects.

### CustomMaterial
- **类型**: `TWeakObjectPtr<UMaterialInterface>`


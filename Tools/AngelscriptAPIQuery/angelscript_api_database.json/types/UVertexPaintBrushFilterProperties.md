# UVertexPaintBrushFilterProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### BrushAreaMode
- **类型**: `EMeshVertexPaintBrushAreaType`
- **描述**: Area Mode specifies the shape of the brush and which triangles will be included relative to the cursor

### AngleThreshold
- **类型**: `float32`
- **描述**: The Region affected by the current operation will be bounded by edge angles larger than this threshold

### bUVSeams
- **类型**: `bool`
- **描述**: The Region affected by the current operation will be bounded by UV borders/seams

### bNormalSeams
- **类型**: `bool`
- **描述**: The Region affected by the current operation will be bounded by Hard Normal edges/seams

### VisibilityFilter
- **类型**: `EMeshVertexPaintVisibilityType`
- **描述**: Control which triangles can be affected by the current operation based on visibility. Applied after all other filters.

### MaterialMode
- **类型**: `EMeshVertexPaintMaterialMode`
- **描述**: Specify which Materials should be used to render the Mesh

### bShowHitColor
- **类型**: `bool`
- **描述**: Display the Color under the cursor


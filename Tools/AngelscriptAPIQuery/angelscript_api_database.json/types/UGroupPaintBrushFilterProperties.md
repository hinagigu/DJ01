# UGroupPaintBrushFilterProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### SubToolType
- **类型**: `EMeshGroupPaintInteractionType`

### BrushSize
- **类型**: `float32`
- **描述**: Relative size of brush

### BrushAreaMode
- **类型**: `EMeshGroupPaintBrushAreaType`
- **描述**: When Volumetric, all faces inside the brush sphere are selected, otherwise only connected faces are selected

### bHitBackFaces
- **类型**: `bool`
- **描述**: Allow the Brush to hit the back-side of the mesh

### SetGroup
- **类型**: `int`
- **描述**: The group that will be assigned to triangles

### bOnlySetUngrouped
- **类型**: `bool`
- **描述**: If true, only triangles with no group assigned will be painted

### EraseGroup
- **类型**: `int`
- **描述**: Group to set as Erased value

### bOnlyEraseCurrent
- **类型**: `bool`
- **描述**: When enabled, only the current group configured in the Paint brush is erased

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
- **类型**: `EMeshGroupPaintVisibilityType`
- **描述**: Control which triangles can be affected by the current operation based on visibility. Applied after all other filters.

### MinTriVertCount
- **类型**: `int`
- **描述**: Number of vertices in a triangle the Lasso must hit to be counted as "inside"

### bShowHitGroup
- **类型**: `bool`
- **描述**: Display the Group ID of the last triangle under the cursor

### bShowAllGroups
- **类型**: `bool`
- **描述**: Display the Group ID for all visible groups in the mesh


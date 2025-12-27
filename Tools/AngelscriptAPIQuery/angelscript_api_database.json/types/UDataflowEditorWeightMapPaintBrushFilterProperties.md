# UDataflowEditorWeightMapPaintBrushFilterProperties

**继承自**: `UInteractiveToolPropertySet`

TODO: Look at EditConditions for all these properties. Which ones make sense for which SubToolType?

## 属性

### SubToolType
- **类型**: `EDataflowEditorWeightMapPaintInteractionType`

### PrimaryBrushType
- **类型**: `EDataflowEditorWeightMapPaintBrushType`

### BrushSize
- **类型**: `float32`
- **描述**: Relative size of brush

### AttributeValue
- **类型**: `float`
- **描述**: The new value to paint on the mesh

### Strength
- **类型**: `float`
- **描述**: How quickly each brush stroke will drive mesh values towards the desired value

### GradientHighValue
- **类型**: `float`
- **描述**: The Gradient upper limit value

### GradientLowValue
- **类型**: `float`
- **描述**: The Gradient lower limit value

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
- **类型**: `EDataflowEditorWeightMapPaintVisibilityType`
- **描述**: Control which triangles can be affected by the current operation based on visibility. Applied after all other filters.


# UVertexBrushSculptProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### PrimaryBrushType
- **类型**: `EMeshVertexSculptBrushType`
- **描述**: Primary Brush Mode

### PrimaryFalloffType
- **类型**: `EMeshSculptFalloffType`
- **描述**: Primary Brush Falloff Type, multiplied by Alpha Mask where applicable

### BrushFilter
- **类型**: `EMeshVertexSculptBrushFilterType`
- **描述**: Filter applied to Stamp Region Triangles, based on first Stroke Stamp

### bFreezeTarget
- **类型**: `bool`
- **描述**: When Freeze Target is toggled on, the Brush Target Surface will be Frozen in its current state, until toggled off. Brush strokes will be applied relative to the Target Surface, for applicable Brushes


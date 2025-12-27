# UVertexPaintBasicProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### SubToolType
- **类型**: `EMeshVertexPaintInteractionType`
- **描述**: Painting Operation to apply when left-clicking and dragging

### PaintColor
- **类型**: `FLinearColor`
- **描述**: The Color that will be assigned to painted triangle vertices

### BlendMode
- **类型**: `EMeshVertexPaintColorBlendMode`
- **描述**: Controls how painted Colors will be combined with the existing Colors

### SecondaryActionType
- **类型**: `EMeshVertexPaintSecondaryActionType`
- **描述**: The Brush Operation that will be applied when holding the Shift key when in Painting

### EraseColor
- **类型**: `FLinearColor`
- **描述**: Color to set when using Erase brush

### SmoothStrength
- **类型**: `float32`
- **描述**: Strength of Smooth Brush

### ChannelFilter
- **类型**: `FModelingToolsColorChannelFilter`
- **描述**: Controls which Color Channels will be affected by Operations. Only enabled Channels are rendered.

### bHardEdges
- **类型**: `bool`
- **描述**: Create Split Colors / Hard Color Edges at the borders of the painted area. Use Soften operations to un-split.


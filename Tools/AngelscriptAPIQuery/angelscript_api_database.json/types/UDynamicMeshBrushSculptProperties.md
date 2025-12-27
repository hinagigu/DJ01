# UDynamicMeshBrushSculptProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### PrimaryBrushType
- **类型**: `EDynamicMeshSculptBrushType`
- **描述**: Primary Brush Mode

### PrimaryBrushSpeed
- **类型**: `float32`
- **描述**: Strength of the Primary Brush

### bPreserveUVFlow
- **类型**: `bool`
- **描述**: If true, try to preserve the shape of the UV/3D mapping. This will limit Smoothing and Remeshing in some cases.

### bFreezeTarget
- **类型**: `bool`
- **描述**: When Freeze Target is toggled on, the Brush Target Surface will be Frozen in its current state, until toggled off. Brush strokes will be applied relative to the Target Surface, for applicable Brushes

### SmoothBrushSpeed
- **类型**: `float32`
- **描述**: Strength of Shift-to-Smooth Brushing and Smoothing Brush

### bDetailPreservingSmooth
- **类型**: `bool`
- **描述**: If enabled, Remeshing is limited during Smoothing to avoid wiping out higher-density triangle areas


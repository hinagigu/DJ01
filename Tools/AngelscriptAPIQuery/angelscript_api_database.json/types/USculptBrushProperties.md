# USculptBrushProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### BrushSize
- **类型**: `FBrushToolRadius`

### BrushFalloffAmount
- **类型**: `float32`
- **描述**: Amount of falloff to apply (0.0 - 1.0)

### Depth
- **类型**: `float32`
- **描述**: Depth of Brush into surface along view ray or surface normal, depending on the Active Brush Type

### bHitBackFaces
- **类型**: `bool`
- **描述**: Allow the Brush to hit the back-side of the mesh

### FlowRate
- **类型**: `float32`
- **描述**: Brush stamps are applied at this time interval. 0 for a single stamp, 1 for continuous stamps, 0.5 is a stamp every half-second

### Spacing
- **类型**: `float32`
- **描述**: Space out stamp centers at distances Spacing*BrushDiameter along the stroke (so Spacing of 1 means that stamps will be adjacent but non-overlapping). Zero spacing means continuous stamps.

### Lazyness
- **类型**: `float32`
- **描述**: Lazy brush smooths out the brush path by averaging the cursor positions


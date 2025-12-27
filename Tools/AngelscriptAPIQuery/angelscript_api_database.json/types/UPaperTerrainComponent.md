# UPaperTerrainComponent

**继承自**: `UPrimitiveComponent`

The terrain visualization component for an associated spline component.
This takes a 2D terrain material and instances sprite geometry along the spline path.

## 属性

### TerrainMaterial
- **类型**: `UPaperTerrainMaterial`

### bClosedSpline
- **类型**: `bool`

### bFilledSpline
- **类型**: `bool`

### RandomSeed
- **类型**: `int`
- **描述**: Random seed used for choosing which spline meshes to use.

### SegmentOverlapAmount
- **类型**: `float32`
- **描述**: The overlap amount between segments

### ReparamStepsPerSegment
- **类型**: `int`
- **描述**: Number of steps per spline segment to place in the reparameterization table

### SpriteCollisionDomain
- **类型**: `ESpriteCollisionMode`
- **描述**: Collision domain (no collision, 2D (experimental), or 3D)

### CollisionThickness
- **类型**: `float32`
- **描述**: The extrusion thickness of collision geometry when using a 3D collision domain

### TerrainColor
- **类型**: `FLinearColor`

## 方法

### SetTerrainColor
```angelscript
void SetTerrainColor(FLinearColor NewColor)
```
Set color of the terrain


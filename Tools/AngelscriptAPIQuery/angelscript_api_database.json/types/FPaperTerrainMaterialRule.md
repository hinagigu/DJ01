# FPaperTerrainMaterialRule

Rule for a single section of a terrain material

## 属性

### StartCap
- **类型**: `UPaperSprite`
- **描述**: The sprite to use at the 'left' (closest to spline start) edge of the terrain segment

### Body
- **类型**: `TArray<TObjectPtr<UPaperSprite>>`
- **描述**: A set of sprites to randomly choose to fill up the interior space between the caps in a terrain segment

### EndCap
- **类型**: `UPaperSprite`
- **描述**: The sprite to use at the 'right' (closest to spline end) edge of the terrain segment

### MinimumAngle
- **类型**: `float32`
- **描述**: Minimum slope angle (in degrees) to apply this rule

### MaximumAngle
- **类型**: `float32`
- **描述**: Maximum slope angle (in degrees) to apply this rule

### bEnableCollision
- **类型**: `bool`
- **描述**: If true, collision is enabled for sections matching this rule

### CollisionOffset
- **类型**: `float32`
- **描述**: How much should the collision be lofted from the spline (positive values go out from the spline, negative values go in to the spline)

### DrawOrder
- **类型**: `int`
- **描述**: Specify a draw order for different materials in a spline. Smaller draw orders are drawn first, negative values are allowed.

### Description
- **类型**: `FText`
- **描述**: Readable description for the rule (unused anywhere, just for clarity when editing the material)

## 方法

### opAssign
```angelscript
FPaperTerrainMaterialRule& opAssign(FPaperTerrainMaterialRule Other)
```


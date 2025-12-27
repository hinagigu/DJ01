# UMaterialExpressionSceneDepthWithoutWater

**继承自**: `UMaterialExpression`

## 属性

### InputMode
- **类型**: `EMaterialSceneAttributeInputMode`
- **描述**: Coordinates - UV coordinates to apply to the scene depth lookup.
OffsetFraction - An offset to apply to the scene depth lookup in a 2d fraction of the screen.

### ConstInput
- **类型**: `FVector2D`
- **描述**: only used if Input is not hooked up

### FallbackDepth
- **类型**: `float32`
- **描述**: Depth to fall back to in case the needed texture isn't available on a particular platform or configuration


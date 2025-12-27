# UMaterialExpressionVectorNoise

**继承自**: `UMaterialExpression`

## 属性

### WorldPositionOriginType
- **类型**: `EPositionOrigin`
- **描述**: Defines the reference space for the Position input.

### NoiseFunction
- **类型**: `EVectorNoiseFunction`
- **描述**: Noise function, affects performance and look

### Quality
- **类型**: `int`
- **描述**: For noise functions where applicable, lower numbers are faster and lower quality, higher numbers are slower and higher quality

### TileSize
- **类型**: `uint`
- **描述**: How many units in each tile (if Tiling is on)
For Perlin noise functions, Tile Size must be a multiple of three

### bTiling
- **类型**: `bool`


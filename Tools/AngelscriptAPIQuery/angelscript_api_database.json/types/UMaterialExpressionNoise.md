# UMaterialExpressionNoise

**继承自**: `UMaterialExpression`

## 属性

### WorldPositionOriginType
- **类型**: `EPositionOrigin`
- **描述**: Defines the reference space for the Position input.

### Scale
- **类型**: `float32`
- **描述**: can also be done with a multiply on the Position

### Quality
- **类型**: `int`
- **描述**: Lower numbers are faster and lower quality, higher numbers are slower and higher quality

### NoiseFunction
- **类型**: `ENoiseFunction`
- **描述**: Noise function, affects performance and look

### Levels
- **类型**: `int`
- **描述**: 1 = fast but little detail, .. larger numbers cost more performance

### OutputMin
- **类型**: `float32`

### OutputMax
- **类型**: `float32`

### LevelScale
- **类型**: `float32`
- **描述**: usually 2 but higher values allow efficient use of few levels

### RepeatSize
- **类型**: `uint`
- **描述**: How many units in each tile (if Tiling is on)

### bTurbulence
- **类型**: `bool`

### bTiling
- **类型**: `bool`


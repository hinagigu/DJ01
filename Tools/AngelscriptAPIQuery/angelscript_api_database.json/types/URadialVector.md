# URadialVector

**继承自**: `UFieldNodeVector`

Set a radial vector value, the direction being the vector from the sample position to the field one. The output is equal to magnitude * direction

## 属性

### Magnitude
- **类型**: `float32`

### Position
- **类型**: `FVector`

## 方法

### SetRadialVector
```angelscript
URadialVector SetRadialVector(float32 Magnitude, FVector Position)
```
Set a radial vector value. The direction is the normalized vector from the field position to the sample one. The output is equal to this direction * magnitude.
@param    Magnitude Magnitude of the radial vector field
@param    Position Center position of the radial vector field


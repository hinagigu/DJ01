# UNoiseField

**继承自**: `UFieldNodeFloat`

Defines a perlin noise scalar value if the sample is within a box

## 属性

### MinRange
- **类型**: `float32`

### MaxRange
- **类型**: `float32`

### Transform
- **类型**: `FTransform`

## 方法

### SetNoiseField
```angelscript
UNoiseField SetNoiseField(float32 MinRange, float32 MaxRange, FTransform Transform)
```
Defines a perlin noise scalar value if the sample is within a box
@param    MinRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    MaxRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    Transform Transform of the box in which the perlin noise will be defined


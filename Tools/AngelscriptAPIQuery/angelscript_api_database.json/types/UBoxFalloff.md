# UBoxFalloff

**继承自**: `UFieldNodeFloat`

Box scalar field that will be defined only within a box

## 属性

### Magnitude
- **类型**: `float32`

### MinRange
- **类型**: `float32`

### MaxRange
- **类型**: `float32`

### Default
- **类型**: `float32`

### Transform
- **类型**: `FTransform`

### Falloff
- **类型**: `EFieldFalloffType`

## 方法

### SetBoxFalloff
```angelscript
UBoxFalloff SetBoxFalloff(float32 Magnitude, float32 MinRange, float32 MaxRange, float32 Default, FTransform Transform, EFieldFalloffType Falloff)
```
Box scalar field that will be defined only within a box
@param    Magnitude Magnitude of the box falloff field
@param    MinRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    MaxRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    Default The field value will be set to Default if the sample distance from the box is higher than the scale of the transform
@param    Transform Translation, Rotation and Scale of the unit box
@param    Falloff Type of falloff function used to model the evolution of the field from the box surface to the sample position


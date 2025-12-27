# URadialFalloff

**继承自**: `UFieldNodeFloat`

Sphere scalar field that will be defined only within a sphere

## 属性

### Magnitude
- **类型**: `float32`

### MinRange
- **类型**: `float32`

### MaxRange
- **类型**: `float32`

### Default
- **类型**: `float32`

### Radius
- **类型**: `float32`

### Position
- **类型**: `FVector`

### Falloff
- **类型**: `EFieldFalloffType`

## 方法

### SetRadialFalloff
```angelscript
URadialFalloff SetRadialFalloff(float32 Magnitude, float32 MinRange, float32 MaxRange, float32 Default, float32 Radius, FVector Position, EFieldFalloffType Falloff)
```
Sphere scalar field that will be defined only within a sphere
@param    Magnitude Magnitude of the sphere falloff field
@param    MinRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    MaxRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    Default The field value will be set to Default if the sample distance from the center is higher than the radius
@param    Radius Radius of the sphere falloff field
@param    Position Center position of the sphere falloff field
@param    Falloff Type of falloff function used if the falloff function is picked


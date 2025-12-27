# UPlaneFalloff

**继承自**: `UFieldNodeFloat`

Plane scalar field that will be defined only within a distance from a plane

## 属性

### Magnitude
- **类型**: `float32`

### MinRange
- **类型**: `float32`

### MaxRange
- **类型**: `float32`

### Default
- **类型**: `float32`

### Distance
- **类型**: `float32`

### Position
- **类型**: `FVector`

### Normal
- **类型**: `FVector`

### Falloff
- **类型**: `EFieldFalloffType`

## 方法

### SetPlaneFalloff
```angelscript
UPlaneFalloff SetPlaneFalloff(float32 Magnitude, float32 MinRange, float32 MaxRange, float32 Default, float32 Distance, FVector Position, FVector Normal, EFieldFalloffType Falloff)
```
Plane scalar field that will be defined only within a distance from a plane
@param    Magnitude Magnitude of the plane falloff field
@param    MinRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    MaxRange The initial function value between 0 and 1 will be scaled between MinRange and MaxRange before being multiplied by magnitude
@param    Default The field value will be set to default if the sample projected distance ((Sample Position - Center Position).dot(Plane Normal)) is higher than the Plane Distance
@param    Distance Distance limit for the plane falloff field starting from the center position and extending in the direction of the plane normal
@param    Position Plane center position of the plane falloff field
@param    Normal Plane normal of the plane falloff field
@param    Falloff Type of falloff function used to model the evolution of the field from the plane surface to the distance isosurface


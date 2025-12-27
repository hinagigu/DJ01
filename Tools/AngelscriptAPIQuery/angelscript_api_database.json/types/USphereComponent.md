# USphereComponent

**继承自**: `UShapeComponent`

A sphere generally used for simple collision. Bounds are rendered as lines in the editor.

## 属性

### SphereRadius
- **类型**: `float32`

## 方法

### GetScaledSphereRadius
```angelscript
float32 GetScaledSphereRadius()
```
@return the radius of the sphere, with component scale applied.

### GetShapeScale
```angelscript
float32 GetShapeScale()
```
Get the scale used by this shape. This is a uniform scale that is the minimum of any non-uniform scaling.
@return the scale used by this shape.

### GetUnscaledSphereRadius
```angelscript
float32 GetUnscaledSphereRadius()
```
@return the radius of the sphere, ignoring component scale.

### SetSphereRadius
```angelscript
void SetSphereRadius(float32 InSphereRadius, bool bUpdateOverlaps)
```
Change the sphere radius. This is the unscaled radius, before component scale is applied.
@param       InSphereRadius: the new sphere radius
@param       bUpdateOverlaps: if true and this shape is registered and collides, updates touching array for owner actor.


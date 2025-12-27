# UBoxComponent

**继承自**: `UShapeComponent`

A box generally used for simple collision. Bounds are rendered as lines in the editor.

## 属性

### BoxExtent
- **类型**: `FVector`

## 方法

### GetScaledBoxExtent
```angelscript
FVector GetScaledBoxExtent()
```
@return the box extent, scaled by the component scale.

### GetUnscaledBoxExtent
```angelscript
FVector GetUnscaledBoxExtent()
```
@return the box extent, ignoring component scale.

### SetBoxExtent
```angelscript
void SetBoxExtent(FVector InBoxExtent, bool bUpdateOverlaps)
```
Change the box extent size. This is the unscaled size, before component scale is applied.
@param       InBoxExtent: new extent (radius) for the box.
@param       bUpdateOverlaps: if true and this shape is registered and collides, updates touching array for owner actor.


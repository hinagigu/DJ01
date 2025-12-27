# UShapeComponent

**继承自**: `UPrimitiveComponent`

ShapeComponent is a PrimitiveComponent that is represented by a simple geometrical shape (sphere, capsule, box, etc).

## 属性

### ShapeColor
- **类型**: `FColor`

### AreaClassOverride
- **类型**: `TSubclassOf<UNavAreaBase>`
- **描述**: Navigation area type override, null / none = no change to nav mesh.
bDynamicObstacle must be true and bUseSystemDefaultAreaClass false to use this.

### bDynamicObstacle
- **类型**: `bool`

### bUseSystemDefaultObstacleAreaClass
- **类型**: `bool`

### LineThickness
- **类型**: `float32`

## 方法

### SetLineThickness
```angelscript
void SetLineThickness(float32 Thickness)
```
Set the LineThickness


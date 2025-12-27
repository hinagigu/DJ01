# AVolume

**继承自**: `ABrush`

An editable 3D volume placed in a level. Different types of volumes perform different functions
@see https://docs.unrealengine.com/latest/INT/Engine/Actors/Volumes

## 方法

### GetBounds
```angelscript
FBoxSphereBounds GetBounds()
```

### EncompassesPoint
```angelscript
bool EncompassesPoint(FVector Point, float32 SphereRadius)
```

### EncompassesPoint
```angelscript
bool EncompassesPoint(FVector Point, float32 SphereRadius, float32& OutDistanceToPoint)
```

### SetBrushColor
```angelscript
void SetBrushColor(FLinearColor InBrushColor)
```


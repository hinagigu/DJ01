# FBoxSphereBounds3d

A bounding box and bounding sphere with the same origin.
@note The full C++ class is located here : Engine\Source\Runtime\Core\Public\Math\BoxSphereBounds.h

## 属性

### Origin
- **类型**: `FVector3d`
- **描述**: Holds the origin of the bounding box and sphere.

### BoxExtent
- **类型**: `FVector3d`
- **描述**: Holds the extent of the bounding box, which is half the size of the box in 3D space

### SphereRadius
- **类型**: `float`
- **描述**: Holds the radius of the bounding sphere.

## 方法

### opAssign
```angelscript
FBoxSphereBounds3d& opAssign(FBoxSphereBounds3d Other)
```


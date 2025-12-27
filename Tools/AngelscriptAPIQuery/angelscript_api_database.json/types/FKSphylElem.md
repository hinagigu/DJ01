# FKSphylElem

Capsule shape used for collision. Z axis is capsule axis.

## 属性

### Center
- **类型**: `FVector`
- **描述**: Position of the capsule's origin

### Rotation
- **类型**: `FRotator`
- **描述**: Rotation of the capsule

### Radius
- **类型**: `float32`
- **描述**: Radius of the capsule

### Length
- **类型**: `float32`
- **描述**: This is of line-segment ie. add Radius to both ends to find total length.

### RestOffset
- **类型**: `float32`
- **描述**: Offset used when generating contact points. This allows you to smooth out
              the Minkowski sum by radius R. Useful for making objects slide smoothly
              on top of irregularities

### Name
- **类型**: `FName`
- **描述**: User-defined name for this shape

### CollisionEnabled
- **类型**: `ECollisionEnabled`
- **描述**: Course per-primitive collision filtering. This allows for individual primitives to
              be toggled in and out of sim and query collision without changing filtering details.

### bContributeToMass
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FKSphylElem& opAssign(FKSphylElem Other)
```


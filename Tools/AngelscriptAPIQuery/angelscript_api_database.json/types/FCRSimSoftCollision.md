# FCRSimSoftCollision

## 属性

### Transform
- **类型**: `FTransform`
- **描述**: The world / global transform of the collisoin

### ShapeType
- **类型**: `ECRSimSoftCollisionType`
- **描述**: The type of collision shape

### MinimumDistance
- **类型**: `float32`
- **描述**: The minimum distance for the collision.
If this is equal or higher than the maximum there's no falloff.
For a cone shape this represents the minimum angle in degrees.

### MaximumDistance
- **类型**: `float32`
- **描述**: The maximum distance for the collision.
If this is equal or lower than the minimum there's no falloff.
For a cone shape this represents the maximum angle in degrees.

### FalloffType
- **类型**: `ERigVMAnimEasingType`
- **描述**: The type of falloff to use

### Coefficient
- **类型**: `float32`
- **描述**: The strength of the collision force

### bInverted
- **类型**: `bool`
- **描述**: If set to true the collision volume will be inverted

## 方法

### opAssign
```angelscript
FCRSimSoftCollision& opAssign(FCRSimSoftCollision Other)
```


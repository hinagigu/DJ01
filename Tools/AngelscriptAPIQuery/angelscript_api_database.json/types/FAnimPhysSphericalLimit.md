# FAnimPhysSphericalLimit

## 属性

### DrivingBone
- **类型**: `FBoneReference`
- **描述**: Bone to attach the sphere to

### SphereLocalOffset
- **类型**: `FVector`
- **描述**: Local offset for the sphere, if no driving bone is set this is in node space, otherwise bone space

### LimitRadius
- **类型**: `float32`
- **描述**: Radius of the sphere

### LimitType
- **类型**: `ESphericalLimitType`
- **描述**: Whether to lock bodies inside or outside of the sphere

## 方法

### opAssign
```angelscript
FAnimPhysSphericalLimit& opAssign(FAnimPhysSphericalLimit Other)
```


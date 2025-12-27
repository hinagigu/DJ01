# FTransform3d

Transform composed of Quat/Translation/Scale.
@note This is implemented in either TransformVectorized.h or TransformNonVectorized.h depending on the platform.

## 属性

### Rotation
- **类型**: `FQuat4d`
- **描述**: Rotation of this transformation, as a quaternion.

### Translation
- **类型**: `FVector3d`
- **描述**: Translation of this transformation, as a vector.

### Scale3D
- **类型**: `FVector3d`
- **描述**: 3D scale (always applied in local space) as a vector.

## 方法

### opAssign
```angelscript
FTransform3d& opAssign(FTransform3d Other)
```


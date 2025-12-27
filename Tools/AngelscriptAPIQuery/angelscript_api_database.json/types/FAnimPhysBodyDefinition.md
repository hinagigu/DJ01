# FAnimPhysBodyDefinition

## 属性

### BoxExtents
- **类型**: `FVector`
- **描述**: Extents of the box to use for simulation

### LocalJointOffset
- **类型**: `FVector`
- **描述**: Vector relative to the body being simulated to attach the constraint to

### ConstraintSetup
- **类型**: `FAnimPhysConstraintSetup`
- **描述**: Data describing the constraints we will apply to the body

### CollisionType
- **类型**: `AnimPhysCollisionType`
- **描述**: Resolution method for planar limits

### SphereCollisionRadius
- **类型**: `float32`
- **描述**: Radius to use if CollisionType is set to CustomSphere

## 方法

### opAssign
```angelscript
FAnimPhysBodyDefinition& opAssign(FAnimPhysBodyDefinition Other)
```


# FConstraintBaseParams

## 属性

### Stiffness
- **类型**: `float32`
- **描述**: Stiffness of the soft constraint. Only used when Soft Constraint is on.

### Damping
- **类型**: `float32`
- **描述**: Damping of the soft constraint. Only used when Soft Constraint is on.

### Restitution
- **类型**: `float32`
- **描述**: Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.

### ContactDistance
- **类型**: `float32`
- **描述**: Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

### bSoftConstraint
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FConstraintBaseParams& opAssign(FConstraintBaseParams Other)
```


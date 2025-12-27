# FConeConstraint

Cone constraint

## 属性

### Swing1LimitDegrees
- **类型**: `float32`
- **描述**: Angle of movement along the XY plane. This defines the first symmetric angle of the cone.

### Swing2LimitDegrees
- **类型**: `float32`
- **描述**: Angle of movement along the XZ plane. This defines the second symmetric angle of the cone.

### Swing1Motion
- **类型**: `EAngularConstraintMotion`
- **描述**: Indicates whether the Swing1 limit is used.

### Swing2Motion
- **类型**: `EAngularConstraintMotion`
- **描述**: Indicates whether the Swing2 limit is used.

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
FConeConstraint& opAssign(FConeConstraint Other)
```


# FLinearConstraint

Distance constraint

## 属性

### Limit
- **类型**: `float32`
- **描述**: The distance allowed between the two joint reference frames. Distance applies on all axes enabled (one axis means line, two axes implies circle, three axes implies sphere)

### XMotion
- **类型**: `ELinearConstraintMotion`
- **描述**: Indicates the linear constraint applied along the X-axis. Free implies no constraint at all. Locked implies no movement along X is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided.

### YMotion
- **类型**: `ELinearConstraintMotion`
- **描述**: Indicates the linear constraint applied along the Y-axis. Free implies no constraint at all. Locked implies no movement along Y is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided.

### ZMotion
- **类型**: `ELinearConstraintMotion`
- **描述**: Indicates the linear constraint applied along theZX-axis. Free implies no constraint at all. Locked implies no movement along Z is allowed. Limited implies the distance in the joint along all active axes must be less than the Distance provided.

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
FLinearConstraint& opAssign(FLinearConstraint Other)
```


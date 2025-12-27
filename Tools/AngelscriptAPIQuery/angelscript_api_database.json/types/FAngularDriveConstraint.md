# FAngularDriveConstraint

Angular Drive

## 属性

### TwistDrive
- **类型**: `FConstraintDrive`
- **描述**: Controls the twist (roll) constraint drive between current orientation/velocity and target orientation/velocity. This is available as long as the twist limit is set to free or limited.

### SwingDrive
- **类型**: `FConstraintDrive`
- **描述**: Controls the cone constraint drive between current orientation/velocity and target orientation/velocity. This is available as long as there is at least one swing limit set to free or limited.

### SlerpDrive
- **类型**: `FConstraintDrive`
- **描述**: Controls the SLERP (spherical lerp) drive between current orientation/velocity and target orientation/velocity. NOTE: This is only available when all three angular limits are either free or limited. Locking any angular limit will turn off the drive implicitly.

### OrientationTarget
- **类型**: `FRotator`
- **描述**: Target orientation relative to the the body reference frame.

### AngularVelocityTarget
- **类型**: `FVector`
- **描述**: Target angular velocity relative to the body reference frame in revolutions per second.

### AngularDriveMode
- **类型**: `EAngularDriveMode`
- **描述**: Whether motors use SLERP (spherical lerp) or decompose into a Swing motor (cone constraints) and Twist motor (roll constraints). NOTE: SLERP will NOT work if any of the angular constraints are locked.

## 方法

### opAssign
```angelscript
FAngularDriveConstraint& opAssign(FAngularDriveConstraint Other)
```


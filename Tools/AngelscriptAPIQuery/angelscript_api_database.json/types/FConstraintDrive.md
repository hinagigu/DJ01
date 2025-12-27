# FConstraintDrive

## 属性

### Stiffness
- **类型**: `float32`
- **描述**: The spring strength of the drive. Force proportional to the position error.

### Damping
- **类型**: `float32`
- **描述**: The damping strength of the drive. Force proportional to the velocity error.

### MaxForce
- **类型**: `float32`
- **描述**: The force limit of the drive.

### bEnablePositionDrive
- **类型**: `bool`

### bEnableVelocityDrive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FConstraintDrive& opAssign(FConstraintDrive Other)
```


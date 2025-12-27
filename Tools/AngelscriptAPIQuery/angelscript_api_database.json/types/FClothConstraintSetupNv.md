# FClothConstraintSetupNv

Container for a constraint setup, these can be horizontal, vertical, shear and bend.

## 属性

### Stiffness
- **类型**: `float32`
- **描述**: How stiff this constraint is, this affects how closely it will follow the desired position

### StiffnessMultiplier
- **类型**: `float32`
- **描述**: A multiplier affecting the above value

### StretchLimit
- **类型**: `float32`
- **描述**: The hard limit on how far this constraint can stretch

### CompressionLimit
- **类型**: `float32`
- **描述**: The hard limit on how far this constraint can compress

## 方法

### opAssign
```angelscript
FClothConstraintSetupNv& opAssign(FClothConstraintSetupNv Other)
```


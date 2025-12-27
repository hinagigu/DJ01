# FSolverInput

## 属性

### LinearMotionStrength
- **类型**: `float32`
- **描述**: * This value is applied to the target information for effectors, which influence back to
* Joint's motion that are affected by the end effector
* The reason min/max is used when we apply the depth through the chain that are affected

### MinLinearMotionStrength
- **类型**: `float32`

### AngularMotionStrength
- **类型**: `float32`
- **描述**: * This value is applied to the target information for effectors, which influence back to
* Joint's motion that are affected by the end effector
* The reason min/max is used when we apply the depth through the chain that are affected

### MinAngularMotionStrength
- **类型**: `float32`

### DefaultTargetClamp
- **类型**: `float32`
- **描述**: This is a scale value (range from 0-0.7) that is used to stablize the target vector. If less, it's more stable, but it can reduce speed of converge.

### Precision
- **类型**: `float32`
- **描述**: The precision to use for the solver

### Damping
- **类型**: `float32`
- **描述**: The precision to use for the fabrik solver

### MaxIterations
- **类型**: `int`
- **描述**: The maximum number of iterations. Values between 4 and 16 are common.

### bUseJacobianTranspose
- **类型**: `bool`
- **描述**: Cheaper solution than default Jacobian Pseudo Inverse Damped Least Square

## 方法

### opAssign
```angelscript
FSolverInput& opAssign(FSolverInput Other)
```


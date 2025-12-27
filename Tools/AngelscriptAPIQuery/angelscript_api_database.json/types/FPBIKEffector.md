# FPBIKEffector

## 属性

### Bone
- **类型**: `FName`
- **描述**: The bone that this effector will pull on.

### Transform
- **类型**: `FTransform`
- **描述**: The target location and rotation for this effector. The solver will try to get the specified bone to reach this location.

### PositionAlpha
- **类型**: `float32`
- **描述**: Range 0-1, default is 1. Blend between the input bone position (0.0) and the current effector position (1.0).

### RotationAlpha
- **类型**: `float32`
- **描述**: Range 0-1, default is 1. Blend between the input bone rotation (0.0) and the current effector rotation (1.0).

### StrengthAlpha
- **类型**: `float32`
- **描述**: Range 0-1 (default is 1.0). The strength of the effector when pulling the bone towards it's target location.
At 0.0, the effector does not pull at all, but the bones between the effector and the root will still slightly resist motion from other effectors.
This can thus act as a "stabilizer" of sorts for parts of the body that you do not want to behave in a pure FK fashion.

### ChainDepth
- **类型**: `int`

### PullChainAlpha
- **类型**: `float32`
- **描述**: Range 0-1 (default is 1.0). When enabled (greater than 0.0), the solver internally partitions the skeleton into 'chains' which extend from the effector to the nearest fork in the skeleton.
These chains are pre-rotated and translated, as a whole, towards the effector targets.
This can improve the results for sparse bone chains, and significantly improve convergence on dense bone chains.
But it may cause undesirable results in highly constrained bone chains (like robot arms).

### PinRotation
- **类型**: `float32`
- **描述**: Range 0-1 (default is 1.0).
Blends the effector bone rotation between the rotation of the effector transform (1.0) and the rotation of the input bone (0.0).

## 方法

### opAssign
```angelscript
FPBIKEffector& opAssign(FPBIKEffector Other)
```


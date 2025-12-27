# UIKRigFBIKSolver

**继承自**: `UIKRigSolver`

## 属性

### RootBone
- **类型**: `FName`
- **描述**: All bones above this bone in the hierarchy will be completely ignored by the solver. Typically this is set to
the top-most skinned bone in the Skeletal Mesh (ie Pelvis, Hips etc), NOT the actual root of the entire skeleton.

If you want to use the solver on a single chain of bones, and NOT translate the chain, ensure that "PinRoot" is
checked on to disable the root from translating to reach the effector goals.

### Iterations
- **类型**: `int`

### SubIterations
- **类型**: `int`

### MassMultiplier
- **类型**: `float32`

### bAllowStretch
- **类型**: `bool`

### RootBehavior
- **类型**: `EPBIKRootBehavior`

### PrePullRootSettings
- **类型**: `FRootPrePullSettings`

### PullChainAlpha
- **类型**: `float32`

### MaxAngle
- **类型**: `float32`

### OverRelaxation
- **类型**: `float32`


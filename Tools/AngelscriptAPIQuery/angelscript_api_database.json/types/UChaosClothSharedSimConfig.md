# UChaosClothSharedSimConfig

**继承自**: `UClothSharedConfigCommon`

Chaos config settings shared between all instances of a skeletal mesh.
Unlike UChaosClothConfig, these settings contain common cloth simulation
parameters that cannot change between the various clothing assets assigned
to a specific skeletal mesh. @seealso UChaosClothConfig.

## 属性

### IterationCount
- **类型**: `int`
- **描述**: The number of time step dependent solver iterations. This sets iterations at 60fps.
This will increase the stiffness of all constraints but will increase the CPU cost.
If the frame rate is higher, the actual number of iterations used by the solver might be less, if the frame rate is lower it might be more.

### MaxIterationCount
- **类型**: `int`
- **描述**: The maximum number of solver iterations.
This is the upper limit of the number of iterations set in solver, when the frame rate is lower than 60fps.

### SubdivisionCount
- **类型**: `int`
- **描述**: The number of solver substeps.
This will increase the precision of the collision inputs and help with constraint resolutions but will increase the CPU cost.


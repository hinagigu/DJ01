# ULinearAnalysisProperties

**继承自**: `UAnalysisProperties`

## 属性

### FunctionAxis
- **类型**: `EAnalysisLinearAxis`
- **描述**: Axis for the analysis function

### BoneSocket
- **类型**: `FBoneSocketTarget`
- **描述**: The bone or socket used for analysis

### Space
- **类型**: `EAnalysisSpace`
- **描述**: The space in which to perform the analysis. Fixed will use the analysis bone/socket at the first frame
of the analysis time range. Changing will use the analysis bone/socket at the relevant frame during the
analysis, but calculate velocities assuming that frame isn't moving. Moving will do the same but velocities
as well as positions/rotations will be relative to this moving frame.

### SpaceBoneSocket
- **类型**: `FBoneSocketTarget`
- **描述**: Bone or socket that defines the analysis space (when it isn't World)

### StartTimeFraction
- **类型**: `float32`
- **描述**: Fraction through each animation at which analysis starts

### EndTimeFraction
- **类型**: `float32`
- **描述**: Fraction through each animation at which analysis ends


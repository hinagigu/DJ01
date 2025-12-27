# UAnimStreamable

**继承自**: `UAnimSequenceBase`

## 属性

### Interpolation
- **类型**: `EAnimInterpolationType`
- **描述**: This defines how values between keys are calculated *

### RetargetSource
- **类型**: `FName`
- **描述**: Base pose to use when retargeting

### BoneCompressionSettings
- **类型**: `UAnimBoneCompressionSettings`
- **描述**: The bone compression settings used to compress bones in this sequence.

### CurveCompressionSettings
- **类型**: `UAnimCurveCompressionSettings`
- **描述**: The curve compression settings used to compress curves in this sequence.

### VariableFrameStrippingSettings
- **类型**: `UVariableFrameStrippingSettings`
- **描述**: The settings used to control whether or not to use variable frame stripping and its amount

### bEnableRootMotion
- **类型**: `bool`
- **描述**: If this is on, it will allow extracting of root motion *

### RootMotionRootLock
- **类型**: `ERootMotionRootLock`
- **描述**: Root Bone will be locked to that position when extracting root motion.*

### bForceRootLock
- **类型**: `bool`
- **描述**: Force Root Bone Lock even if Root Motion is not enabled

### bUseNormalizedRootMotionScale
- **类型**: `bool`
- **描述**: If this is on, it will use a normalized scale value for the root motion extracted: FVector(1.0, 1.0, 1.0) *


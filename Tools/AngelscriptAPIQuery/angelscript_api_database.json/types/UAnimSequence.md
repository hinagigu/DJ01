# UAnimSequence

**继承自**: `UAnimSequenceBase`

## 属性

### bAllowFrameStripping
- **类型**: `bool`
- **描述**: Allow frame stripping to be performed on this animation if the platform requests it
Can be disabled if animation has high frequency movements that are being lost.

### CompressionErrorThresholdScale
- **类型**: `float32`
- **描述**: Set a scale for error threshold on compression. This is useful if the animation will
be played back at a different scale (e.g. if you know the animation will be played
on an actor/component that is scaled up by a factor of 10, set this value to 10)

### BoneCompressionSettings
- **类型**: `UAnimBoneCompressionSettings`
- **描述**: The bone compression settings used to compress bones in this sequence.

### CurveCompressionSettings
- **类型**: `UAnimCurveCompressionSettings`
- **描述**: The curve compression settings used to compress curves in this sequence.

### VariableFrameStrippingSettings
- **类型**: `UVariableFrameStrippingSettings`

### AdditiveAnimType
- **类型**: `EAdditiveAnimationType`
- **描述**: Additive animation type. *

### RefPoseType
- **类型**: `EAdditiveBasePoseType`
- **描述**: Additive refrerence pose type. Refer above enum type

### RefFrameIndex
- **类型**: `int`
- **描述**: Additve reference frame if RefPoseType == AnimFrame *

### RefPoseSeq
- **类型**: `UAnimSequence`
- **描述**: Additive reference animation if it's relevant - i.e. AnimScaled or AnimFrame *

### RetargetSource
- **类型**: `FName`
- **描述**: Base pose to use when retargeting

### RetargetSourceAsset
- **类型**: `TSoftObjectPtr<USkeletalMesh>`
- **描述**: If RetargetSource is set to Default (None), this is asset for the base pose to use when retargeting. Transform data will be saved in RetargetSourceAssetReferencePose.

### Interpolation
- **类型**: `EAnimInterpolationType`
- **描述**: This defines how values between keys are calculated *

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

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: Importing data and options used for this mesh

### StripAnimDataOnDedicatedServer
- **类型**: `EStripAnimDataOnDedicatedServerSettings`
- **描述**: Enum used to decide whether we should strip animation data on dedicated server

### bDoNotOverrideCompression
- **类型**: `bool`


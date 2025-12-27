# FAnimNode_ModifyBone

Simple controller that replaces or adds to the translation/rotation of a single bone.

## 属性

### BoneToModify
- **类型**: `FBoneReference`
- **描述**: Name of bone to control. This is the main bone chain to modify from. *

### Translation
- **类型**: `FVector`

### Rotation
- **类型**: `FRotator`

### Scale
- **类型**: `FVector`

### TranslationMode
- **类型**: `EBoneModificationMode`
- **描述**: Whether and how to modify the translation of this bone.

### RotationMode
- **类型**: `EBoneModificationMode`
- **描述**: Whether and how to modify the translation of this bone.

### ScaleMode
- **类型**: `EBoneModificationMode`
- **描述**: Whether and how to modify the translation of this bone.

### TranslationSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame to apply Translation in.

### RotationSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame to apply Rotation in.

### ScaleSpace
- **类型**: `EBoneControlSpace`
- **描述**: Reference frame to apply Scale in.

### ComponentPose
- **类型**: `FComponentSpacePoseLink`

### LODThreshold
- **类型**: `int`

### AlphaInputType
- **类型**: `EAnimAlphaInputType`

### bAlphaBoolEnabled
- **类型**: `bool`

### Alpha
- **类型**: `float32`

### AlphaScaleBias
- **类型**: `FInputScaleBias`

### AlphaBoolBlend
- **类型**: `FInputAlphaBoolBlend`

### AlphaCurveName
- **类型**: `FName`

### AlphaScaleBiasClamp
- **类型**: `FInputScaleBiasClamp`

## 方法

### opAssign
```angelscript
FAnimNode_ModifyBone& opAssign(FAnimNode_ModifyBone Other)
```


# FAnimNode_CopyBoneDelta

Simple controller to copy a transform relative to the ref pose to the target bone,
instead of the copy bone node which copies the absolute transform

## 属性

### SourceBone
- **类型**: `FBoneReference`

### TargetBone
- **类型**: `FBoneReference`

### bCopyTranslation
- **类型**: `bool`

### bCopyRotation
- **类型**: `bool`

### bCopyScale
- **类型**: `bool`

### CopyMode
- **类型**: `CopyBoneDeltaMode`

### TranslationMultiplier
- **类型**: `float32`

### RotationMultiplier
- **类型**: `float32`

### ScaleMultiplier
- **类型**: `float32`

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
FAnimNode_CopyBoneDelta& opAssign(FAnimNode_CopyBoneDelta Other)
```


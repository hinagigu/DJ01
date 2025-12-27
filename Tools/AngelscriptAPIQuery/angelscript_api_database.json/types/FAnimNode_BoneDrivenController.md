# FAnimNode_BoneDrivenController

This is the runtime version of a bone driven controller, which maps part of the state from one bone to another (e.g., 2 * source.x -> target.z)

## 属性

### SourceBone
- **类型**: `FBoneReference`
- **描述**: Bone to use as controller input

### DrivingCurve
- **类型**: `UCurveFloat`
- **描述**: Curve used to map from the source attribute to the driven attributes if present (otherwise the Multiplier will be used)

### Multiplier
- **类型**: `float32`
- **描述**: Multiplier to apply to the input value (Note: Ignored when a curve is used)

### RangeMin
- **类型**: `float`
- **描述**: Minimum limit of the input value (mapped to RemappedMin, only used when limiting the source range)
If this is rotation, the unit is radian

### RangeMax
- **类型**: `float`
- **描述**: Maximum limit of the input value (mapped to RemappedMax, only used when limiting the source range)
If this is rotation, the unit is radian

### RemappedMin
- **类型**: `float`
- **描述**: Minimum value to apply to the destination (remapped from the input range)
If this is rotation, the unit is radian

### RemappedMax
- **类型**: `float`
- **描述**: Maximum value to apply to the destination (remapped from the input range)
If this is rotation, the unit is radian

### ParameterName
- **类型**: `FName`
- **描述**: Name of Morph Target to drive using the source attribute

### TargetBone
- **类型**: `FBoneReference`
- **描述**: Bone to drive using controller input

### DestinationMode
- **类型**: `EDrivenDestinationMode`
- **描述**: Type of destination to drive, currently either bone or morph target

### ModificationMode
- **类型**: `EDrivenBoneModificationMode`
- **描述**: The type of modification to make to the destination component(s)

### SourceComponent
- **类型**: `EComponentType`
- **描述**: Transform component to use as input

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

### bUseRange
- **类型**: `bool`

### bAffectTargetTranslationX
- **类型**: `bool`

### bAffectTargetTranslationY
- **类型**: `bool`

### bAffectTargetTranslationZ
- **类型**: `bool`

### bAffectTargetRotationX
- **类型**: `bool`

### bAffectTargetRotationY
- **类型**: `bool`

### bAffectTargetRotationZ
- **类型**: `bool`

### bAffectTargetScaleX
- **类型**: `bool`

### bAffectTargetScaleY
- **类型**: `bool`

### bAffectTargetScaleZ
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FAnimNode_BoneDrivenController& opAssign(FAnimNode_BoneDrivenController Other)
```


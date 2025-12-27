# FAnimNode_BlendListByEnum

Blend List by Enum, it changes based on enum input that enters

## 属性

### ActiveEnumValue
- **类型**: `uint8`
- **描述**: The currently selected pose (as an enum value)

### BlendPose
- **类型**: `TArray<FPoseLink>`

### BlendTime
- **类型**: `TArray<float32>`

### TransitionType
- **类型**: `EBlendListTransitionType`

### BlendType
- **类型**: `EAlphaBlendOption`

### bResetChildOnActivation
- **类型**: `bool`
- **描述**: This reinitializes the re-activated child if the child's weight was zero.

### CustomBlendCurve
- **类型**: `UCurveFloat`

### BlendProfile
- **类型**: `UBlendProfile`

## 方法

### opAssign
```angelscript
FAnimNode_BlendListByEnum& opAssign(FAnimNode_BlendListByEnum Other)
```


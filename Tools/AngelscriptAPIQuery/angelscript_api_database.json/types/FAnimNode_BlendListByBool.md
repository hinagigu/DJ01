# FAnimNode_BlendListByBool

This node is effectively a 'branch', picking one of two input poses based on an input Boolean value

## 属性

### bActiveValue
- **类型**: `bool`
- **描述**: Which input should be connected to the output?

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
FAnimNode_BlendListByBool& opAssign(FAnimNode_BlendListByBool Other)
```


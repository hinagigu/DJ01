# FAnimNode_IKRig

## 属性

### Source
- **类型**: `FPoseLink`
- **描述**: The input pose to start the IK solve relative to.

### RigDefinitionAsset
- **类型**: `UIKRigDefinition`
- **描述**: The IK rig to use to modify the incoming source pose.

### Goals
- **类型**: `TArray<FIKRigGoal>`

### bStartFromRefPose
- **类型**: `bool`
- **描述**: optionally ignore the input pose and start from the reference pose each solve

### bEnableDebugDraw
- **类型**: `bool`
- **描述**: Toggle debug drawing of goals when node is selected.

### DebugScale
- **类型**: `float32`
- **描述**: Adjust size of debug drawing.

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
FAnimNode_IKRig& opAssign(FAnimNode_IKRig Other)
```


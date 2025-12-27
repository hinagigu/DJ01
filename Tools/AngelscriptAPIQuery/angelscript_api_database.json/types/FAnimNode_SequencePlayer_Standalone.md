# FAnimNode_SequencePlayer_Standalone

Sequence player node that can be used standalone (without constant folding)

## 属性

### GroupName
- **类型**: `FName`
- **描述**: The group name that we synchronize with (NAME_None if it is not part of any group).

### GroupRole
- **类型**: `EAnimGroupRole`
- **描述**: The role this node can assume within the group (ignored if GroupName is not set)

### Method
- **类型**: `EAnimSyncMethod`
- **描述**: How this node will synchronize with other animations.

### bIgnoreForRelevancyTest
- **类型**: `bool`
- **描述**: If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node

### Sequence
- **类型**: `UAnimSequenceBase`
- **描述**: The animation sequence asset to play

### PlayRateBasis
- **类型**: `float32`
- **描述**: The Basis in which the PlayRate is expressed in. This is used to rescale PlayRate inputs.
For example a Basis of 100 means that the PlayRate input will be divided by 100.

### PlayRate
- **类型**: `float32`
- **描述**: The play rate multiplier. Can be negative, which will cause the animation to play in reverse.

### PlayRateScaleBiasClampConstants
- **类型**: `FInputScaleBiasClampConstants`
- **描述**: Additional scaling, offsetting and clamping of PlayRate input.
Performed after PlayRateBasis.

### StartPosition
- **类型**: `float32`
- **描述**: The start position between 0 and the length of the sequence to use when initializing. When looping, play will still jump back to the beginning when reaching the end.

### bLoopAnimation
- **类型**: `bool`
- **描述**: Should the animation loop back to the start when it reaches the end?

### bStartFromMatchingPose
- **类型**: `bool`
- **描述**: Use pose matching to choose the start position. Requires experimental PoseSearch plugin.

### BlendWeight
- **类型**: `float32`
- **描述**: Last encountered blendweight for this node

### InternalTimeAccumulator
- **类型**: `float32`
- **描述**: Accumulated time used to reference the asset in this node

## 方法

### opAssign
```angelscript
FAnimNode_SequencePlayer_Standalone& opAssign(FAnimNode_SequencePlayer_Standalone Other)
```


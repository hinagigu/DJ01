# FAnimNode_AimOffsetLookAt

This node uses a source transform of a socket on the skeletal mesh to automatically calculate
Yaw and Pitch directions for a referenced aim offset given a point in the world to look at.

## 属性

### BasePose
- **类型**: `FPoseLink`

### LODThreshold
- **类型**: `int`

### SourceSocketName
- **类型**: `FName`

### PivotSocketName
- **类型**: `FName`

### LookAtLocation
- **类型**: `FVector`

### SocketAxis
- **类型**: `FVector`

### Alpha
- **类型**: `float32`

### GroupName
- **类型**: `FName`
- **描述**: The group name that we synchronize with (NAME_None if it is not part of any group). Note that
this is the name of the group used to sync the output of this node - it will not force
syncing of animations contained by it.

### GroupRole
- **类型**: `EAnimGroupRole`
- **描述**: The role this node can assume within the group (ignored if GroupName is not set). Note
that this is the role of the output of this node, not of animations contained by it.

### Method
- **类型**: `EAnimSyncMethod`
- **描述**: How this node will synchronize with other animations. Note that this determines how the output
of this node is used for synchronization, not of animations contained by it.

### bIgnoreForRelevancyTest
- **类型**: `bool`
- **描述**: If true, "Relevant anim" nodes that look for the highest weighted animation in a state will ignore this node

### X
- **类型**: `float32`
- **描述**: The X coordinate to sample in the blendspace

### Y
- **类型**: `float32`
- **描述**: The Y coordinate to sample in the blendspace

### PlayRate
- **类型**: `float32`
- **描述**: The play rate multiplier. Can be negative, which will cause the animation to play in reverse.

### bLoop
- **类型**: `bool`
- **描述**: Should the animation loop back to the start when it reaches the end?

### bResetPlayTimeWhenBlendSpaceChanges
- **类型**: `bool`
- **描述**: Whether we should reset the current play time when the blend space changes

### StartPosition
- **类型**: `float32`
- **描述**: The start position in [0, 1] to use when initializing. When looping, play will still jump back to the beginning when reaching the end.

### BlendSpace
- **类型**: `UBlendSpace`
- **描述**: The blendspace asset to play

### BlendWeight
- **类型**: `float32`
- **描述**: Last encountered blendweight for this node

### InternalTimeAccumulator
- **类型**: `float32`
- **描述**: Accumulated time used to reference the asset in this node

## 方法

### opAssign
```angelscript
FAnimNode_AimOffsetLookAt& opAssign(FAnimNode_AimOffsetLookAt Other)
```


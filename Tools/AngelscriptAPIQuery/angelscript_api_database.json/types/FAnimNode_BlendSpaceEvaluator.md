# FAnimNode_BlendSpaceEvaluator

Evaluates a BlendSpace at a specific using a specific time input rather than advancing time
internally. Typically the playback position of the animation for this node will represent
something other than time, like jump height. Note that events output from the sequences playing
and being blended together should not be used. In addition, synchronization of animations
will potentially be discontinuous if the blend weights are updated, as the leader/follower changes.

## 属性

### NormalizedTime
- **类型**: `float32`

### bTeleportToNormalizedTime
- **类型**: `bool`
- **描述**: If true, teleport to normalized time, does NOT advance time (does not trigger notifies, does not
extract Root Motion, etc.). If false, will advance time (will trigger notifies, extract root motion
if applicable, etc).

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
FAnimNode_BlendSpaceEvaluator& opAssign(FAnimNode_BlendSpaceEvaluator Other)
```


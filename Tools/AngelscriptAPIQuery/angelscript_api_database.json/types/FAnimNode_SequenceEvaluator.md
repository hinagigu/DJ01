# FAnimNode_SequenceEvaluator

Sequence evaluator node that can be used with constant folding

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
- **描述**: The animation sequence asset to evaluate

### ExplicitTime
- **类型**: `float32`
- **描述**: The time at which to evaluate the associated sequence

### bUseExplicitFrame
- **类型**: `bool`
- **描述**: Whether to use ExplicitFrame (true) or ExplicitTime (false) when evaluating the associated sequence

### ExplicitFrame
- **类型**: `int`
- **描述**: The frame at which to evaluate the associated sequence

### bShouldLoop
- **类型**: `bool`
- **描述**: This only works if bTeleportToExplicitTime is false OR this node is set to use SyncGroup

### bTeleportToExplicitTime
- **类型**: `bool`
- **描述**: If true, teleport to explicit time, does NOT advance time (does not trigger notifies, does not extract Root Motion, etc.)
      If false, will advance time (will trigger notifies, extract root motion if applicable, etc.)
      Note: using a sync group forces advancing time regardless of what this option is set to.

### ReinitializationBehavior
- **类型**: `ESequenceEvalReinit`
- **描述**: What to do when SequenceEvaluator is reinitialized

### StartPosition
- **类型**: `float32`
- **描述**: The start up position, it only applies when ReinitializationBehavior == StartPosition. Only used when bTeleportToExplicitTime is false.

### BlendWeight
- **类型**: `float32`
- **描述**: Last encountered blendweight for this node

### InternalTimeAccumulator
- **类型**: `float32`
- **描述**: Accumulated time used to reference the asset in this node

## 方法

### opAssign
```angelscript
FAnimNode_SequenceEvaluator& opAssign(FAnimNode_SequenceEvaluator Other)
```


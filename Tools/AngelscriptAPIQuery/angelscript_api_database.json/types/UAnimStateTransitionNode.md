# UAnimStateTransitionNode

**继承自**: `UAnimStateNodeBase`

## 属性

### PriorityOrder
- **类型**: `int`
- **描述**: The priority order of this transition. If multiple transitions out of a state go
true at the same time, the one with the smallest priority order will take precedent

### CrossfadeDuration
- **类型**: `float32`
- **描述**: The duration to cross-fade for

### BlendMode
- **类型**: `EAlphaBlendOption`

### CustomBlendCurve
- **类型**: `UCurveFloat`

### BlendProfile
- **类型**: `UBlendProfile`
- **描述**: The blend profile to use to evaluate this transition per-bone

### bAutomaticRuleBasedOnSequencePlayerInState
- **类型**: `bool`
- **描述**: Try setting the rule automatically based on most relevant asset player node's remaining time and the Automatic Rule Trigger Time of the transition, ignoring the internal time

### AutomaticRuleTriggerTime
- **类型**: `float32`
- **描述**: When should the automatic transition rule trigger relative to the time remaining on the relevant asset player:
 < 0 means trigger the transition 'Crossfade Duration' seconds before the end of the asset player, so a standard blend would finish just as the asset player ends
>= 0 means trigger the transition 'Automatic Rule Trigger Time' seconds before the end of the asset player

### SyncGroupNameToRequireValidMarkersRule
- **类型**: `FName`
- **描述**: If SyncGroupName is specified, Transition will only be taken if the SyncGroup has valid markers (other transition rules still apply in addition to that).

### LogicType
- **类型**: `ETransitionLogicType`

### TransitionStart
- **类型**: `FAnimNotifyEvent`

### TransitionEnd
- **类型**: `FAnimNotifyEvent`

### TransitionInterrupt
- **类型**: `FAnimNotifyEvent`

### Bidirectional
- **类型**: `bool`
- **描述**: This transition can go both directions


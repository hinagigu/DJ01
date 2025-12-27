# UBTTask_MoveTo

**继承自**: `UBTTask_BlackboardBase`

Move To task node.
Moves the AI pawn toward the specified Actor or Location blackboard entry using the navigation system.

## 属性

### AcceptableRadius
- **类型**: `float32`
- **描述**: fixed distance added to threshold between AI and goal location in destination reach test

### FilterClass
- **类型**: `TSubclassOf<UNavigationQueryFilter>`
- **描述**: "None" will result in default filter being used

### ObservedBlackboardValueTolerance
- **类型**: `float32`
- **描述**: if task is expected to react to changes to location represented by BB key
    this property can be used to tweak sensitivity of the mechanism. Value is
    recommended to be less than AcceptableRadius

### bObserveBlackboardValue
- **类型**: `bool`

### bAllowStrafe
- **类型**: `bool`

### bAllowPartialPath
- **类型**: `bool`

### bTrackMovingGoal
- **类型**: `bool`

### bRequireNavigableEndLocation
- **类型**: `bool`

### bProjectGoalLocation
- **类型**: `bool`

### bReachTestIncludesAgentRadius
- **类型**: `bool`

### bReachTestIncludesGoalRadius
- **类型**: `bool`


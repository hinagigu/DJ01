# UAISystem

**继承自**: `UAISystemBase`

## 属性

### PerceptionSystemClassName
- **类型**: `FSoftClassPath`
- **描述**: Class that will be used to spawn the perception system, can be game-specific

### HotSpotManagerClassName
- **类型**: `FSoftClassPath`
- **描述**: Class that will be used to spawn the hot spot manager, can be game-specific

### EnvQueryManagerClassName
- **类型**: `FSoftClassPath`
- **描述**: Class that will be used to spawn the env query manager, can be game-specific

### AcceptanceRadius
- **类型**: `float32`
- **描述**: Default AI movement's acceptance radius used to determine whether
AI reached path's end

### PathfollowingRegularPathPointAcceptanceRadius
- **类型**: `float32`
- **描述**: Value used for pathfollowing's internal code to determine whether AI reached path's point.
    @note this value is not used for path's last point. @see AcceptanceRadius

### PathfollowingNavLinkAcceptanceRadius
- **类型**: `float32`
- **描述**: Similarly to PathfollowingRegularPathPointAcceptanceRadius used by pathfollowing's internals
    but gets applied only when next point on a path represents a begining of navigation link

### bFinishMoveOnGoalOverlap
- **类型**: `bool`
- **描述**: If true, overlapping the goal will be counted by default as finishing a move

### bAcceptPartialPaths
- **类型**: `bool`
- **描述**: Sets default value for rather move tasks accept partial paths or not

### bAllowStrafing
- **类型**: `bool`
- **描述**: Sets default value for rather move tasks allow strafing or not

### bAllowControllersAsEQSQuerier
- **类型**: `bool`
- **描述**: if enable will make EQS not complaint about using Controllers as queriers. Default behavior (false) will
    in places automatically convert controllers to pawns, and complain if code user bypasses the conversion or uses
    pawn-less controller

### bEnableDebuggerPlugin
- **类型**: `bool`
- **描述**: if set, GameplayDebuggerPlugin will be loaded on module's startup

### bForgetStaleActors
- **类型**: `bool`
- **描述**: If set, actors will be forgotten by the perception system when their stimulus has expired.
    If not set, the perception system will remember the actor even if they are no longer perceived and their
    stimuli has exceeded its max age

### bAddBlackboardSelfKey
- **类型**: `bool`
- **描述**: If set to true will result in automatically adding the SelfActor key to new Blackboard assets. It will
    also result in making sure all the BB assets loaded do have the SelfKey entry, via PostLoad

### bClearBBEntryOnBTEQSFail
- **类型**: `bool`

### bBlackboardKeyDecoratorAllowsNoneAsValue
- **类型**: `bool`
- **描述**: If enabled, blackboard based decorators will set key to 'Invalid' on creation or when selected key no longer exists (instead of using the first key of the blackboard).

### DefaultBlackboard
- **类型**: `TSoftObjectPtr<UBlackboardData>`
- **描述**: If set, new BTs will use this BB as default.

### DefaultSightCollisionChannel
- **类型**: `ECollisionChannel`
- **描述**: Which collision channel to use for sight checks by default


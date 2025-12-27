# AAIController

**继承自**: `AController`

AIController is the base class of controllers for AI-controlled Pawns.

Controllers are non-physical actors that can be attached to a pawn to control its actions.
AIControllers manage the artificial intelligence for the pawns they control.
In networked games, they only exist on the server.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Controller/

## 属性

### BrainComponent
- **类型**: `UBrainComponent`
- **描述**: Component responsible for behaviors.

### PerceptionComponent
- **类型**: `UAIPerceptionComponent`

### Blackboard
- **类型**: `UBlackboardComponent`
- **描述**: blackboard

### DefaultNavigationFilterClass
- **类型**: `TSubclassOf<UNavigationQueryFilter>`

### ReceiveMoveCompleted
- **类型**: `FAIMoveCompletedSignature`

### bStartAILogicOnPossess
- **类型**: `bool`

### bStopAILogicOnUnposses
- **类型**: `bool`

### bSkipExtraLOSChecks
- **类型**: `bool`

### bAllowStrafe
- **类型**: `bool`

### bWantsPlayerState
- **类型**: `bool`

### bSetControlRotationFromPawnOrientation
- **类型**: `bool`

### ActionsComp
- **类型**: `UDEPRECATED_PawnActionsComponent`

## 方法

### ClaimTaskResource
```angelscript
void ClaimTaskResource(TSubclassOf<UGameplayTaskResource> ResourceClass)
```

### GetAIPerceptionComponent
```angelscript
UAIPerceptionComponent GetAIPerceptionComponent()
```

### GetFocalPoint
```angelscript
FVector GetFocalPoint()
```
Retrieve the final position that controller should be looking at.

### GetFocalPointOnActor
```angelscript
FVector GetFocalPointOnActor(const AActor Actor)
```
Retrieve the focal point this controller should focus to on given actor.

### GetFocusActor
```angelscript
AActor GetFocusActor()
```
Get the focused actor.

### GetImmediateMoveDestination
```angelscript
FVector GetImmediateMoveDestination()
```
Returns position of current path segment's end.

### GetMoveStatus
```angelscript
EPathFollowingStatus GetMoveStatus()
```
Returns status of path following

### GetPathFollowingComponent
```angelscript
UPathFollowingComponent GetPathFollowingComponent()
```
Returns PathFollowingComponent subobject *

### HasPartialPath
```angelscript
bool HasPartialPath()
```
Returns true if the current PathFollowingComponent's path is partial (does not reach desired destination).

### ClearFocus
```angelscript
void ClearFocus()
```
Clears Focus, will also clear FocalPoint as a result

### SetFocalPoint
```angelscript
void SetFocalPoint(FVector FP)
```
Set the position that controller should be looking at.

### SetFocus
```angelscript
void SetFocus(AActor NewFocus)
```
Set Focus for actor, will set FocalPoint as a result.

### MoveToActor
```angelscript
EPathFollowingRequestResult MoveToActor(AActor Goal, float32 AcceptanceRadius, bool bStopOnOverlap, bool bUsePathfinding, bool bCanStrafe, TSubclassOf<UNavigationQueryFilter> FilterClass, bool bAllowPartialPath)
```
Makes AI go toward specified Goal actor (destination will be continuously updated), aborts any active path following
@param AcceptanceRadius - finish move if pawn gets close enough
@param bStopOnOverlap - add pawn's radius to AcceptanceRadius
@param bUsePathfinding - use navigation data to calculate path (otherwise it will go in straight line)
@param bCanStrafe - set focus related flag: bAllowStrafe
@param FilterClass - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used
@param bAllowPartialPath - use incomplete path when goal can't be reached
    @note AcceptanceRadius has default value or -1 due to Header Parser not being able to recognize UPathFollowingComponent::DefaultAcceptanceRadius

### MoveToLocation
```angelscript
EPathFollowingRequestResult MoveToLocation(FVector Dest, float32 AcceptanceRadius, bool bStopOnOverlap, bool bUsePathfinding, bool bProjectDestinationToNavigation, bool bCanStrafe, TSubclassOf<UNavigationQueryFilter> FilterClass, bool bAllowPartialPath)
```
Makes AI go toward specified Dest location, aborts any active path following
@param AcceptanceRadius - finish move if pawn gets close enough
@param bStopOnOverlap - add pawn's radius to AcceptanceRadius
@param bUsePathfinding - use navigation data to calculate path (otherwise it will go in straight line)
@param bProjectDestinationToNavigation - project location on navigation data before using it
@param bCanStrafe - set focus related flag: bAllowStrafe
@param FilterClass - navigation filter for pathfinding adjustments. If none specified DefaultNavigationFilterClass will be used
@param bAllowPartialPath - use incomplete path when goal can't be reached
    @note AcceptanceRadius has default value or -1 due to Header Parser not being able to recognize UPathFollowingComponent::DefaultAcceptanceRadius

### OnUsingBlackBoard
```angelscript
void OnUsingBlackBoard(UBlackboardComponent BlackboardComp, UBlackboardData BlackboardAsset)
```

### RunBehaviorTree
```angelscript
bool RunBehaviorTree(UBehaviorTree BTAsset)
```
Starts executing behavior tree.

### SetMoveBlockDetection
```angelscript
void SetMoveBlockDetection(bool bEnable)
```
Updates state of movement block detection.

### SetPathFollowingComponent
```angelscript
void SetPathFollowingComponent(UPathFollowingComponent NewPFComponent)
```
Note that this function does not do any pathfollowing state transfer.
    Intended to be called as part of initialization/setup process

### UnclaimTaskResource
```angelscript
void UnclaimTaskResource(TSubclassOf<UGameplayTaskResource> ResourceClass)
```

### UseBlackboard
```angelscript
bool UseBlackboard(UBlackboardData BlackboardAsset, UBlackboardComponent& BlackboardComponent)
```
Makes AI use the specified Blackboard asset & creates a Blackboard Component if one does not already exist.
@param       BlackboardAsset                 The Blackboard asset to use.
@param       BlackboardComponent             The Blackboard component that was used or created to work with the passed-in Blackboard Asset.
@return true if we successfully linked the blackboard asset to the blackboard component.


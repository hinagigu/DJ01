# __AIHelper

## 方法

### GetAIController
```angelscript
AAIController GetAIController(AActor ControlledActor)
```
The way it works exactly is if the actor passed in is a pawn, then the function retrieves
    pawn's controller cast to AIController. Otherwise the function returns actor cast to AIController.

### GetBlackboard
```angelscript
UBlackboardComponent GetBlackboard(AActor Target)
```

### GetCurrentPath
```angelscript
UNavigationPath GetCurrentPath(AController Controller)
```
Returns a NEW UOBJECT that is a COPY of navigation path given controller is currently using.
    The result being a copy means you won't be able to influence agent's pathfollowing
    by manipulating received path.
    Please use GetCurrentPathPoints if you only need the array of path points.

### GetCurrentPathIndex
```angelscript
int GetCurrentPathIndex(const AController Controller)
```
Return the path index the given controller is currently at. Returns INDEX_NONE if no path.

### GetCurrentPathPoints
```angelscript
TArray<FVector> GetCurrentPathPoints(AController Controller)
```
Returns an array of navigation path points given controller is currently using.

### GetNextNavLinkIndex
```angelscript
int GetNextNavLinkIndex(const AController Controller)
```
Return the path index of the next nav link for the current path of the given controller. Returns INDEX_NONE if no path or no incoming nav link.

### IsValidAIDirection
```angelscript
bool IsValidAIDirection(FVector DirectionVector)
```

### IsValidAILocation
```angelscript
bool IsValidAILocation(FVector Location)
```

### IsValidAIRotation
```angelscript
bool IsValidAIRotation(FRotator Rotation)
```

### LockAIResourcesWithAnimation
```angelscript
void LockAIResourcesWithAnimation(UAnimInstance AnimInstance, bool bLockMovement, bool LockAILogic)
```
locks indicated AI resources of animated pawn

### SendAIMessage
```angelscript
void SendAIMessage(APawn Target, FName Message, UObject MessageSource, bool bSuccess)
```

### SimpleMoveToActor
```angelscript
void SimpleMoveToActor(AController Controller, const AActor Goal)
```

### SimpleMoveToLocation
```angelscript
void SimpleMoveToLocation(AController Controller, FVector Goal)
```

### SpawnAIFromClass
```angelscript
APawn SpawnAIFromClass(TSubclassOf<APawn> PawnClass, UBehaviorTree BehaviorTree, FVector Location, FRotator Rotation, bool bNoCollisionFail, AActor Owner)
```
Spawns AI agent of a given class. The PawnClass needs to have AIController
set for the function to spawn a controller as well.
@param BehaviorTree if set, and the function has successfully spawned
     and AI controller, this BehaviorTree asset will be assigned to the AI
     controller, and run.
@param Owner lets you spawn the AI in a sublevel rather than in the
     persistent level (which is the default behavior).

### UnlockAIResourcesWithAnimation
```angelscript
void UnlockAIResourcesWithAnimation(UAnimInstance AnimInstance, bool bUnlockMovement, bool UnlockAILogic)
```
unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources


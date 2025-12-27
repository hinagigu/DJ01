# __UNavigationSystemV1

## 方法

### FindPathToActorSynchronously
```angelscript
UNavigationPath FindPathToActorSynchronously(FVector PathStart, AActor GoalActor, float32 TetherDistance, AActor PathfindingContext, TSubclassOf<UNavigationQueryFilter> FilterClass)
```
Finds path instantly, in a FindPath Synchronously. Main advantage over FindPathToLocationSynchronously is that
    the resulting path will automatically get updated if goal actor moves more than TetherDistance away from last path node
    @param PathfindingContext could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query

### FindPathToLocationSynchronously
```angelscript
UNavigationPath FindPathToLocationSynchronously(FVector PathStart, FVector PathEnd, AActor PathfindingContext, TSubclassOf<UNavigationQueryFilter> FilterClass)
```
Finds path instantly, in a FindPath Synchronously.
    @param PathfindingContext could be one of following: NavigationData (like Navmesh actor), Pawn or Controller. This parameter determines parameters of specific pathfinding query

### GetNavigationSystem
```angelscript
UNavigationSystemV1 GetNavigationSystem()
```
Blueprint functions

### GetPathCost
```angelscript
ENavigationQueryResult GetPathCost(FVector PathStart, FVector PathEnd, float& PathCost, ANavigationData NavData, TSubclassOf<UNavigationQueryFilter> FilterClass)
```
Potentially expensive. Use with caution. Consider using UPathFollowingComponent::GetRemainingPathCost instead

### GetPathLength
```angelscript
ENavigationQueryResult GetPathLength(FVector PathStart, FVector PathEnd, float& PathLength, ANavigationData NavData, TSubclassOf<UNavigationQueryFilter> FilterClass)
```
Potentially expensive. Use with caution

### IsNavigationBeingBuilt
```angelscript
bool IsNavigationBeingBuilt()
```

### IsNavigationBeingBuiltOrLocked
```angelscript
bool IsNavigationBeingBuiltOrLocked()
```

### GetRandomLocationInNavigableRadius
```angelscript
bool GetRandomLocationInNavigableRadius(FVector Origin, FVector& RandomLocation, float32 Radius, ANavigationData NavData, TSubclassOf<UNavigationQueryFilter> FilterClass)
```
Generates a random location in navigable space within given radius of Origin.
    @return Return Value represents if the call was successful

### GetRandomReachablePointInRadius
```angelscript
bool GetRandomReachablePointInRadius(FVector Origin, FVector& RandomLocation, float32 Radius, ANavigationData NavData, TSubclassOf<UNavigationQueryFilter> FilterClass)
```
Generates a random location reachable from given Origin location.
    @return Return Value represents if the call was successful

### ProjectPointToNavigation
```angelscript
bool ProjectPointToNavigation(FVector Point, FVector& ProjectedLocation, ANavigationData NavData, TSubclassOf<UNavigationQueryFilter> FilterClass, FVector QueryExtent)
```
Project a point onto the NavigationData

### NavigationRaycast
```angelscript
bool NavigationRaycast(FVector RayStart, FVector RayEnd, FVector& HitLocation, TSubclassOf<UNavigationQueryFilter> FilterClass, AController Querier)
```
Performs navigation raycast on NavigationData appropriate for given Querier.
    @param Querier if not passed default navigation data will be used
    @param HitLocation if line was obstructed this will be set to hit location. Otherwise it contains SegmentEnd
    @return true if line from RayStart to RayEnd was obstructed. Also, true when no navigation data present

### StaticClass
```angelscript
UClass StaticClass()
```


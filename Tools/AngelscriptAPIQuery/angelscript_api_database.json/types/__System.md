# __System

## 方法

### AsyncLineTraceByChannel
```angelscript
FTraceHandle AsyncLineTraceByChannel(EAsyncTraceType InTraceType, FVector Start, FVector End, ECollisionChannel TraceChannel, FCollisionQueryParams Params, FCollisionResponseParams ResponseParam, FScriptTraceDelegate InDelegate, uint UserData)
```

### AsyncLineTraceByObjectType
```angelscript
FTraceHandle AsyncLineTraceByObjectType(EAsyncTraceType InTraceType, FVector Start, FVector End, FCollisionObjectQueryParams ObjectQueryParams, FCollisionQueryParams Params, FScriptTraceDelegate InDelegate, uint UserData)
```

### AsyncLineTraceByProfile
```angelscript
FTraceHandle AsyncLineTraceByProfile(EAsyncTraceType InTraceType, FVector Start, FVector End, FName ProfileName, FCollisionQueryParams Params, FScriptTraceDelegate InDelegate, uint UserData)
```

### AsyncSweepByChannel
```angelscript
FTraceHandle AsyncSweepByChannel(EAsyncTraceType InTraceType, FVector Start, FVector End, FQuat Rot, ECollisionChannel TraceChannel, FCollisionShape CollisionShape, FCollisionQueryParams Params, FCollisionResponseParams ResponseParam, FScriptTraceDelegate InDelegate, uint UserData)
```

### AsyncSweepByObjectType
```angelscript
FTraceHandle AsyncSweepByObjectType(EAsyncTraceType InTraceType, FVector Start, FVector End, FQuat Rot, FCollisionObjectQueryParams ObjectQueryParams, FCollisionShape CollisionShape, FCollisionQueryParams Params, FScriptTraceDelegate InDelegate, uint UserData)
```

### AsyncSweepByProfile
```angelscript
FTraceHandle AsyncSweepByProfile(EAsyncTraceType InTraceType, FVector Start, FVector End, FQuat Rot, FName ProfileName, FCollisionShape CollisionShape, FCollisionQueryParams Params, FScriptTraceDelegate InDelegate, uint UserData)
```

### AsyncOverlapByChannel
```angelscript
FTraceHandle AsyncOverlapByChannel(FVector Pos, FQuat Rot, ECollisionChannel TraceChannel, FCollisionShape CollisionShape, FCollisionQueryParams Params, FCollisionResponseParams ResponseParam, FScriptOverlapDelegate InDelegate, uint UserData)
```

### AsyncOverlapByObjectType
```angelscript
FTraceHandle AsyncOverlapByObjectType(FVector Pos, FQuat Rot, FCollisionObjectQueryParams ObjectQueryParams, FCollisionShape CollisionShape, FCollisionQueryParams Params, FScriptOverlapDelegate InDelegate, uint UserData)
```

### QueryTraceData
```angelscript
bool QueryTraceData(FTraceHandle Handle, FTraceDatum& OutData)
```

### QueryOverlapData
```angelscript
bool QueryOverlapData(FTraceHandle Handle, FOverlapDatum& OutData)
```

### IsTraceHandleValid
```angelscript
bool IsTraceHandleValid(FTraceHandle Handle, bool bOverlapTrace)
```

### AddFloatHistorySample
```angelscript
FDebugFloatHistory AddFloatHistorySample(float32 Value, FDebugFloatHistory FloatHistory)
```

### BeginTransaction
```angelscript
int BeginTransaction(FString Context, FText Description, UObject PrimaryObject)
```
Begin a new undo transaction. An undo transaction is defined as all actions which take place when the user selects "undo" a single time.
@note If there is already an active transaction in progress, then this increments that transaction's action counter instead of beginning a new transaction.
@note You must call TransactObject before modifying each object that should be included in this undo transaction.
@note Only available in the editor.

@param       Context                 The context for the undo session. Typically the tool/editor that caused the undo operation.
@param       Description             The description for the undo session. This is the text that will appear in the "Edit" menu next to the Undo item.
@param       PrimaryObject   The primary object that the undo session operators on (can be null, and mostly is).

@return      The number of active actions when BeginTransaction was called (values greater than 0 indicate that there was already an existing undo transaction in progress), or -1 on failure.

### BoxOverlapActors
```angelscript
bool BoxOverlapActors(FVector BoxPos, FVector BoxExtent, TArray<EObjectTypeQuery> ObjectTypes, UClass ActorClassFilter, TArray<AActor> ActorsToIgnore, TArray<AActor>& OutActors)
```
Returns an array of actors that overlap the given axis-aligned box.
@param WorldContext  World context
@param BoxPos                Center of box.
@param BoxExtent             Extents of box.
@param Filter                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors             Returned array of actors. Unsorted.
@return                              true if there was an overlap that passed the filters, false otherwise.

### BoxOverlapComponents
```angelscript
bool BoxOverlapComponents(FVector BoxPos, FVector Extent, TArray<EObjectTypeQuery> ObjectTypes, UClass ComponentClassFilter, TArray<AActor> ActorsToIgnore, TArray<UPrimitiveComponent>& OutComponents)
```
Returns an array of components that overlap the given axis-aligned box.
@param WorldContext  World context
@param BoxPos                Center of box.
@param BoxExtent             Extents of box.
@param Filter                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors             Returned array of actors. Unsorted.
@return                              true if there was an overlap that passed the filters, false otherwise.

### BoxTraceMulti
```angelscript
bool BoxTraceMulti(FVector Start, FVector End, FVector HalfSize, FRotator Orientation, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a box along the given line and returns all hits encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

@param Start                  Start of line segment.
@param End                    End of line segment.
@param HalfSize           Distance from the center of box along each axis
@param Orientation    Orientation of the box
@param TraceChannel
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHits                A list of hits, sorted along the trace from start to finish. The blocking hit will be the last hit, if there was one.
@return                               True if there was a blocking hit, false otherwise.

### BoxTraceMultiByProfile
```angelscript
bool BoxTraceMultiByProfile(FVector Start, FVector End, FVector HalfSize, FRotator Orientation, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweep a box against the world and return all initial overlaps using a specific profile, then overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

@param Start                  Start of line segment.
@param End                    End of line segment.
@param HalfSize           Distance from the center of box along each axis
@param Orientation    Orientation of the box
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHits                A list of hits, sorted along the trace from start to finish. The blocking hit will be the last hit, if there was one.
@return                               True if there was a blocking hit, false otherwise.

### BoxTraceMultiForObjects
```angelscript
bool BoxTraceMultiForObjects(FVector Start, FVector End, FVector HalfSize, FRotator Orientation, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a box along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param Start                  Start of line segment.
@param End                    End of line segment.
@param Orientation
@param HalfSize               Radius of the sphere to sweep
@param ObjectTypes    Array of Object Types to trace
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHits                A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                               True if there was a hit, false otherwise.

### BoxTraceSingle
```angelscript
bool BoxTraceSingle(FVector Start, FVector End, FVector HalfSize, FRotator Orientation, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a box along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

@param Start                  Start of line segment.
@param End                    End of line segment.
@param HalfSize           Distance from the center of box along each axis
@param Orientation    Orientation of the box
@param TraceChannel
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit                 Properties of the trace hit.
@return                               True if there was a hit, false otherwise.

### BoxTraceSingleByProfile
```angelscript
bool BoxTraceSingleByProfile(FVector Start, FVector End, FVector HalfSize, FRotator Orientation, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweep a box against the world and return the first blocking hit using a specific profile

@param Start                  Start of line segment.
@param End                    End of line segment.
@param HalfSize           Distance from the center of box along each axis
@param Orientation    Orientation of the box
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit                 Properties of the trace hit.
@return                               True if there was a hit, false otherwise.

### BoxTraceSingleForObjects
```angelscript
bool BoxTraceSingleForObjects(FVector Start, FVector End, FVector HalfSize, FRotator Orientation, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a box along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param Start                  Start of line segment.
@param End                    End of line segment.
@param Orientation
@param HalfSize               Radius of the sphere to sweep
@param ObjectTypes    Array of Object Types to trace
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit                 Properties of the trace hit.
@return                               True if there was a hit, false otherwise.

### BreakARFilter
```angelscript
void BreakARFilter(FARFilter InARFilter, TArray<FName>& PackageNames, TArray<FName>& PackagePaths, TArray<FSoftObjectPath>& SoftObjectPaths, TArray<FTopLevelAssetPath>& ClassPaths, TSet<FTopLevelAssetPath>& RecursiveClassPathsExclusionSet, TArray<FName>& ClassNames, TSet<FName>& RecursiveClassesExclusionSet, bool& bRecursivePaths, bool& bRecursiveClasses, bool& bIncludeOnlyOnDiskAssets)
```
Breaks an ARFilter struct into its component pieces. You should be using ClassPaths and RecursiveClassPathsExclusionSet from this node, ClassNames and RecursiveClassesExclusionSet are deprecated.

@param ClassNames [DEPRECATED] - Class names are now represented by path names. Please use the ClassPaths output instead.
@param RecursiveClassesExclusionSet [DEPRECATED] - Class names are now represented by path names. Please use the RecursiveClassPathsExclusionSet output instead.

### BreakSoftClassPath
```angelscript
void BreakSoftClassPath(FSoftClassPath InSoftClassPath, FString& PathString)
```
Gets the path string out of a Soft Class Path

### BreakSoftObjectPath
```angelscript
void BreakSoftObjectPath(FSoftObjectPath InSoftObjectPath, FString& PathString)
```
Gets the path string out of a Soft Object Path

### BreakTopLevelAssetPath
```angelscript
void BreakTopLevelAssetPath(FTopLevelAssetPath TopLevelAssetPath, FString& PathString)
```
Gets the path string out of a TopLevelAssetPath

### CancelTransaction
```angelscript
void CancelTransaction(int Index)
```
Cancel the current transaction, and no longer capture actions to be placed in the undo buffer.
@note Only available in the editor.

@param       Index           The action counter to cancel transactions from (as returned by a call to BeginTransaction).

### CanLaunchURL
```angelscript
bool CanLaunchURL(FString URL)
```

### CapsuleOverlapActors
```angelscript
bool CapsuleOverlapActors(FVector CapsulePos, float32 Radius, float32 HalfHeight, TArray<EObjectTypeQuery> ObjectTypes, UClass ActorClassFilter, TArray<AActor> ActorsToIgnore, TArray<AActor>& OutActors)
```
Returns an array of actors that overlap the given capsule.
@param WorldContext  World context
@param CapsulePos    Center of the capsule.
@param Radius                Radius of capsule hemispheres and radius of center cylinder portion.
@param HalfHeight    Half-height of the capsule (from center of capsule to tip of hemisphere.
@param Filter                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors             Returned array of actors. Unsorted.
@return                              true if there was an overlap that passed the filters, false otherwise.

### CapsuleOverlapComponents
```angelscript
bool CapsuleOverlapComponents(FVector CapsulePos, float32 Radius, float32 HalfHeight, TArray<EObjectTypeQuery> ObjectTypes, UClass ComponentClassFilter, TArray<AActor> ActorsToIgnore, TArray<UPrimitiveComponent>& OutComponents)
```
Returns an array of components that overlap the given capsule.
@param WorldContext  World context
@param CapsulePos    Center of the capsule.
@param Radius                Radius of capsule hemispheres and radius of center cylinder portion.
@param HalfHeight    Half-height of the capsule (from center of capsule to tip of hemisphere.
@param Filter                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors             Returned array of actors. Unsorted.
@return                              true if there was an overlap that passed the filters, false otherwise.

### CapsuleTraceMulti
```angelscript
bool CapsuleTraceMulti(FVector Start, FVector End, float32 Radius, float32 HalfHeight, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a capsule along the given line and returns all hits encountered up to and including the first blocking hit.
This trace finds the objects that RESPOND to the given TraceChannel

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the capsule to sweep
@param HalfHeight    Distance from center of capsule to tip of hemisphere endcap.
@param TraceChannel
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHits               A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                              True if there was a blocking hit, false otherwise.

### CapsuleTraceMultiByProfile
```angelscript
bool CapsuleTraceMultiByProfile(FVector Start, FVector End, float32 Radius, float32 HalfHeight, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweep a capsule against the world and return all initial overlaps using a specific profile, then overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

@param WorldContext   World context
@param Start                  Start of line segment.
@param End                    End of line segment.
@param Radius                 Radius of the capsule to sweep
@param HalfHeight             Distance from center of capsule to tip of hemisphere endcap.
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHits                A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                               True if there was a blocking hit, false otherwise.

### CapsuleTraceMultiForObjects
```angelscript
bool CapsuleTraceMultiForObjects(FVector Start, FVector End, float32 Radius, float32 HalfHeight, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a capsule along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the capsule to sweep
@param HalfHeight    Distance from center of capsule to tip of hemisphere endcap.
@param ObjectTypes   Array of Object Types to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHits               A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                              True if there was a hit, false otherwise.

### CapsuleTraceSingle
```angelscript
bool CapsuleTraceSingle(FVector Start, FVector End, float32 Radius, float32 HalfHeight, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a capsule along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPOND to the given TraceChannel

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the capsule to sweep
@param HalfHeight    Distance from center of capsule to tip of hemisphere endcap.
@param TraceChannel
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### CapsuleTraceSingleByProfile
```angelscript
bool CapsuleTraceSingleByProfile(FVector Start, FVector End, float32 Radius, float32 HalfHeight, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweep a capsule against the world and return the first blocking hit using a specific profile

@param WorldContext   World context
@param Start                  Start of line segment.
@param End                    End of line segment.
@param Radius                 Radius of the capsule to sweep
@param HalfHeight             Distance from center of capsule to tip of hemisphere endcap.
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit                 Properties of the trace hit.
@return                               True if there was a hit, false otherwise.

### CapsuleTraceSingleForObjects
```angelscript
bool CapsuleTraceSingleForObjects(FVector Start, FVector End, float32 Radius, float32 HalfHeight, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a capsule along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the capsule to sweep
@param HalfHeight    Distance from center of capsule to tip of hemisphere endcap.
@param ObjectTypes   Array of Object Types to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### CollectGarbage
```angelscript
void CollectGarbage()
```
Deletes all unreferenced objects, keeping only referenced objects (this command will be queued and happen at the end of the frame)
Note: This can be a slow operation, and should only be performed where a hitch would be acceptable

### ComponentOverlapActors
```angelscript
bool ComponentOverlapActors(UPrimitiveComponent Component, FTransform ComponentTransform, TArray<EObjectTypeQuery> ObjectTypes, UClass ActorClassFilter, TArray<AActor> ActorsToIgnore, TArray<AActor>& OutActors)
```
Returns an array of actors that overlap the given component.
@param Component                             Component to test with.
@param ComponentTransform    Defines where to place the component for overlap testing.
@param Filter                                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter                   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors                             Returned array of actors. Unsorted.
@return                                              true if there was an overlap that passed the filters, false otherwise.

### ComponentOverlapComponents
```angelscript
bool ComponentOverlapComponents(UPrimitiveComponent Component, FTransform ComponentTransform, TArray<EObjectTypeQuery> ObjectTypes, UClass ComponentClassFilter, TArray<AActor> ActorsToIgnore, TArray<UPrimitiveComponent>& OutComponents)
```
Returns an array of components that overlap the given component.
@param Component                             Component to test with.
@param ComponentTransform    Defines where to place the component for overlap testing.
@param Filter                                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter                   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors                             Returned array of actors. Unsorted.
@return                                              true if there was an overlap that passed the filters, false otherwise.

### ControlScreensaver
```angelscript
void ControlScreensaver(bool bAllowScreenSaver)
```
Allows or inhibits screensaver
@param       bAllowScreenSaver               If false, don't allow screensaver if possible, otherwise allow default behavior

### Conv_ComponentReferenceToSoftComponentReference
```angelscript
FSoftComponentReference Conv_ComponentReferenceToSoftComponentReference(FComponentReference ComponentReference)
```

### Conv_ObjectToClass
```angelscript
UClass Conv_ObjectToClass(UObject Object, TSubclassOf<UObject> Class)
```
Casts from an object to a class, this will only work if the object is already a class

### Conv_PrimaryAssetIdToString
```angelscript
FString Conv_PrimaryAssetIdToString(FPrimaryAssetId PrimaryAssetId)
```
Converts a Primary Asset Id to a string. The other direction is not provided because it cannot be validated

### Conv_PrimaryAssetTypeToString
```angelscript
FString Conv_PrimaryAssetTypeToString(FPrimaryAssetType PrimaryAssetType)
```
Converts a Primary Asset Type to a string. The other direction is not provided because it cannot be validated

### Conv_SoftClassPathToSoftClassRef
```angelscript
TSoftClassPtr<UObject> Conv_SoftClassPathToSoftClassRef(FSoftClassPath SoftClassPath)
```
Converts a Soft Class Path into a base Soft Class Reference, this is not guaranteed to be resolvable

### Conv_SoftClassReferenceToString
```angelscript
FString Conv_SoftClassReferenceToString(TSoftClassPtr<UObject> SoftClassReference)
```
Converts a Soft Class Reference to a path string

### Conv_SoftObjectReferenceToString
```angelscript
FString Conv_SoftObjectReferenceToString(TSoftObjectPtr<UObject> SoftObjectReference)
```
Converts a Soft Object Reference to a path string

### Conv_SoftObjPathToSoftObjRef
```angelscript
TSoftObjectPtr<UObject> Conv_SoftObjPathToSoftObjRef(FSoftObjectPath SoftObjectPath)
```
Converts a Soft Object Path into a base Soft Object Reference, this is not guaranteed to be resolvable

### Conv_SoftObjRefToSoftClassPath
```angelscript
FSoftClassPath Conv_SoftObjRefToSoftClassPath(TSoftClassPtr<UObject> SoftClassReference)
```
Converts a Soft Class Reference into a Soft Class Path (which can be used like a Soft Object Path)

### Conv_SoftObjRefToSoftObjPath
```angelscript
FSoftObjectPath Conv_SoftObjRefToSoftObjPath(TSoftObjectPtr<UObject> SoftObjectReference)
```
Converts a Soft Object Reference into a Soft Object Path

### ConvertToAbsolutePath
```angelscript
FString ConvertToAbsolutePath(FString Filename)
```
Converts passed in filename to use a absolute path

### ConvertToRelativePath
```angelscript
FString ConvertToRelativePath(FString Filename)
```
Converts passed in filename to use a relative path

### CreateCopyForUndoBuffer
```angelscript
void CreateCopyForUndoBuffer(UObject ObjectToModify)
```
Mark as modified.

### Delay
```angelscript
void Delay(float32 Duration, FLatentActionInfo LatentInfo)
```
Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

@param WorldContext  World context.
@param Duration              length of delay (in seconds).
@param LatentInfo    The latent action.

### DelayUntilNextTick
```angelscript
void DelayUntilNextTick(FLatentActionInfo LatentInfo)
```
Perform a latent action with a delay of one tick.  Calling again while it is counting down will be ignored.

@param WorldContext  World context.
@param LatentInfo    The latent action.

### DoesClassImplementInterface
```angelscript
bool DoesClassImplementInterface(const UClass TestClass, TSubclassOf<UInterface> Interface)
```
Checks if the given class implements a specific interface, works for both native and blueprint interfacse

### DoesImplementInterface
```angelscript
bool DoesImplementInterface(const UObject TestObject, TSubclassOf<UInterface> Interface)
```
Checks if the given object implements a specific interface, works for both native and blueprint interfacse

### DrawDebugArrow
```angelscript
void DrawDebugArrow(FVector LineStart, FVector LineEnd, float32 ArrowSize, FLinearColor LineColor, float32 Duration, float32 Thickness)
```
Draw directional arrow, pointing from LineStart to LineEnd.

### DrawDebugBox
```angelscript
void DrawDebugBox(FVector Center, FVector Extent, FLinearColor LineColor, FRotator Rotation, float32 Duration, float32 Thickness)
```
Draw a debug box

### DrawDebugCamera
```angelscript
void DrawDebugCamera(const ACameraActor CameraActor, FLinearColor CameraColor, float32 Duration)
```
Draw a debug camera shape.

### DrawDebugCapsule
```angelscript
void DrawDebugCapsule(FVector Center, float32 HalfHeight, float32 Radius, FRotator Rotation, FLinearColor LineColor, float32 Duration, float32 Thickness)
```
Draw a debug capsule

### DrawDebugCircle
```angelscript
void DrawDebugCircle(FVector Center, float32 Radius, int NumSegments, FLinearColor LineColor, float32 Duration, float32 Thickness, FVector YAxis, FVector ZAxis, bool bDrawAxis)
```
Draw a debug circle!

### DrawDebugConeInDegrees
```angelscript
void DrawDebugConeInDegrees(FVector Origin, FVector Direction, float32 Length, float32 AngleWidth, float32 AngleHeight, int NumSides, FLinearColor LineColor, float32 Duration, float32 Thickness)
```
Draw a debug cone
Angles are specified in degrees

### DrawDebugCoordinateSystem
```angelscript
void DrawDebugCoordinateSystem(FVector AxisLoc, FRotator AxisRot, float32 Scale, float32 Duration, float32 Thickness)
```
Draw a debug coordinate system.

### DrawDebugCylinder
```angelscript
void DrawDebugCylinder(FVector Start, FVector End, float32 Radius, int Segments, FLinearColor LineColor, float32 Duration, float32 Thickness)
```
Draw a debug cylinder

### DrawDebugFloatHistoryLocation
```angelscript
void DrawDebugFloatHistoryLocation(FDebugFloatHistory FloatHistory, FVector DrawLocation, FVector2D DrawSize, FLinearColor DrawColor, float32 Duration)
```
Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawLocation for the location in the world, rotation will face camera of first player.

### DrawDebugFloatHistoryTransform
```angelscript
void DrawDebugFloatHistoryTransform(FDebugFloatHistory FloatHistory, FTransform DrawTransform, FVector2D DrawSize, FLinearColor DrawColor, float32 Duration)
```
Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawTransform for the position in the world.

### DrawDebugFrustum
```angelscript
void DrawDebugFrustum(FTransform FrustumTransform, FLinearColor FrustumColor, float32 Duration, float32 Thickness)
```
Draws a debug frustum.

### DrawDebugLine
```angelscript
void DrawDebugLine(FVector LineStart, FVector LineEnd, FLinearColor LineColor, float32 Duration, float32 Thickness)
```
Draw a debug line

### DrawDebugPlane
```angelscript
void DrawDebugPlane(FPlane PlaneCoordinates, FVector Location, float32 Size, FLinearColor PlaneColor, float32 Duration)
```
Draws a debug plane.

### DrawDebugPoint
```angelscript
void DrawDebugPoint(FVector Position, float32 Size, FLinearColor PointColor, float32 Duration)
```
Draw a debug point

### DrawDebugSphere
```angelscript
void DrawDebugSphere(FVector Center, float32 Radius, int Segments, FLinearColor LineColor, float32 Duration, float32 Thickness)
```
Draw a debug sphere

### DrawDebugString
```angelscript
void DrawDebugString(FVector TextLocation, FString Text, AActor TestBaseActor, FLinearColor TextColor, float32 Duration)
```
Draw a debug string at a 3d world location.

### EndTransaction
```angelscript
int EndTransaction()
```
Attempt to end the current undo transaction. Only successful if the transaction's action counter is 1.
@note Only available in the editor.

@return      The number of active actions when EndTransaction was called (a value of 1 indicates that the transaction was successfully closed), or -1 on failure.

### EqualEqual_PrimaryAssetId
```angelscript
bool EqualEqual_PrimaryAssetId(FPrimaryAssetId A, FPrimaryAssetId B)
```
Returns true if the values are equal (A == B)

### EqualEqual_PrimaryAssetType
```angelscript
bool EqualEqual_PrimaryAssetType(FPrimaryAssetType A, FPrimaryAssetType B)
```
Returns true if the values are equal (A == B)

### EqualEqual_SoftClassReference
```angelscript
bool EqualEqual_SoftClassReference(TSoftClassPtr<UObject> A, TSoftClassPtr<UObject> B)
```
Returns true if the values are equal (A == B)

### EqualEqual_SoftObjectReference
```angelscript
bool EqualEqual_SoftObjectReference(TSoftObjectPtr<UObject> A, TSoftObjectPtr<UObject> B)
```
Returns true if the values are equal (A == B)

### ExecuteConsoleCommand
```angelscript
void ExecuteConsoleCommand(FString Command, APlayerController SpecificPlayer)
```
Executes a console command, optionally on a specific controller

@param       Command                 Command to send to the console
@param       SpecificPlayer  If specified, the console command will be routed through the specified player

### FlushDebugStrings
```angelscript
void FlushDebugStrings()
```
Removes all debug strings.

@param WorldContext  World context

### FlushPersistentDebugLines
```angelscript
void FlushPersistentDebugLines()
```
Flush all persistent debug lines and shapes.

@param WorldContext  World context

### ForceCloseAdBanner
```angelscript
void ForceCloseAdBanner()
```
Forces closed any displayed ad. Can lead to loss of revenue
(iOS and Android only)

### GetActorListFromComponentList
```angelscript
void GetActorListFromComponentList(TArray<UPrimitiveComponent> ComponentList, UClass ActorClassFilter, TArray<AActor>& OutActorList)
```
Returns an array of unique actors represented by the given list of components.
@param ComponentList         List of components.
@param ClassFilter           If set, will only return results of this class or subclasses of it.
@param OutActorList          Start of line segment.

### GetAdIDCount
```angelscript
int GetAdIDCount()
```
Retrieves the total number of Ad IDs that can be selected between

### GetBuildConfiguration
```angelscript
FString GetBuildConfiguration()
```
Build configuration, for displaying to end users in diagnostics.

### GetBuildVersion
```angelscript
FString GetBuildVersion()
```
Build version, for displaying to end users in diagnostics.

### GetClassDisplayName
```angelscript
FString GetClassDisplayName(const UClass Class)
```
Returns the display name of a class

### GetClassFromPrimaryAssetId
```angelscript
TSubclassOf<UObject> GetClassFromPrimaryAssetId(FPrimaryAssetId PrimaryAssetId)
```
Returns the Blueprint Class associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

### GetClassTopLevelAssetPath
```angelscript
FTopLevelAssetPath GetClassTopLevelAssetPath(const UClass Class)
```
Returns the full path to the specified class as a Top Level Asset Path used by asset utilities

### GetCommandLine
```angelscript
FString GetCommandLine()
```
Returns the command line that the process was launched with.

### GetComponentBounds
```angelscript
void GetComponentBounds(const USceneComponent Component, FVector& Origin, FVector& BoxExtent, float32& SphereRadius)
```
Get bounds

### GetConsoleVariableBoolValue
```angelscript
bool GetConsoleVariableBoolValue(FString VariableName)
```
Evaluates, if it exists, whether the specified integer console variable has a non-zero value (true) or not (false).

@param       VariableName    Name of the console variable to find.
@return      True if found and has a non-zero value, false otherwise.

### GetConsoleVariableFloatValue
```angelscript
float32 GetConsoleVariableFloatValue(FString VariableName)
```
Attempts to retrieve the value of the specified float console variable, if it exists.

@param       VariableName    Name of the console variable to find.
@return      The value if found, 0 otherwise.

### GetConsoleVariableIntValue
```angelscript
int GetConsoleVariableIntValue(FString VariableName)
```
Attempts to retrieve the value of the specified integer console variable, if it exists.

@param       VariableName    Name of the console variable to find.
@return      The value if found, 0 otherwise.

### GetConsoleVariableStringValue
```angelscript
FString GetConsoleVariableStringValue(FString VariableName)
```
Attempts to retrieve the value of the specified string console variable, if it exists.

@param       VariableName    Name of the console variable to find.
@return      The value if found, empty string otherwise.

### GetConvenientWindowedResolutions
```angelscript
bool GetConvenientWindowedResolutions(TArray<FIntPoint>& Resolutions)
```
Gets the list of windowed resolutions which are convenient for the current primary display size.
@return true if successfully queried the device for available resolutions.

### GetCurrentBundleState
```angelscript
bool GetCurrentBundleState(FPrimaryAssetId PrimaryAssetId, bool bForceCurrentState, TArray<FName>& OutBundles)
```
Returns the list of loaded bundles for a given Primary Asset. This will return false if the asset is not loaded at all.
If ForceCurrentState is true it will return the current state even if a load is in process

### GetDefaultLanguage
```angelscript
FString GetDefaultLanguage()
```
Get the default language (for localization) used by this platform
@note This is typically the same as GetDefaultLocale unless the platform distinguishes between the two
@note This should be returned in IETF language tag form:
 - A two-letter ISO 639-1 language code (eg, "zh")
 - An optional four-letter ISO 15924 script code (eg, "Hans")
 - An optional two-letter ISO 3166-1 country code (eg, "CN")
@return The language as an IETF language tag (eg, "zh-Hans-CN")

### GetDefaultLocale
```angelscript
FString GetDefaultLocale()
```
Get the default locale (for internationalization) used by this platform
@note This should be returned in IETF language tag form:
 - A two-letter ISO 639-1 language code (eg, "zh")
 - An optional four-letter ISO 15924 script code (eg, "Hans")
 - An optional two-letter ISO 3166-1 country code (eg, "CN")
@return The locale as an IETF language tag (eg, "zh-Hans-CN")

### GetDeviceId
```angelscript
FString GetDeviceId()
```
Returns the platform specific unique device id

### GetDisplayName
```angelscript
FString GetDisplayName(const UObject Object)
```
Returns the display name (or actor label), for displaying as a debugging aid.
Note: In editor builds, this is the actor label.  In non-editor builds, this is the actual object name.  This function should not be used to uniquely identify actors!
It is not localized and should not be used for display to an end user of a game.

### GetEngineVersion
```angelscript
FString GetEngineVersion()
```
Engine build number, for displaying to end users.

### GetEnumTopLevelAssetPath
```angelscript
FTopLevelAssetPath GetEnumTopLevelAssetPath(const UEnum Enum)
```
Returns the full path to the specified enum as a Top Level Asset Path used by asset utilities

### GetFrameCount
```angelscript
int64 GetFrameCount()
```
Returns the value of GFrameCounter, a running count of the number of frames that have occurred.

### GetGameBundleId
```angelscript
FString GetGameBundleId()
```
Retrieves the game's platform-specific bundle identifier or package name of the game

@return The game's bundle identifier or package name.

### GetGameName
```angelscript
FString GetGameName()
```
Get the name of the current game

### GetGamepadButtonGlyph
```angelscript
UTexture2D GetGamepadButtonGlyph(FString ButtonKey, int ControllerIndex)
```
Returns glyph assigned to a gamepad button (or a null ptr if not assigned) (iOS and tvOS only)

### GetGamepadControllerName
```angelscript
FString GetGamepadControllerName(int ControllerId)
```
Returns name of controller if assigned to a gamepad (or None if not assigned) (Android and iOS only)

### GetGameTimeInSeconds
```angelscript
float GetGameTimeInSeconds()
```
Get the current game time, in seconds. This stops when the game is paused and is affected by slomo.

@param WorldContextObject    World context

### GetLocalCurrencyCode
```angelscript
FString GetLocalCurrencyCode()
```
Returns the currency code associated with the device's locale
@return the currency code associated with the device's locale

### GetLocalCurrencySymbol
```angelscript
FString GetLocalCurrencySymbol()
```
Returns the currency symbol associated with the device's locale
@return the currency symbol associated with the device's locale

### GetMinYResolutionFor3DView
```angelscript
int GetMinYResolutionFor3DView()
```
Gets the smallest Y resolution we want to support in the 3D view, clamped within reasons
@return value in pixels

### GetMinYResolutionForUI
```angelscript
int GetMinYResolutionForUI()
```
Gets the smallest Y resolution we want to support in the UI, clamped within reasons
@return value in pixels

### GetObjectFromPrimaryAssetId
```angelscript
UObject GetObjectFromPrimaryAssetId(FPrimaryAssetId PrimaryAssetId)
```
Returns the Object associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

### GetObjectName
```angelscript
FString GetObjectName(const UObject Object)
```
Returns the actual object name.

### GetOuterObject
```angelscript
UObject GetOuterObject(const UObject Object)
```
Returns the outer object of an object.

### GetPathName
```angelscript
FString GetPathName(const UObject Object)
```
Returns the full path to the specified object as a string

### GetPlatformTime_Seconds
```angelscript
float GetPlatformTime_Seconds()
```
Returns the current platform time in seconds. Not coupled to any gameplay or other containerization logic - this
function is useful for timing execution time or timestamping data. Marked as callable rather than pure because
implicit evaluation may be confusing, both for blueprint authors and blueprint readers. For implicit execution
simply wrap it in a blueprint pure function.

### GetPlatformUserDir
```angelscript
FString GetPlatformUserDir()
```
Get the current user dir from the OS

### GetPlatformUserName
```angelscript
FString GetPlatformUserName()
```
Get the current user name from the OS

### GetPreferredLanguages
```angelscript
TArray<FString> GetPreferredLanguages()
```
Returns an array of the user's preferred languages in order of preference
@return An array of language IDs ordered from most preferred to least

### GetPrimaryAssetIdFromClass
```angelscript
FPrimaryAssetId GetPrimaryAssetIdFromClass(TSubclassOf<UObject> Class)
```
Returns the Primary Asset Id for a Class, this can return an invalid one if not registered

### GetPrimaryAssetIdFromObject
```angelscript
FPrimaryAssetId GetPrimaryAssetIdFromObject(UObject Object)
```
Returns the Primary Asset Id for an Object, this can return an invalid one if not registered

### GetPrimaryAssetIdFromSoftClassReference
```angelscript
FPrimaryAssetId GetPrimaryAssetIdFromSoftClassReference(TSoftClassPtr<UObject> SoftClassReference)
```
Returns the Primary Asset Id for a Soft Class Reference, this can return an invalid one if not registered

### GetPrimaryAssetIdFromSoftObjectReference
```angelscript
FPrimaryAssetId GetPrimaryAssetIdFromSoftObjectReference(TSoftObjectPtr<UObject> SoftObjectReference)
```
Returns the Primary Asset Id for a Soft Object Reference, this can return an invalid one if not registered

### GetPrimaryAssetIdList
```angelscript
void GetPrimaryAssetIdList(FPrimaryAssetType PrimaryAssetType, TArray<FPrimaryAssetId>& OutPrimaryAssetIdList)
```
Returns list of PrimaryAssetIds for a PrimaryAssetType

### GetPrimaryAssetsWithBundleState
```angelscript
void GetPrimaryAssetsWithBundleState(TArray<FName> RequiredBundles, TArray<FName> ExcludedBundles, TArray<FPrimaryAssetType> ValidTypes, bool bForceCurrentState, TArray<FPrimaryAssetId>& OutPrimaryAssetIdList)
```
Returns the list of assets that are in a given bundle state. Required Bundles must be specified
If ExcludedBundles is not empty, it will not return any assets in those bundle states
If ValidTypes is not empty, it will only return assets of those types
If ForceCurrentState is true it will use the current state even if a load is in process

### GetProjectContentDirectory
```angelscript
FString GetProjectContentDirectory()
```
Get the content directory of the current project

### GetProjectDirectory
```angelscript
FString GetProjectDirectory()
```
Get the directory of the current project

### GetProjectSavedDirectory
```angelscript
FString GetProjectSavedDirectory()
```
Get the saved directory of the current project

### GetRenderingDetailMode
```angelscript
int GetRenderingDetailMode()
```
Get the clamped state of r.DetailMode, see console variable help (allows for scalability, cannot be used in construction scripts)
0: low, show objects with DetailMode low
1: medium, show objects with DetailMode medium or below
2: high, show objects with DetailMode high or below
3: epic, show all objects

### GetRenderingMaterialQualityLevel
```angelscript
int GetRenderingMaterialQualityLevel()
```
Get the clamped state of r.MaterialQualityLevel, see console variable help (allows for scalability, cannot be used in construction scripts)
0: low
1: high
2: medium

### GetSoftClassPath
```angelscript
FSoftClassPath GetSoftClassPath(const UClass Class)
```
Returns the full path to the specified class as a Soft Class Path (that can be used as a Soft Object Path)

### GetSoftClassReferenceFromPrimaryAssetId
```angelscript
TSoftClassPtr<UObject> GetSoftClassReferenceFromPrimaryAssetId(FPrimaryAssetId PrimaryAssetId)
```
Returns the Blueprint Class Id associated with a Primary Asset Id, this works even if the asset is not loaded

### GetSoftClassTopLevelAssetPath
```angelscript
FTopLevelAssetPath GetSoftClassTopLevelAssetPath(TSoftClassPtr<UObject> SoftClassReference)
```
Converts a Soft Class Reference to a Top Level Asset Path used by asset utilities

### GetSoftObjectPath
```angelscript
FSoftObjectPath GetSoftObjectPath(const UObject Object)
```
Returns the full path to the specified object as a Soft Object Path

### GetSoftObjectReferenceFromPrimaryAssetId
```angelscript
TSoftObjectPtr<UObject> GetSoftObjectReferenceFromPrimaryAssetId(FPrimaryAssetId PrimaryAssetId)
```
Returns the Object Id associated with a Primary Asset Id, this works even if the asset is not loaded

### GetStructTopLevelAssetPath
```angelscript
FTopLevelAssetPath GetStructTopLevelAssetPath(const UScriptStruct Struct)
```
Returns the full path to the specified struct as a Top Level Asset Path used by asset utilities

### GetSupportedFullscreenResolutions
```angelscript
bool GetSupportedFullscreenResolutions(TArray<FIntPoint>& Resolutions)
```
Gets the list of support fullscreen resolutions.
@return true if successfully queried the device for available resolutions.

### GetSystemPath
```angelscript
FString GetSystemPath(const UObject Object)
```
Returns the full file system path to a UObject
If given a non-asset UObject, it will return an empty string

### GetVolumeButtonsHandledBySystem
```angelscript
bool GetVolumeButtonsHandledBySystem()
```
Returns true if system default handling of volume up and volume down buttons enabled (Android only)

### HasMultipleLocalPlayers
```angelscript
bool HasMultipleLocalPlayers()
```
Returns whether there are currently multiple local players in the given world

### HideAdBanner
```angelscript
void HideAdBanner()
```
Hides the ad banner (iAd on iOS, or AdMob on Android). Will force close the ad if it's open
(iOS and Android only)

### IsControllerAssignedToGamepad
```angelscript
bool IsControllerAssignedToGamepad(int ControllerId)
```
Returns true if controller id assigned to a gamepad (Android and iOS only)

### IsDedicatedServer
```angelscript
bool IsDedicatedServer()
```
Returns whether this is running on a dedicated server

### IsInterstitialAdAvailable
```angelscript
bool IsInterstitialAdAvailable()
```
Returns true if the requested interstitial ad is loaded and ready
(Android only)

### IsInterstitialAdRequested
```angelscript
bool IsInterstitialAdRequested()
```
Returns true if the requested interstitial ad has been successfully requested (false if load request fails)
(Android only)

### IsLoggedIn
```angelscript
bool IsLoggedIn(const APlayerController SpecificPlayer)
```
Returns whether the player is logged in to the currently active online subsystem.

@param Player Specific player's login status to get. May not be supported on all platforms. If null, defaults to the player with ControllerId 0.

### IsPackagedForDistribution
```angelscript
bool IsPackagedForDistribution()
```
Returns whether this is a build that is packaged for distribution

### IsScreensaverEnabled
```angelscript
bool IsScreensaverEnabled()
```
Returns true if screen saver is enabled.

### IsServer
```angelscript
bool IsServer()
```
Returns whether the world this object is in is the host or not

### IsStandalone
```angelscript
bool IsStandalone()
```
Returns whether this game instance is stand alone (no networking).

### IsUnattended
```angelscript
bool IsUnattended()
```
Returns true if running unattended (-unattended is on the command line)

@return      Unattended state

### IsValid
```angelscript
bool IsValid(const UObject Object)
```
Return true if the object is usable : non-null and not pending kill

### IsValidClass
```angelscript
bool IsValidClass(UClass Class)
```
Return true if the class is usable : non-null and not pending kill

### IsValidPrimaryAssetId
```angelscript
bool IsValidPrimaryAssetId(FPrimaryAssetId PrimaryAssetId)
```
Returns true if the Primary Asset Id is valid

### IsValidPrimaryAssetType
```angelscript
bool IsValidPrimaryAssetType(FPrimaryAssetType PrimaryAssetType)
```
Returns list of Primary Asset Ids for a PrimaryAssetType

### IsValidSoftClassReference
```angelscript
bool IsValidSoftClassReference(TSoftClassPtr<UObject> SoftClassReference)
```
Returns true if the Soft Class Reference is not null

### IsValidSoftObjectReference
```angelscript
bool IsValidSoftObjectReference(TSoftObjectPtr<UObject> SoftObjectReference)
```
Returns true if the Soft Object Reference is not null

### ClearAndInvalidateTimerHandle
```angelscript
void ClearAndInvalidateTimerHandle(FTimerHandle& Handle)
```
Clears a set timer.
@param Handle                The handle of the timer to clear.

### ClearTimer
```angelscript
void ClearTimer(UObject Object, FString FunctionName)
```
Clears a set timer.
@param Object                Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName  Delegate function name. Can be a K2 function or a Custom Event.

### GetTimerElapsedTime
```angelscript
float32 GetTimerElapsedTime(UObject Object, FString FunctionName)
```
Returns elapsed time for the given delegate (time since current countdown iteration began).
@param Object                Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName  Delegate function name. Can be a K2 function or a Custom Event.
@return                              How long has elapsed since the current iteration of the timer began.

### GetTimerElapsedTimeHandle
```angelscript
float32 GetTimerElapsedTimeHandle(FTimerHandle Handle)
```
Returns elapsed time for the given handle (time since current countdown iteration began).
@param Handle                The handle of the timer to get the elapsed time of.
@return                              How long has elapsed since the current iteration of the timer began.

### GetTimerRemainingTime
```angelscript
float32 GetTimerRemainingTime(UObject Object, FString FunctionName)
```
Returns time until the timer will next execute its delegate.
@param Object                Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName  Delegate function name. Can be a K2 function or a Custom Event.
@return                              How long is remaining in the current iteration of the timer.

### GetTimerRemainingTimeHandle
```angelscript
float32 GetTimerRemainingTimeHandle(FTimerHandle Handle)
```
Returns time until the timer will next execute its handle.
@param Handle                The handle of the timer to time remaining of.
@return                              How long is remaining in the current iteration of the timer.

### InvalidateTimerHandle
```angelscript
FTimerHandle InvalidateTimerHandle(FTimerHandle& Handle)
```
Invalidate the supplied TimerHandle and return it.
@param Handle                The handle of the timer to invalidate.
@return                              Return the invalidated timer handle for convenience.

### IsTimerActive
```angelscript
bool IsTimerActive(UObject Object, FString FunctionName)
```
Returns true if a timer exists and is active for the given delegate, false otherwise.
@param Object                Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName  Delegate function name. Can be a K2 function or a Custom Event.
@return                              True if the timer exists and is active.

### IsTimerActiveHandle
```angelscript
bool IsTimerActiveHandle(FTimerHandle Handle)
```
Returns true if a timer exists and is active for the given handle, false otherwise.
@param Handle                The handle of the timer to check whether it is active.
@return                              True if the timer exists and is active.

### IsTimerPaused
```angelscript
bool IsTimerPaused(UObject Object, FString FunctionName)
```
Returns true if a timer exists and is paused for the given delegate, false otherwise.
@param Object         Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName   Delegate function name. Can be a K2 function or a Custom Event.
@return                               True if the timer exists and is paused.

### IsTimerPausedHandle
```angelscript
bool IsTimerPausedHandle(FTimerHandle Handle)
```
Returns true if a timer exists and is paused for the given handle, false otherwise.
@param Handle                The handle of the timer to check whether it is paused.
@return                              True if the timer exists and is paused.

### IsValidTimerHandle
```angelscript
bool IsValidTimerHandle(FTimerHandle Handle)
```
Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.
@param Handle                The handle of the timer to check validity of.
@return                              Whether the timer handle is valid.

### PauseTimer
```angelscript
void PauseTimer(UObject Object, FString FunctionName)
```
Pauses a set timer at its current elapsed time.
@param Object                Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName  Delegate function name. Can be a K2 function or a Custom Event.

### PauseTimerHandle
```angelscript
void PauseTimerHandle(FTimerHandle Handle)
```
Pauses a set timer at its current elapsed time.
@param Handle                The handle of the timer to pause.

### SetTimer
```angelscript
FTimerHandle SetTimer(UObject Object, FName FunctionName, float32 Time, bool bLooping, bool bMaxOncePerFrame, float32 InitialStartDelay, float32 InitialStartDelayVariance)
```
Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.
@param Object                                        Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName                          Delegate function name. Can be a K2 function or a Custom Event.
@param Time                                          How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set.
@param bLooping                                      True to keep executing the delegate every Time seconds, false to execute delegate only once.
@param bMaxOncePerFrame                      For looping timers, whether to execute only once when the timer would otherwise expires multiple times in the current frame.
@param InitialStartDelay                     Initial delay passed to the timer manager to allow some variance in when the timer starts, in seconds.
@param InitialStartDelayVariance     Use this to add some variance to when the timer starts in lieu of doing a random range on the InitialStartDelay input, in seconds.
@return                                                      The timer handle to pass to other timer functions to manipulate this timer.

### SetTimerDelegate
```angelscript
FTimerHandle SetTimerDelegate(FTimerDynamicDelegate Delegate, float32 Time, bool bLooping, bool bMaxOncePerFrame, float32 InitialStartDelay, float32 InitialStartDelayVariance)
```
Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.
@param Event                                         Event. Can be a K2 function or a Custom Event.
@param Time                                          How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set.
@param bLooping                                      True to keep executing the delegate every Time seconds, false to execute delegate only once.
@param bMaxOncePerFrame                      For looping timers, whether to execute only once when the timer would otherwise expires multiple times in the current frame.
@param InitialStartDelay                     Initial delay passed to the timer manager, in seconds.
@param InitialStartDelayVariance     Use this to add some variance to when the timer starts in lieu of doing a random range on the InitialStartDelay input, in seconds.
@return                                                      The timer handle to pass to other timer functions to manipulate this timer.

### SetTimerForNextTick
```angelscript
FTimerHandle SetTimerForNextTick(UObject Object, FString FunctionName)
```
Set a timer to execute a delegate on the next tick.
@param Object                                        Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName                          Delegate function name. Can be a K2 function or a Custom Event.
@return                                                      The timer handle to pass to other timer functions to manipulate this timer.

### SetTimerForNextTickDelegate
```angelscript
FTimerHandle SetTimerForNextTickDelegate(FTimerDynamicDelegate Delegate)
```
Set a timer to execute a delegate next tick.
@param Event                                         Event. Can be a K2 function or a Custom Event.
@return                                                      The timer handle to pass to other timer functions to manipulate this timer.

### TimerExists
```angelscript
bool TimerExists(UObject Object, FString FunctionName)
```
Returns true is a timer for the given delegate exists, false otherwise.
@param Object         Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName   Delegate function name. Can be a K2 function or a Custom Event.
@return                               True if the timer exists.

### TimerExistsHandle
```angelscript
bool TimerExistsHandle(FTimerHandle Handle)
```
Returns true is a timer for the given handle exists, false otherwise.
@param Handle                The handle to check whether it exists.
@return                              True if the timer exists.

### UnPauseTimer
```angelscript
void UnPauseTimer(UObject Object, FString FunctionName)
```
Resumes a paused timer from its current elapsed time.
@param Object                Object that implements the delegate function. Defaults to self (this blueprint)
@param FunctionName  Delegate function name. Can be a K2 function or a Custom Event.

### UnPauseTimerHandle
```angelscript
void UnPauseTimerHandle(FTimerHandle Handle)
```
Resumes a paused timer from its current elapsed time.
@param Handle                The handle of the timer to unpause.

### LaunchURL
```angelscript
void LaunchURL(FString URL)
```
Opens the specified URL in the platform's web browser of choice

### LineTraceMulti
```angelscript
bool LineTraceMulti(FVector Start, FVector End, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Does a collision trace along the given line and returns all hits encountered up to and including the first blocking hit.
This trace finds the objects that RESPOND to the given TraceChannel

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param TraceChannel  The channel to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a blocking hit, false otherwise.

### LineTraceMultiByProfile
```angelscript
bool LineTraceMultiByProfile(FVector Start, FVector End, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Trace a ray against the world using a specific profile and return overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

@param WorldContext   World context
@param Start                  Start of line segment.
@param End                    End of line segment.
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit         Properties of the trace hit.
@return                               True if there was a blocking hit, false otherwise.

### LineTraceMultiForObjects
```angelscript
bool LineTraceMultiForObjects(FVector Start, FVector End, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Does a collision trace along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param ObjectTypes   Array of Object Types to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### LineTraceSingle
```angelscript
bool LineTraceSingle(FVector Start, FVector End, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Does a collision trace along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param TraceChannel
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### LineTraceSingleByProfile
```angelscript
bool LineTraceSingleByProfile(FVector Start, FVector End, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Trace a ray against the world using a specific profile and return the first blocking hit

@param WorldContext   World context
@param Start                  Start of line segment.
@param End                    End of line segment.
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit                 Properties of the trace hit.
@return                               True if there was a hit, false otherwise.

### LineTraceSingleForObjects
```angelscript
bool LineTraceSingleForObjects(FVector Start, FVector End, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Does a collision trace along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param ObjectTypes   Array of Object Types to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### LoadAsset_Blocking
```angelscript
UObject LoadAsset_Blocking(TSoftObjectPtr<UObject> Asset)
```
Resolves or loads a Soft Object Reference immediately, this will cause hitches and Async Load Asset should be used if possible

### LoadClassAsset_Blocking
```angelscript
UClass LoadClassAsset_Blocking(TSoftClassPtr<UObject> AssetClass)
```
Resolves or loads a Soft Class Reference immediately, this will cause hitches and Async Load Class Asset should be used if possible

### LoadInterstitialAd
```angelscript
void LoadInterstitialAd(int AdIdIndex)
```
Will load a fullscreen interstitial AdMob ad. Call this before using ShowInterstitialAd
(Android only)

@param AdIdIndex The index of the ID to select for the ad to show

### LogString
```angelscript
void LogString(FString InString, bool bPrintToLog)
```
Prints a string to the log
If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

@param       InString                The string to log out
@param       bPrintToLog             Whether or not to print the output to the log

### MakeARFilter
```angelscript
FARFilter MakeARFilter(TArray<FName> PackageNames, TArray<FName> PackagePaths, TArray<FSoftObjectPath> SoftObjectPaths, TArray<FTopLevelAssetPath> ClassPaths, TSet<FTopLevelAssetPath> RecursiveClassPathsExclusionSet, TArray<FName> ClassNames, TSet<FName> RecursiveClassesExclusionSet, bool bRecursivePaths, bool bRecursiveClasses, bool bIncludeOnlyOnDiskAssets)
```
Builds an ARFilter struct. You should be using ClassPaths and RecursiveClassPathsExclusionSet, ClassNames and RecursiveClassesExclusionSet are deprecated.

@param ClassNames [DEPRECATED] - Class names are now represented by path names. If non-empty, this input will result in a runtime warning. Please use the ClassPaths input instead.
@param RecursiveClassesExclusionSet [DEPRECATED] - Class names are now represented by path names. If non-empty, this input will result in a runtime warning. Please use the RecursiveClassPathsExclusionSet input instead.

### MakeLiteralBool
```angelscript
bool MakeLiteralBool(bool Value)
```
Creates a literal bool
@param       Value   value to set the bool to
@return      The literal bool

### MakeLiteralByte
```angelscript
uint8 MakeLiteralByte(uint8 Value)
```
Creates a literal byte
@param       Value   value to set the byte to
@return      The literal byte

### MakeLiteralDouble
```angelscript
float MakeLiteralDouble(float Value)
```
Creates a literal float (double-precision)
@param       Value   value to set the float (double-precision) to
@return      The literal float (double-precision)

### MakeLiteralInt
```angelscript
int MakeLiteralInt(int Value)
```
Creates a literal integer
@param       Value   value to set the integer to
@return      The literal integer

### MakeLiteralInt64
```angelscript
int64 MakeLiteralInt64(int64 Value)
```
Creates a literal 64-bit integer
@param       Value   value to set the 64-bit integer to
@return      The literal 64-bit integer

### MakeLiteralName
```angelscript
FName MakeLiteralName(FName Value)
```
Creates a literal name
@param       Value   value to set the name to
@return      The literal name

### MakeLiteralString
```angelscript
FString MakeLiteralString(FString Value)
```
Creates a literal string
@param       Value   value to set the string to
@return      The literal string

### MakeLiteralText
```angelscript
FText MakeLiteralText(FText Value)
```
Creates a literal FText
@param       Value   value to set the FText to
@return      The literal FText

### MakeSoftClassPath
```angelscript
FSoftClassPath MakeSoftClassPath(FString PathString)
```
Builds a Soft Class Path struct from a string that contains a full /folder/packagename.class path.
For blueprint classes, this needs to point to the actual class (often with _C) and not the blueprint editor asset

### MakeSoftObjectPath
```angelscript
FSoftObjectPath MakeSoftObjectPath(FString PathString)
```
Builds a Soft Object Path struct from a string that contains a full /folder/packagename.object path

### MakeTopLevelAssetPath
```angelscript
FTopLevelAssetPath MakeTopLevelAssetPath(FString PackageName, FString AssetName)
```
Builds a TopLevelAssetPath struct from single Path string or from PackageName and AssetName string.

### MoveComponentTo
```angelscript
void MoveComponentTo(USceneComponent Component, FVector TargetRelativeLocation, FRotator TargetRelativeRotation, bool bEaseOut, bool bEaseIn, float32 OverTime, bool bForceShortestRotationPath, EMoveComponentAction MoveAction, FLatentActionInfo LatentInfo)
```
* Interpolate a component to the specified relative location and rotation over the course of OverTime seconds.
* @param Component                                             Component to interpolate
* @param TargetRelativeLocation                Relative target location
* @param TargetRelativeRotation                Relative target rotation
* @param bEaseOut                                              if true we will ease out (ie end slowly) during interpolation
* @param bEaseIn                                               if true we will ease in (ie start slowly) during interpolation
* @param OverTime                                              duration of interpolation
* @param bForceShortestRotationPath    if true we will always use the shortest path for rotation
* @param MoveAction                                    required movement behavior @see EMoveComponentAction
* @param LatentInfo                                    The latent action

### NormalizeFilename
```angelscript
FString NormalizeFilename(FString InFilename)
```
Convert all / and \ to TEXT("/")

### NotEqual_PrimaryAssetId
```angelscript
bool NotEqual_PrimaryAssetId(FPrimaryAssetId A, FPrimaryAssetId B)
```
Returns true if the values are not equal (A != B)

### NotEqual_PrimaryAssetType
```angelscript
bool NotEqual_PrimaryAssetType(FPrimaryAssetType A, FPrimaryAssetType B)
```
Returns true if the values are not equal (A != B)

### NotEqual_SoftClassReference
```angelscript
bool NotEqual_SoftClassReference(TSoftClassPtr<UObject> A, TSoftClassPtr<UObject> B)
```
Returns true if the values are not equal (A != B)

### NotEqual_SoftObjectReference
```angelscript
bool NotEqual_SoftObjectReference(TSoftObjectPtr<UObject> A, TSoftObjectPtr<UObject> B)
```
Returns true if the values are not equal (A != B)

### ParseCommandLine
```angelscript
void ParseCommandLine(FString InCmdLine, TArray<FString>& OutTokens, TArray<FString>& OutSwitches, TMap<FString,FString>& OutParams)
```
* Parses the given string into loose tokens, switches (arguments that begin with - or /) and parameters (-mySwitch=myVar)
*
* @param        InCmdLine                       The the string to parse (ie '-foo -bar=/game/baz testtoken' )
* @param        OutTokens[out]          Filled with all loose tokens found in the string (ie: testToken in above example)
* @param        OutSwitches[out]        Filled with all switches found in the string (ie -foo)
* @param        OutParams[out]          Filled with all switches found in the string with the format key = value (ie: -bar, /game/baz)

### ParseParam
```angelscript
bool ParseParam(FString InString, FString InParam)
```
Returns true if the string has -param in it (do not specify the leading -)

### ParseParamValue
```angelscript
bool ParseParamValue(FString InString, FString InParam, FString& OutValue)
```
Returns 'value' if -option=value is in the string

### PrintString
```angelscript
void PrintString(FString InString, bool bPrintToScreen, bool bPrintToLog, FLinearColor TextColor, float32 Duration, FName Key)
```
Prints a string to the log, and optionally, to the screen
If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

@param       InString                The string to log out
@param       bPrintToScreen  Whether or not to print the output to the screen
@param       bPrintToLog             Whether or not to print the output to the log
@param       bPrintToConsole Whether or not to print the output to the console
@param       TextColor               The color of the text to display
@param       Duration                The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config.
@param       Key                             If a non-empty key is provided, the message will replace any existing on-screen messages with the same key.

### PrintText
```angelscript
void PrintText(FText InText, bool bPrintToScreen, bool bPrintToLog, FLinearColor TextColor, float32 Duration, FName Key)
```
Prints text to the log, and optionally, to the screen
If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

@param       InText                  The text to log out
@param       bPrintToScreen  Whether or not to print the output to the screen
@param       bPrintToLog             Whether or not to print the output to the log
@param       bPrintToConsole Whether or not to print the output to the console
@param       TextColor               The color of the text to display
@param       Duration                The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config.
@param       Key                             If a non-empty key is provided, the message will replace any existing on-screen messages with the same key.

### QuitEditor
```angelscript
void QuitEditor()
```
Exit the editor

### QuitGame
```angelscript
void QuitGame(APlayerController SpecificPlayer, EQuitPreference QuitPreference, bool bIgnorePlatformRestrictions)
```
Exit the current game
@param       SpecificPlayer  The specific player to quit the game. If not specified, player 0 will quit.
@param       QuitPreference  Form of quitting.
@param       bIgnorePlatformRestrictions     Ignores and best-practices based on platform (e.g on some consoles, games should never quit). Non-shipping only

### RegisterForRemoteNotifications
```angelscript
void RegisterForRemoteNotifications()
```
Requests permission to send remote notifications to the user's device.
(Android and iOS only)

### ResetEditorProperty
```angelscript
bool ResetEditorProperty(UObject Object, FName PropertyName, EPropertyAccessChangeNotifyMode ChangeNotifyMode)
```
Attempts to reset the value of a named property on the given object so that it matches the value of the archetype.

@param Object The object you want to reset a property value on.
@param PropertyName The name of the object property to reset the value of.
@param ChangeNotifyMode When to emit property change notifications.

@return Whether the property value was found and correctly reset.

### ResetGamepadAssignments
```angelscript
void ResetGamepadAssignments()
```
Resets the gamepad to player controller id assignments (Android and iOS only)

### ResetGamepadAssignmentToController
```angelscript
void ResetGamepadAssignmentToController(int ControllerId)
```
* Resets the gamepad assignment to player controller id (Android and iOS only)

### RetriggerableDelay
```angelscript
void RetriggerableDelay(float32 Duration, FLatentActionInfo LatentInfo)
```
Perform a latent action with a retriggerable delay (specified in seconds).  Calling again while it is counting down will reset the countdown to Duration.

@param WorldContext  World context.
@param Duration              length of delay (in seconds).
@param LatentInfo    The latent action.

### SetGamepadsBlockDeviceFeedback
```angelscript
void SetGamepadsBlockDeviceFeedback(bool bBlock)
```
Sets whether attached gamepads will block feedback from the device itself (Mobile only).

### SetSuppressViewportTransitionMessage
```angelscript
void SetSuppressViewportTransitionMessage(bool bState)
```
Sets the state of the transition message rendered by the viewport. (The blue text displayed when the game is paused and so forth.)

@param WorldContextObject    World context
@param State                                 set true to suppress transition message

### SetUserActivity
```angelscript
void SetUserActivity(FUserActivity UserActivity)
```
Tells the engine what the user is doing for debug, analytics, etc.

### SetVolumeButtonsHandledBySystem
```angelscript
void SetVolumeButtonsHandledBySystem(bool bEnabled)
```
Allows or inhibits system default handling of volume up and volume down buttons (Android only)
@param       bEnabled                                If true, allow Android to handle volume up and down events

### SetWindowTitle
```angelscript
void SetWindowTitle(FText Title)
```
Sets the game window title

### ShowAdBanner
```angelscript
void ShowAdBanner(int AdIdIndex, bool bShowOnBottomOfScreen)
```
Will show an ad banner (iAd on iOS, or AdMob on Android) on the top or bottom of screen, on top of the GL view (doesn't resize the view)
(iOS and Android only)

@param AdIdIndex The index of the ID to select for the ad to show
@param bShowOnBottomOfScreen If true, the iAd will be shown at the bottom of the screen, top otherwise

### ShowInterstitialAd
```angelscript
void ShowInterstitialAd()
```
Shows the loaded interstitial ad (loaded with LoadInterstitialAd)
(Android only)

### ShowPlatformSpecificAchievementsScreen
```angelscript
void ShowPlatformSpecificAchievementsScreen(const APlayerController SpecificPlayer)
```
Displays the built-in achievements GUI (iOS and Android only; this function may be renamed or moved in a future release)

@param SpecificPlayer Specific player's achievements to show. May not be supported on all platforms. If null, defaults to the player with ControllerId 0

### ShowPlatformSpecificLeaderboardScreen
```angelscript
void ShowPlatformSpecificLeaderboardScreen(FString CategoryName)
```
Displays the built-in leaderboard GUI (iOS and Android only; this function may be renamed or moved in a future release)

### SnapshotObject
```angelscript
void SnapshotObject(UObject Object)
```
Notify the current transaction (if any) that this object is about to be modified and should be snapshot for intermediate update.
@note Internally this calls SnapshotTransactionBuffer on the given object.
@note Only available in the editor.

@param       Object          The object that is about to be modified.

### SphereOverlapActors
```angelscript
bool SphereOverlapActors(FVector SpherePos, float32 SphereRadius, TArray<EObjectTypeQuery> ObjectTypes, UClass ActorClassFilter, TArray<AActor> ActorsToIgnore, TArray<AActor>& OutActors)
```
Returns an array of actors that overlap the given sphere.
@param WorldContext  World context
@param SpherePos             Center of sphere.
@param SphereRadius  Size of sphere.
@param Filter                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors             Returned array of actors. Unsorted.
@return                              true if there was an overlap that passed the filters, false otherwise.

### SphereOverlapComponents
```angelscript
bool SphereOverlapComponents(FVector SpherePos, float32 SphereRadius, TArray<EObjectTypeQuery> ObjectTypes, UClass ComponentClassFilter, TArray<AActor> ActorsToIgnore, TArray<UPrimitiveComponent>& OutComponents)
```
Returns an array of components that overlap the given sphere.
@param WorldContext  World context
@param SpherePos             Center of sphere.
@param SphereRadius  Size of sphere.
@param Filter                Option to restrict results to only static or only dynamic.  For efficiency.
@param ClassFilter   If set, will only return results of this class or subclasses of it.
@param ActorsToIgnore                Ignore these actors in the list
@param OutActors             Returned array of actors. Unsorted.
@return                              true if there was an overlap that passed the filters, false otherwise.

### SphereTraceMulti
```angelscript
bool SphereTraceMulti(FVector Start, FVector End, float32 Radius, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a sphere along the given line and returns all hits encountered up to and including the first blocking hit.
This trace finds the objects that RESPOND to the given TraceChannel

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the sphere to sweep
@param TraceChannel
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHits               A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                              True if there was a blocking hit, false otherwise.

### SphereTraceMultiByProfile
```angelscript
bool SphereTraceMultiByProfile(FVector Start, FVector End, float32 Radius, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweep a sphere against the world and return all initial overlaps using a specific profile, then overlapping hits and then first blocking hit
Results are sorted, so a blocking hit (if found) will be the last element of the array
Only the single closest blocking result will be generated, no tests will be done after that

@param WorldContext   World context
@param Start                  Start of line segment.
@param End                    End of line segment.
@param Radius         Radius of the sphere to sweep
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHits                A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                               True if there was a blocking hit, false otherwise.

### SphereTraceMultiForObjects
```angelscript
bool SphereTraceMultiForObjects(FVector Start, FVector End, float32 Radius, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, TArray<FHitResult>& OutHits, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a sphere along the given line and returns all hits encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param WorldContext  World context
@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the sphere to sweep
@param ObjectTypes   Array of Object Types to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHits               A list of hits, sorted along the trace from start to finish.  The blocking hit will be the last hit, if there was one.
@return                              True if there was a hit, false otherwise.

### SphereTraceSingle
```angelscript
bool SphereTraceSingle(FVector Start, FVector End, float32 Radius, ETraceTypeQuery TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a sphere along the given line and returns the first blocking hit encountered.
This trace finds the objects that RESPONDS to the given TraceChannel

@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the sphere to sweep
@param TraceChannel
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### SphereTraceSingleByProfile
```angelscript
bool SphereTraceSingleByProfile(FVector Start, FVector End, float32 Radius, FName ProfileName, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweep a sphere against the world and return the first blocking hit using a specific profile

@param Start                  Start of line segment.
@param End                    End of line segment.
@param Radius                 Radius of the sphere to sweep
@param ProfileName    The 'profile' used to determine which components to hit
@param bTraceComplex  True to test against complex collision, false to test against simplified collision.
@param OutHit                 Properties of the trace hit.
@return                               True if there was a hit, false otherwise.

### SphereTraceSingleForObjects
```angelscript
bool SphereTraceSingleForObjects(FVector Start, FVector End, float32 Radius, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, FHitResult& OutHit, bool bIgnoreSelf, FLinearColor TraceColor, FLinearColor TraceHitColor, float32 DrawTime)
```
Sweeps a sphere along the given line and returns the first hit encountered.
This only finds objects that are of a type specified by ObjectTypes.

@param Start                 Start of line segment.
@param End                   End of line segment.
@param Radius                Radius of the sphere to sweep
@param ObjectTypes   Array of Object Types to trace
@param bTraceComplex True to test against complex collision, false to test against simplified collision.
@param OutHit                Properties of the trace hit.
@return                              True if there was a hit, false otherwise.

### TransactObject
```angelscript
void TransactObject(UObject Object)
```
Notify the current transaction (if any) that this object is about to be modified and should be placed into the undo buffer.
@note Internally this calls Modify on the given object, so will also mark the owner package dirty.
@note Only available in the editor.

@param       Object          The object that is about to be modified.

### UnloadPrimaryAsset
```angelscript
void UnloadPrimaryAsset(FPrimaryAssetId PrimaryAssetId)
```
Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

### UnloadPrimaryAssetList
```angelscript
void UnloadPrimaryAssetList(TArray<FPrimaryAssetId> PrimaryAssetIdList)
```
Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

### UnregisterForRemoteNotifications
```angelscript
void UnregisterForRemoteNotifications()
```
Requests Requests unregistering from receiving remote notifications to the user's device.
(Android only)


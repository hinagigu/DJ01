# UActorComponent

**继承自**: `UObject`

ActorComponent is the base class for components that define reusable behavior that can be added to different types of Actors.
ActorComponents that have a transform are known as SceneComponents and those that can be rendered are PrimitiveComponents.

@see [ActorComponent](https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/Actors/Components/index.html#actorcomponents)
@see USceneComponent
@see UPrimitiveComponent

## 属性

### PrimaryComponentTick
- **类型**: `FActorComponentTickFunction`
- **描述**: Main tick function for the Component

### ComponentTags
- **类型**: `TArray<FName>`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the component

### AssetUserDataEditorOnly
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the component

### OnComponentActivated
- **类型**: `FActorComponentActivatedSignature`

### OnComponentDeactivated
- **类型**: `FActorComponentDeactivateSignature`

### bReplicateUsingRegisteredSubObjectList
- **类型**: `bool`

### bReplicates
- **类型**: `bool`

### bAutoActivate
- **类型**: `bool`

### bEditableWhenInherited
- **类型**: `bool`

### bCanEverAffectNavigation
- **类型**: `bool`

### bIsEditorOnly
- **类型**: `bool`

## 方法

### MarkRenderStateDirty
```angelscript
void MarkRenderStateDirty()
```

### HasBegunPlay
```angelscript
bool HasBegunPlay()
```

### SetbTickInEditor
```angelscript
void SetbTickInEditor(bool Value)
```

### SetbIsEditorOnly
```angelscript
void SetbIsEditorOnly(bool Value)
```

### GetComponentCreationMethod
```angelscript
EComponentCreationMethod GetComponentCreationMethod()
```

### SetIsVisualizationComponent
```angelscript
void SetIsVisualizationComponent(bool Value)
```

### IsVisualizationComponent
```angelscript
bool IsVisualizationComponent()
```

### Activate
```angelscript
void Activate(bool bReset)
```
Activates the SceneComponent, should be overridden by native child classes.
@param bReset - Whether the activation should happen even if ShouldActivate returns false.

### AddTickPrerequisiteActor
```angelscript
void AddTickPrerequisiteActor(AActor PrerequisiteActor)
```
Make this component tick after PrerequisiteActor

### AddTickPrerequisiteComponent
```angelscript
void AddTickPrerequisiteComponent(UActorComponent PrerequisiteComponent)
```
Make this component tick after PrerequisiteComponent.

### ComponentHasTag
```angelscript
bool ComponentHasTag(FName Tag)
```
See if this component contains the supplied tag

### Deactivate
```angelscript
void Deactivate()
```
Deactivates the SceneComponent.

### GetComponentTickInterval
```angelscript
float32 GetComponentTickInterval()
```
Returns the tick interval for this component's primary tick function, which is the frequency in seconds at which it will be executed

### GetOwner
```angelscript
AActor GetOwner()
```
Follow the Outer chain to get the  AActor  that 'Owns' this component

### IsActive
```angelscript
bool IsActive()
```
Returns whether the component is active or not
@return - The active state of the component.

### IsBeingDestroyed
```angelscript
bool IsBeingDestroyed()
```
Returns whether the component is in the process of being destroyed.

### IsComponentTickEnabled
```angelscript
bool IsComponentTickEnabled()
```
Returns whether this component has tick enabled or not

### DestroyComponent
```angelscript
void DestroyComponent(UObject Object)
```
Unregister and mark for pending kill a component.  This may not be used to destroy a component that is owned by an actor unless the owning actor is calling the function.

### AsyncPhysicsTick
```angelscript
void AsyncPhysicsTick(float DeltaSeconds, float SimSeconds)
```
Event called every async physics tick if bAsyncPhysicsTickEnabled is true

### BeginPlay
```angelscript
void BeginPlay()
```
Blueprint implementable event for when the component is beginning play, called before its owning actor's BeginPlay
or when the component is dynamically created if the Actor has already BegunPlay.

### EndPlay
```angelscript
void EndPlay(EEndPlayReason EndPlayReason)
```
Blueprint implementable event for when the component ends play, generally via destruction or its Actor's EndPlay.

### Tick
```angelscript
void Tick(float DeltaSeconds)
```
Event called every frame if tick is enabled

### RemoveTickPrerequisiteActor
```angelscript
void RemoveTickPrerequisiteActor(AActor PrerequisiteActor)
```
Remove tick dependency on PrerequisiteActor.

### RemoveTickPrerequisiteComponent
```angelscript
void RemoveTickPrerequisiteComponent(UActorComponent PrerequisiteComponent)
```
Remove tick dependency on PrerequisiteComponent.

### SetActive
```angelscript
void SetActive(bool bNewActive, bool bReset)
```
Sets whether the component is active or not
@param bNewActive - The new active state of the component
@param bReset - Whether the activation should happen even if ShouldActivate returns false.

### SetAutoActivate
```angelscript
void SetAutoActivate(bool bNewAutoActivate)
```
Sets whether the component should be auto activate or not. Only safe during construction scripts.
@param bNewAutoActivate - The new auto activate state of the component

### SetComponentTickEnabled
```angelscript
void SetComponentTickEnabled(bool bEnabled)
```
Set this component's tick functions to be enabled or disabled. Only has an effect if the function is registered

@param       bEnabled - Whether it should be enabled or not

### SetComponentTickInterval
```angelscript
void SetComponentTickInterval(float32 TickInterval)
```
Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect on next tick.
@param TickInterval   The duration between ticks for this component's primary tick function

### SetComponentTickIntervalAndCooldown
```angelscript
void SetComponentTickIntervalAndCooldown(float32 TickInterval)
```
Sets the tick interval for this component's primary tick function. Does not enable the tick interval. Takes effect imediately.
@param TickInterval   The duration between ticks for this component's primary tick function

### SetIsReplicated
```angelscript
void SetIsReplicated(bool ShouldReplicate)
```
Enable or disable replication. This is the equivalent of RemoteRole for actors (only a bool is required for components)

### SetTickableWhenPaused
```angelscript
void SetTickableWhenPaused(bool bTickableWhenPaused)
```
Sets whether this component can tick when paused.

### SetTickGroup
```angelscript
void SetTickGroup(ETickingGroup NewTickGroup)
```
Changes the ticking group for this component

### ToggleActive
```angelscript
void ToggleActive()
```
Toggles the active state of the component


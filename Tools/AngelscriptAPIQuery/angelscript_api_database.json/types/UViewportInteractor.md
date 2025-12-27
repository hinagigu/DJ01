# UViewportInteractor

**继承自**: `UObject`

Represents the interactor in the world

## 方法

### CanCarry
```angelscript
bool CanCarry()
```
Gets if the interactor can carry an object

### GetDraggingMode
```angelscript
EViewportInteractionDraggingMode GetDraggingMode()
```
Gets the current interactor data dragging mode

### GetHitResultGizmoFilterMode
```angelscript
EHitResultGizmoFilterMode GetHitResultGizmoFilterMode()
```
Gets current gizmo filter mode used for Interaction

### GetHoverLocation
```angelscript
FVector GetHoverLocation()
```
Gets the interactor laser hover location

### GetLaserPointer
```angelscript
bool GetLaserPointer(FVector& LaserPointerStart, FVector& LaserPointerEnd, bool bEvenIfBlocked, float32 LaserLengthOverride)
```
Gets the start and end point of the laser pointer for the specified hand

@param LasertPointerStart    (Out) The start location of the laser pointer in world space
@param LasertPointerEnd              (Out) The end location of the laser pointer in world space
@param bEvenIfBlocked                If true, returns a laser pointer even if the hand has UI in front of it (defaults to false)
@param LaserLengthOverride   If zero the default laser length (VREdMode::GetLaserLength) is used

@return      True if we have motion controller data for this hand and could return a valid result

### GetLastRoomSpaceTransform
```angelscript
FTransform GetLastRoomSpaceTransform()
```
Gets the last hand transform of the interactor, in the local tracking space

### GetLastTransform
```angelscript
FTransform GetLastTransform()
```
Gets the last world transform of this interactor

### GetOtherInteractor
```angelscript
UViewportInteractor GetOtherInteractor()
```
Gets the paired interactor assigned by the world interaction, can return null when there is no other interactor

### GetRoomSpaceTransform
```angelscript
FTransform GetRoomSpaceTransform()
```
Gets the hand transform of the interactor, in the local tracking space

### GetTransform
```angelscript
FTransform GetTransform()
```
Gets the world transform of this interactor

### GetTransformAndForwardVector
```angelscript
bool GetTransformAndForwardVector(FTransform& OutHandTransform, FVector& OutForwardVector)
```
Creates a hand transform and forward vector for a laser pointer for a given hand

@param OutHandTransform      The created hand transform
@param OutForwardVector      The forward vector of the hand

@return      True if we have motion controller data for this hand and could return a valid result

### GetWorldInteraction
```angelscript
UViewportWorldInteraction GetWorldInteraction()
```
Gets the world interaction

### HandleInputAxis_BP
```angelscript
void HandleInputAxis_BP(FViewportActionKeyInput Action, FKey Key, float Delta, float DeltaTime, bool& bOutWasHandled)
```
To be overridden. Called by HandleInputAxis before delegates and default input implementation

### HandleInputKey_BP
```angelscript
void HandleInputKey_BP(FViewportActionKeyInput Action, FKey Key, EInputEvent Event, bool& bOutWasHandled)
```
To be overridden. Called by HandleInputKey before delegates and default input implementation

### IsHoveringOverGizmo
```angelscript
bool IsHoveringOverGizmo()
```
If the interactor laser is currently hovering over a gizmo handle

### SetCanCarry
```angelscript
void SetCanCarry(bool bInCanCarry)
```
Sets if the interactor can carry an object

### SetDraggingMode
```angelscript
void SetDraggingMode(EViewportInteractionDraggingMode NewDraggingMode)
```
Sets the current dragging mode for this interactor

### SetHitResultGizmoFilterMode
```angelscript
void SetHitResultGizmoFilterMode(EHitResultGizmoFilterMode newFilter)
```
Sets the current gizmo filter mode used for Interaction

### Shutdown
```angelscript
void Shutdown()
```
Whenever the ViewportWorldInteraction is shut down, the interacts will shut down as well

### Tick
```angelscript
void Tick(float DeltaTime)
```
Update for this interactor called by the ViewportWorldInteraction


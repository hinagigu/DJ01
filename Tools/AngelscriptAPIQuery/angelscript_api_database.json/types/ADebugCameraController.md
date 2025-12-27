# ADebugCameraController

**继承自**: `APlayerController`

Camera controller that allows you to fly around a level mostly unrestricted by normal movement rules.

To turn it on, please press Alt+C or both (left and right) analogs on XBox pad,
or use the "ToggleDebugCamera" console command. Check the debug camera bindings
in DefaultPawn.cpp for the camera controls.

## 属性

### SpeedScale
- **类型**: `float32`

### InitialMaxSpeed
- **类型**: `float32`

### InitialAccel
- **类型**: `float32`

### InitialDecel
- **类型**: `float32`

## 方法

### GetSelectedActor
```angelscript
AActor GetSelectedActor()
```
Returns the currently selected actor, or null if it is invalid or not set

### OnActivate
```angelscript
void OnActivate(APlayerController OriginalPC)
```
Function called on activation of debug camera controller.
@param OriginalPC The active player controller before this debug camera controller was possessed by the player.

### OnActorSelected
```angelscript
void OnActorSelected(AActor NewSelectedActor, FVector SelectHitLocation, FVector SelectHitNormal, FHitResult Hit)
```
Called when an actor has been selected with the primary key (e.g. left mouse button).

The selection trace starts from the center of the debug camera's view.

@param SelectHitLocation The exact world-space location where the selection trace hit the New Selected Actor.
@param SelectHitNormal The world-space surface normal of the New Selected Actor at the hit location.

### OnDeactivate
```angelscript
void OnDeactivate(APlayerController RestoredPC)
```
Function called on deactivation of debug camera controller.
@param RestoredPC The Player Controller that the player input is being returned to.

### SetPawnMovementSpeedScale
```angelscript
void SetPawnMovementSpeedScale(float32 NewSpeedScale)
```
Sets the pawn movement speed scale.

### ToggleDisplay
```angelscript
void ToggleDisplay()
```
Toggles the display of debug info and input commands for the Debug Camera.


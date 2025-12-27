# UViewportWorldInteraction

**继承自**: `UEditorWorldExtension`

## 方法

### AddActorToExcludeFromHitTests
```angelscript
void AddActorToExcludeFromHitTests(AActor ActorToExcludeFromHitTests)
```
Adds an actor to the list of actors to never allow an interactor to hit in the scene.  No selection.  No hover.
There's no need to remove actors from this list.  They'll expire from it automatically when destroyed.

@param       ActorToExcludeFromHitTests      The actor that should be forever excluded from hit tests

### AddInteractor
```angelscript
void AddInteractor(UViewportInteractor Interactor)
```
Adds interactor to the worldinteraction

### GetHeadTransform
```angelscript
FTransform GetHeadTransform()
```
Gets the transform of the viewport / user's HMD in world space

### GetInteractors
```angelscript
TArray<UViewportInteractor> GetInteractors()
```
Gets all the interactors

### GetRoomSpaceHeadTransform
```angelscript
FTransform GetRoomSpaceHeadTransform()
```
Gets the transform of the viewport / user's HMD in room space

### GetRoomTransform
```angelscript
FTransform GetRoomTransform()
```
Gets the world space transform of the calibrated VR room origin.  When using a seated VR device, this will feel like the
      camera's world transform (before any HMD positional or rotation adjustments are applied.)

### GetTransformGizmoActor
```angelscript
ABaseTransformGizmo GetTransformGizmoActor()
```
Gets the transform gizmo actor, or returns null if we currently don't have one

### GetWorldScaleFactor
```angelscript
float32 GetWorldScaleFactor()
```
Gets the world scale factor, which can be multiplied by a scale vector to convert to room space

### RemoveInteractor
```angelscript
void RemoveInteractor(UViewportInteractor Interactor)
```
Removes interactor from the worldinteraction and removes the interactor from its paired interactor if any

### SetHeadTransform
```angelscript
void SetHeadTransform(FTransform NewHeadTransform)
```
Sets a new transform for the room so that the HMD is aligned to the new transform.
              The Head is kept level to the ground and only rotated on the yaw

### SetRoomTransformForNextFrame
```angelscript
void SetRoomTransformForNextFrame(FTransform NewRoomTransform)
```

### SetWorldToMetersScale
```angelscript
void SetWorldToMetersScale(float32 NewWorldToMetersScale, bool bCompensateRoomWorldScale)
```
Sets GNewWorldToMetersScale


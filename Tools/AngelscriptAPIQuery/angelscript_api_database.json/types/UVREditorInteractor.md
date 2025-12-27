# UVREditorInteractor

**继承自**: `UViewportInteractor`

VREditor default interactor

## 属性

### bIsUndoRedoSwipeEnabled
- **类型**: `bool`
- **描述**: Whether swiping left/right on touchpad/joystick triggers undo/redo

### HandMeshComponent
- **类型**: `UStaticMeshComponent`
- **描述**: Access to the current handmesh. Use ReplaceHandMeshComponent() to update the entire StaticMeshComponent.

## 方法

### GetControllerHandSide
```angelscript
FName GetControllerHandSide()
```
Sets the EControllerHand for this motioncontroller

### GetControllerSide
```angelscript
EControllerHand GetControllerSide()
```
Get the side of the controller

### GetControllerType
```angelscript
EControllerType GetControllerType()
```
Returns what controller type this is for asymmetric control schemes

### GetHMDDeviceType
```angelscript
FName GetHMDDeviceType()
```
@return Returns the type of HMD we're dealing with

### GetLaserEnd
```angelscript
FVector GetLaserEnd()
```

### GetLaserStart
```angelscript
FVector GetLaserStart()
```
Getters and setters

### GetLastTrackpadPosition
```angelscript
FVector2D GetLastTrackpadPosition()
```
Get the last position of the trackpad or analog stick

### GetMotionControllerComponent
```angelscript
UMotionControllerComponent GetMotionControllerComponent()
```
Get the motioncontroller component of this interactor

### GetSelectAndMoveTriggerValue
```angelscript
float32 GetSelectAndMoveTriggerValue()
```
Gets the trigger value

### GetSlideDelta
```angelscript
float32 GetSlideDelta()
```
Returns the slide delta for pushing and pulling objects. Needs to be implemented by derived classes (e.g. touchpad for vive controller or scrollweel for mouse )

### GetTeleportActor
```angelscript
AVREditorTeleporter GetTeleportActor()
```

### GetTrackpadPosition
```angelscript
FVector2D GetTrackpadPosition()
```
Get the current position of the trackpad or analog stick

### Init
```angelscript
void Init(UVREditorMode InVRMode)
```
Initialize default values

### IsClickingOnUI
```angelscript
bool IsClickingOnUI()
```
Gets if the interactor is clicking on any UI

### IsHoveringOverUI
```angelscript
bool IsHoveringOverUI()
```
Gets if this interactor is hovering over UI

### IsTouchingTrackpad
```angelscript
bool IsTouchingTrackpad()
```
Check if the touchpad is currently touched

### ReplaceHandMeshComponent
```angelscript
void ReplaceHandMeshComponent(UStaticMesh NewMesh, FVector MeshScale)
```
Replace the default VR controller mesh with a custom one.

### SetControllerHandSide
```angelscript
void SetControllerHandSide(FName InControllerHandSide)
```
Sets the EControllerHand for this motioncontroller

### SetControllerType
```angelscript
void SetControllerType(EControllerType InControllerType)
```
Set what controller type this is for asymmetric control schemes

### SetForceLaserColor
```angelscript
void SetForceLaserColor(FLinearColor InColor)
```
Next frame this will be used as color for the laser

### SetForceShowLaser
```angelscript
void SetForceShowLaser(bool bInForceShow)
```
Set if we want to force to show the laser

### SetupComponent
```angelscript
void SetupComponent(AActor OwningActor)
```
Sets up all components

### TryOverrideControllerType
```angelscript
bool TryOverrideControllerType(EControllerType InControllerType)
```
Temporary set what controller type this is for asymmetric control schemes.
You can't override the controller type when there's already an override.
Remove the temporary controller type with EControllerType::Unknown
@return true if the controller type was changed

### UpdateHandMeshRelativeTransform
```angelscript
void UpdateHandMeshRelativeTransform()
```


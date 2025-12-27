# AVREditorTeleporter

**继承自**: `AActor`

VR Editor teleport manager and the visual representation of the teleport

## 方法

### DoTeleport
```angelscript
void DoTeleport()
```
Do and finalize teleport.

### GetInteractorTryingTeleport
```angelscript
UViewportInteractor GetInteractorTryingTeleport()
```
Get the actor we're currently trying to teleport with.
Valid during aiming and teleporting.

### GetSlideDelta
```angelscript
float32 GetSlideDelta(UVREditorInteractor Interactor, bool Axis)
```
Get slide delta to push/pull or scale the teleporter

### GetVRMode
```angelscript
UVREditorMode GetVRMode()
```

### Init
```angelscript
void Init(UVREditorMode InMode)
```
Initializes the teleporter

### IsAiming
```angelscript
bool IsAiming()
```
Whether we are currently aiming to teleport.

### IsTeleporting
```angelscript
bool IsTeleporting()
```

### SetColor
```angelscript
void SetColor(FLinearColor Color)
```
Sets the color for the teleporter visuals

### SetVisibility
```angelscript
void SetVisibility(bool bVisible)
```
Hide or show the teleporter visuals

### Shutdown
```angelscript
void Shutdown()
```
Shuts down the teleporter

### StartAiming
```angelscript
void StartAiming(UViewportInteractor Interactor)
```
Functions we call to handle teleporting in navigation mode

### StartTeleport
```angelscript
void StartTeleport()
```
Start teleporting, does a ray trace with the hand passed and calculates the locations for lerp movement in Teleport

### StopAiming
```angelscript
void StopAiming()
```
Cancel teleport aiming mode without doing the teleport

### TeleportDone
```angelscript
void TeleportDone()
```
Called when teleport is done for cleanup


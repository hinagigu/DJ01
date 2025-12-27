# UCameraModifier

**继承自**: `UObject`

A CameraModifier is a base class for objects that may adjust the final camera properties after
being computed by the APlayerCameraManager (@see ModifyCamera). A CameraModifier
can be stateful, and is associated uniquely with a specific APlayerCameraManager.

## 属性

### Priority
- **类型**: `uint8`

### CameraOwner
- **类型**: `APlayerCameraManager`
- **描述**: Camera this object is associated with.

### AlphaInTime
- **类型**: `float32`

### AlphaOutTime
- **类型**: `float32`

### Alpha
- **类型**: `float32`
- **描述**: Current blend alpha.

### bDebug
- **类型**: `bool`

### bExclusive
- **类型**: `bool`

## 方法

### BlueprintModifyCamera
```angelscript
void BlueprintModifyCamera(float DeltaTime, FVector ViewLocation, FRotator ViewRotation, float FOV, FVector& NewViewLocation, FRotator& NewViewRotation, float32& NewFOV)
```
Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's transform.
Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.
@param       DeltaTime       Change in time since last update
@param       ViewLocation            The current camera location.
@param       ViewRotation            The current camera rotation.
@param       FOV                                     The current camera fov.
@param       NewViewLocation         (out) The modified camera location.
@param       NewViewRotation         (out) The modified camera rotation.
@param       NewFOV                          (out) The modified camera FOV.

### BlueprintModifyPostProcess
```angelscript
void BlueprintModifyPostProcess(float DeltaTime, float32& PostProcessBlendWeight, FPostProcessSettings& PostProcessSettings)
```
Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's postprocess effects.
Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.
@param       DeltaTime                               Change in time since last update
@param       PostProcessBlendWeight  (out) Blend weight applied to the entire postprocess structure.
@param       PostProcessSettings             (out) Post process structure defining what settings and values to override.

### DisableModifier
```angelscript
void DisableModifier(bool bImmediate)
```
Disables this modifier.
@param  bImmediate  - true to disable with no blend out, false (default) to allow blend out

### EnableModifier
```angelscript
void EnableModifier()
```
Enables this modifier.

### GetViewTarget
```angelscript
AActor GetViewTarget()
```
@return Returns the actor the camera is currently viewing.

### IsDisabled
```angelscript
bool IsDisabled()
```
@return Returns true if modifier is disabled, false otherwise.

### IsPendingDisable
```angelscript
bool IsPendingDisable()
```
@return Returns true if modifier is pending disable, false otherwise.


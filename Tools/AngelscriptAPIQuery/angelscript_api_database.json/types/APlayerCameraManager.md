# APlayerCameraManager

**继承自**: `AActor`

A PlayerCameraManager is responsible for managing the camera for a particular
player. It defines the final view properties used by other systems (e.g. the renderer),
meaning you can think of it as your virtual eyeball in the world. It can compute the
final camera properties directly, or it can arbitrate/blend between other objects or
actors that influence the camera (e.g. blending from one CameraActor to another).

The PlayerCameraManagers primary external responsibility is to reliably respond to
various Get*() functions, such as GetCameraViewPoint. Most everything else is
implementation detail and overrideable by user projects.

By default, a PlayerCameraManager maintains a "view target", which is the primary actor
the camera is associated with. It can also apply various "post" effects to the final
view state, such as camera animations, shakes, post-process effects or special
effects such as dirt on the lens.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Camera/

## 属性

### TransformComponent
- **类型**: `USceneComponent`

### DefaultFOV
- **类型**: `float32`

### DefaultOrthoWidth
- **类型**: `float32`

### DefaultAspectRatio
- **类型**: `float32`

### DefaultModifiers
- **类型**: `TArray<TSubclassOf<UCameraModifier>>`

### FreeCamDistance
- **类型**: `float32`

### FreeCamOffset
- **类型**: `FVector`

### ViewTargetOffset
- **类型**: `FVector`

### OnAudioFadeChangeEvent
- **类型**: `FOnAudioFadeChangeSignature`

### AutoPlaneShift
- **类型**: `float32`

### ViewPitchMin
- **类型**: `float32`

### ViewPitchMax
- **类型**: `float32`

### ViewYawMin
- **类型**: `float32`

### ViewYawMax
- **类型**: `float32`

### ViewRollMin
- **类型**: `float32`

### ViewRollMax
- **类型**: `float32`

### bIsOrthographic
- **类型**: `bool`

### bAutoCalculateOrthoPlanes
- **类型**: `bool`

### bUpdateOrthoPlanes
- **类型**: `bool`

### bUseCameraHeightAsViewTarget
- **类型**: `bool`

### bDefaultConstrainAspectRatio
- **类型**: `bool`

### bClientSimulatingViewTarget
- **类型**: `bool`

### bUseClientSideCameraUpdates
- **类型**: `bool`

### bGameCameraCutThisFrame
- **类型**: `bool`

## 方法

### AddNewCameraModifier
```angelscript
UCameraModifier AddNewCameraModifier(TSubclassOf<UCameraModifier> ModifierClass)
```
Creates and initializes a new camera modifier of the specified class.
@param ModifierClass - The class of camera modifier to create.
@return Returns the newly created camera modifier.

### BlueprintUpdateCamera
```angelscript
bool BlueprintUpdateCamera(AActor CameraTarget, FVector& NewCameraLocation, FRotator& NewCameraRotation, float32& NewCameraFOV)
```
Blueprint hook to allow blueprints to override existing camera behavior or implement custom cameras.
If this function returns true, we will use the given returned values and skip further calculations to determine
final camera POV.

### ClearCameraLensEffects
```angelscript
void ClearCameraLensEffects()
```
Removes all camera lens effects.

### FindCameraModifierByClass
```angelscript
UCameraModifier FindCameraModifierByClass(TSubclassOf<UCameraModifier> ModifierClass)
```
Returns camera modifier for this camera of the given class, if it exists.
Exact class match only. If there are multiple modifiers of the same class, the first one is returned.

### GetCameraLocation
```angelscript
FVector GetCameraLocation()
```
Returns camera's current location.

### GetCameraRotation
```angelscript
FRotator GetCameraRotation()
```
Returns camera's current rotation.

### GetFOVAngle
```angelscript
float32 GetFOVAngle()
```
Returns the camera's current full FOV angle, in degrees.

### GetOwningPlayerController
```angelscript
APlayerController GetOwningPlayerController()
```
Returns the PlayerController that owns this camera.

### OnPhotographyMultiPartCaptureEnd
```angelscript
void OnPhotographyMultiPartCaptureEnd()
```
Event triggered upon the end of a multi-part photograph capture, when manual
free-roaming photographic camera control is about to be returned to the user.
Here you may re-enable whatever was turned off within
OnPhotographyMultiPartCaptureStart.

### OnPhotographyMultiPartCaptureStart
```angelscript
void OnPhotographyMultiPartCaptureStart()
```
Event triggered upon the start of a multi-part photograph capture (i.e. a
stereoscopic or 360-degree shot).  This is an ideal time to turn off
rendering effects that tile badly (UI, subtitles, vignette, very aggressive
bloom, etc; most of these are automatically disabled when
r.Photography.AutoPostprocess is 1).

### OnPhotographySessionEnd
```angelscript
void OnPhotographySessionEnd()
```
Event triggered upon leaving Photography mode (after unpausing, if
r.Photography.AutoPause is 1).

### OnPhotographySessionStart
```angelscript
void OnPhotographySessionStart()
```
Event triggered upon entering Photography mode (before pausing, if
r.Photography.AutoPause is 1).

### PhotographyCameraModify
```angelscript
void PhotographyCameraModify(FVector NewCameraLocation, FVector PreviousCameraLocation, FVector OriginalCameraLocation, FVector& ResultCameraLocation)
```
Implementable blueprint hook to allow a PlayerCameraManager subclass to
constrain or otherwise modify the camera during free-camera photography.
For example, a blueprint may wish to limit the distance from the camera's
original point, or forbid the camera from passing through walls.
NewCameraLocation contains the proposed new camera location.
PreviousCameraLocation contains the camera location in the previous frame.
OriginalCameraLocation contains the camera location before the game was put
into photography mode.
Return ResultCameraLocation as modified according to your constraints.

### RemoveCameraModifier
```angelscript
bool RemoveCameraModifier(UCameraModifier ModifierToRemove)
```
Removes the given camera modifier from this camera (if it's on the camera in the first place) and discards it.
@return True if successfully removed, false otherwise.

### SetGameCameraCutThisFrame
```angelscript
void SetGameCameraCutThisFrame()
```
Sets the bGameCameraCutThisFrame flag to true (indicating we did a camera cut this frame; useful for game code to call, e.g., when performing a teleport that should be seamless)

### SetManualCameraFade
```angelscript
void SetManualCameraFade(float32 InFadeAmount, FLinearColor Color, bool bInFadeAudio)
```
Turns on camera fading at the given opacity. Does not auto-animate, allowing user to animate themselves.
Call StopCameraFade to turn fading back off.

### StartCameraFade
```angelscript
void StartCameraFade(float32 FromAlpha, float32 ToAlpha, float32 Duration, FLinearColor Color, bool bShouldFadeAudio, bool bHoldWhenFinished)
```
Does a camera fade to/from a solid color.  Animates automatically.
@param FromAlpha - Alpha at which to begin the fade. Range [0..1], where 0 is fully transparent and 1 is fully opaque solid color.
@param ToAlpha - Alpha at which to finish the fade.
@param Duration - How long the fade should take, in seconds.
@param Color - Color to fade to/from.
@param bShouldFadeAudio - True to fade audio volume along with the alpha of the solid color.
@param bHoldWhenFinished - True for fade to hold at the ToAlpha until explicitly stopped (e.g. with StopCameraFade)

### StartCameraShake
```angelscript
UCameraShakeBase StartCameraShake(TSubclassOf<UCameraShakeBase> ShakeClass, float32 Scale, ECameraShakePlaySpace PlaySpace, FRotator UserPlaySpaceRot)
```
Plays a camera shake on this camera.
@param Shake - The class of camera shake to play.
@param Scale - Scalar defining how "intense" to play the shake. 1.0 is normal (as authored).
@param PlaySpace - Which coordinate system to play the shake in (affects oscillations and camera anims)
@param UserPlaySpaceRot - Coordinate system to play shake when PlaySpace == CAPS_UserDefined.

### StartCameraShakeFromSource
```angelscript
UCameraShakeBase StartCameraShakeFromSource(TSubclassOf<UCameraShakeBase> ShakeClass, UCameraShakeSourceComponent SourceComponent, float32 Scale, ECameraShakePlaySpace PlaySpace, FRotator UserPlaySpaceRot)
```
Plays a camera shake on this camera.
@param Shake - The class of camera shake to play.
@param SourceComponent - The source from which the camera shake originates.
@param Scale - Applies an additional constant scale on top of the dynamic scale computed with the distance to the source
@param PlaySpace - Which coordinate system to play the shake in (affects oscillations and camera anims)
@param UserPlaySpaceRot - Coordinate system to play shake when PlaySpace == CAPS_UserDefined.

### StopAllCameraShakes
```angelscript
void StopAllCameraShakes(bool bImmediately)
```
Stops all active camera shakes on this camera.

### StopAllCameraShakesFromSource
```angelscript
void StopAllCameraShakesFromSource(UCameraShakeSourceComponent SourceComponent, bool bImmediately)
```
Stops playing all shakes originating from the given source.

### StopAllInstancesOfCameraShake
```angelscript
void StopAllInstancesOfCameraShake(TSubclassOf<UCameraShakeBase> Shake, bool bImmediately)
```
Stops playing all shakes of the given class.

### StopAllInstancesOfCameraShakeFromSource
```angelscript
void StopAllInstancesOfCameraShakeFromSource(TSubclassOf<UCameraShakeBase> Shake, UCameraShakeSourceComponent SourceComponent, bool bImmediately)
```
Stops playing all shakes of the given class originating from the given source.

### StopCameraFade
```angelscript
void StopCameraFade()
```
Stops camera fading.

### StopCameraShake
```angelscript
void StopCameraShake(UCameraShakeBase ShakeInstance, bool bImmediately)
```
Immediately stops the given shake instance and invalidates it.


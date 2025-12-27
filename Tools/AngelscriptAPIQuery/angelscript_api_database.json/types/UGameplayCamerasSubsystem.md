# UGameplayCamerasSubsystem

**继承自**: `UWorldSubsystem`

World subsystem that holds global objects for handling camera animation sequences.

## 方法

### IsCameraAnimationActive
```angelscript
bool IsCameraAnimationActive(APlayerController PlayerController, FCameraAnimationHandle Handle)
```
Returns whether the given camera animation is playing.
@param PlayerController The player controller on which to play the animation.
@param Handle                A handle to a previously started camera animation.
@return                              Whether the corresponding camera animation is playing or not.

### PlayCameraAnimation
```angelscript
FCameraAnimationHandle PlayCameraAnimation(APlayerController PlayerController, UCameraAnimationSequence Sequence, FCameraAnimationParams Params)
```
Play a new camera animation sequence.
@param PlayerController The player controller on which to play the animation.
@param Sequence              The sequence to use for the new camera animation.
@param Params                The parameters for the new camera animation instance.

### StopAllCameraAnimations
```angelscript
void StopAllCameraAnimations(APlayerController PlayerController, bool bImmediate)
```
Stop all camera animation instances.
@param PlayerController The player controller on which to play the animation.
@param bImmediate    True to stop it right now and ignore blend out, false to let it blend out as indicated.

### StopAllCameraAnimationsOf
```angelscript
void StopAllCameraAnimationsOf(APlayerController PlayerController, UCameraAnimationSequence Sequence, bool bImmediate)
```
Stop playing all instances of the given camera animation sequence.
@param PlayerController The player controller on which to play the animation.
@param Sequence              The sequence of which to stop all instances.
@param bImmediate    True to stop it right now and ignore blend out, false to let it blend out as indicated.

### StopCameraAnimation
```angelscript
void StopCameraAnimation(APlayerController PlayerController, FCameraAnimationHandle Handle, bool bImmediate)
```
Stops the given camera animation instance.
@param PlayerController The player controller on which to play the animation.
@param Hanlde                A handle to a previously started camera animation.
@param bImmediate    True to stop it right now and ignore blend out, false to let it blend out as indicated.


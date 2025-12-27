# ULegacyCameraShake

**继承自**: `UCameraShakeBase`

Legacy camera shake which can do either oscillation or run camera anims.

## 属性

### OscillationDuration
- **类型**: `float32`
- **描述**: Duration in seconds of current screen shake. Less than 0 means indefinite, 0 means no oscillation.

### OscillationBlendInTime
- **类型**: `float32`
- **描述**: Duration of the blend-in, where the oscillation scales from 0 to 1.

### OscillationBlendOutTime
- **类型**: `float32`
- **描述**: Duration of the blend-out, where the oscillation scales from 1 to 0.

### RotOscillation
- **类型**: `FROscillator`

### LocOscillation
- **类型**: `FVOscillator`

### FOVOscillation
- **类型**: `FFOscillator`

### AnimPlayRate
- **类型**: `float32`
- **描述**: Scalar defining how fast to play the anim.

### AnimScale
- **类型**: `float32`
- **描述**: Scalar defining how "intense" to play the anim.

### AnimBlendInTime
- **类型**: `float32`
- **描述**: Linear blend-in time.

### AnimBlendOutTime
- **类型**: `float32`
- **描述**: Linear blend-out time.

### RandomAnimSegmentDuration
- **类型**: `float32`
- **描述**: When bRandomAnimSegment is true, this defines how long the anim should play.

### AnimSequence
- **类型**: `UCameraAnimationSequence`
- **描述**: Source camera animation sequence to play. Can be null.

### OscillatorTimeRemaining
- **类型**: `float32`
- **描述**: Time remaining for oscillation shakes. Less than 0.f means shake infinitely.

### bRandomAnimSegment
- **类型**: `bool`

## 方法

### BlueprintUpdateCameraShake
```angelscript
void BlueprintUpdateCameraShake(float DeltaTime, float Alpha, FMinimalViewInfo POV, FMinimalViewInfo& ModifiedPOV)
```
Called every tick to let the shake modify the point of view

### IsFinished
```angelscript
bool IsFinished()
```
Called to allow a shake to decide when it's finished playing.

### PlayShake
```angelscript
void PlayShake(float Scale)
```
Called when the shake starts playing

### StopShake
```angelscript
void StopShake(bool bImmediately)
```
Called when the shake is explicitly stopped.
@param bImmediatly           If true, shake stops right away regardless of blend out settings. If false, shake may blend out according to its settings.


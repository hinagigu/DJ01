# UGeometryCacheComponent

**继承自**: `UMeshComponent`

GeometryCacheComponent, encapsulates a GeometryCache asset instance and implements functionality for rendering/and playback of GeometryCaches

## 属性

### bRunning
- **类型**: `bool`

### bLooping
- **类型**: `bool`

### bExtrapolateFrames
- **类型**: `bool`
- **描述**: Enable frame extrapolation for sub-frame sampling of non-constant topologies with imported motion vectors

### bManualTick
- **类型**: `bool`

### bOverrideWireframeColor
- **类型**: `bool`
- **描述**: Do we override the wireframe rendering color?

### GeometryCache
- **类型**: `UGeometryCache`

## 方法

### GetAnimationTime
```angelscript
float32 GetAnimationTime()
```
Set the current animation time for GeometryCache. Includes the influence of elapsed time and SetStartTimeOffset

### GetDuration
```angelscript
float32 GetDuration()
```
Get the duration of the playback

### GetMotionVectorScale
```angelscript
float32 GetMotionVectorScale()
```
Get the motion vector scale.

### GetNumberOfFrames
```angelscript
int GetNumberOfFrames()
```
Get the number of frames

### GetOverrideWireframeColor
```angelscript
bool GetOverrideWireframeColor()
```
Check whether we are overriding the wireframe color or not.

### GetPlaybackDirection
```angelscript
float32 GetPlaybackDirection()
```
Set the current animation time for GeometryCache. Includes the influence of elapsed time and SetStartTimeOffset

### GetPlaybackSpeed
```angelscript
float32 GetPlaybackSpeed()
```
Get current playback speed for GeometryCache.

### GetStartTimeOffset
```angelscript
float32 GetStartTimeOffset()
```
Get current start time offset for GeometryCache.

### GetWireframeOverrideColor
```angelscript
FLinearColor GetWireframeOverrideColor()
```
Get the wireframe override color, used when overriding the wireframe color is enabled.

### IsExtrapolatingFrames
```angelscript
bool IsExtrapolatingFrames()
```
Get whether this GeometryCache is extrapolating frames.

### IsLooping
```angelscript
bool IsLooping()
```
Get whether this GeometryCache is looping or not.

### IsPlaying
```angelscript
bool IsPlaying()
```
Get whether this GeometryCache is playing or not.

### IsPlayingReversed
```angelscript
bool IsPlayingReversed()
```
Get whether this GeometryCache is playing in reverse or not.

### Pause
```angelscript
void Pause()
```
Pause playback of GeometryCache

### Play
```angelscript
void Play()
```
Start playback of GeometryCache

### PlayFromStart
```angelscript
void PlayFromStart()
```
Start playback of GeometryCache from the start

### PlayReversed
```angelscript
void PlayReversed()
```
Start playback of GeometryCache in reverse

### PlayReversedFromEnd
```angelscript
void PlayReversedFromEnd()
```
Start playback of GeometryCache from the end and play in reverse

### SetExtrapolateFrames
```angelscript
void SetExtrapolateFrames(bool bNewExtrapolating)
```
Set whether this GeometryCache is extrapolating frames.

### SetGeometryCache
```angelscript
bool SetGeometryCache(UGeometryCache NewGeomCache)
```
Change the Geometry Cache used by this instance.

### SetLooping
```angelscript
void SetLooping(bool bNewLooping)
```
Set whether this GeometryCache is looping or not.

### SetMotionVectorScale
```angelscript
void SetMotionVectorScale(float32 NewMotionVectorScale)
```
Set new motion vector scale.

### SetOverrideWireframeColor
```angelscript
void SetOverrideWireframeColor(bool bOverride)
```
Override wireframe color?

### SetPlaybackSpeed
```angelscript
void SetPlaybackSpeed(float32 NewPlaybackSpeed)
```
Set new playback speed for GeometryCache.

### SetStartTimeOffset
```angelscript
void SetStartTimeOffset(float32 NewStartTimeOffset)
```
Set current start time offset for GeometryCache.

### SetWireframeOverrideColor
```angelscript
void SetWireframeOverrideColor(FLinearColor Color)
```
Set the color, used when overriding the wireframe color is enabled.

### Stop
```angelscript
void Stop()
```
Stop playback of GeometryCache

### TickAtThisTime
```angelscript
void TickAtThisTime(float32 Time, bool bInIsRunning, bool bInBackwards, bool bInIsLooping)
```


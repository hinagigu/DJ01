# UTimelineComponent

**继承自**: `UActorComponent`

TimelineComponent holds a series of events, floats, vectors or colors with associated keyframes.
Events can be triggered at keyframes along the timeline.
Floats, vectors, and colors are interpolated between keyframes along the timeline.

## 方法

### AddEvent
```angelscript
void AddEvent(float32 Time, FOnTimelineEvent EventFunc)
```
Add a callback event to the timeline

### AddInterpFloat
```angelscript
void AddInterpFloat(UCurveFloat FloatCurve, FOnTimelineFloat InterpFunc, FName PropertyName, FName TrackName)
```
Add a float interpolation to the timeline

### AddInterpLinearColor
```angelscript
void AddInterpLinearColor(UCurveLinearColor LinearColorCurve, FOnTimelineLinearColor InterpFunc, FName PropertyName, FName TrackName)
```
Add a linear color interpolation to the timeline

### AddInterpVector
```angelscript
void AddInterpVector(UCurveVector VectorCurve, FOnTimelineVector InterpFunc, FName PropertyName, FName TrackName)
```
Add a vector interpolation to the timeline

### GetIgnoreTimeDilation
```angelscript
bool GetIgnoreTimeDilation()
```
Get whether to ignore time dilation.

### GetPlaybackPosition
```angelscript
float32 GetPlaybackPosition()
```
Get the current playback position of the Timeline

### GetPlayRate
```angelscript
float32 GetPlayRate()
```
Get the current play rate for this timeline

### GetScaledTimelineLength
```angelscript
float32 GetScaledTimelineLength()
```
Get length of the timeline divided by the play rate

### GetTimelineLength
```angelscript
float32 GetTimelineLength()
```
Get length of the timeline

### IsLooping
```angelscript
bool IsLooping()
```
Get whether we are looping or not

### IsPlaying
```angelscript
bool IsPlaying()
```
Get whether this timeline is playing or not.

### IsReversing
```angelscript
bool IsReversing()
```
Get whether we are reversing or not

### Play
```angelscript
void Play()
```
Start playback of timeline

### PlayFromStart
```angelscript
void PlayFromStart()
```
Start playback of timeline from the start

### Reverse
```angelscript
void Reverse()
```
Start playback of timeline in reverse

### ReverseFromEnd
```angelscript
void ReverseFromEnd()
```
Start playback of timeline in reverse from the end

### SetFloatCurve
```angelscript
void SetFloatCurve(UCurveFloat NewFloatCurve, FName FloatTrackName)
```
Update a certain float track's curve

### SetIgnoreTimeDilation
```angelscript
void SetIgnoreTimeDilation(bool bNewIgnoreTimeDilation)
```
Set whether to ignore time dilation.

### SetLinearColorCurve
```angelscript
void SetLinearColorCurve(UCurveLinearColor NewLinearColorCurve, FName LinearColorTrackName)
```
Update a certain linear color track's curve

### SetLooping
```angelscript
void SetLooping(bool bNewLooping)
```
true means we would loop, false means we should not.

### SetNewTime
```angelscript
void SetNewTime(float32 NewTime)
```
Set the new playback position time to use

### SetPlaybackPosition
```angelscript
void SetPlaybackPosition(float32 NewPosition, bool bFireEvents, bool bFireUpdate)
```
Jump to a position in the timeline.
@param bFireEvents If true, event functions that are between current position and new playback position will fire.
@param bFireUpdate If true, the update output exec will fire after setting the new playback position.

### SetPlayRate
```angelscript
void SetPlayRate(float32 NewRate)
```
Sets the new play rate for this timeline

### SetTimelineFinishedFunc
```angelscript
void SetTimelineFinishedFunc(FOnTimelineEvent NewTimelineFinishedFunc)
```
Set the delegate to call when timeline is finished

### SetTimelineLength
```angelscript
void SetTimelineLength(float32 NewLength)
```
Set length of the timeline

### SetTimelineLengthMode
```angelscript
void SetTimelineLengthMode(ETimelineLengthMode NewLengthMode)
```
Sets the length mode of the timeline

### SetTimelinePostUpdateFunc
```angelscript
void SetTimelinePostUpdateFunc(FOnTimelineEvent NewTimelinePostUpdateFunc)
```
Set the delegate to call after each timeline tick

### SetVectorCurve
```angelscript
void SetVectorCurve(UCurveVector NewVectorCurve, FName VectorTrackName)
```
Update a certain vector track's curve

### Stop
```angelscript
void Stop()
```
Stop playback of timeline


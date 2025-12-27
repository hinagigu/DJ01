# UMovieSceneSequencePlayer

**继承自**: `UObject`

Abstract class that provides consistent player behaviour for various animation players

## 属性

### OnPlay
- **类型**: `FOnMovieSceneSequencePlayerEvent`

### OnPlayReverse
- **类型**: `FOnMovieSceneSequencePlayerEvent`

### OnStop
- **类型**: `FOnMovieSceneSequencePlayerEvent`

### OnPause
- **类型**: `FOnMovieSceneSequencePlayerEvent`

### OnFinished
- **类型**: `FOnMovieSceneSequencePlayerEvent`

## 方法

### ChangePlaybackDirection
```angelscript
void ChangePlaybackDirection()
```
Changes the direction of playback (go in reverse if it was going forward, or vice versa)

### GetBoundObjects
```angelscript
TArray<UObject> GetBoundObjects(FMovieSceneObjectBindingID ObjectBinding)
```
Retrieve all objects currently bound to the specified binding identifier

### GetCompletionModeOverride
```angelscript
EMovieSceneCompletionModeOverride GetCompletionModeOverride()
```
Get the state of the completion mode override

### GetCurrentTime
```angelscript
FQualifiedFrameTime GetCurrentTime()
```
Get the current playback position
@return The current playback position

### GetDisableCameraCuts
```angelscript
bool GetDisableCameraCuts()
```
Set whether to disable camera cuts

### GetDuration
```angelscript
FQualifiedFrameTime GetDuration()
```
Get the total duration of the sequence

### GetEndTime
```angelscript
FQualifiedFrameTime GetEndTime()
```
Get the offset within the level sequence to finish playing

### GetFrameDuration
```angelscript
int GetFrameDuration()
```
Get this sequence's duration in frames

### GetFrameRate
```angelscript
FFrameRate GetFrameRate()
```
Get this sequence's display rate.

### GetObjectBindings
```angelscript
TArray<FMovieSceneObjectBindingID> GetObjectBindings(UObject InObject)
```
Get the object bindings for the requested object

### GetPlayRate
```angelscript
float32 GetPlayRate()
```
Get the playback rate of this player.

### GetSequence
```angelscript
UMovieSceneSequence GetSequence()
```
Access the sequence this player is playing
@return the sequence currently assigned to this player

### GetSequenceName
```angelscript
FString GetSequenceName(bool bAddClientInfo)
```
Get the name of the sequence this player is playing
@param bAddClientInfo  If true, add client index if running as a client
@return the name of the sequence, or None if no sequence is set

### GetStartTime
```angelscript
FQualifiedFrameTime GetStartTime()
```
Get the offset within the level sequence to start playing

### GoToEndAndStop
```angelscript
void GoToEndAndStop()
```
Go to end of the sequence and stop. Adheres to 'When Finished' section rules.

### IsPaused
```angelscript
bool IsPaused()
```
Check whether the sequence is paused.

### IsPlaying
```angelscript
bool IsPlaying()
```
Check whether the sequence is actively playing.

### IsReversed
```angelscript
bool IsReversed()
```
Check whether playback is reversed.

### Pause
```angelscript
void Pause()
```
Pause playback.

### Play
```angelscript
void Play()
```
Start playback forwards from the current time cursor position, using the current play rate.

### PlayLooping
```angelscript
void PlayLooping(int NumLoops)
```
Start playback from the current time cursor position, looping the specified number of times.
@param NumLoops - The number of loops to play. -1 indicates infinite looping.

### PlayReverse
```angelscript
void PlayReverse()
```
Reverse playback.

### PlayTo
```angelscript
void PlayTo(FMovieSceneSequencePlaybackParams PlaybackParams, FMovieSceneSequencePlayToParams PlayToParams)
```
Play from the current position to the requested position and pause. If requested position is before the current position,
playback will be reversed. Playback to the requested position will be cancelled if Stop() or Pause() is invoked during this
playback.

@param PlaybackParams The position settings (ie. the position to play to)

### RemoveWeight
```angelscript
void RemoveWeight()
```
Removes a previously assigned weight

### RestoreState
```angelscript
void RestoreState()
```
Restore any changes made by this player to their original state

### RPC_ExplicitServerUpdateEvent
```angelscript
void RPC_ExplicitServerUpdateEvent(EUpdatePositionMethod Method, FFrameTime RelevantTime, int NewSerialNumber)
```
Called on the server whenever an explicit change in time has occurred through one of the (Play|Jump|Scrub)To methods

### RPC_OnFinishPlaybackEvent
```angelscript
void RPC_OnFinishPlaybackEvent(FFrameTime StoppedTime, int NewSerialNumber)
```
Called on the server when playback has reached the end. Could lead to stopping or pausing.

### RPC_OnStopEvent
```angelscript
void RPC_OnStopEvent(FFrameTime StoppedTime, int NewSerialNumber)
```
Called on the server when Stop() is called in order to differentiate Stops from Pauses.

### Scrub
```angelscript
void Scrub()
```
Scrub playback.

### SetCompletionModeOverride
```angelscript
void SetCompletionModeOverride(EMovieSceneCompletionModeOverride CompletionModeOverride)
```
Set the state of the completion mode override. Note, setting the state to force restore state will only take effect if the sequence hasn't started playing

### SetDisableCameraCuts
```angelscript
void SetDisableCameraCuts(bool bInDisableCameraCuts)
```
Set whether to disable camera cuts

### SetFrameRange
```angelscript
void SetFrameRange(int StartFrame, int Duration, float32 SubFrames)
```
Set the valid play range for this sequence, determined by a starting frame number (in this sequence player's plaback frame), and a number of frames duration

@param StartFrame      The frame number to start playing back the sequence
@param Duration        The number of frames to play

### SetFrameRate
```angelscript
void SetFrameRate(FFrameRate FrameRate)
```
Set the frame-rate that this player should play with, making all frame numbers in the specified time-space

### SetPlaybackPosition
```angelscript
void SetPlaybackPosition(FMovieSceneSequencePlaybackParams PlaybackParams)
```
Set the current time of the player by evaluating from the current time to the specified time, as if the sequence is playing.
Triggers events that lie within the evaluated range. Does not alter the persistent playback status of the player (IsPlaying).

@param PlaybackParams The position settings (ie. the position to set playback to)

### SetPlayRate
```angelscript
void SetPlayRate(float32 PlayRate)
```
Set the playback rate of this player. Negative values will play the animation in reverse.
@param PlayRate - The new rate of playback for the animation.

### SetTimeRange
```angelscript
void SetTimeRange(float32 StartTime, float32 Duration)
```
Set the valid play range for this sequence, determined by a starting time  and a duration (in seconds)

@param StartTime       The time to start playing back the sequence in seconds
@param Duration        The length to play for

### SetWeight
```angelscript
void SetWeight(float InWeight)
```
Set a manual weight to be multiplied with all blendable elements within this sequence
@note: It is recommended that a weight between 0 and 1 is supplied, though this is not enforced
@note: It is recommended that either FMovieSceneSequencePlaybackSettings::DynamicWeighting should be true for this player or the asset it's playing back should be set to enable dynamic weight to avoid undesirable behavior

@param InWeight    The weight to suuply to all elements in this sequence

### Stop
```angelscript
void Stop()
```
Stop playback and move the cursor to the end (or start, for reversed playback) of the sequence.

### StopAtCurrentTime
```angelscript
void StopAtCurrentTime()
```
Stop playback without moving the cursor.


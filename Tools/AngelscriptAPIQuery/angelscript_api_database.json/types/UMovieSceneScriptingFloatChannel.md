# UMovieSceneScriptingFloatChannel

**继承自**: `UMovieSceneScriptingChannel`

## 方法

### AddKey
```angelscript
UMovieSceneScriptingFloatKey AddKey(FFrameNumber InTime, float32 NewValue, float32 SubFrame, EMovieSceneTimeUnit TimeUnit, EMovieSceneKeyInterpolation InInterpolation)
```
Add a key to this channel. This initializes a new key and returns a reference to it.
@param        InTime                  The frame this key should go on. Respects TimeUnit to determine if it is a display rate frame or a tick resolution frame.
@param        NewValue                The value that this key should be created with.
@param        SubFrame                Optional [0-1) clamped sub-frame to put this key on. Ignored if TimeUnit is set to Tick Resolution.
@param        TimeUnit                Is the specified InTime in Display Rate frames or Tick Resolution.
@param        InInterpolation Interpolation method the key should use.
@return       The key that was created with the specified values at the specified time.

### ComputeEffectiveRange
```angelscript
FSequencerScriptingRange ComputeEffectiveRange()
```
Compute the effective range of this channel, for example, the extents of its key times

@return A range that represents the greatest range of times occupied by this channel, in the sequence's frame resolution

### EvaluateKeys
```angelscript
TArray<float32> EvaluateKeys(FSequencerScriptingRange Range, FFrameRate FrameRate)
```
Gets baked keys in this channel.
@return       An array of float's contained by this channel.
                      Returns baked keys in the specified range.

### GetDefault
```angelscript
float32 GetDefault()
```
Get this channel's default value that will be used when no keys are present. Only a valid
value when HasDefault() returns true.

### GetKeys
```angelscript
TArray<UMovieSceneScriptingKey> GetKeys()
```
Gets all of the keys in this channel.
@return       An array of UMovieSceneScriptingFloatKey's contained by this channel.
                      Returns all keys even if clipped by the owning section's boundaries or outside of the current sequence play range.

### GetKeysByIndex
```angelscript
TArray<UMovieSceneScriptingKey> GetKeysByIndex(TArray<int> Indices)
```
Gets the keys in this channel specified by the specific index
@Indices  The indices from which to get the keys from
@return       An array of UMovieSceneScriptingKey's contained by this channel.
                      Returns all keys specified by the indices, even if out of range.

### GetNumKeys
```angelscript
int GetNumKeys()
```
Returns number of keys in this channel.

### GetPostInfinityExtrapolation
```angelscript
ERichCurveExtrapolation GetPostInfinityExtrapolation()
```
@return Gets the Post-infinity extrapolation state. See ERichCurveExtrapolation for more detail.

### GetPreInfinityExtrapolation
```angelscript
ERichCurveExtrapolation GetPreInfinityExtrapolation()
```
@return Gets the Pre-infinity extrapolation state. See ERichCurveExtrapolation for more detail.

### HasDefault
```angelscript
bool HasDefault()
```
@return Does this channel have a default value set?

### RemoveDefault
```angelscript
void RemoveDefault()
```
Remove this channel's default value causing the channel to have no effect where no keys are present

### RemoveKey
```angelscript
void RemoveKey(UMovieSceneScriptingKey Key)
```
Removes the specified key. Does nothing if the key is not specified or the key belongs to another channel.

### SetDefault
```angelscript
void SetDefault(float32 InDefaultValue)
```
Set this channel's default value that should be used when no keys are present.
Sets bHasDefaultValue to true automatically.

### SetPostInfinityExtrapolation
```angelscript
void SetPostInfinityExtrapolation(ERichCurveExtrapolation InExtrapolation)
```
Sets the Post-infinity extrapolation state. See ERichCurveExtrapolation for more detail.
@param InExtrapolation The new extrapolation mode this key should use for evaluating after this key.

### SetPreInfinityExtrapolation
```angelscript
void SetPreInfinityExtrapolation(ERichCurveExtrapolation InExtrapolation)
```
Sets the Pre-infinity extrapolation state. See ERichCurveExtrapolation for more detail.
@param InExtrapolation The new extrapolation mode this key should use for evaluating before this key.


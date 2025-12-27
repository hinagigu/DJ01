# UMovieSceneScriptingStringKey

**继承自**: `UMovieSceneScriptingKey`

Exposes a Sequencer string type key to Python/Blueprints.
Stores a reference to the data so changes to this class are forwarded onto the underlying data structures.

## 方法

### GetTime
```angelscript
FFrameTime GetTime(EMovieSceneTimeUnit TimeUnit)
```
Gets the time for this key from the owning channel.
@param TimeUnit       Should the time be returned in Display Rate frames (possibly with a sub-frame value) or in Tick Resolution with no sub-frame values?
@return                       The time of this key which combines both the frame number and the sub-frame it is on. Sub-frame will be zero if you request Tick Resolution.

### GetValue
```angelscript
FString GetValue()
```
Gets the value for this key from the owning channel.
@return       The value for this key.

### SetTime
```angelscript
void SetTime(FFrameNumber NewFrameNumber, float32 SubFrame, EMovieSceneTimeUnit TimeUnit)
```
Sets the time for this key in the owning channel. Will replace any key that already exists at that frame number in this channel.
@param NewFrameNumber What frame should this key be moved to? This should be in the time unit specified by TimeUnit.
@param SubFrame               If using Display Rate time, what is the sub-frame this should go to? Clamped [0-1), and ignored with when TimeUnit is set to Tick Resolution.
@param TimeUnit               Should the NewFrameNumber be interpreted as Display Rate frames or in Tick Resolution?

### SetValue
```angelscript
void SetValue(FString InNewValue)
```
Sets the value for this key, reflecting it in the owning channel.
@param InNewValue     The new value for this key.


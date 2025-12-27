# UMovieSceneScriptingDoubleKey

**继承自**: `UMovieSceneScriptingKey`

Exposes a Sequencer double type key to Python/Blueprints.
Stores a reference to the data so changes to this class are forwarded onto the underlying data structures.

## 方法

### GetArriveTangent
```angelscript
float32 GetArriveTangent()
```
If Interpolation Mode is RCIM_Cubic, the arriving tangent at this key
@return Arrival Tangent value. Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

### GetArriveTangentWeight
```angelscript
float32 GetArriveTangentWeight()
```
If Tangent Weight Mode is RCTWM_WeightedArrive or RCTWM_WeightedBoth, the weight of the arriving tangent on the left side.
@return Tangent Weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

### GetInterpolationMode
```angelscript
ERichCurveInterpMode GetInterpolationMode()
```
Gets the interpolation mode for this key from the owning channel.
@return       Interpolation mode this key uses to interpolate between this key and the next.

### GetLeaveTangent
```angelscript
float32 GetLeaveTangent()
```
If Interpolation Mode is RCIM_Cubic, the leaving tangent at this key
@return Leaving Tangent value. Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

### GetLeaveTangentWeight
```angelscript
float32 GetLeaveTangentWeight()
```
If Tangent Weight Mode is RCTWM_WeightedLeave or RCTWM_WeightedBoth, the weight of the leaving tangent on the right side.
@return Tangent Weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

### GetTangentMode
```angelscript
ERichCurveTangentMode GetTangentMode()
```
Gets the tangent mode for this key from the owning channel.
@return       Tangent mode that this key is using specifying which tangent values are respected when evaluating.

### GetTangentWeightMode
```angelscript
ERichCurveTangentWeightMode GetTangentWeightMode()
```
If Interpolation Mode is RCIM_Cubic, the tangent weight mode at this key
@return Tangent Weight Mode. See ERichCurveTangentWeightMode for more detail on what each mode does.

### GetTime
```angelscript
FFrameTime GetTime(EMovieSceneTimeUnit TimeUnit)
```
Gets the time for this key from the owning channel.
@param TimeUnit       Should the time be returned in Display Rate frames (possibly with a sub-frame value) or in Tick Resolution with no sub-frame values?
@return                       The time of this key which combines both the frame number and the sub-frame it is on. Sub-frame will be zero if you request Tick Resolution.

### GetValue
```angelscript
float GetValue()
```
Gets the value for this key from the owning channel.
@return       The double value this key represents.

### SetArriveTangent
```angelscript
void SetArriveTangent(float32 InNewValue)
```
If Interpolation Mode is RCIM_Cubic, the arriving tangent at this key.
@param InNewValue     Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

### SetArriveTangentWeight
```angelscript
void SetArriveTangentWeight(float32 InNewValue)
```
If Tangent Weight Mode is RCTWM_WeightedArrive or RCTWM_WeightedBoth, the weight of the arriving tangent on the left side.
@param InNewValue     Specifies the new arriving tangent weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

### SetInterpolationMode
```angelscript
void SetInterpolationMode(ERichCurveInterpMode InNewValue)
```
Sets the interpolation mode for this key, reflecting it in the owning channel.
@param InNewValue     Interpolation mode this key should use to interpolate between this key and the next.

### SetLeaveTangent
```angelscript
void SetLeaveTangent(float32 InNewValue)
```
If Interpolation Mode is RCIM_Cubic, the leaving tangent at this key.
@param InNewValue     Represents the geometric tangents in the form of "tan(y/x)" where y is the key's value and x is the seconds (both relative to key)

### SetLeaveTangentWeight
```angelscript
void SetLeaveTangentWeight(float32 InNewValue)
```
If Tangent Weight Mode is RCTWM_WeightedLeave or RCTWM_WeightedBoth, the weight of the leaving tangent on the right side.
@param InNewValue     Specifies the new leaving tangent weight. Represents the length of the hypotenuse in the form of "sqrt(x*x+y*y)" using the same definitions for x and y as tangents.

### SetTangentMode
```angelscript
void SetTangentMode(ERichCurveTangentMode InNewValue)
```
Sets the tangent mode for this key, reflecting it in the owning channel.
@param InNewValue     Tangent mode that this key should use to specify which tangent values are respected when evaluating. See ERichCurveTangentMode for more details.

### SetTangentWeightMode
```angelscript
void SetTangentWeightMode(ERichCurveTangentWeightMode InNewValue)
```
If Interpolation Mode is RCIM_Cubic, the tangent weight mode at this key.
@param InNewValue     Specifies which tangent weights should be respected when evaluating the key.

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
void SetValue(float InNewValue)
```
Sets the value for this key, reflecting it in the owning channel.
@param InNewValue     The new double value for this key.


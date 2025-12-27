# USynthComponentMonoWaveTable

**继承自**: `USynthComponent`

## 属性

### OnTableAltered
- **类型**: `FOnTableAltered`

### OnNumTablesChanged
- **类型**: `FNumTablesChanged`

### CurrentPreset
- **类型**: `UMonoWaveTableSynthPreset`
- **描述**: The settings asset to use for this synth

## 方法

### GetCurveTangent
```angelscript
float32 GetCurveTangent(int TableIndex)
```
Get the curve interpolation type (What the curve is doing between keyframes)

### GetKeyFrameValuesForTable
```angelscript
TArray<float32> GetKeyFrameValuesForTable(float32 TableIndex)
```
Get an array of floats that represent the key frames in the requested curve

### GetMaxTableIndex
```angelscript
int GetMaxTableIndex()
```
Get the number of curves in the wave table. (returns -1 if there is no asset)

### GetNumTableEntries
```angelscript
int GetNumTableEntries()
```
Start BP functionality // Get the number of table elements from Blueprint

### NoteOff
```angelscript
void NoteOff(float32 InMidiNote)
```
Starts a new note (retrigs modulators, etc.)

### NoteOn
```angelscript
void NoteOn(float32 InMidiNote, float32 InVelocity)
```
Starts a new note (retrigs modulators, etc.)

### RefreshAllWaveTables
```angelscript
void RefreshAllWaveTables()
```
Refresh all wavetables (from Game Thread data)

### RefreshWaveTable
```angelscript
void RefreshWaveTable(int Index)
```
Refresh a particular wavetable (from Game Thread data)

### SetAmpEnvelopeAttackTime
```angelscript
void SetAmpEnvelopeAttackTime(float32 InAttackTimeMsec)
```
Set Amp envelope attack time (msec)

### SetAmpEnvelopeBiasDepth
```angelscript
void SetAmpEnvelopeBiasDepth(float32 InDepth)
```
Set the bias depth of the the Amp envelope

### SetAmpEnvelopeBiasInvert
```angelscript
void SetAmpEnvelopeBiasInvert(bool bInBiasInvert)
```
Set whether or not the Amp envelope's bias is inverted

### SetAmpEnvelopeDecayTime
```angelscript
void SetAmpEnvelopeDecayTime(float32 InDecayTimeMsec)
```
Set Amp envelope decay time (msec)

### SetAmpEnvelopeDepth
```angelscript
void SetAmpEnvelopeDepth(float32 InDepth)
```
Set the overall depth of the Amp envelope

### SetAmpEnvelopeInvert
```angelscript
void SetAmpEnvelopeInvert(bool bInInvert)
```
Set whether or not the Amp envelope is inverted

### SetAmpEnvelopeReleaseTime
```angelscript
void SetAmpEnvelopeReleaseTime(float32 InReleaseTimeMsec)
```
Set Amp envelope release time (msec)

### SetAmpEnvelopeSustainGain
```angelscript
void SetAmpEnvelopeSustainGain(float32 InSustainGain)
```
Set Amp envelope sustain gain [0.0, 1.0]

### SetCurveInterpolationType
```angelscript
bool SetCurveInterpolationType(CurveInterpolationType InterpolationType, int TableIndex)
```
Set the curve interpolation type (What the curve is doing between keyframes)
This should only be used for live-editing features! (changing the curves at runtime is expensive)

### SetCurveTangent
```angelscript
bool SetCurveTangent(int TableIndex, float32 InNewTangent)
```
Set the curve tangent ("Curve depth" between keyframes)
This should only be used for live-editing features! (changing the curves at runtime is expensive)

### SetCurveValue
```angelscript
bool SetCurveValue(int TableIndex, int KeyframeIndex, float32 NewValue)
```
Set a Keyframe value given a Table number and Keyframe number.
         Returns false if the request was invalid.
         NewValue will be clamped from +/- 1.0

### SetFilterEnvelopeAttackTime
```angelscript
void SetFilterEnvelopeAttackTime(float32 InAttackTimeMsec)
```
Set Low-Pass Filter envelope attack time (msec)

### SetFilterEnvelopeBiasDepth
```angelscript
void SetFilterEnvelopeBiasDepth(float32 InDepth)
```
Set Low-Pass Filter envelope bias depth

### SetFilterEnvelopeBiasInvert
```angelscript
void SetFilterEnvelopeBiasInvert(bool bInBiasInvert)
```
Set Low-Pass Filter envelope bias inversion

### SetFilterEnvelopeDepth
```angelscript
void SetFilterEnvelopeDepth(float32 InDepth)
```
Set Low-Pass Filter envelope depth

### SetFilterEnvelopeInvert
```angelscript
void SetFilterEnvelopeInvert(bool bInInvert)
```
Set Low-Pass Filter envelope inversion

### SetFilterEnvelopenDecayTime
```angelscript
void SetFilterEnvelopenDecayTime(float32 InDecayTimeMsec)
```
Set Low-Pass Filter envelope decay time (msec)

### SetFilterEnvelopeReleaseTime
```angelscript
void SetFilterEnvelopeReleaseTime(float32 InReleaseTimeMsec)
```
Set Low-Pass Filter envelope release time (msec)

### SetFilterEnvelopeSustainGain
```angelscript
void SetFilterEnvelopeSustainGain(float32 InSustainGain)
```
Set Low-Pass Filter envelope sustain gain

### SetFrequency
```angelscript
void SetFrequency(float32 FrequencyHz)
```
Sets the oscillator's frequency

### SetFrequencyPitchBend
```angelscript
void SetFrequencyPitchBend(float32 FrequencyOffsetCents)
```
Set a frequency offset in cents (for pitch modulation such as the Pitch Bend Wheel)

### SetFrequencyWithMidiNote
```angelscript
void SetFrequencyWithMidiNote(float32 InMidiNote)
```
Set the oscillator's frequency via midi note number

### SetLowPassFilterResonance
```angelscript
void SetLowPassFilterResonance(float32 InNewQ)
```
Set the Cut-off frequency of the low-pass filter

### SetPositionEnvelopeAttackTime
```angelscript
void SetPositionEnvelopeAttackTime(float32 InAttackTimeMsec)
```
Set Position envelope attack time (msec)

### SetPositionEnvelopeBiasDepth
```angelscript
void SetPositionEnvelopeBiasDepth(float32 InDepth)
```
Set Position envelope bias depth

### SetPositionEnvelopeBiasInvert
```angelscript
void SetPositionEnvelopeBiasInvert(bool bInBiasInvert)
```
Set Position envelope bias inversion

### SetPositionEnvelopeDecayTime
```angelscript
void SetPositionEnvelopeDecayTime(float32 InDecayTimeMsec)
```
Set Position envelope decay time (msec)

### SetPositionEnvelopeDepth
```angelscript
void SetPositionEnvelopeDepth(float32 InDepth)
```
Set Position envelope envelope depth

### SetPositionEnvelopeInvert
```angelscript
void SetPositionEnvelopeInvert(bool bInInvert)
```
Set Position envelope envelope inversion

### SetPositionEnvelopeReleaseTime
```angelscript
void SetPositionEnvelopeReleaseTime(float32 InReleaseTimeMsec)
```
Set Position envelope release time (msec)

### SetPositionEnvelopeSustainGain
```angelscript
void SetPositionEnvelopeSustainGain(float32 InSustainGain)
```
Set Position envelope sustain gain

### SetPosLfoDepth
```angelscript
void SetPosLfoDepth(float32 InLfoDepth)
```
Set the Modulation depth of the Lfo controlling the Table Position around the current position value
         0.0 = no modulation, 1.0 = current position +/- 0.5 (Lfo + Position result will clamp [0.0, 1.0])

### SetPosLfoFrequency
```angelscript
void SetPosLfoFrequency(float32 InLfoFrequency)
```
Set frequency of LFO controlling Table Position (in Hz)

### SetPosLfoType
```angelscript
void SetPosLfoType(ESynthLFOType InLfoType)
```
Set the shape of the Lfo controlling the position

### SetSustainPedalState
```angelscript
void SetSustainPedalState(bool InSustainPedalState)
```
Inform the synth if the sustain pedal is pressed or not

### SetWaveTablePosition
```angelscript
void SetWaveTablePosition(float32 InPosition)
```
Sets the wavetable position. Expects a percentage between 0.0 and 1.0


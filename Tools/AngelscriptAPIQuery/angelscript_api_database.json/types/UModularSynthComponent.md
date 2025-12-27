# UModularSynthComponent

**继承自**: `USynthComponent`

UModularSynthComponent
Implementation of a USynthComponent.

## 属性

### VoiceCount
- **类型**: `int`

## 方法

### CreatePatch
```angelscript
FPatchId CreatePatch(ESynth1PatchSource PatchSource, TArray<FSynth1PatchCable> PatchCables, bool bEnableByDefault)
```
Creates a new modular synth patch between a modulation source and a set of modulation destinations

### NoteOff
```angelscript
void NoteOff(float32 Note, bool bAllNotesOff, bool bKillAllNotes)
```
Stop the note (will only do anything if a voice is playing with that note)

### NoteOn
```angelscript
void NoteOn(float32 Note, int Velocity, float32 Duration)
```
Play a new note. Optionally pass in a duration to automatically turn off the note.

### SetAttackTime
```angelscript
void SetAttackTime(float32 AttackTimeMsec)
```
Sets the envelope attack time in msec.

### SetChorusDepth
```angelscript
void SetChorusDepth(float32 Depth)
```
Sets the chorus depth

### SetChorusEnabled
```angelscript
void SetChorusEnabled(bool EnableChorus)
```
Sets whether or not chorus is enabled.

### SetChorusFeedback
```angelscript
void SetChorusFeedback(float32 Feedback)
```
Sets the chorus feedback

### SetChorusFrequency
```angelscript
void SetChorusFrequency(float32 Frequency)
```
Sets the chorus frequency

### SetDecayTime
```angelscript
void SetDecayTime(float32 DecayTimeMsec)
```
Sets the envelope decay time in msec.

### SetEnableLegato
```angelscript
void SetEnableLegato(bool LegatoEnabled)
```
Sets whether or not to use legato for the synthesizer.

### SetEnablePatch
```angelscript
bool SetEnablePatch(FPatchId PatchId, bool bIsEnabled)
```

### SetEnablePolyphony
```angelscript
void SetEnablePolyphony(bool bEnablePolyphony)
```
Sets whether or not to use polyphony for the synthesizer.
@param bEnablePolyphony Whether or not to enable polyphony for the synth.

### SetEnableRetrigger
```angelscript
void SetEnableRetrigger(bool RetriggerEnabled)
```
Sets whether or not to retrigger envelope per note on.

### SetEnableUnison
```angelscript
void SetEnableUnison(bool EnableUnison)
```
Sets whether or not the synth is in unison mode (i.e. no spread)

### SetFilterAlgorithm
```angelscript
void SetFilterAlgorithm(ESynthFilterAlgorithm FilterAlgorithm)
```
Sets the filter algorithm.

### SetFilterFrequency
```angelscript
void SetFilterFrequency(float32 FilterFrequencyHz)
```
Sets the filter cutoff frequency in hz.

### SetFilterFrequencyMod
```angelscript
void SetFilterFrequencyMod(float32 FilterFrequencyHz)
```
Sets the filter cutoff frequency in hz.

### SetFilterQ
```angelscript
void SetFilterQ(float32 FilterQ)
```
Sets the filter Q (resonance)

### SetFilterQMod
```angelscript
void SetFilterQMod(float32 FilterQ)
```
Sets a modulated filter Q (resonance)

### SetFilterType
```angelscript
void SetFilterType(ESynthFilterType FilterType)
```
Sets the filter type.

### SetGainDb
```angelscript
void SetGainDb(float32 GainDb)
```
Sets the synth gain in decibels.

### SetLFOFrequency
```angelscript
void SetLFOFrequency(int LFOIndex, float32 FrequencyHz)
```
Sets the LFO frequency in hz
@param LFOIndex Which LFO to set the frequency for.
@param FrequencyHz The LFO frequency to use.

### SetLFOFrequencyMod
```angelscript
void SetLFOFrequencyMod(int LFOIndex, float32 FrequencyModHz)
```
Sets the LFO frequency modulation in hz
@param LFOIndex Which LFO to set the frequency for.
@param FrequencyModHz The LFO frequency to use.

### SetLFOGain
```angelscript
void SetLFOGain(int LFOIndex, float32 Gain)
```
Sets the LFO gain factor
@param LFOIndex Which LFO to set the frequency for.
@param Gain The gain factor to use for the LFO.

### SetLFOGainMod
```angelscript
void SetLFOGainMod(int LFOIndex, float32 GainMod)
```
Sets the LFO gain mod factor (external modulation)
@param LFOIndex Which LFO to set the frequency for.
@param Gain The gain factor to use for the LFO.

### SetLFOMode
```angelscript
void SetLFOMode(int LFOIndex, ESynthLFOMode LFOMode)
```
Sets the LFO type
@param LFOIndex Which LFO to set the frequency for.
@param LFOMode The LFO mode to use.

### SetLFOPatch
```angelscript
void SetLFOPatch(int LFOIndex, ESynthLFOPatchType LFOPatchType)
```
Sets the LFO patch type. LFO patch determines what parameter is modulated by the LFO.
@param LFOIndex Which LFO to set the frequency for.
@param LFOPatchType The LFO patch type to use.

### SetLFOType
```angelscript
void SetLFOType(int LFOIndex, ESynthLFOType LFOType)
```
Sets the LFO type
@param LFOIndex Which LFO to set the frequency for.
@param LFOType The LFO type to use.

### SetModEnvAttackTime
```angelscript
void SetModEnvAttackTime(float32 AttackTimeMsec)
```
Sets the envelope modulator attack time in msec

### SetModEnvBiasInvert
```angelscript
void SetModEnvBiasInvert(bool bInvert)
```
Sets whether or not to invert the bias output of the envelope modulator.

### SetModEnvBiasPatch
```angelscript
void SetModEnvBiasPatch(ESynthModEnvBiasPatch InPatchType)
```
Sets whether or not to modulate a param based on the envelope. Uses bias envelope output (offset from sustain gain).

### SetModEnvDecayTime
```angelscript
void SetModEnvDecayTime(float32 DecayTimeMsec)
```
Sets the envelope modulator attack time in msec

### SetModEnvDepth
```angelscript
void SetModEnvDepth(float32 Depth)
```
Sets the envelope modulator depth (amount to apply the output modulation)

### SetModEnvInvert
```angelscript
void SetModEnvInvert(bool bInvert)
```
Sets whether or not to invert the envelope modulator.

### SetModEnvPatch
```angelscript
void SetModEnvPatch(ESynthModEnvPatch InPatchType)
```
Sets whether or not to modulate a param based on the envelope. Uses bias envelope output (offset from sustain gain).

### SetModEnvReleaseTime
```angelscript
void SetModEnvReleaseTime(float32 Release)
```
Sets the envelope modulator release

### SetModEnvSustainGain
```angelscript
void SetModEnvSustainGain(float32 SustainGain)
```
Sets the envelope modulator sustain gain

### SetOscCents
```angelscript
void SetOscCents(int OscIndex, float32 Cents)
```
Sets the oscillator cents.
@param OscIndex Which oscillator to set the type for.
@param Cents The amount of cents to set the oscillator to (relative to base frequency/pitch)..

### SetOscFrequencyMod
```angelscript
void SetOscFrequencyMod(int OscIndex, float32 OscFreqMod)
```
Set the oscillator frequency modulation
@param OscIndex Which oscillator to set the type for.
@param OscFreqMod The oscillator frequency modulation to use.

### SetOscGain
```angelscript
void SetOscGain(int OscIndex, float32 OscGain)
```
Set the oscillator gain.
@param OscIndex Which oscillator to set the type for.
@param OscGain The oscillator gain.

### SetOscGainMod
```angelscript
void SetOscGainMod(int OscIndex, float32 OscGainMod)
```
Set the oscillator gain modulation.
@param OscIndex Which oscillator to set the type for.
@param OscGainMod The oscillator gain modulation to use.

### SetOscOctave
```angelscript
void SetOscOctave(int OscIndex, float32 Octave)
```
Sets the oscillator octaves
@param OscIndex Which oscillator to set the type for.
@param Octave Which octave to set the oscillator to (relative to base frequency/pitch).

### SetOscPulsewidth
```angelscript
void SetOscPulsewidth(int OscIndex, float32 Pulsewidth)
```
Sets the square wave pulsewidth [0.0, 1.0]

### SetOscSemitones
```angelscript
void SetOscSemitones(int OscIndex, float32 Semitones)
```
Sets the oscillator semitones.
@param OscIndex Which oscillator to set the type for.
@param Semitones The amount of semitones to set the oscillator to (relative to base frequency/pitch).

### SetOscSync
```angelscript
void SetOscSync(bool bIsSynced)
```
Set whether or not to follow the phase of osc2 to osc1

### SetOscType
```angelscript
void SetOscType(int OscIndex, ESynth1OscType OscType)
```
Set the oscillator type.
@param OscIndex Which oscillator to set the type for.
@param OscType The oscillator type to set.

### SetPan
```angelscript
void SetPan(float32 Pan)
```
Sets the pan of the synth [-1.0, 1.0].

### SetPitchBend
```angelscript
void SetPitchBend(float32 PitchBend)
```
Sets the synth pitch bend amount.

### SetPortamento
```angelscript
void SetPortamento(float32 Portamento)
```
Sets the synth portamento [0.0, 1.0]

### SetReleaseTime
```angelscript
void SetReleaseTime(float32 ReleaseTimeMsec)
```
Sets the envelope release time in msec.

### SetSpread
```angelscript
void SetSpread(float32 Spread)
```
Sets the amount of spread of the oscillators. [0.0, 1.0]

### SetStereoDelayFeedback
```angelscript
void SetStereoDelayFeedback(float32 DelayFeedback)
```
Sets the amount of stereo delay feedback [0.0, 1.0]

### SetStereoDelayIsEnabled
```angelscript
void SetStereoDelayIsEnabled(bool StereoDelayEnabled)
```
Sets whether not stereo delay is enabled.

### SetStereoDelayMode
```angelscript
void SetStereoDelayMode(ESynthStereoDelayMode StereoDelayMode)
```
Sets whether not stereo delay is enabled.

### SetStereoDelayRatio
```angelscript
void SetStereoDelayRatio(float32 DelayRatio)
```
Sets the amount of stereo delay ratio between left and right delay lines [0.0, 1.0]

### SetStereoDelayTime
```angelscript
void SetStereoDelayTime(float32 DelayTimeMsec)
```
Sets the amount of stereo delay time in msec.

### SetStereoDelayWetlevel
```angelscript
void SetStereoDelayWetlevel(float32 DelayWetlevel)
```
Sets the amount of stereo delay wetlevel [0.0, 1.0]

### SetSustainGain
```angelscript
void SetSustainGain(float32 SustainGain)
```
Sets the envelope sustain gain value.

### SetSynthPreset
```angelscript
void SetSynthPreset(FModularSynthPreset SynthPreset)
```
Sets the preset struct for the synth


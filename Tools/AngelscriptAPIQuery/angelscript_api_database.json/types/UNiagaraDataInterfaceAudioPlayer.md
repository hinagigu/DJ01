# UNiagaraDataInterfaceAudioPlayer

**继承自**: `UNiagaraDataInterface`

This Data Interface can be used to play one-shot audio effects driven by particle data.

## 属性

### SoundToPlay
- **类型**: `USoundBase`
- **描述**: Reference to the audio asset to play

### Attenuation
- **类型**: `USoundAttenuation`
- **描述**: Optional sound attenuation setting to use

### Concurrency
- **类型**: `USoundConcurrency`
- **描述**: Optional sound concurrency setting to use

### ParameterNames
- **类型**: `TArray<FName>`
- **描述**: A set of parameter names that can be referenced via index when setting sound cue parameters on persistent audio

### ConfigurationUserParameter
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: If bound to a valid user parameter object of type UNiagaraDataInterfaceAudioPlayerSettings, then configured settings like sound attenuation are set via the user parameter. This allows the sound settings to be dynamically changed via blueprint or C++.
Only used by persistent audio, one-shot audio ignores this option.

### bLimitPlaysPerTick
- **类型**: `bool`

### MaxPlaysPerTick
- **类型**: `int`
- **描述**: This sets the max number of sounds played each tick.
If more particles try to play a sound in a given tick, then it will play sounds until the limit is reached and discard the rest.
The particles to discard when over the limit are *not* chosen in a deterministic way.

### bStopWhenComponentIsDestroyed
- **类型**: `bool`
- **描述**: If false then it the audio component keeps playing after the niagara component was destroyed. Looping sounds are always stopped when the component is destroyed.

### bAllowLoopingOneShotSounds
- **类型**: `bool`
- **描述**: Playing looping sounds as persistent audio is not a problem, as the sound is stopped when a particle dies, but one-shot audio outlives the niagara system and can never be stopped.

### bOnlyActiveDuringGameplay
- **类型**: `bool`
- **描述**: If true then this data interface only processes sounds during active gameplay. This is useful when you are working in the preview window and the sounds annoy you.


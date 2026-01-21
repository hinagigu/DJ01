# UComboGraphGameplayCueNotify_HitImpact

**继承自**: `UGameplayCueNotify_Static`

Non instanced GameplayCueNotify for spawning particle and sound FX.

Slightly modified version of UGameplayCueNotify_HitImpact to handle spawning of particle / sound FX from passed in Effect Context in Cue Paramaters.

Checks Objects to test if it is:

- A Niagara Emitter template, and will spawn emitter at location
- A Cascade Particle system, and will spawn system at location
- A Sound Base (Cue, Wave, ...), and will spawn sound at location

Cue parameters should only contain the soft object paths to the actual asset that this cue handler will async load if necessary.

## 属性

### bAsyncLoadAllAtOnce
- **类型**: `bool`
- **描述**: Whether to do a single async load request for all assets that are passed down through gameplay cue parameters effect context.

Set it to true to issue a single async load resolved when all the assets are loaded in memory.

Set it to false to load all assets in parallel issuing multiple requests and resolved individually.

### NiagaraSpawnScale
- **类型**: `FVector`
- **描述**: For passed down assets that are Niagara Systems, this is the scale vector to use.

### CascadeSpawnScale
- **类型**: `FVector`
- **描述**: For passed down assets that are Cascade Emitters, this is the scale vector to use.

### VolumeMultiplier
- **类型**: `float32`
- **描述**: A linear scalar multiplied with the volume, in order to make the sound louder or softer.

### PitchMultiplier
- **类型**: `float32`
- **描述**: PitchMultiplier - A linear scalar multiplied with the pitch.

### StartTime
- **类型**: `float32`
- **描述**: How far in to the sound to begin playback at

### AttenuationSettings
- **类型**: `USoundAttenuation`
- **描述**: Override attenuation settings package to play sound with

### ConcurrencySettings
- **类型**: `USoundConcurrency`
- **描述**: Override concurrency settings package to play sound with

(The actor used as the "owner" for concurrency settings purposes will be the target of the gameplay cue. Allows PlaySound calls to do a concurrency limit per owner.)


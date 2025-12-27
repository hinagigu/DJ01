# UReverbEffect

**继承自**: `UObject`

## 属性

### bBypassEarlyReflections
- **类型**: `bool`

### ReflectionsDelay
- **类型**: `float32`
- **描述**: Reflections Delay - 0.0 < 0.007 < 0.3 Seconds - the time between the listener receiving the direct path sound and the first reflection

### GainHF
- **类型**: `float32`
- **描述**: Reverb Gain High Frequency - 0.0 < 0.89 < 1.0 - attenuates the high frequency reflected sound

### ReflectionsGain
- **类型**: `float32`
- **描述**: Reflections Gain - 0.0 < 0.05 < 3.16 - controls the amount of initial reflections

### bBypassLateReflections
- **类型**: `bool`

### LateDelay
- **类型**: `float32`
- **描述**: Late Reverb Delay - 0.0 < 0.011 < 0.1 Seconds - time difference between late reverb and first reflections

### DecayTime
- **类型**: `float32`
- **描述**: Decay Time - 0.1 < 1.49 < 20.0 Seconds - larger is more reverb

### Density
- **类型**: `float32`
- **描述**: Density - 0.0 < 1.0 < 1.0 - Coloration of the late reverb - lower value is more grainy

### Diffusion
- **类型**: `float32`
- **描述**: Diffusion - 0.0 < 1.0 < 1.0 - Echo density in the reverberation decay - lower is more grainy

### AirAbsorptionGainHF
- **类型**: `float32`
- **描述**: Air Absorption - 0.0 < 0.994 < 1.0 - lower value means more absorption

### DecayHFRatio
- **类型**: `float32`
- **描述**: Decay High Frequency Ratio - 0.1 < 0.83 < 2.0 - how much quicker or slower the high frequencies decay relative to the lower frequencies.

### LateGain
- **类型**: `float32`
- **描述**: Late Reverb Gain - 0.0 < 1.26 < 10.0 - gain of the late reverb

### Gain
- **类型**: `float32`
- **描述**: Reverb Gain - 0.0 < 0.32 < 1.0 - overall reverb gain - master volume control


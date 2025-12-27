# UParticleModuleBeamNoise

**继承自**: `UParticleModuleBeamBase`

## 属性

### Frequency
- **类型**: `int`
- **描述**: The frequency of noise points.

### Frequency_LowRange
- **类型**: `int`
- **描述**: If not 0, then the frequency will select a random value in the range
        [Frequency_LowRange..Frequency]

### NoiseRange
- **类型**: `FRawDistributionVector`
- **描述**: The noise point ranges.

### NoiseRangeScale
- **类型**: `FRawDistributionFloat`
- **描述**: A scale factor that will be applied to the noise range.

### NoiseSpeed
- **类型**: `FRawDistributionVector`
- **描述**: The speed with which to move each noise point.

### NoiseLockRadius
- **类型**: `float32`
- **描述**: Default target-point information to use if the beam method is endpoint.

### NoiseLockTime
- **类型**: `float32`
- **描述**: How long the  noise points should be locked - 0.0 indicates forever.

### NoiseTension
- **类型**: `float32`
- **描述**: The tension to apply to the tessellated noise line.

### NoiseTangentStrength
- **类型**: `FRawDistributionFloat`
- **描述**: The strength of noise tangents, if enabled.

### NoiseTessellation
- **类型**: `int`
- **描述**: The amount of tessellation between noise points.

### FrequencyDistance
- **类型**: `float32`
- **描述**: The distance at which to deposit noise points.
If 0.0, then use the static frequency value.
If not, distribute noise points at the given distance, up to the static Frequency value.
At that point, evenly distribute them along the beam.

### NoiseScale
- **类型**: `FRawDistributionFloat`
- **描述**: The scale factor to apply to noise range.
The lookup value is determined by dividing the number of noise points present by the
maximum number of noise points (Frequency).

### bLowFreq_Enabled
- **类型**: `bool`

### bNRScaleEmitterTime
- **类型**: `bool`

### bSmooth
- **类型**: `bool`

### bOscillate
- **类型**: `bool`

### bUseNoiseTangents
- **类型**: `bool`

### bTargetNoise
- **类型**: `bool`

### bApplyNoiseScale
- **类型**: `bool`


# UAnimCompress_PerTrackCompression

**继承自**: `UAnimCompress_RemoveLinearKeys`

## 属性

### MaxZeroingThreshold
- **类型**: `float32`
- **描述**: Maximum threshold to use when replacing a component with zero. Lower values retain more keys, but yield less compression.

### MaxPosDiffBitwise
- **类型**: `float32`
- **描述**: Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression.

### MaxAngleDiffBitwise
- **类型**: `float32`
- **描述**: Maximum angle difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression.

### MaxScaleDiffBitwise
- **类型**: `float32`
- **描述**: Maximum position difference to use when testing if an animation key may be removed. Lower values retain more keys, but yield less compression.

### AllowedRotationFormats
- **类型**: `TArray<AnimationCompressionFormat>`
- **描述**: Which encoding formats is the per-track compressor allowed to try on rotation keys

### AllowedTranslationFormats
- **类型**: `TArray<AnimationCompressionFormat>`
- **描述**: Which encoding formats is the per-track compressor allowed to try on translation keys

### AllowedScaleFormats
- **类型**: `TArray<AnimationCompressionFormat>`
- **描述**: Which encoding formats is the per-track compressor allowed to try on scale keys

### ResampledFramerate
- **类型**: `float32`
- **描述**: When bResampleAnimation is true, this defines the desired framerate

### MinKeysForResampling
- **类型**: `int`
- **描述**: Animations with fewer keys than MinKeysForResampling will not be resampled.

### TrackHeightBias
- **类型**: `int`
- **描述**: A bias added to the track height before using it to calculate the adaptive error

### ParentingDivisor
- **类型**: `float32`
- **描述**: Reduces the error tolerance the further up the tree that a key occurs
EffectiveErrorTolerance = Max(BaseErrorTolerance / Power(ParentingDivisor, Max(Height+Bias,0) * ParentingDivisorExponent), ZeroingThreshold)
Only has an effect bUseAdaptiveError is true

### ParentingDivisorExponent
- **类型**: `float32`
- **描述**: Reduces the error tolerance the further up the tree that a key occurs
EffectiveErrorTolerance = Max(BaseErrorTolerance / Power(ParentingDivisor, Max(Height+Bias,0) * ParentingDivisorExponent), ZeroingThreshold)
Only has an effect bUseAdaptiveError is true

### RotationErrorSourceRatio
- **类型**: `float32`
- **描述**: This ratio determines how much error in end effector rotation can come from a given track's rotation error or translation error.
If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from translation error.

### TranslationErrorSourceRatio
- **类型**: `float32`
- **描述**: This ratio determines how much error in end effector translation can come from a given track's rotation error or translation error.
If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from translation error.

### ScaleErrorSourceRatio
- **类型**: `float32`
- **描述**: This ratio determines how much error in end effector scale can come from a given track's rotation error or scale error.
If 1, all of it must come from rotation error, if 0.5, half can come from each, and if 0.0, all must come from scale error.

### MaxErrorPerTrackRatio
- **类型**: `float32`
- **描述**: A fraction that determines how much of the total error budget can be introduced by any particular track

### bResampleAnimation
- **类型**: `bool`

### bUseAdaptiveError
- **类型**: `bool`

### bUseOverrideForEndEffectors
- **类型**: `bool`

### bUseAdaptiveError2
- **类型**: `bool`


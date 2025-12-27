# FSoundAttenuationSettings

The settings for attenuating.

## 属性

### SpatializationAlgorithm
- **类型**: `ESoundSpatializationAlgorithm`

### AudioLinkSettingsOverride
- **类型**: `UAudioLinkSettingsAbstract`

### BinauralRadius
- **类型**: `float32`

### CustomLowpassAirAbsorptionCurve
- **类型**: `FRuntimeFloatCurve`

### CustomHighpassAirAbsorptionCurve
- **类型**: `FRuntimeFloatCurve`

### AbsorptionMethod
- **类型**: `EAirAbsorptionMethod`

### OcclusionTraceChannel
- **类型**: `ECollisionChannel`

### ReverbSendMethod
- **类型**: `EReverbSendMethod`

### PriorityAttenuationMethod
- **类型**: `EPriorityAttenuationMethod`

### NonSpatializedRadiusStart
- **类型**: `float32`

### NonSpatializedRadiusEnd
- **类型**: `float32`

### NonSpatializedRadiusMode
- **类型**: `ENonSpatializedRadiusSpeakerMapMode`

### StereoSpread
- **类型**: `float32`

### LPFRadiusMin
- **类型**: `float32`

### LPFRadiusMax
- **类型**: `float32`

### LPFFrequencyAtMin
- **类型**: `float32`

### LPFFrequencyAtMax
- **类型**: `float32`

### HPFFrequencyAtMin
- **类型**: `float32`

### HPFFrequencyAtMax
- **类型**: `float32`

### FocusAzimuth
- **类型**: `float32`

### NonFocusAzimuth
- **类型**: `float32`

### FocusDistanceScale
- **类型**: `float32`

### NonFocusDistanceScale
- **类型**: `float32`

### FocusPriorityScale
- **类型**: `float32`

### NonFocusPriorityScale
- **类型**: `float32`

### FocusVolumeAttenuation
- **类型**: `float32`

### NonFocusVolumeAttenuation
- **类型**: `float32`

### FocusAttackInterpSpeed
- **类型**: `float32`

### FocusReleaseInterpSpeed
- **类型**: `float32`

### OcclusionLowPassFilterFrequency
- **类型**: `float32`

### OcclusionVolumeAttenuation
- **类型**: `float32`

### OcclusionInterpolationTime
- **类型**: `float32`

### ReverbWetLevelMin
- **类型**: `float32`

### ReverbWetLevelMax
- **类型**: `float32`

### ReverbDistanceMin
- **类型**: `float32`

### ReverbDistanceMax
- **类型**: `float32`

### ManualReverbSendLevel
- **类型**: `float32`

### PriorityAttenuationMin
- **类型**: `float32`

### PriorityAttenuationMax
- **类型**: `float32`

### PriorityAttenuationDistanceMin
- **类型**: `float32`

### PriorityAttenuationDistanceMax
- **类型**: `float32`

### ManualPriorityAttenuation
- **类型**: `float32`

### CustomReverbSendCurve
- **类型**: `FRuntimeFloatCurve`

### SubmixSendSettings
- **类型**: `TArray<FAttenuationSubmixSendSettings>`

### CustomPriorityAttenuationCurve
- **类型**: `FRuntimeFloatCurve`

### PluginSettings
- **类型**: `FSoundAttenuationPluginSettings`

### DistanceAlgorithm
- **类型**: `EAttenuationDistanceModel`

### AttenuationShape
- **类型**: `EAttenuationShape`

### FalloffMode
- **类型**: `ENaturalSoundFalloffMode`

### dBAttenuationAtMax
- **类型**: `float32`

### AttenuationShapeExtents
- **类型**: `FVector`

### ConeOffset
- **类型**: `float32`

### FalloffDistance
- **类型**: `float32`

### ConeSphereRadius
- **类型**: `float32`

### ConeSphereFalloffDistance
- **类型**: `float32`

### CustomAttenuationCurve
- **类型**: `FRuntimeFloatCurve`

### bAttenuate
- **类型**: `bool`

### bSpatialize
- **类型**: `bool`

### bAttenuateWithLPF
- **类型**: `bool`

### bEnableListenerFocus
- **类型**: `bool`

### bEnableFocusInterpolation
- **类型**: `bool`

### bEnableOcclusion
- **类型**: `bool`

### bUseComplexCollisionForOcclusion
- **类型**: `bool`

### bEnableReverbSend
- **类型**: `bool`

### bEnablePriorityAttenuation
- **类型**: `bool`

### bApplyNormalizationToStereoSounds
- **类型**: `bool`

### bEnableLogFrequencyScaling
- **类型**: `bool`

### bEnableSubmixSends
- **类型**: `bool`

### bEnableSourceDataOverride
- **类型**: `bool`

### bEnableSendToAudioLink
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FSoundAttenuationSettings& opAssign(FSoundAttenuationSettings Other)
```


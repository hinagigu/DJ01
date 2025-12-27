# FPostProcessSettings

To be able to use struct PostProcessSettings. // Each property consists of a bool to enable it (by default off),
// the variable declaration and further down the default value for it.
// The comment should include the meaning and usable range.

## 属性

### BloomMethod
- **类型**: `EBloomMethod`

### AutoExposureMethod
- **类型**: `EAutoExposureMethod`

### TemperatureType
- **类型**: `ETemperatureMethod`

### WhiteTemp
- **类型**: `float32`

### WhiteTint
- **类型**: `float32`

### ColorSaturation
- **类型**: `FVector4`

### ColorContrast
- **类型**: `FVector4`

### ColorGamma
- **类型**: `FVector4`

### ColorGain
- **类型**: `FVector4`

### ColorOffset
- **类型**: `FVector4`

### ColorSaturationShadows
- **类型**: `FVector4`

### ColorContrastShadows
- **类型**: `FVector4`

### ColorGammaShadows
- **类型**: `FVector4`

### ColorGainShadows
- **类型**: `FVector4`

### ColorOffsetShadows
- **类型**: `FVector4`

### ColorSaturationMidtones
- **类型**: `FVector4`

### ColorContrastMidtones
- **类型**: `FVector4`

### ColorGammaMidtones
- **类型**: `FVector4`

### ColorGainMidtones
- **类型**: `FVector4`

### ColorOffsetMidtones
- **类型**: `FVector4`

### ColorSaturationHighlights
- **类型**: `FVector4`

### ColorContrastHighlights
- **类型**: `FVector4`

### ColorGammaHighlights
- **类型**: `FVector4`

### ColorGainHighlights
- **类型**: `FVector4`

### ColorOffsetHighlights
- **类型**: `FVector4`

### ColorCorrectionHighlightsMin
- **类型**: `float32`

### ColorCorrectionHighlightsMax
- **类型**: `float32`

### ColorCorrectionShadowsMax
- **类型**: `float32`

### BlueCorrection
- **类型**: `float32`

### ExpandGamut
- **类型**: `float32`

### ToneCurveAmount
- **类型**: `float32`

### FilmSlope
- **类型**: `float32`

### FilmToe
- **类型**: `float32`

### FilmShoulder
- **类型**: `float32`

### FilmBlackClip
- **类型**: `float32`

### FilmWhiteClip
- **类型**: `float32`

### SceneColorTint
- **类型**: `FLinearColor`

### SceneFringeIntensity
- **类型**: `float32`

### ChromaticAberrationStartOffset
- **类型**: `float32`

### BloomIntensity
- **类型**: `float32`

### BloomThreshold
- **类型**: `float32`

### BloomSizeScale
- **类型**: `float32`

### Bloom1Size
- **类型**: `float32`

### Bloom2Size
- **类型**: `float32`

### Bloom3Size
- **类型**: `float32`

### Bloom4Size
- **类型**: `float32`

### Bloom5Size
- **类型**: `float32`

### Bloom6Size
- **类型**: `float32`

### Bloom1Tint
- **类型**: `FLinearColor`

### Bloom2Tint
- **类型**: `FLinearColor`

### Bloom3Tint
- **类型**: `FLinearColor`

### Bloom4Tint
- **类型**: `FLinearColor`

### Bloom5Tint
- **类型**: `FLinearColor`

### Bloom6Tint
- **类型**: `FLinearColor`

### BloomConvolutionScatterDispersion
- **类型**: `float32`

### BloomConvolutionSize
- **类型**: `float32`

### BloomConvolutionTexture
- **类型**: `UTexture2D`

### BloomConvolutionCenterUV
- **类型**: `FVector2D`

### BloomConvolutionPreFilterMin
- **类型**: `float32`

### BloomConvolutionPreFilterMax
- **类型**: `float32`

### BloomConvolutionPreFilterMult
- **类型**: `float32`

### BloomConvolutionBufferScale
- **类型**: `float32`

### BloomDirtMask
- **类型**: `UTexture`

### BloomDirtMaskIntensity
- **类型**: `float32`

### BloomDirtMaskTint
- **类型**: `FLinearColor`

### DynamicGlobalIlluminationMethod
- **类型**: `EDynamicGlobalIlluminationMethod`

### IndirectLightingColor
- **类型**: `FLinearColor`

### IndirectLightingIntensity
- **类型**: `float32`

### LumenSceneLightingQuality
- **类型**: `float32`

### LumenSceneDetail
- **类型**: `float32`

### LumenSceneViewDistance
- **类型**: `float32`

### LumenSceneLightingUpdateSpeed
- **类型**: `float32`

### LumenFinalGatherQuality
- **类型**: `float32`

### LumenFinalGatherLightingUpdateSpeed
- **类型**: `float32`

### LumenMaxTraceDistance
- **类型**: `float32`

### LumenDiffuseColorBoost
- **类型**: `float32`

### LumenSkylightLeaking
- **类型**: `float32`

### LumenFullSkylightLeakingDistance
- **类型**: `float32`

### LumenSurfaceCacheResolution
- **类型**: `float32`

### ReflectionMethod
- **类型**: `EReflectionMethod`

### LumenReflectionQuality
- **类型**: `float32`

### LumenRayLightingMode
- **类型**: `ELumenRayLightingModeOverride`

### LumenMaxRoughnessToTraceReflections
- **类型**: `float32`

### LumenMaxReflectionBounces
- **类型**: `int`

### LumenMaxRefractionBounces
- **类型**: `int`

### ScreenSpaceReflectionIntensity
- **类型**: `float32`

### ScreenSpaceReflectionQuality
- **类型**: `float32`

### ScreenSpaceReflectionMaxRoughness
- **类型**: `float32`

### AmbientCubemapTint
- **类型**: `FLinearColor`

### AmbientCubemapIntensity
- **类型**: `float32`

### AmbientCubemap
- **类型**: `UTextureCube`

### CameraShutterSpeed
- **类型**: `float32`

### CameraISO
- **类型**: `float32`

### DepthOfFieldFstop
- **类型**: `float32`

### DepthOfFieldMinFstop
- **类型**: `float32`

### DepthOfFieldBladeCount
- **类型**: `int`

### AutoExposureBias
- **类型**: `float32`

### AutoExposureBiasCurve
- **类型**: `UCurveFloat`

### AutoExposureMeterMask
- **类型**: `UTexture`

### AutoExposureLowPercent
- **类型**: `float32`

### AutoExposureHighPercent
- **类型**: `float32`

### AutoExposureMinBrightness
- **类型**: `float32`

### AutoExposureMaxBrightness
- **类型**: `float32`

### AutoExposureSpeedUp
- **类型**: `float32`

### AutoExposureSpeedDown
- **类型**: `float32`

### HistogramLogMin
- **类型**: `float32`

### HistogramLogMax
- **类型**: `float32`

### LocalExposureHighlightContrastScale
- **类型**: `float32`

### LocalExposureShadowContrastScale
- **类型**: `float32`

### LocalExposureHighlightContrastCurve
- **类型**: `UCurveFloat`

### LocalExposureShadowContrastCurve
- **类型**: `UCurveFloat`

### LocalExposureHighlightThreshold
- **类型**: `float32`

### LocalExposureShadowThreshold
- **类型**: `float32`

### LocalExposureDetailStrength
- **类型**: `float32`

### LocalExposureBlurredLuminanceBlend
- **类型**: `float32`

### LocalExposureBlurredLuminanceKernelSizePercent
- **类型**: `float32`

### LocalExposureMiddleGreyBias
- **类型**: `float32`

### LensFlareIntensity
- **类型**: `float32`

### LensFlareTint
- **类型**: `FLinearColor`

### LensFlareBokehSize
- **类型**: `float32`

### LensFlareThreshold
- **类型**: `float32`

### LensFlareBokehShape
- **类型**: `UTexture`

### LensFlareTints
- **类型**: `FLinearColor`
- **描述**: RGB defines the lens flare color, A it's position. This is a temporary solution.

### VignetteIntensity
- **类型**: `float32`

### Sharpen
- **类型**: `float32`

### FilmGrainIntensity
- **类型**: `float32`

### FilmGrainIntensityShadows
- **类型**: `float32`

### FilmGrainIntensityMidtones
- **类型**: `float32`

### FilmGrainIntensityHighlights
- **类型**: `float32`

### FilmGrainShadowsMax
- **类型**: `float32`

### FilmGrainHighlightsMin
- **类型**: `float32`

### FilmGrainHighlightsMax
- **类型**: `float32`

### FilmGrainTexelSize
- **类型**: `float32`

### FilmGrainTexture
- **类型**: `UTexture2D`

### AmbientOcclusionIntensity
- **类型**: `float32`

### AmbientOcclusionStaticFraction
- **类型**: `float32`

### AmbientOcclusionRadius
- **类型**: `float32`

### AmbientOcclusionFadeDistance
- **类型**: `float32`

### AmbientOcclusionFadeRadius
- **类型**: `float32`

### AmbientOcclusionPower
- **类型**: `float32`

### AmbientOcclusionBias
- **类型**: `float32`

### AmbientOcclusionQuality
- **类型**: `float32`

### AmbientOcclusionMipBlend
- **类型**: `float32`

### AmbientOcclusionMipScale
- **类型**: `float32`

### AmbientOcclusionMipThreshold
- **类型**: `float32`

### AmbientOcclusionTemporalBlendWeight
- **类型**: `float32`

### RayTracingAOSamplesPerPixel
- **类型**: `int`

### RayTracingAOIntensity
- **类型**: `float32`

### RayTracingAORadius
- **类型**: `float32`

### ColorGradingIntensity
- **类型**: `float32`

### ColorGradingLUT
- **类型**: `UTexture`

### DepthOfFieldSensorWidth
- **类型**: `float32`

### DepthOfFieldSqueezeFactor
- **类型**: `float32`

### DepthOfFieldFocalDistance
- **类型**: `float32`

### DepthOfFieldDepthBlurAmount
- **类型**: `float32`

### DepthOfFieldDepthBlurRadius
- **类型**: `float32`

### DepthOfFieldFocalRegion
- **类型**: `float32`

### DepthOfFieldNearTransitionRegion
- **类型**: `float32`

### DepthOfFieldFarTransitionRegion
- **类型**: `float32`

### DepthOfFieldScale
- **类型**: `float32`

### DepthOfFieldNearBlurSize
- **类型**: `float32`

### DepthOfFieldFarBlurSize
- **类型**: `float32`

### DepthOfFieldOcclusion
- **类型**: `float32`

### DepthOfFieldSkyFocusDistance
- **类型**: `float32`

### DepthOfFieldVignetteSize
- **类型**: `float32`

### MotionBlurAmount
- **类型**: `float32`

### MotionBlurMax
- **类型**: `float32`

### MotionBlurTargetFPS
- **类型**: `int`

### MotionBlurPerObjectSize
- **类型**: `float32`

### TranslucencyType
- **类型**: `ETranslucencyType`

### RayTracingTranslucencyMaxRoughness
- **类型**: `float32`

### RayTracingTranslucencyRefractionRays
- **类型**: `int`

### RayTracingTranslucencySamplesPerPixel
- **类型**: `int`

### RayTracingTranslucencyShadows
- **类型**: `EReflectedAndRefractedRayTracedShadows`

### PathTracingMaxBounces
- **类型**: `int`

### PathTracingSamplesPerPixel
- **类型**: `int`

### PathTracingMaxPathExposure
- **类型**: `float32`

### WeightedBlendables
- **类型**: `FWeightedBlendables`

### bOverride_TemperatureType
- **类型**: `bool`

### bOverride_WhiteTemp
- **类型**: `bool`

### bOverride_WhiteTint
- **类型**: `bool`

### bOverride_ColorSaturation
- **类型**: `bool`

### bOverride_ColorContrast
- **类型**: `bool`

### bOverride_ColorGamma
- **类型**: `bool`

### bOverride_ColorGain
- **类型**: `bool`

### bOverride_ColorOffset
- **类型**: `bool`

### bOverride_ColorSaturationShadows
- **类型**: `bool`

### bOverride_ColorContrastShadows
- **类型**: `bool`

### bOverride_ColorGammaShadows
- **类型**: `bool`

### bOverride_ColorGainShadows
- **类型**: `bool`

### bOverride_ColorOffsetShadows
- **类型**: `bool`

### bOverride_ColorSaturationMidtones
- **类型**: `bool`

### bOverride_ColorContrastMidtones
- **类型**: `bool`

### bOverride_ColorGammaMidtones
- **类型**: `bool`

### bOverride_ColorGainMidtones
- **类型**: `bool`

### bOverride_ColorOffsetMidtones
- **类型**: `bool`

### bOverride_ColorSaturationHighlights
- **类型**: `bool`

### bOverride_ColorContrastHighlights
- **类型**: `bool`

### bOverride_ColorGammaHighlights
- **类型**: `bool`

### bOverride_ColorGainHighlights
- **类型**: `bool`

### bOverride_ColorOffsetHighlights
- **类型**: `bool`

### bOverride_ColorCorrectionShadowsMax
- **类型**: `bool`

### bOverride_ColorCorrectionHighlightsMin
- **类型**: `bool`

### bOverride_ColorCorrectionHighlightsMax
- **类型**: `bool`

### bOverride_BlueCorrection
- **类型**: `bool`

### bOverride_ExpandGamut
- **类型**: `bool`

### bOverride_ToneCurveAmount
- **类型**: `bool`

### bOverride_FilmSlope
- **类型**: `bool`

### bOverride_FilmToe
- **类型**: `bool`

### bOverride_FilmShoulder
- **类型**: `bool`

### bOverride_FilmBlackClip
- **类型**: `bool`

### bOverride_FilmWhiteClip
- **类型**: `bool`

### bOverride_SceneColorTint
- **类型**: `bool`

### bOverride_SceneFringeIntensity
- **类型**: `bool`

### bOverride_ChromaticAberrationStartOffset
- **类型**: `bool`

### bOverride_AmbientCubemapTint
- **类型**: `bool`

### bOverride_AmbientCubemapIntensity
- **类型**: `bool`

### bOverride_BloomMethod
- **类型**: `bool`

### bOverride_BloomIntensity
- **类型**: `bool`

### bOverride_BloomThreshold
- **类型**: `bool`

### bOverride_Bloom1Tint
- **类型**: `bool`

### bOverride_Bloom1Size
- **类型**: `bool`

### bOverride_Bloom2Size
- **类型**: `bool`

### bOverride_Bloom2Tint
- **类型**: `bool`

### bOverride_Bloom3Tint
- **类型**: `bool`

### bOverride_Bloom3Size
- **类型**: `bool`

### bOverride_Bloom4Tint
- **类型**: `bool`

### bOverride_Bloom4Size
- **类型**: `bool`

### bOverride_Bloom5Tint
- **类型**: `bool`

### bOverride_Bloom5Size
- **类型**: `bool`

### bOverride_Bloom6Tint
- **类型**: `bool`

### bOverride_Bloom6Size
- **类型**: `bool`

### bOverride_BloomSizeScale
- **类型**: `bool`

### bOverride_BloomConvolutionTexture
- **类型**: `bool`

### bOverride_BloomConvolutionScatterDispersion
- **类型**: `bool`

### bOverride_BloomConvolutionSize
- **类型**: `bool`

### bOverride_BloomConvolutionCenterUV
- **类型**: `bool`

### bOverride_BloomConvolutionPreFilterMin
- **类型**: `bool`

### bOverride_BloomConvolutionPreFilterMax
- **类型**: `bool`

### bOverride_BloomConvolutionPreFilterMult
- **类型**: `bool`

### bOverride_BloomConvolutionBufferScale
- **类型**: `bool`

### bOverride_BloomDirtMaskIntensity
- **类型**: `bool`

### bOverride_BloomDirtMaskTint
- **类型**: `bool`

### bOverride_BloomDirtMask
- **类型**: `bool`

### bOverride_CameraShutterSpeed
- **类型**: `bool`

### bOverride_CameraISO
- **类型**: `bool`

### bOverride_AutoExposureMethod
- **类型**: `bool`

### bOverride_AutoExposureLowPercent
- **类型**: `bool`

### bOverride_AutoExposureHighPercent
- **类型**: `bool`

### bOverride_AutoExposureMinBrightness
- **类型**: `bool`

### bOverride_AutoExposureMaxBrightness
- **类型**: `bool`

### bOverride_AutoExposureSpeedUp
- **类型**: `bool`

### bOverride_AutoExposureSpeedDown
- **类型**: `bool`

### bOverride_AutoExposureBias
- **类型**: `bool`

### bOverride_AutoExposureBiasCurve
- **类型**: `bool`

### bOverride_AutoExposureMeterMask
- **类型**: `bool`

### bOverride_AutoExposureApplyPhysicalCameraExposure
- **类型**: `bool`

### bOverride_HistogramLogMin
- **类型**: `bool`

### bOverride_HistogramLogMax
- **类型**: `bool`

### bOverride_LocalExposureHighlightContrastScale
- **类型**: `bool`

### bOverride_LocalExposureShadowContrastScale
- **类型**: `bool`

### bOverride_LocalExposureHighlightContrastCurve
- **类型**: `bool`

### bOverride_LocalExposureShadowContrastCurve
- **类型**: `bool`

### bOverride_LocalExposureHighlightThreshold
- **类型**: `bool`

### bOverride_LocalExposureShadowThreshold
- **类型**: `bool`

### bOverride_LocalExposureDetailStrength
- **类型**: `bool`

### bOverride_LocalExposureBlurredLuminanceBlend
- **类型**: `bool`

### bOverride_LocalExposureBlurredLuminanceKernelSizePercent
- **类型**: `bool`

### bOverride_LocalExposureMiddleGreyBias
- **类型**: `bool`

### bOverride_LensFlareIntensity
- **类型**: `bool`

### bOverride_LensFlareTint
- **类型**: `bool`

### bOverride_LensFlareTints
- **类型**: `bool`

### bOverride_LensFlareBokehSize
- **类型**: `bool`

### bOverride_LensFlareBokehShape
- **类型**: `bool`

### bOverride_LensFlareThreshold
- **类型**: `bool`

### bOverride_VignetteIntensity
- **类型**: `bool`

### bOverride_Sharpen
- **类型**: `bool`

### bOverride_FilmGrainIntensity
- **类型**: `bool`

### bOverride_FilmGrainIntensityShadows
- **类型**: `bool`

### bOverride_FilmGrainIntensityMidtones
- **类型**: `bool`

### bOverride_FilmGrainIntensityHighlights
- **类型**: `bool`

### bOverride_FilmGrainShadowsMax
- **类型**: `bool`

### bOverride_FilmGrainHighlightsMin
- **类型**: `bool`

### bOverride_FilmGrainHighlightsMax
- **类型**: `bool`

### bOverride_FilmGrainTexelSize
- **类型**: `bool`

### bOverride_FilmGrainTexture
- **类型**: `bool`

### bOverride_AmbientOcclusionIntensity
- **类型**: `bool`

### bOverride_AmbientOcclusionStaticFraction
- **类型**: `bool`

### bOverride_AmbientOcclusionRadius
- **类型**: `bool`

### bOverride_AmbientOcclusionFadeDistance
- **类型**: `bool`

### bOverride_AmbientOcclusionFadeRadius
- **类型**: `bool`

### bOverride_AmbientOcclusionRadiusInWS
- **类型**: `bool`

### bOverride_AmbientOcclusionPower
- **类型**: `bool`

### bOverride_AmbientOcclusionBias
- **类型**: `bool`

### bOverride_AmbientOcclusionQuality
- **类型**: `bool`

### bOverride_AmbientOcclusionMipBlend
- **类型**: `bool`

### bOverride_AmbientOcclusionMipScale
- **类型**: `bool`

### bOverride_AmbientOcclusionMipThreshold
- **类型**: `bool`

### bOverride_AmbientOcclusionTemporalBlendWeight
- **类型**: `bool`

### bOverride_RayTracingAO
- **类型**: `bool`

### bOverride_RayTracingAOSamplesPerPixel
- **类型**: `bool`

### bOverride_RayTracingAOIntensity
- **类型**: `bool`

### bOverride_RayTracingAORadius
- **类型**: `bool`

### bOverride_IndirectLightingColor
- **类型**: `bool`

### bOverride_IndirectLightingIntensity
- **类型**: `bool`

### bOverride_ColorGradingIntensity
- **类型**: `bool`

### bOverride_ColorGradingLUT
- **类型**: `bool`

### bOverride_DepthOfFieldFocalDistance
- **类型**: `bool`

### bOverride_DepthOfFieldFstop
- **类型**: `bool`

### bOverride_DepthOfFieldMinFstop
- **类型**: `bool`

### bOverride_DepthOfFieldBladeCount
- **类型**: `bool`

### bOverride_DepthOfFieldSensorWidth
- **类型**: `bool`

### bOverride_DepthOfFieldSqueezeFactor
- **类型**: `bool`

### bOverride_DepthOfFieldDepthBlurRadius
- **类型**: `bool`

### bOverride_DepthOfFieldUseHairDepth
- **类型**: `bool`

### bOverride_DepthOfFieldDepthBlurAmount
- **类型**: `bool`

### bOverride_DepthOfFieldFocalRegion
- **类型**: `bool`

### bOverride_DepthOfFieldNearTransitionRegion
- **类型**: `bool`

### bOverride_DepthOfFieldFarTransitionRegion
- **类型**: `bool`

### bOverride_DepthOfFieldScale
- **类型**: `bool`

### bOverride_DepthOfFieldNearBlurSize
- **类型**: `bool`

### bOverride_DepthOfFieldFarBlurSize
- **类型**: `bool`

### bOverride_MobileHQGaussian
- **类型**: `bool`

### bOverride_DepthOfFieldOcclusion
- **类型**: `bool`

### bOverride_DepthOfFieldSkyFocusDistance
- **类型**: `bool`

### bOverride_DepthOfFieldVignetteSize
- **类型**: `bool`

### bOverride_MotionBlurAmount
- **类型**: `bool`

### bOverride_MotionBlurMax
- **类型**: `bool`

### bOverride_MotionBlurTargetFPS
- **类型**: `bool`

### bOverride_MotionBlurPerObjectSize
- **类型**: `bool`

### bOverride_ReflectionMethod
- **类型**: `bool`

### bOverride_LumenReflectionQuality
- **类型**: `bool`

### bOverride_ScreenSpaceReflectionIntensity
- **类型**: `bool`

### bOverride_ScreenSpaceReflectionQuality
- **类型**: `bool`

### bOverride_ScreenSpaceReflectionMaxRoughness
- **类型**: `bool`

### bOverride_ScreenSpaceReflectionRoughnessScale
- **类型**: `bool`

### bOverride_RayTracingReflectionsMaxRoughness
- **类型**: `bool`

### bOverride_RayTracingReflectionsMaxBounces
- **类型**: `bool`

### bOverride_RayTracingReflectionsSamplesPerPixel
- **类型**: `bool`

### bOverride_RayTracingReflectionsShadows
- **类型**: `bool`

### bOverride_RayTracingReflectionsTranslucency
- **类型**: `bool`

### bOverride_TranslucencyType
- **类型**: `bool`

### bOverride_RayTracingTranslucencyMaxRoughness
- **类型**: `bool`

### bOverride_RayTracingTranslucencyRefractionRays
- **类型**: `bool`

### bOverride_RayTracingTranslucencySamplesPerPixel
- **类型**: `bool`

### bOverride_RayTracingTranslucencyShadows
- **类型**: `bool`

### bOverride_RayTracingTranslucencyRefraction
- **类型**: `bool`

### bOverride_DynamicGlobalIlluminationMethod
- **类型**: `bool`

### bOverride_LumenSceneLightingQuality
- **类型**: `bool`

### bOverride_LumenSceneDetail
- **类型**: `bool`

### bOverride_LumenSceneViewDistance
- **类型**: `bool`

### bOverride_LumenSceneLightingUpdateSpeed
- **类型**: `bool`

### bOverride_LumenFinalGatherQuality
- **类型**: `bool`

### bOverride_LumenFinalGatherLightingUpdateSpeed
- **类型**: `bool`

### bOverride_LumenFinalGatherScreenTraces
- **类型**: `bool`

### bOverride_LumenMaxTraceDistance
- **类型**: `bool`

### bOverride_LumenDiffuseColorBoost
- **类型**: `bool`

### bOverride_LumenSkylightLeaking
- **类型**: `bool`

### bOverride_LumenFullSkylightLeakingDistance
- **类型**: `bool`

### bOverride_LumenRayLightingMode
- **类型**: `bool`

### bOverride_LumenReflectionsScreenTraces
- **类型**: `bool`

### bOverride_LumenFrontLayerTranslucencyReflections
- **类型**: `bool`

### bOverride_LumenMaxRoughnessToTraceReflections
- **类型**: `bool`

### bOverride_LumenMaxReflectionBounces
- **类型**: `bool`

### bOverride_LumenMaxRefractionBounces
- **类型**: `bool`

### bOverride_LumenSurfaceCacheResolution
- **类型**: `bool`

### bOverride_RayTracingGI
- **类型**: `bool`

### bOverride_RayTracingGIMaxBounces
- **类型**: `bool`

### bOverride_RayTracingGISamplesPerPixel
- **类型**: `bool`

### bOverride_PathTracingMaxBounces
- **类型**: `bool`

### bOverride_PathTracingSamplesPerPixel
- **类型**: `bool`

### bOverride_PathTracingMaxPathExposure
- **类型**: `bool`

### bOverride_PathTracingEnableEmissiveMaterials
- **类型**: `bool`

### bOverride_PathTracingEnableReferenceDOF
- **类型**: `bool`

### bOverride_PathTracingEnableReferenceAtmosphere
- **类型**: `bool`

### bOverride_PathTracingEnableDenoiser
- **类型**: `bool`

### bOverride_PathTracingIncludeEmissive
- **类型**: `bool`

### bOverride_PathTracingIncludeDiffuse
- **类型**: `bool`

### bOverride_PathTracingIncludeIndirectDiffuse
- **类型**: `bool`

### bOverride_PathTracingIncludeSpecular
- **类型**: `bool`

### bOverride_PathTracingIncludeIndirectSpecular
- **类型**: `bool`

### bOverride_PathTracingIncludeVolume
- **类型**: `bool`

### bOverride_PathTracingIncludeIndirectVolume
- **类型**: `bool`

### bMobileHQGaussian
- **类型**: `bool`

### LumenFinalGatherScreenTraces
- **类型**: `bool`

### LumenReflectionsScreenTraces
- **类型**: `bool`

### LumenFrontLayerTranslucencyReflections
- **类型**: `bool`

### AutoExposureApplyPhysicalCameraExposure
- **类型**: `bool`

### AmbientOcclusionRadiusInWS
- **类型**: `bool`

### RayTracingAO
- **类型**: `bool`

### DepthOfFieldUseHairDepth
- **类型**: `bool`

### RayTracingTranslucencyRefraction
- **类型**: `bool`

### PathTracingEnableEmissiveMaterials
- **类型**: `bool`

### PathTracingEnableReferenceDOF
- **类型**: `bool`

### PathTracingEnableReferenceAtmosphere
- **类型**: `bool`

### PathTracingEnableDenoiser
- **类型**: `bool`

### PathTracingIncludeEmissive
- **类型**: `bool`

### PathTracingIncludeDiffuse
- **类型**: `bool`

### PathTracingIncludeIndirectDiffuse
- **类型**: `bool`

### PathTracingIncludeSpecular
- **类型**: `bool`

### PathTracingIncludeIndirectSpecular
- **类型**: `bool`

### PathTracingIncludeVolume
- **类型**: `bool`

### PathTracingIncludeIndirectVolume
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FPostProcessSettings& opAssign(FPostProcessSettings Other)
```


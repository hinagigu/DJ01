# URendererSettings

**继承自**: `UDeveloperSettings`

Rendering settings.

## 属性

### MobileShadingPath
- **类型**: `EMobileShadingPath`
- **描述**: The shading path to use on mobile platforms. Changing this setting requires restarting the editor. Mobile HDR is required for Deferred Shading.

### MobileAntiAliasing
- **类型**: `EMobileAntiAliasingMethod`
- **描述**: The mobile default anti-aliasing method.

### MobileFloatPrecisionMode
- **类型**: `EMobileFloatPrecisionMode`
- **描述**: Project wide mobile float precision mode for shaders and materials. Changing this setting requires restarting the editor.

### MinScreenRadiusForLights
- **类型**: `float32`
- **描述**: Screen radius at which lights are culled. Larger values can improve performance but causes lights to pop off when they affect a small area of the screen.

### MinScreenRadiusForEarlyZPass
- **类型**: `float32`
- **描述**: Screen radius at which objects are culled for the early Z pass. Larger values can improve performance but very large values can degrade performance if large occluders are not rendered.

### MinScreenRadiusForCSMdepth
- **类型**: `float32`
- **描述**: Screen radius at which objects are culled for cascaded shadow map depth passes. Larger values can improve performance but can cause artifacts as objects stop casting shadows.

### VirtualTextureTileSize
- **类型**: `uint`
- **描述**: Size in pixels for virtual texture tiles, will be rounded to next power-of-2. Changing this setting requires restarting the editor.

### VirtualTextureTileBorderSize
- **类型**: `uint`
- **描述**: Size in pixels for virtual texture tile borders, will be rounded to next power-of-2. Larger borders allow higher degree of anisotropic filtering, but uses more disk/cache memory. Changing this setting requires restarting the editor.

### VirtualTextureFeedbackFactor
- **类型**: `uint`
- **描述**: Lower factor will increase virtual texture feedback resolution which increases CPU/GPU overhead, but may decrease streaming latency, especially if materials use many virtual textures.

### WorkingColorSpaceChoice
- **类型**: `EWorkingColorSpace`
- **描述**: Choose from list of provided working color spaces, or custom to provide user-defined space.

### RedChromaticityCoordinate
- **类型**: `FVector2D`
- **描述**: Working color space red chromaticity coordinates.

### GreenChromaticityCoordinate
- **类型**: `FVector2D`
- **描述**: Working color space green chromaticity coordinates.

### BlueChromaticityCoordinate
- **类型**: `FVector2D`
- **描述**: Working color space blue chromaticity coordinates.

### WhiteChromaticityCoordinate
- **类型**: `FVector2D`
- **描述**: Working color space white chromaticity coordinates.

### DynamicGlobalIllumination
- **类型**: `EDynamicGlobalIlluminationMethod`
- **描述**: Dynamic Global Illumination Method

### Reflections
- **类型**: `EReflectionMethod`
- **描述**: Reflection Method

### ReflectionCaptureResolution
- **类型**: `int`
- **描述**: The cubemap resolution for all reflection capture probes. Must be power of 2. Note that for very high values the memory and performance impact may be severe.

### LumenRayLightingMode
- **类型**: `ELumenRayLightingMode`
- **描述**: Controls how Lumen Reflection rays are lit when Lumen is using Hardware Ray Tracing.  By default, Lumen uses the Surface Cache for best performance, but can be set to 'Hit Lighting' for higher quality.

### LumenSoftwareTracingMode
- **类型**: `ELumenSoftwareTracingMode`
- **描述**: Controls which tracing method Lumen uses when using Software Ray Tracing.

### ShadowMapMethod
- **类型**: `EShadowMapMethod`
- **描述**: Select the primary shadow mapping method. Automatically uses 'Shadow Maps' when Forward Shading is enabled for the project as Virtual Shadow Maps are not supported.

### DistanceFieldVoxelDensity
- **类型**: `float32`
- **描述**: Determines how the default scale of a mesh converts into distance field voxel dimensions. Changing this will cause all distance fields to be rebuilt.  Large values can consume memory very quickly!  Changing this setting requires restarting the editor.

### TranslucentSortPolicy
- **类型**: `ETranslucentSortPolicy`
- **描述**: The sort mode for translucent primitives, affecting how they are ordered and how they change order as the camera moves. Requires that Separate Translucency (under Postprocessing) is true.

### TranslucentSortAxis
- **类型**: `FVector`
- **描述**: The axis that sorting will occur along when Translucent Sort Policy is set to SortAlongAxis.

### FoveationLevel
- **类型**: `EFixedFoveationLevels`
- **描述**: Set the level of foveation to apply when generating the Variable Rate Shading attachment. This feature is currently experimental.
This can yield some fairly significant performance benefits on GPUs that support Tier 2 VRS.
Lower settings will result in almost no discernible artifacting on most HMDs; higher settings will show some artifacts towards the edges of the view.

### CustomDepthStencil
- **类型**: `ECustomDepthStencil`
- **描述**: Whether the custom depth pass for tagging primitives for postprocessing passes is enabled. Enabling it on demand can save memory but may cause a hitch the first time the feature is used.

### bEnableAlphaChannelInPostProcessing
- **类型**: `EAlphaChannelMode`
- **描述**: Configures alpha channel support in renderer's post processing chain. Still experimental: works only with Temporal AA, Motion Blur, Circle Depth Of Field. This option also force disable the separate translucency.

### DefaultFeatureAutoExposure
- **类型**: `EAutoExposureMethodUI`
- **描述**: The default method for AutoExposure(postprocess volume/camera/game setting can still override and enable or disable it independently)

### DefaultFeatureAutoExposureBias
- **类型**: `float32`
- **描述**: Default Value for auto exposure bias.

### DefaultFeatureLocalExposureHighlightContrast
- **类型**: `float32`
- **描述**: Default Value for Local Exposure Highlight Contrast.

### DefaultFeatureLocalExposureShadowContrast
- **类型**: `float32`
- **描述**: Default Value for Local Exposure Shadow Contrast.

### DefaultFeatureAntiAliasing
- **类型**: `EAntiAliasingMethod`
- **描述**: Selects the anti-aliasing method to use.

### MSAASampleCount
- **类型**: `ECompositingSampleCount`
- **描述**: Default number of samples for MSAA.

### DefaultLightUnits
- **类型**: `ELightUnits`
- **描述**: Which units to use for newly placed point, spot and rect lights

### DefaultBackBufferPixelFormat
- **类型**: `EDefaultBackBufferPixelFormat`
- **描述**: Pixel format used for back buffer, when not specified

### DefaultManualScreenPercentage
- **类型**: `float32`

### DefaultScreenPercentageDesktopMode
- **类型**: `EScreenPercentageMode`

### DefaultScreenPercentageMobileMode
- **类型**: `EScreenPercentageMode`

### DefaultScreenPercentageVRMode
- **类型**: `EScreenPercentageMode`

### DefaultScreenPercentagePathTracerMode
- **类型**: `EScreenPercentageMode`

### EarlyZPass
- **类型**: `EEarlyZPass`
- **描述**: Whether to use a depth only pass to initialize Z culling for the base pass.

### ClearSceneMethod
- **类型**: `EClearSceneOptions`
- **描述**: Select how the g-buffer is cleared in game mode (only affects deferred shading).

### VelocityPass
- **类型**: `EVelocityOutputPass`
- **描述**: When to write velocity buffer. Changing this setting requires restarting the editor.

### VertexDeformationOutputsVelocity
- **类型**: `EVertexDeformationOutputsVelocity`
- **描述**: Enables materials with World Position Offset and/or World Displacement to output velocities during the velocity pass even when the actor has not moved. 
If the VelocityPass is set to 'Write after base pass' this can incur a performance cost due to additional draw calls. 
That performance cost is higher if many objects are using World Position Offset. A forest of trees for example.

### GPUSimulationTextureSizeX
- **类型**: `int`
- **描述**: The X size of the GPU simulation texture size. SizeX*SizeY determines the maximum number of GPU simulated particles in an emitter. Potentially overridden by CVar settings in BaseDeviceProfile.ini.

### GPUSimulationTextureSizeY
- **类型**: `int`
- **描述**: The Y size of the GPU simulation texture size. SizeX*SizeY determines the maximum number of GPU simulated particles in an emitter. Potentially overridden by CVar settings in BaseDeviceProfile.ini.

### GBufferFormat
- **类型**: `EGBufferFormat`
- **描述**: Selects which GBuffer format should be used. Affects performance primarily via how much GPU memory bandwidth used. This also controls Substrate normal quality and, in this case, a restart is required.

### MorphTargetMaxBlendWeight
- **类型**: `float32`
- **描述**: Blend target weights will be checked against this value for validation. Absolue values greather than this number will be clamped to [-MorphTargetMaxBlendWeight, MorphTargetMaxBlendWeight].

### LightFunctionAtlasPixelFormat
- **类型**: `ELightFunctionAtlasPixelFormat`
- **描述**: Select the format of the light function atlas texture.

### WireframeCullThreshold
- **类型**: `float32`
- **描述**: Screen radius at which wireframe objects are culled. Larger values can improve performance when viewing a scene in wireframe.

### DefaultSkinCacheBehavior
- **类型**: `ESkinCacheDefaultBehavior`
- **描述**: Default behavior if all skeletal meshes are included/excluded from the skin cache. If Support Ray Tracing is enabled on a mesh, the skin cache will be used for Ray Tracing updates on that mesh regardless of this setting.

### SkinCacheSceneMemoryLimitInMB
- **类型**: `float32`
- **描述**: Maximum amount of memory (in MB) per world/scene allowed for the Compute Skin Cache to generate output vertex data and recompute tangents.

### MobileLocalLightSetting
- **类型**: `EMobileLocalLightSetting`
- **描述**: Select which Local Light Setting to use for Mobile. Changing this setting requires restarting the editor.

### UnlimitedBonInfluencesThreshold
- **类型**: `int`
- **描述**: When Unlimited Bone Influence is enabled, it still uses a fixed bone inflence buffer until the max bone influence of a mesh exceeds this value

### DefaultBoneInfluenceLimit
- **类型**: `FPerPlatformInt`
- **描述**: When BoneInfluenceLimit on a skeletal mesh LOD is set to 0, this setting is used instead. If this setting is 0, no limit will be applied here and the max bone influences will be determined by other project settings. Changing this setting requires restarting the editor.

### MaxSkinBones
- **类型**: `FPerPlatformInt`
- **描述**: Max number of bones that can be skinned on the GPU in a single draw call. The default value is set by the Compat.MAX_GPUSKIN_BONES consolevariable. Changing this setting requires restarting the editor.

### MobilePlanarReflectionMode
- **类型**: `EMobilePlanarReflectionMode`
- **描述**: The PlanarReflection will work differently on different mode on mobile platform, choose the proper mode as expect. Changing this setting requires restarting the editor.

### bStreamSkeletalMeshLODs
- **类型**: `FPerPlatformBool`
- **描述**: Whether to stream skeletal mesh LODs by default.

### bDiscardSkeletalMeshOptionalLODs
- **类型**: `FPerPlatformBool`
- **描述**: Whether to discard skeletal mesh LODs below minimum LOD levels at cook time.

### VisualizeCalibrationColorMaterialPath
- **类型**: `FSoftObjectPath`
- **描述**: When the VisualizeCalibrationColor show flag is enabled, this path will be used as the post-process material to render. The post-process material's Blendable Location property must be set to "After Tonemapping" for proper calibration display.

### VisualizeCalibrationCustomMaterialPath
- **类型**: `FSoftObjectPath`
- **描述**: When the VisualizeCalibrationCustom show flag is enabled, this path will be used as the post-process material to render. The post-process material's Blendable Location property must be set to "After Tonemapping" for proper calibration display.

### VisualizeCalibrationGrayscaleMaterialPath
- **类型**: `FSoftObjectPath`
- **描述**: When the VisualizeCalibrationGrayscale show flag is enabled, this path will be used as the post-process material to render. The post-process material's Blendable Location property must be set to "After Tonemapping" for proper calibration display.

### bMobileSupportDeferredOnOpenGL
- **类型**: `bool`

### bMobileSupportGPUScene
- **类型**: `bool`

### bMobileAllowDitheredLODTransition
- **类型**: `bool`

### bMobileVirtualTextures
- **类型**: `bool`

### bDiscardUnusedQualityLevels
- **类型**: `bool`

### bOcclusionCulling
- **类型**: `bool`

### bPrecomputedVisibilityWarning
- **类型**: `bool`

### bTextureStreaming
- **类型**: `bool`

### bUseDXT5NormalMaps
- **类型**: `bool`

### bVirtualTextures
- **类型**: `bool`

### bVirtualTextureEnableAutoImport
- **类型**: `bool`

### bVirtualTexturedLightmaps
- **类型**: `bool`

### bVirtualTextureAnisotropicFiltering
- **类型**: `bool`

### bEnableVirtualTextureOpacityMask
- **类型**: `bool`

### bClearCoatEnableSecondNormal
- **类型**: `bool`

### ReflectionEnvironmentLightmapMixBasedOnRoughness
- **类型**: `bool`

### bUseHardwareRayTracingForLumen
- **类型**: `bool`

### LumenFrontLayerTranslucencyReflections
- **类型**: `bool`

### LumenRayTracedTranslucentRefractions
- **类型**: `bool`

### bEnableRayTracing
- **类型**: `bool`

### bEnableRayTracingShadows
- **类型**: `bool`

### bEnableRayTracingTextureLOD
- **类型**: `bool`

### bEnablePathTracing
- **类型**: `bool`

### bGenerateMeshDistanceFields
- **类型**: `bool`

### bNanite
- **类型**: `bool`

### bAllowStaticLighting
- **类型**: `bool`

### bUseNormalMapsForStaticLighting
- **类型**: `bool`

### bForwardShading
- **类型**: `bool`

### bVertexFoggingForOpaque
- **类型**: `bool`

### bSeparateTranslucency
- **类型**: `bool`

### bLocalFogVolumeApplyOnTranslucent
- **类型**: `bool`

### bDynamicFoveation
- **类型**: `bool`

### bCustomDepthTaaJitter
- **类型**: `bool`

### bDefaultFeatureBloom
- **类型**: `bool`

### bDefaultFeatureAmbientOcclusion
- **类型**: `bool`

### bDefaultFeatureAmbientOcclusionStaticFraction
- **类型**: `bool`

### bDefaultFeatureAutoExposure
- **类型**: `bool`

### bExtendDefaultLuminanceRangeInAutoExposureSettings
- **类型**: `bool`

### bDefaultFeatureMotionBlur
- **类型**: `bool`

### bDefaultFeatureLensFlare
- **类型**: `bool`

### bTemporalUpsampling
- **类型**: `bool`

### bRenderUnbuiltPreviewShadowsInGame
- **类型**: `bool`

### bStencilForLODDither
- **类型**: `bool`

### bEarlyZPassOnlyMaterialMasking
- **类型**: `bool`

### bEnableCSMCaching
- **类型**: `bool`

### bDBuffer
- **类型**: `bool`

### bSelectiveBasePassOutputs
- **类型**: `bool`

### bDefaultParticleCutouts
- **类型**: `bool`

### bGlobalClipPlane
- **类型**: `bool`

### bUseGPUMorphTargets
- **类型**: `bool`

### bSupportSkyAtmosphere
- **类型**: `bool`

### bSupportSkyAtmosphereAffectsHeightFog
- **类型**: `bool`

### bSupportLocalFogVolumes
- **类型**: `bool`

### bSupportCloudShadowOnForwardLitTranslucent
- **类型**: `bool`

### bVolumetricFogUsesLightFunctionAtlas
- **类型**: `bool`

### bDeferredLightingUsesLightFunctionAtlas
- **类型**: `bool`

### bSingleLayerWaterUsesLightFunctionAtlas
- **类型**: `bool`

### bTranslucentUsesLightFunctionAtlas
- **类型**: `bool`

### bSupportIESProfileOnTranslucent
- **类型**: `bool`

### bSupportRectLightOnTranslucent
- **类型**: `bool`

### bNvidiaAftermathEnabled
- **类型**: `bool`

### bMultiView
- **类型**: `bool`

### bMobilePostProcessing
- **类型**: `bool`

### bMobileMultiView
- **类型**: `bool`

### bRoundRobinOcclusion
- **类型**: `bool`

### bMeshStreaming
- **类型**: `bool`

### bEnableHeterogeneousVolumes
- **类型**: `bool`

### bShouldHeterogeneousVolumesCastShadows
- **类型**: `bool`

### bCompositeHeterogeneousVolumesWithTranslucency
- **类型**: `bool`

### bSupportStationarySkylight
- **类型**: `bool`

### bSupportLowQualityLightmaps
- **类型**: `bool`

### bSupportPointLightWholeSceneShadows
- **类型**: `bool`

### bSupportTranslucentPerObjectShadow
- **类型**: `bool`

### bSupportCloudShadowOnSingleLayerWater
- **类型**: `bool`

### bEnableSubstrate
- **类型**: `bool`

### SubstrateOpaqueMaterialRoughRefraction
- **类型**: `bool`

### SubstrateDebugAdvancedVisualizationShaders
- **类型**: `bool`

### bMaterialRoughDiffuse
- **类型**: `bool`

### bMaterialEnergyConservation
- **类型**: `bool`

### bOrderedIndependentTransparencyEnable
- **类型**: `bool`

### bUseHairStrandsAutoLODMode
- **类型**: `bool`

### bSupportSkinCacheShaders
- **类型**: `bool`

### bSkipCompilingGPUSkinVF
- **类型**: `bool`

### bMobileEnableStaticAndCSMShadowReceivers
- **类型**: `bool`

### bMobileEnableMovableLightCSMShaderCulling
- **类型**: `bool`

### bMobileForwardEnableClusteredReflections
- **类型**: `bool`

### bMobileEnableNoPrecomputedLightingCSMShader
- **类型**: `bool`

### bMobileAllowDistanceFieldShadows
- **类型**: `bool`

### bMobileAllowMovableDirectionalLights
- **类型**: `bool`

### bMobileAllowMovableSpotlightShadows
- **类型**: `bool`

### bSupport16BitBoneIndex
- **类型**: `bool`

### bGPUSkinLimit2BoneInfluences
- **类型**: `bool`

### bSupportDepthOnlyIndexBuffers
- **类型**: `bool`

### bSupportReversedIndexBuffers
- **类型**: `bool`

### bMobileAmbientOcclusion
- **类型**: `bool`

### bMobileDBuffer
- **类型**: `bool`

### bUseUnlimitedBoneInfluences
- **类型**: `bool`

### bAlwaysUseDeformerForUnlimitedBoneInfluences
- **类型**: `bool`

### bMobileSupportsGen4TAA
- **类型**: `bool`


# UMaterial

**继承自**: `UMaterialInterface`

A Material is an asset which can be applied to a mesh to control the visual look of the scene.
When light from the scene hits the surface, the shading model of the material is used to calculate how that light interacts with the surface.

Warning: Creating new materials directly increases shader compile times!  Consider creating a Material Instance off of an existing material instead.

## 属性

### PhysMaterial
- **类型**: `UPhysicalMaterial`
- **描述**: Physical material to use for this graphics material. Used for sounds, effects etc.

### PhysMaterialMask
- **类型**: `UPhysicalMaterialMask`
- **描述**: Physical material mask to use for this graphics material. Used for sounds, effects etc.

### PhysicalMaterialMap
- **类型**: `UPhysicalMaterial`
- **描述**: Physical material mask map to use for this graphics material. Used for sounds, effects etc.

### MaterialDomain
- **类型**: `EMaterialDomain`

### MaterialDecalResponse
- **类型**: `EMaterialDecalResponse`

### NaniteOverrideMaterial
- **类型**: `FMaterialOverrideNanite`
- **描述**: An override material which will be used instead of this one when rendering with Nanite.

### DisplacementScaling
- **类型**: `FDisplacementScaling`

### ShadingModel
- **类型**: `EMaterialShadingModel`
- **描述**: Determines how inputs are combined to create the material's final color.

### OpacityMaskClipValue
- **类型**: `float32`
- **描述**: If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue.
If BlendMode is BLEND_Translucent, BLEND_Additive, or BLEND_Modulate, and "Output Depth and Velocity" is enabled,
the object velocity is not rendered where Opacity < OpacityMaskClipValue.

### TranslucencyPass
- **类型**: `EMaterialTranslucencyPass`
- **描述**: Specifies the separate pass in which to render translucency.
This can be used to avoid artifacts caused by certain post processing effects.

### TranslucencyLightingMode
- **类型**: `ETranslucencyLightingMode`
- **描述**: Sets the lighting mode that will be used on this material if it is translucent.

### NumCustomizedUVs
- **类型**: `int`
- **描述**: Number of customized UV inputs to display.  Unconnected customized UV inputs will just pass through the vertex UVs.

### TranslucencyDirectionalLightingIntensity
- **类型**: `float32`
- **描述**: Useful for artificially increasing the influence of the normal on the lighting result for translucency.
A value larger than 1 increases the influence of the normal, a value smaller than 1 makes the lighting more ambient.

### TranslucentShadowDensityScale
- **类型**: `float32`
- **描述**: Scale used to make translucent shadows more or less opaque than the material's actual opacity.

### TranslucentSelfShadowDensityScale
- **类型**: `float32`
- **描述**: Scale used to make translucent self-shadowing more or less opaque than the material's shadow on other objects.
This is only used when the object is casting a volumetric translucent shadow.

### TranslucentSelfShadowSecondDensityScale
- **类型**: `float32`
- **描述**: Used to make a second self shadow gradient, to add interesting shading in the shadow of the first.

### TranslucentSelfShadowSecondOpacity
- **类型**: `float32`
- **描述**: Controls the strength of the second self shadow gradient.

### TranslucentBackscatteringExponent
- **类型**: `float32`
- **描述**: Controls how diffuse the material's backscattering is when using the MSM_Subsurface shading model.
Larger exponents give a less diffuse look (smaller, brighter backscattering highlight).
This is only used when the object is casting a volumetric translucent shadow from a directional light.

### TranslucentMultipleScatteringExtinction
- **类型**: `FLinearColor`
- **描述**: Colored extinction factor used to approximate multiple scattering in dense volumes.
This is only used when the object is casting a volumetric translucent shadow.

### TranslucentShadowStartOffset
- **类型**: `float32`
- **描述**: Local space distance to bias the translucent shadow.  Positive values move the shadow away from the light.

### FloatPrecisionMode
- **类型**: `EMaterialFloatPrecisionMode`

### ShadingRate
- **类型**: `EMaterialShadingRate`
- **描述**: Select what shading rate to apply, on platforms that support variable rate shading.
Non-1x1 rates will reduce the rasterization fidelity for the material; they will not super-sample the material.
This can save GPU performance on materials where reduced fidelity is acceptable.

### BlendableLocation
- **类型**: `EBlendableLocation`

### StencilCompare
- **类型**: `EMaterialStencilCompare`

### StencilRefValue
- **类型**: `uint8`

### NeuralProfileId
- **类型**: `int8`
- **描述**: Set by reference object cannot be modified.

### RefractionMethod
- **类型**: `ERefractionMode`
- **描述**: Controls how the Refraction input is interpreted and how the refraction offset into scene color is computed for this material.

### RefractionCoverageMode
- **类型**: `ERefractionCoverageMode`
- **描述**: Controls whether refraction takes into account the material surface coverage, or not.

### BlendablePriority
- **类型**: `int`

### PreshaderGap
- **类型**: `uint16`
- **描述**: If non-zero, overrides r.Material.PreshaderGapInterval for this material.  Workaround for a platform specific register overflow bug.

### RefractionDepthBias
- **类型**: `float32`
- **描述**: This is the refraction depth bias, larger values offset distortion to prevent closer objects from rendering into the distorted surface at acute viewing angles but increases the disconnect between surface and where the refraction starts.

### MaxWorldPositionOffsetDisplacement
- **类型**: `float32`

### bAlwaysEvaluateWorldPositionOffset
- **类型**: `bool`

### BlendMode
- **类型**: `EBlendMode`

### bCastDynamicShadowAsMasked
- **类型**: `bool`

### bEnableResponsiveAA
- **类型**: `bool`

### bScreenSpaceReflections
- **类型**: `bool`

### bContactShadows
- **类型**: `bool`

### TwoSided
- **类型**: `bool`

### bIsThinSurface
- **类型**: `bool`

### DitheredLODTransition
- **类型**: `bool`

### DitherOpacityMask
- **类型**: `bool`

### bAllowNegativeEmissiveColor
- **类型**: `bool`

### bHasPixelAnimation
- **类型**: `bool`

### bEnableTessellation
- **类型**: `bool`

### bEnableMobileSeparateTranslucency
- **类型**: `bool`

### bDisableDepthTest
- **类型**: `bool`

### bWriteOnlyAlpha
- **类型**: `bool`

### bGenerateSphericalParticleNormals
- **类型**: `bool`

### bTangentSpaceNormal
- **类型**: `bool`

### bUseEmissiveForDynamicAreaLighting
- **类型**: `bool`

### bUsedWithSkeletalMesh
- **类型**: `bool`

### bUsedWithEditorCompositing
- **类型**: `bool`

### bUsedWithParticleSprites
- **类型**: `bool`

### bUsedWithBeamTrails
- **类型**: `bool`

### bUsedWithMeshParticles
- **类型**: `bool`

### bUsedWithNiagaraSprites
- **类型**: `bool`

### bUsedWithNiagaraRibbons
- **类型**: `bool`

### bUsedWithNiagaraMeshParticles
- **类型**: `bool`

### bUsedWithGeometryCache
- **类型**: `bool`

### bUsedWithStaticLighting
- **类型**: `bool`

### bUsedWithMorphTargets
- **类型**: `bool`

### bUsedWithSplineMeshes
- **类型**: `bool`

### bUsedWithInstancedStaticMeshes
- **类型**: `bool`

### bUsedWithGeometryCollections
- **类型**: `bool`

### bUsedWithClothing
- **类型**: `bool`

### bUsedWithWater
- **类型**: `bool`

### bUsedWithHairStrands
- **类型**: `bool`

### bUsedWithLidarPointCloud
- **类型**: `bool`

### bUsedWithVirtualHeightfieldMesh
- **类型**: `bool`

### bUsedWithNanite
- **类型**: `bool`

### bUsedWithVolumetricCloud
- **类型**: `bool`

### bUsedWithHeterogeneousVolumes
- **类型**: `bool`

### bAutomaticallySetUsageInEditor
- **类型**: `bool`

### bFullyRough
- **类型**: `bool`

### bUseLightmapDirectionality
- **类型**: `bool`

### bMobileEnableHighQualityBRDF
- **类型**: `bool`

### bUseAlphaToCoverage
- **类型**: `bool`

### bForwardRenderUsePreintegratedGFForSimpleIBL
- **类型**: `bool`

### bUseHQForwardReflections
- **类型**: `bool`

### bForwardBlendsSkyLightCubemaps
- **类型**: `bool`

### bUsePlanarForwardReflections
- **类型**: `bool`

### bNormalCurvatureToRoughness
- **类型**: `bool`

### AllowTranslucentCustomDepthWrites
- **类型**: `bool`

### bAllowFrontLayerTranslucency
- **类型**: `bool`

### Wireframe
- **类型**: `bool`

### bAllowVariableRateShading
- **类型**: `bool`

### bUseMaterialAttributes
- **类型**: `bool`

### bEnableExecWire
- **类型**: `bool`

### bEnableNewHLSLGenerator
- **类型**: `bool`

### bCastRayTracedShadows
- **类型**: `bool`

### bUseTranslucencyVertexFog
- **类型**: `bool`

### bApplyCloudFogging
- **类型**: `bool`

### bIsSky
- **类型**: `bool`

### bComputeFogPerPixel
- **类型**: `bool`

### bOutputTranslucentVelocity
- **类型**: `bool`

### BlendableOutputAlpha
- **类型**: `bool`

### bUsedWithNeuralNetworks
- **类型**: `bool`

### bEnableStencilTest
- **类型**: `bool`

### bIsBlendable
- **类型**: `bool`


# UParticleModuleLight

**继承自**: `UParticleModuleLightBase`

## 属性

### bUseInverseSquaredFalloff
- **类型**: `bool`
- **描述**: Whether to use physically based inverse squared falloff from the light.  If unchecked, the LightExponent distribution will be used instead.

### bAffectsTranslucency
- **类型**: `bool`
- **描述**: Whether lights from this module should affect translucency.
Use with caution.  Modules enabling this should only make a few particle lights at most, and the smaller they are, the less they will cost.

### bPreviewLightRadius
- **类型**: `bool`
- **描述**: Will draw wireframe spheres to preview the light radius if enabled.
Note: this is intended for previewing and the value will not be saved, it will always revert to disabled.

### SpawnFraction
- **类型**: `float32`
- **描述**: Fraction of particles in this emitter to create lights on.

### ColorScaleOverLife
- **类型**: `FRawDistributionVector`
- **描述**: Scale that is applied to the particle's color to calculate the light's color, and can be setup as a curve over the particle's lifetime.

### BrightnessOverLife
- **类型**: `FRawDistributionFloat`
- **描述**: Brightness scale for the light, which can be setup as a curve over the particle's lifetime.

### RadiusScale
- **类型**: `FRawDistributionFloat`
- **描述**: Scales the particle's radius, to calculate the light's radius.

### LightExponent
- **类型**: `FRawDistributionFloat`
- **描述**: Provides the light's exponent when inverse squared falloff is disabled.

### InverseExposureBlend
- **类型**: `float32`

### LightingChannels
- **类型**: `FLightingChannels`

### VolumetricScatteringIntensity
- **类型**: `float32`

### bHighQualityLights
- **类型**: `bool`
- **描述**: Converts the particle lights into high quality lights as if they came from a PointLightComponent.  High quality lights cost significantly more on both CPU and GPU.

### bShadowCastingLights
- **类型**: `bool`
- **描述**: Whether to cast shadows from the particle lights.  Requires High Quality Lights to be enabled.
Warning: This can be incredibly expensive on the GPU - use with caution.

### bOverrideInverseExposureBlend
- **类型**: `bool`


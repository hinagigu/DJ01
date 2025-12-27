# UMaterialExpressionVolumetricAdvancedMaterialOutput

**继承自**: `UMaterialExpressionCustomOutput`

Material output expression for writing advanced volumetric material properties.

## 属性

### ConstPhaseG
- **类型**: `float32`
- **描述**: Only used if PhaseG is not hooked up. Parameter 'g' input to the phase function  describing how much forward(g<0) or backward (g>0) light scatter around.

### ConstPhaseG2
- **类型**: `float32`
- **描述**: Only used if PhaseG2 is not hooked up. Parameter 'g' input to the second phase function  describing how much forward(g<0) or backward (g>0) light scatter around. Valid range is [-1,1].

### ConstPhaseBlend
- **类型**: `float32`
- **描述**: Only used if PhaseBlend is not hooked up. Lerp factor when blending the two phase functions parameterized by G and G2. Valid range is [0,1].

### PerSamplePhaseEvaluation
- **类型**: `bool`
- **描述**: Set this to true to force the phase function to be evaluated per sample, instead once per pixel (globally). Per sample evaluation is slower.

### MultiScatteringApproximationOctaveCount
- **类型**: `uint`
- **描述**: How many octave to use for the multiple-scattering approximation. This makes the shader more expensive so you should only use 0 or 1 for better performance, and tweak multiple scattering parameters accordingly. 0 means single scattering only. The maximum value is 2 (expenssive).

### ConstMultiScatteringContribution
- **类型**: `float32`
- **描述**: Only used if MultiScatteringContribution is not hooked up. Multi-scattering approximation: represents how much contribution each successive octave will add. Valid range is [0,1], from low to high contribution

### ConstMultiScatteringOcclusion
- **类型**: `float32`
- **描述**: Only used if MultiScatteringOcclusion is not hooked up. Multi-scattering approximation: represents how much occlusion will be reduced for each successive octave. Valid range is [0,1], from low to high occlusion.

### ConstMultiScatteringEccentricity
- **类型**: `float32`
- **描述**: Only used if MultiScatteringEccentricity is not hooked up. Multi-scattering approximation: represents how much the phase will become isotropic for each successive octave. Valid range is [0,1], from anisotropic to isotropic phase.

### bGroundContribution
- **类型**: `bool`
- **描述**: Sample the shadowed lighting contribution from the ground onto the medium (single scattering). This adds some costs to the tracing when enabled.

### bGrayScaleMaterial
- **类型**: `bool`
- **描述**: Set this for the material to only be considered grey scale, only using the R chanel of the input parameters internally. The lighting will still be colored. This is an optimisation.

### bRayMarchVolumeShadow
- **类型**: `bool`
- **描述**: Disable this to use the cloud shadow map instead of secondary raymarching. This is usually enough for clouds viewed from the ground and it result in a performance boost. Shadow now have infinite length but also becomes less accurate and gray scale.

### bClampMultiScatteringContribution
- **类型**: `bool`
- **描述**: Set whether multiple scattering contribution entry is clamped in [0,1] or not. When disabled, the artist is in charge for ensuring the visual remain in a reasonable brighness range.


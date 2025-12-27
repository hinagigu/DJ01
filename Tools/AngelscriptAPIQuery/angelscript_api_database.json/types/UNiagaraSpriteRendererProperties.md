# UNiagaraSpriteRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### Material
- **类型**: `UMaterialInterface`
- **描述**: The material used to render the particle. Note that it must have the Use with Niagara Sprites flag checked.

### MaterialUserParamBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Use the UMaterialInterface bound to this user variable if it is set to a valid value. If this is bound to a valid value and Material is also set, UserParamBinding wins.

### SourceMode
- **类型**: `ENiagaraRendererSourceDataMode`
- **描述**: Whether or not to draw a single element for the Emitter or to draw the particles.

### Alignment
- **类型**: `ENiagaraSpriteAlignment`
- **描述**: Imagine the particle texture having an arrow pointing up, these modes define how the particle aligns that texture to other particle attributes.

### FacingMode
- **类型**: `ENiagaraSpriteFacingMode`
- **描述**: Determines how the particle billboard orients itself relative to the camera.

### SortMode
- **类型**: `ENiagaraSortMode`
- **描述**: Determines how we sort the particles prior to rendering.

### MacroUVRadius
- **类型**: `float32`
- **描述**: World space radius that UVs generated with the ParticleMacroUV material node will tile based on.

### PivotInUVSpace
- **类型**: `FVector2D`
- **描述**: Determines the location of the pivot point of this particle. It follows Unreal's UV space, which has the upper left of the image at 0,0 and bottom right at 1,1. The middle is at 0.5, 0.5.
NOTE: This value is ignored if "Pivot Offset Binding" is bound to a valid attribute

### SubImageSize
- **类型**: `FVector2D`
- **描述**: When using SubImage lookups for particles, this variable contains the number of columns in X and the number of rows in Y.

### SortPrecision
- **类型**: `ENiagaraRendererSortPrecision`
- **描述**: Sort precision to use when sorting is active.

### GpuTranslucentLatency
- **类型**: `ENiagaraRendererGpuTranslucentLatency`
- **描述**: Gpu simulations run at different points in the frame depending on what features are used, i.e. depth buffer, distance fields, etc.
Opaque materials will run latent when these features are used.
Translucent materials can choose if they want to use this frames or the previous frames data to match opaque draws.

### PixelCoverageMode
- **类型**: `ENiagaraRendererPixelCoverageMode`
- **描述**: This setting controls what happens when a sprite becomes less than a pixel in size.
Disabling will apply nothing and can result in flickering issues, especially with Temporal Super Resolution.
Automatic will enable the appropriate settings when the material blend mode is some form of translucency, project setting must also be enabled.
When coverage is less than a pixel, we also calculate a percentage of coverage, and then darken or reduce opacity
to visually compensate. The different enabled settings allow you to control how the coverage amount is applied to
your particle color.  If particle color is not connected to your material the compensation will not be applied.

### PixelCoverageBlend
- **类型**: `float32`
- **描述**: When pixel coverage is enabled this allows you to control the blend of the pixel coverage color adjustment.
i.e. 1.0 = full, 0.5 = 50/50 blend, 0.0 = none

### MinFacingCameraBlendDistance
- **类型**: `float32`
- **描述**: When FacingMode is FacingCameraDistanceBlend, the distance at which the sprite is fully facing the camera plane.

### MaxFacingCameraBlendDistance
- **类型**: `float32`
- **描述**: When FacingMode is FacingCameraDistanceBlend, the distance at which the sprite is fully facing the camera position

### MinCameraDistance
- **类型**: `float32`

### MaxCameraDistance
- **类型**: `float32`

### RendererVisibility
- **类型**: `uint`
- **描述**: If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.

### MaterialParameters
- **类型**: `FNiagaraRendererMaterialParameters`
- **描述**: If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.

### bUseMaterialCutoutTexture
- **类型**: `bool`

### CutoutTexture
- **类型**: `UTexture2D`
- **描述**: Texture to generate bounding geometry from.

### BoundingMode
- **类型**: `ESubUVBoundingVertexCount`
- **描述**: More bounding vertices results in reduced overdraw, but adds more triangle overhead.
The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,
and when the particles using the texture will be few and large.

### OpacitySourceMode
- **类型**: `EOpacitySourceMode`

### AlphaThreshold
- **类型**: `float32`
- **描述**: Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.
Raising this threshold slightly can reduce overdraw in particles using this animation asset.

### bSubImageBlend
- **类型**: `bool`

### bRemoveHMDRollInVR
- **类型**: `bool`

### bSortOnlyWhenTranslucent
- **类型**: `bool`

### bEnableCameraDistanceCulling
- **类型**: `bool`

### bCastShadows
- **类型**: `bool`


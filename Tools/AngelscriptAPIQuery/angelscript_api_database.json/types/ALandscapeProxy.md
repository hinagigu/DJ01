# ALandscapeProxy

**继承自**: `APartitionActor`

## 属性

### bEnableNanite
- **类型**: `bool`

### PerLODOverrideMaterials
- **类型**: `TArray<FLandscapePerLODMaterialOverride>`

### NaniteLODIndex
- **类型**: `int`
- **描述**: LOD level of the landscape when generating the Nanite mesh. Mostly there for debug reasons, since Nanite is meant to allow high density meshes, we want to use 0 most of the times.

### bNaniteSkirtEnabled
- **类型**: `bool`

### NaniteSkirtDepth
- **类型**: `float32`

### NanitePositionPrecision
- **类型**: `int`

### NaniteMaxEdgeLengthFactor
- **类型**: `float32`

### MaxLODLevel
- **类型**: `int`
- **描述**: Max LOD level to use when rendering, -1 means the max available

### LOD0ScreenSize
- **类型**: `float32`
- **描述**: This is the starting screen size used to calculate the distribution. You can increase the value if you want less LOD0 component, and you use very large landscape component.

### LODGroupKey
- **类型**: `uint`
- **描述**: Specifies the LOD Group (Zero is No Group). All landscapes in the same group calculate their LOD together, allowing matching border LODs to fix geometry seams.

### LOD0DistributionSetting
- **类型**: `float32`
- **描述**: The distribution setting used to change the LOD 0 generation, 1.25 is the normal distribution, numbers influence directly the LOD0 proportion on screen.

### LODDistributionSetting
- **类型**: `float32`
- **描述**: The distribution setting used to change the LOD generation, 3 is the normal distribution, small number mean you want your last LODs to take more screen space and big number mean you want your first LODs to take more screen space.

### ScalableLOD0ScreenSize
- **类型**: `FPerQualityLevelFloat`
- **描述**: Scalable (per-quality) version of 'LOD 0 Screen Size'.

### ScalableLOD0DistributionSetting
- **类型**: `FPerQualityLevelFloat`
- **描述**: Scalable (per-quality) version of 'LOD 0'.

### ScalableLODDistributionSetting
- **类型**: `FPerQualityLevelFloat`
- **描述**: Scalable (per-quality) version of 'Other LODs'.

### bUseScalableLODSettings
- **类型**: `bool`
- **描述**: Allows to specify LOD distribution settings per quality level. Using this will ignore the r.LandscapeLOD0DistributionScale CVar.

### LODBlendRange
- **类型**: `float32`
- **描述**: This controls the area that blends LOD between neighboring sections. At 1.0 it blends across the entire section, and lower numbers reduce the blend region to be closer to the boundary.

### ExportLOD
- **类型**: `int`
- **描述**: LOD level to use when exporting the landscape to obj or FBX

### StaticLightingLOD
- **类型**: `int`
- **描述**: LOD level to use when running lightmass (increase to 1 or 2 for large landscapes to stop lightmass crashing)

### DefaultPhysMaterial
- **类型**: `UPhysicalMaterial`
- **描述**: Default physical material, used when no per-layer values physical materials

### StreamingDistanceMultiplier
- **类型**: `float32`
- **描述**: Allows artists to adjust the distance where textures using UV 0 are streamed in/out.
1.0 is the default, whereas a higher value increases the streamed-in resolution.
Value can be < 0 (from legcay content, or code changes)

### LandscapeHoleMaterial
- **类型**: `UMaterialInterface`
- **描述**: Material used to render landscape components with holes. If not set, LandscapeMaterial will be used (blend mode will be overridden to Masked if it is set to Opaque)

### RuntimeVirtualTextures
- **类型**: `TArray<TObjectPtr<URuntimeVirtualTexture>>`

### bVirtualTextureRenderWithQuad
- **类型**: `bool`

### bVirtualTextureRenderWithQuadHQ
- **类型**: `bool`

### VirtualTextureNumLods
- **类型**: `int`

### VirtualTextureLodBias
- **类型**: `int`

### NegativeZBoundsExtension
- **类型**: `float32`
- **描述**: Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example
Extension value in the negative Z axis, positive value increases bound size
Note that this can also be overridden per-component when the component is selected with the component select tool

### PositiveZBoundsExtension
- **类型**: `float32`
- **描述**: Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example
Extension value in the positive Z axis, positive value increases bound size
Note that this can also be overridden per-component when the component is selected with the component select tool

### StaticLightingResolution
- **类型**: `float32`
- **描述**: The resolution to cache lighting at, in texels/quad in one axis
Total resolution would be changed by StaticLightingResolution*StaticLightingResolution
Automatically calculate proper value for removing seams

### ShadowCacheInvalidationBehavior
- **类型**: `EShadowCacheInvalidationBehavior`

### LightingChannels
- **类型**: `FLightingChannels`

### NonNaniteVirtualShadowMapConstantDepthBias
- **类型**: `float32`
- **描述**: Constant bias to handle the worst artifacts of the continuous LOD morphing when rendering to VSM.
Only applies when using non-Nanite landscape and VSM.

### NonNaniteVirtualShadowMapInvalidationHeightErrorThreshold
- **类型**: `float32`
- **描述**: For non-Nanite landscape, cached VSM pages need to be invalidated when continuous LOD morphing introduces a height difference that is too large between the current landscape component's profile and the one that was used when the shadow was shadow was last cached.
This height threshold (in Unreal units) controls this invalidation rate (a smaller threshold will reduce the likeliness of shadow artifacts, but will make the invalidations occur more frequently, which is not desirable in terms of performance.
Disabled if 0.0.
Only applies when using non-Nanite landscape and VSM.

### NonNaniteVirtualShadowMapInvalidationScreenSizeLimit
- **类型**: `float32`
- **描述**: Screen size under which VSM invalidation stops occurring.
As the height difference between 2 mip levels increases when the LOD level increases (because of undersampling), VSM pages tend to be invalidated more frequently even though it's getting less and less relevant to do so, since this will mean that the screen size of the landscape section decreases, thus the artifacts actually become less noticeable.
We therefore artificially attenuate the VSM invalidation rate as the screen size decreases, to avoid invalidating VSM pages too often, as it becomes less and less impactful.
A higher value will accentuate this attenuation (better performance but more artifacts) and vice versa.
If 0.0, the attenuation of the VSM invalidation rate will be disabled entirely.
Only applies when using non-Nanite landscape and VSM.

### CustomDepthStencilWriteMask
- **类型**: `ERendererStencilMask`

### CustomDepthStencilValue
- **类型**: `int`

### LDMaxDrawDistance
- **类型**: `float32`

### LightmassSettings
- **类型**: `FLightmassPrimitiveSettings`
- **描述**: The Lightmass settings for this object.

### CollisionMipLevel
- **类型**: `int`
- **描述**: Landscape LOD to use for collision tests. Higher numbers use less memory and process faster, but are much less accurate

### SimpleCollisionMipLevel
- **类型**: `int`
- **描述**: If set higher than the "Collision Mip Level", this specifies the Landscape LOD to use for "simple collision" tests, otherwise the "Collision Mip Level" is used for both simple and complex collision.
Does not work with an XY offset map (mesh collision)

### BodyInstance
- **类型**: `FBodyInstance`

### NavigationGeometryGatheringMode
- **类型**: `ENavDataGatheringMode`

### bUseDynamicMaterialInstance
- **类型**: `bool`
- **描述**: When set to true it will generate MaterialInstanceDynamic for each components, so material can be changed at runtime

### MaxPaintedLayersPerComponent
- **类型**: `int`

### bUseLandscapeForCullingInvisibleHLODVertices
- **类型**: `bool`
- **描述**: Flag whether or not this Landscape's surface can be used for culling hidden triangles *

### HLODTextureSizePolicy
- **类型**: `ELandscapeHLODTextureSizePolicy`
- **描述**: Specify how to choose the texture size of the resulting HLOD mesh

### HLODTextureSize
- **类型**: `int`
- **描述**: Specify the texture size to use for the HLOD mesh if HLODTextureSizePolicy is set to SpecificSize

### HLODMeshSourceLODPolicy
- **类型**: `ELandscapeHLODMeshSourceLODPolicy`
- **描述**: Specify how to choose the LOD used as input for the HLOD mesh

### HLODMeshSourceLOD
- **类型**: `int`
- **描述**: Specify which LOD to use for the HLOD mesh if HLODMeshSourceLODPolicy is set to SpecificLOD

### bUseCompressedHeightmapStorage
- **类型**: `bool`
- **描述**: Enable compressed heightmap texture storage.

### bStripPhysicsWhenCookedClient
- **类型**: `bool`
- **描述**: Strip Physics/collision components when cooked for client

### bStripPhysicsWhenCookedServer
- **类型**: `bool`
- **描述**: Strip Physics/collision components when cooked for server

### bStripGrassWhenCookedClient
- **类型**: `bool`
- **描述**: Strip Grass data when cooked for client

### bStripGrassWhenCookedServer
- **类型**: `bool`
- **描述**: Strip Grass data when cooked for server

### LandscapeMaterial
- **类型**: `UMaterialInterface`

### VirtualTextureRenderPassType
- **类型**: `ERuntimeVirtualTextureMainPassType`

### CastShadow
- **类型**: `bool`

### bCastDynamicShadow
- **类型**: `bool`

### bCastStaticShadow
- **类型**: `bool`

### bCastContactShadow
- **类型**: `bool`

### bCastFarShadow
- **类型**: `bool`

### bCastHiddenShadow
- **类型**: `bool`

### bCastShadowAsTwoSided
- **类型**: `bool`

### bAffectDistanceFieldLighting
- **类型**: `bool`

### bUseMaterialPositionOffsetInStaticLighting
- **类型**: `bool`

### bRenderCustomDepth
- **类型**: `bool`

### bGenerateOverlapEvents
- **类型**: `bool`

### bBakeMaterialPositionOffsetIntoCollision
- **类型**: `bool`

### bUsedForNavigation
- **类型**: `bool`

### bFillCollisionUnderLandscapeForNavmesh
- **类型**: `bool`

## 方法

### GetHeightAtLocation
```angelscript
bool GetHeightAtLocation(FVector Location, float32& OutHeight)
```

### DeleteUnusedLayers
```angelscript
void DeleteUnusedLayers()
```
Delete all unused layers in components. Warning: any update of the component could re-introduce them.

### EditorApplySpline
```angelscript
void EditorApplySpline(USplineComponent InSplineComponent, float32 StartWidth, float32 EndWidth, float32 StartSideFalloff, float32 EndSideFalloff, float32 StartRoll, float32 EndRoll, int NumSubdivisions, bool bRaiseHeights, bool bLowerHeights, ULandscapeLayerInfoObject PaintLayer, FName EditLayerName)
```
Deform landscape using a given spline
@param InSplineComponent - The component containing the spline data
@param StartWidth - Width of the spline at the start node, in Spline Component local space
@param EndWidth   - Width of the spline at the end node, in Spline Component local space
@param StartSideFalloff - Width of the falloff at either side of the spline at the start node, in Spline Component local space
@param EndSideFalloff - Width of the falloff at either side of the spline at the end node, in Spline Component local space
@param StartRoll - Roll applied to the spline at the start node, in degrees. 0 is flat
@param EndRoll - Roll applied to the spline at the end node, in degrees. 0 is flat
@param NumSubdivisions - Number of triangles to place along the spline when applying it to the landscape. Higher numbers give better results, but setting it too high will be slow and may cause artifacts
@param bRaiseHeights - Allow the landscape to be raised up to the level of the spline. If both bRaiseHeights and bLowerHeights are false, no height modification of the landscape will be performed
@param bLowerHeights - Allow the landscape to be lowered down to the level of the spline. If both bRaiseHeights and bLowerHeights are false, no height modification of the landscape will be performed
@param PaintLayer - LayerInfo to paint, or none to skip painting. The landscape must be configured with the same layer info in one of its layers or this will do nothing!
@param EditLayerName - Name of the landscape edit layer to affect (in Edit Layers mode)

### EditorSetLandscapeMaterial
```angelscript
void EditorSetLandscapeMaterial(UMaterialInterface NewLandscapeMaterial)
```
Setter for LandscapeMaterial. Has no effect outside the editor.

### GetLandscapeActor
```angelscript
ALandscape GetLandscapeActor()
```

### LandscapeExportHeightmapToRenderTarget
```angelscript
bool LandscapeExportHeightmapToRenderTarget(UTextureRenderTarget2D InRenderTarget, bool InExportHeightIntoRGChannel, bool InExportLandscapeProxies)
```
Output a landscape heightmap to a render target
@param InRenderTarget - Valid render target with a format of RTF_RGBA16f, RTF_RGBA32f or RTF_RGBA8
@param InExportHeightIntoRGChannel - Tell us if we should export the height that is internally stored as R & G (for 16 bits) to a single R channel of the render target (the format need to be RTF_RGBA16f or RTF_RGBA32f)
                                                                         Note that using RTF_RGBA16f with InExportHeightIntoRGChannel == false, could have precision loss.
@param InExportLandscapeProxies - Option to also export components of all proxies of Landscape actor (if LandscapeProxy is the Landscape Actor)

### LandscapeExportWeightmapToRenderTarget
```angelscript
bool LandscapeExportWeightmapToRenderTarget(UTextureRenderTarget2D InRenderTarget, FName InLayerName)
```
Output a landscape weightmap to a render target
Only works in the editor

### LandscapeImportHeightmapFromRenderTarget
```angelscript
bool LandscapeImportHeightmapFromRenderTarget(UTextureRenderTarget2D InRenderTarget, bool InImportHeightFromRGChannel)
```
Overwrites a landscape heightmap with render target data
@param InRenderTarget - Valid render target with a format of RTF_RGBA16f, RTF_RGBA32f or RTF_RGBA8
@param InImportHeightFromRGChannel - Only relevant when using format RTF_RGBA16f or RTF_RGBA32f, and will tell us if we should import the height data from the R channel only of the Render target or from R & G.
                                                                         Note that using RTF_RGBA16f with InImportHeightFromRGChannel == false, could have precision loss
Only works in the editor

### LandscapeImportWeightmapFromRenderTarget
```angelscript
bool LandscapeImportWeightmapFromRenderTarget(UTextureRenderTarget2D InRenderTarget, FName InLayerName)
```
Overwrites a landscape weightmap with render target data
Only works in the editor

### SetLandscapeMaterialScalarParameterValue
```angelscript
void SetLandscapeMaterialScalarParameterValue(FName ParameterName, float32 Value)
```
Set a MID scalar (float) parameter value for all landscape components.

### SetLandscapeMaterialTextureParameterValue
```angelscript
void SetLandscapeMaterialTextureParameterValue(FName ParameterName, UTexture Value)
```
Set an MID texture parameter value for all landscape components.

### SetLandscapeMaterialVectorParameterValue
```angelscript
void SetLandscapeMaterialVectorParameterValue(FName ParameterName, FLinearColor Value)
```
Set an MID vector parameter value for all landscape components.

### SetVirtualTextureRenderPassType
```angelscript
void SetVirtualTextureRenderPassType(ERuntimeVirtualTextureMainPassType InType)
```


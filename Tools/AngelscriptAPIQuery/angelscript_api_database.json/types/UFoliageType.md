# UFoliageType

**继承自**: `UObject`

## 属性

### Density
- **类型**: `float32`
- **描述**: Foliage instances will be placed at this density, specified in instances per 1000x1000 unit area

### DensityAdjustmentFactor
- **类型**: `float32`
- **描述**: The factor by which to adjust the density of instances. Values >1 will increase density while values <1 will decrease it.

### Radius
- **类型**: `float32`
- **描述**: The minimum distance between foliage instances

### bSingleInstanceModeOverrideRadius
- **类型**: `bool`
- **描述**: Option to override radius used to detect collision with other instances when painting in single instance mode

### SingleInstanceModeRadius
- **类型**: `float32`
- **描述**: The radius used in single instance mode to detect collision with other instances

### Scaling
- **类型**: `EFoliageScaling`
- **描述**: Specifies foliage instance scaling behavior when painting.

### ScaleX
- **类型**: `FFloatInterval`
- **描述**: Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's X Scale property

### ScaleY
- **类型**: `FFloatInterval`
- **描述**: Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Y Scale property

### ScaleZ
- **类型**: `FFloatInterval`
- **描述**: Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Z Scale property

### VertexColorMaskByChannel
- **类型**: `FFoliageVertexColorChannelMask`

### ZOffset
- **类型**: `FFloatInterval`

### AlignMaxAngle
- **类型**: `float32`

### RandomPitchAngle
- **类型**: `float32`

### GroundSlopeAngle
- **类型**: `FFloatInterval`

### Height
- **类型**: `FFloatInterval`

### LandscapeLayers
- **类型**: `TArray<FName>`

### MinimumLayerWeight
- **类型**: `float32`

### ExclusionLandscapeLayers
- **类型**: `TArray<FName>`

### MinimumExclusionLayerWeight
- **类型**: `float32`

### CollisionScale
- **类型**: `FVector`

### AverageNormalSampleCount
- **类型**: `int`

### Mobility
- **类型**: `EComponentMobility`

### CullDistance
- **类型**: `FInt32Interval`
- **描述**: The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables.
When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all.

### ShadowCacheInvalidationBehavior
- **类型**: `EShadowCacheInvalidationBehavior`

### OverriddenLightMapRes
- **类型**: `int`

### LightmapType
- **类型**: `ELightmapType`

### WorldPositionOffsetDisableDistance
- **类型**: `int`

### BodyInstance
- **类型**: `FBodyInstance`
- **描述**: Custom collision for foliage

### CustomNavigableGeometry
- **类型**: `EHasCustomNavigableGeometry`
- **描述**: Force navmesh

### LightingChannels
- **类型**: `FLightingChannels`

### CustomDepthStencilWriteMask
- **类型**: `ERendererStencilMask`

### CustomDepthStencilValue
- **类型**: `int`

### TranslucencySortPriority
- **类型**: `int`

### CollisionRadius
- **类型**: `float32`
- **描述**: The CollisionRadius determines when two instances overlap. When two instances overlap a winner will be picked based on rules and priority.

### ShadeRadius
- **类型**: `float32`
- **描述**: The ShadeRadius determines when two instances overlap. If an instance can grow in the shade this radius is ignored.

### NumSteps
- **类型**: `int`
- **描述**: The number of times we age the species and spread its seeds.

### InitialSeedDensity
- **类型**: `float32`
- **描述**: Specifies the number of seeds to populate along 10 meters. The number is implicitly squared to cover a 10m x 10m area

### AverageSpreadDistance
- **类型**: `float32`
- **描述**: The average distance between the spreading instance and its seeds. For example, a tree with an AverageSpreadDistance 10 will ensure the average distance between the tree and its seeds is 10cm

### SpreadVariance
- **类型**: `float32`
- **描述**: Specifies how much seed distance varies from the average. For example, a tree with an AverageSpreadDistance 10 and a SpreadVariance 1 will produce seeds with an average distance of 10cm plus or minus 1cm

### SeedsPerStep
- **类型**: `int`
- **描述**: The number of seeds an instance will spread in a single step of the simulation.

### DistributionSeed
- **类型**: `int`
- **描述**: The seed that determines placement of initial seeds.

### MaxInitialSeedOffset
- **类型**: `float32`
- **描述**: The seed that determines placement of initial seeds.

### bCanGrowInShade
- **类型**: `bool`
- **描述**: If true, seeds of this type will ignore shade radius during overlap tests with other types.

### bSpawnsInShade
- **类型**: `bool`
- **描述**: Whether new seeds are spawned exclusively in shade. Occurs in a second pass after all types that do not spawn in shade have been simulated.
Only valid when CanGrowInShade is true.

### MaxInitialAge
- **类型**: `float32`
- **描述**: Allows a new seed to be older than 0 when created. New seeds will be randomly assigned an age in the range [0,MaxInitialAge]

### MaxAge
- **类型**: `float32`
- **描述**: Specifies the oldest a seed can be. After reaching this age the instance will still spread seeds, but will not get any older

### OverlapPriority
- **类型**: `float32`
- **描述**: When two instances overlap we must determine which instance to remove.
The instance with a lower OverlapPriority will be removed.
In the case where OverlapPriority is the same regular simulation rules apply.

### ProceduralScale
- **类型**: `FFloatInterval`
- **描述**: The scale range of this type when being procedurally generated. Configured with the Scale Curve.

### ScaleCurve
- **类型**: `FRuntimeFloatCurve`
- **描述**: Instance scale factor as a function of normalized age (i.e. Current Age / Max Age).
X = 0 corresponds to Age = 0, X = 1 corresponds to Age = Max Age.
Y = 0 corresponds to Min Scale, Y = 1 corresponds to Max Scale.

### DensityFalloff
- **类型**: `FFoliageDensityFalloff`

### RuntimeVirtualTextures
- **类型**: `TArray<TObjectPtr<URuntimeVirtualTexture>>`

### VirtualTextureCullMips
- **类型**: `int`

### VirtualTextureRenderPassType
- **类型**: `ERuntimeVirtualTextureMainPassType`

### AlignToNormal
- **类型**: `bool`

### AverageNormal
- **类型**: `bool`

### AverageNormalSingleComponent
- **类型**: `bool`

### RandomYaw
- **类型**: `bool`

### CollisionWithWorld
- **类型**: `bool`

### CastShadow
- **类型**: `bool`

### bAffectDynamicIndirectLighting
- **类型**: `bool`

### bAffectDistanceFieldLighting
- **类型**: `bool`

### bCastDynamicShadow
- **类型**: `bool`

### bCastStaticShadow
- **类型**: `bool`

### bCastContactShadow
- **类型**: `bool`

### bCastShadowAsTwoSided
- **类型**: `bool`

### bReceivesDecals
- **类型**: `bool`

### bOverrideLightMapRes
- **类型**: `bool`

### bUseAsOccluder
- **类型**: `bool`

### bVisibleInRayTracing
- **类型**: `bool`

### bEvaluateWorldPositionOffset
- **类型**: `bool`

### bRenderCustomDepth
- **类型**: `bool`

### ReapplyDensity
- **类型**: `bool`

### ReapplyRadius
- **类型**: `bool`

### ReapplyAlignToNormal
- **类型**: `bool`

### ReapplyRandomYaw
- **类型**: `bool`

### ReapplyScaling
- **类型**: `bool`

### ReapplyScaleX
- **类型**: `bool`

### ReapplyScaleY
- **类型**: `bool`

### ReapplyScaleZ
- **类型**: `bool`

### ReapplyRandomPitchAngle
- **类型**: `bool`

### ReapplyGroundSlope
- **类型**: `bool`

### ReapplyHeight
- **类型**: `bool`

### ReapplyLandscapeLayers
- **类型**: `bool`

### ReapplyZOffset
- **类型**: `bool`

### ReapplyCollisionWithWorld
- **类型**: `bool`

### ReapplyVertexColorMask
- **类型**: `bool`

### bEnableDensityScaling
- **类型**: `bool`

### bEnableDiscardOnLoad
- **类型**: `bool`

### bEnableCullDistanceScaling
- **类型**: `bool`

### bIncludeInHLOD
- **类型**: `bool`


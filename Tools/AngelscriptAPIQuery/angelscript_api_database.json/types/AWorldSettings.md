# AWorldSettings

**继承自**: `AInfo`

Actor containing all script accessible world properties.

## 属性

### VisibilityCellSize
- **类型**: `int`
- **描述**: World space size of precomputed visibility cells in x and y.
Smaller sizes produce more effective occlusion culling at the cost of increased runtime memory usage and lighting build times.

### VisibilityAggressiveness
- **类型**: `EVisibilityAggressiveness`
- **描述**: Determines how aggressive precomputed visibility should be.
More aggressive settings cull more objects but also cause more visibility errors like popping.

### AISystemClass
- **类型**: `TSoftClassPtr<UAISystemBase>`

### NavigationSystemConfig
- **类型**: `UNavigationSystemConfig`

### WorldPartition
- **类型**: `UWorldPartition`

### InstancedFoliageGridSize
- **类型**: `uint`
- **描述**: Size of the grid for instanced foliage actors, only used for partitioned worlds

### bShowInstancedFoliageGrid
- **类型**: `bool`

### LandscapeSplineMeshesGridSize
- **类型**: `uint`

### NavigationDataChunkGridSize
- **类型**: `uint`
- **描述**: Size of the grid for navigation data chunk actors

### NavigationDataBuilderLoadingCellSize
- **类型**: `uint`
- **描述**: Loading cell size used when building navigation data iteratively.
The actual cell size used will be rounded using the NavigationDataChunkGridSize.
It's recommended to use a value as high as the hardware memory allows to load.

### BaseNavmeshDataLayers
- **类型**: `TArray<TObjectPtr<UDataLayerAsset>>`
- **描述**: A list of runtime data layers that should be included in the base navmesh.
Editor data layers and actors outside data layers will be included.

### WorldToMeters
- **类型**: `float32`

### KillZ
- **类型**: `float32`

### KillZDamageType
- **类型**: `TSubclassOf<UDamageType>`

### GlobalGravityZ
- **类型**: `float32`

### DefaultPhysicsVolumeClass
- **类型**: `TSubclassOf<ADefaultPhysicsVolume>`

### PhysicsCollisionHandlerClass
- **类型**: `TSubclassOf<UPhysicsCollisionHandler>`

### DefaultGameMode
- **类型**: `TSubclassOf<AGameModeBase>`

### PackedLightAndShadowMapTextureSize
- **类型**: `int`
- **描述**: Maximum size of textures for packed light and shadow maps

### DefaultColorScale
- **类型**: `FVector`

### DefaultMaxDistanceFieldOcclusionDistance
- **类型**: `float32`
- **描述**: Max occlusion distance used by mesh distance fields, overridden if there is a movable skylight.

### GlobalDistanceFieldViewDistance
- **类型**: `float32`
- **描述**: Distance from the camera that the global distance field should cover.

### DynamicIndirectShadowsSelfShadowingIntensity
- **类型**: `float32`
- **描述**: Controls the intensity of self-shadowing from capsule indirect shadows.
These types of shadows use approximate occluder representations, so reducing self-shadowing intensity can hide those artifacts.

### LightmassSettings
- **类型**: `FLightmassWorldInfoSettings`

### NaniteSettings
- **类型**: `FNaniteSettings`
- **描述**: NANITE SETTINGS *

### DefaultReverbSettings
- **类型**: `FReverbSettings`
- **描述**: Default reverb settings used by audio volumes.

### DefaultAmbientZoneSettings
- **类型**: `FInteriorSettings`
- **描述**: Default interior settings applied to sounds that have "apply ambient volumes" set to true on their SoundClass.

### DefaultBaseSoundMix
- **类型**: `USoundMix`
- **描述**: Default Base SoundMix.

### HLODSetupAsset
- **类型**: `TSoftClassPtr<UHierarchicalLODSetup>`
- **描述**: If set overrides the level settings and global project settings

### OverrideBaseMaterial
- **类型**: `TSoftObjectPtr<UMaterialInterface>`
- **描述**: If set overrides the project-wide base material used for Proxy Materials

### HierarchicalLODSetup
- **类型**: `TArray<FHierarchicalSimplification>`
- **描述**: Hierarchical LOD Setup

### HLODBakingTransform
- **类型**: `FTransform`
- **描述**: Specify the transform to apply to the source meshes when building HLODs.

### BookMarks
- **类型**: `UBookMark`

### MinGlobalTimeDilation
- **类型**: `float32`
- **描述**: Lowest acceptable global time dilation.

### MaxGlobalTimeDilation
- **类型**: `float32`
- **描述**: Highest acceptable global time dilation.

### MinUndilatedFrameTime
- **类型**: `float32`
- **描述**: Smallest possible frametime, not considering dilation. Equiv to 1/FastestFPS.

### MaxUndilatedFrameTime
- **类型**: `float32`
- **描述**: Largest possible frametime, not considering dilation. Equiv to 1/SlowestFPS.

### BroadphaseSettings
- **类型**: `FBroadphaseSettings`

### bPrecomputeVisibility
- **类型**: `bool`

### bPlaceCellsOnlyAlongCameraTracks
- **类型**: `bool`

### bEnableWorldBoundsChecks
- **类型**: `bool`

### bEnableNavigationSystem
- **类型**: `bool`

### bEnableAISystem
- **类型**: `bool`

### bEnableWorldComposition
- **类型**: `bool`

### bUseClientSideLevelStreamingVolumes
- **类型**: `bool`

### bEnableWorldOriginRebasing
- **类型**: `bool`

### bGlobalGravitySet
- **类型**: `bool`

### bMinimizeBSPSections
- **类型**: `bool`

### bForceNoPrecomputedLighting
- **类型**: `bool`

### bOverrideDefaultBroadphaseSettings
- **类型**: `bool`

### bGenerateSingleClusterForLevel
- **类型**: `bool`

### bHideEnableStreamingWarning
- **类型**: `bool`

### bReuseAddressAndPort
- **类型**: `bool`


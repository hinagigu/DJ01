# FISMComponentDescriptor

## 属性

### StaticMesh
- **类型**: `UStaticMesh`

### OverrideMaterials
- **类型**: `TArray<TObjectPtr<UMaterialInterface>>`

### OverlayMaterial
- **类型**: `UMaterialInterface`

### RuntimeVirtualTextures
- **类型**: `TArray<TObjectPtr<URuntimeVirtualTexture>>`

### ComponentClass
- **类型**: `TSubclassOf<UInstancedStaticMeshComponent>`

### Mobility
- **类型**: `EComponentMobility`

### VirtualTextureRenderPassType
- **类型**: `ERuntimeVirtualTextureMainPassType`

### LightmapType
- **类型**: `ELightmapType`

### LightingChannels
- **类型**: `FLightingChannels`

### RayTracingGroupId
- **类型**: `int`

### RayTracingGroupCullingPriority
- **类型**: `ERayTracingGroupCullingPriority`

### bHasCustomNavigableGeometry
- **类型**: `EHasCustomNavigableGeometry`

### CustomDepthStencilWriteMask
- **类型**: `ERendererStencilMask`

### BodyInstance
- **类型**: `FBodyInstance`

### InstanceStartCullDistance
- **类型**: `int`

### InstanceEndCullDistance
- **类型**: `int`

### InstanceLODDistanceScale
- **类型**: `float32`

### VirtualTextureCullMips
- **类型**: `int`

### TranslucencySortPriority
- **类型**: `int`

### OverriddenLightMapRes
- **类型**: `int`

### CustomDepthStencilValue
- **类型**: `int`

### HLODBatchingPolicy
- **类型**: `EHLODBatchingPolicy`

### WorldPositionOffsetDisableDistance
- **类型**: `int`

### ShadowCacheInvalidationBehavior
- **类型**: `EShadowCacheInvalidationBehavior`

### DetailMode
- **类型**: `EDetailMode`

### bCastShadow
- **类型**: `bool`

### bEmissiveLightSource
- **类型**: `bool`

### bCastDynamicShadow
- **类型**: `bool`

### bCastStaticShadow
- **类型**: `bool`

### bCastContactShadow
- **类型**: `bool`

### bCastShadowAsTwoSided
- **类型**: `bool`

### bCastHiddenShadow
- **类型**: `bool`

### bAffectDynamicIndirectLighting
- **类型**: `bool`

### bAffectDynamicIndirectLightingWhileHidden
- **类型**: `bool`

### bAffectDistanceFieldLighting
- **类型**: `bool`

### bReceivesDecals
- **类型**: `bool`

### bOverrideLightMapRes
- **类型**: `bool`

### bUseAsOccluder
- **类型**: `bool`

### bEnableDensityScaling
- **类型**: `bool`

### bEnableDiscardOnLoad
- **类型**: `bool`

### bRenderCustomDepth
- **类型**: `bool`

### bVisibleInRayTracing
- **类型**: `bool`

### bHiddenInGame
- **类型**: `bool`

### bIsEditorOnly
- **类型**: `bool`

### bVisible
- **类型**: `bool`

### bEvaluateWorldPositionOffset
- **类型**: `bool`

### bReverseCulling
- **类型**: `bool`

### bUseGpuLodSelection
- **类型**: `bool`

### bIncludeInHLOD
- **类型**: `bool`

### bConsiderForActorPlacementWhenHidden
- **类型**: `bool`

### bUseDefaultCollision
- **类型**: `bool`

### bGenerateOverlapEvents
- **类型**: `bool`

### bOverrideNavigationExport
- **类型**: `bool`

### bForceNavigationObstacle
- **类型**: `bool`

### bFillCollisionUnderneathForNavmesh
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FISMComponentDescriptor& opAssign(FISMComponentDescriptor Other)
```


# UNiagaraSystem

**继承自**: `UFXSystemAsset`

A Niagara System contains multiple Niagara Emitters to create various effects.
Niagara Systems can be placed in the world, unlike Emitters, and expose User Parameters to configure an effect at runtime.

## 属性

### TemplateAssetDescription
- **类型**: `FText`

### CustomDepthStencilWriteMask
- **类型**: `ERendererStencilMask`

### CustomDepthStencilValue
- **类型**: `int`

### TranslucencySortPriority
- **类型**: `int`

### TranslucencySortDistanceOffset
- **类型**: `float32`

### bDumpDebugSystemInfo
- **类型**: `bool`

### bDumpDebugEmitterInfo
- **类型**: `bool`

### bRequireCurrentFrameData
- **类型**: `bool`
- **描述**: When enabled, we follow the settings on the UNiagaraComponent for tick order. When this option is disabled, we ignore any dependencies from data interfaces or other variables and instead fire off the simulation as early in the frame as possible. This greatly
      reduces overhead and allows the game thread to run faster, but comes at a tradeoff if the dependencies might leave gaps or other visual artifacts.

### EffectType
- **类型**: `UNiagaraEffectType`
- **描述**: An effect types defines settings shared between systems, for example scalability and validation rules.
Things like environment fx usually have a different effect type than gameplay relevant fx such as weapon impacts.
This way whole classes of effects can be adjusted at once.

### bOverrideScalabilitySettings
- **类型**: `bool`

### SystemScalabilityOverrides
- **类型**: `FNiagaraSystemScalabilityOverrides`

### Platforms
- **类型**: `FNiagaraPlatformSet`

### ParameterCollectionOverrides
- **类型**: `TArray<TObjectPtr<UNiagaraParameterCollectionInstance>>`

### FixedBounds
- **类型**: `FBox`
- **描述**: The fixed bounding box value for the whole system. When placed in the level and the bounding box is not visible to the camera, the effect is culled from rendering.

### bDeterminism
- **类型**: `bool`
- **描述**: When disabled we will generate a RandomSeed per instance on reset which is not deterministic.
When enabled we will always use the RandomSeed from the system plus the components RandomSeedOffset, this allows for determinism but variance between components.

### RandomSeed
- **类型**: `int`
- **描述**: Seed used for system script random number generator.

### WarmupTime
- **类型**: `float32`
- **描述**: Warm up time in seconds. Used to calculate WarmupTickCount. Rounds down to the nearest multiple of WarmupTickDelta.

### WarmupTickCount
- **类型**: `int`
- **描述**: Number of ticks to process for warmup. You can set by this or by time via WarmupTime.

### WarmupTickDelta
- **类型**: `float32`
- **描述**: Delta time to use for warmup ticks.

### bFixedTickDelta
- **类型**: `bool`

### FixedTickDeltaTime
- **类型**: `float32`
- **描述**: If activated, the system ticks with a fixed delta time instead of the varying game thread delta time. This leads to much more stable simulations.
When the fixed tick delta is smaller than the game thread tick time the simulation is substepping by executing multiple ticks per frame.
Note that activating this feature forces the system to tick on the game thread instead of an async task in parallel.

The max number of substeps per frame can be set via fx.Niagara.SystemSimulation.MaxTickSubsteps

### bBakeOutRapidIteration
- **类型**: `bool`

### bBakeOutRapidIterationOnCook
- **类型**: `bool`

### bCompressAttributes
- **类型**: `bool`

### bTrimAttributes
- **类型**: `bool`

### bTrimAttributesOnCook
- **类型**: `bool`

### bIgnoreParticleReadsForAttributeTrim
- **类型**: `bool`

### bDisableDebugSwitches
- **类型**: `bool`

### bDisableDebugSwitchesOnCook
- **类型**: `bool`

### bSupportLargeWorldCoordinates
- **类型**: `bool`

### bOverrideCastShadow
- **类型**: `bool`

### bOverrideReceivesDecals
- **类型**: `bool`

### bOverrideRenderCustomDepth
- **类型**: `bool`

### bOverrideCustomDepthStencilValue
- **类型**: `bool`

### bOverrideCustomDepthStencilWriteMask
- **类型**: `bool`

### bOverrideTranslucencySortPriority
- **类型**: `bool`

### bOverrideTranslucencySortDistanceOffset
- **类型**: `bool`

### bCastShadow
- **类型**: `bool`

### bReceivesDecals
- **类型**: `bool`

### bRenderCustomDepth
- **类型**: `bool`

### bDisableExperimentalVM
- **类型**: `bool`

### bInitialOwnerVelocityFromActor
- **类型**: `bool`

### bFixedBounds
- **类型**: `bool`

### bOverrideAllowCullingForLocalPlayers
- **类型**: `bool`

### bAllowCullingForLocalPlayersOverride
- **类型**: `bool`

### bAllowSystemStateFastPath
- **类型**: `bool`


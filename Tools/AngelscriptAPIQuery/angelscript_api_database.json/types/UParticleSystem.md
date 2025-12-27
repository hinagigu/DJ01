# UParticleSystem

**继承自**: `UFXSystemAsset`

A ParticleSystem is a complete particle effect that contains any number of ParticleEmitters. By allowing multiple emitters
in a system, the designer can create elaborate particle effects that are held in a single system. Once created using
Cascade, a ParticleSystem can then be inserted into a level or created in script.

## 属性

### UpdateTime_FPS
- **类型**: `float32`
- **描述**: UpdateTime_FPS - the frame per second to update at in FixedTime mode

### WarmupTime
- **类型**: `float32`
- **描述**: WarmupTime - the time to warm-up the particle system when first rendered
Warning: WarmupTime is implemented by simulating the particle system for the time requested upon activation.
This is extremely prone to cause hitches, especially with large particle counts - use with caution.

### WarmupTickRate
- **类型**: `float32`
- **描述**: WarmupTickRate - the time step for each tick during warm up.
       Increasing this improves performance. Decreasing, improves accuracy.
       Set to 0 to use the default tick time.

### ThumbnailWarmup
- **类型**: `float32`
- **描述**: The time to warm-up the system for the thumbnail image

### LODDistanceCheckTime
- **类型**: `float32`
- **描述**: How often (in seconds) the system should perform the LOD distance check.

### MacroUVRadius
- **类型**: `float32`
- **描述**: World space radius that UVs generated with the ParticleMacroUV material node will tile based on.

### LODDistances
- **类型**: `TArray<float32>`
- **描述**: The array of distances for each LOD level in the system.
Used when LODMethod is set to PARTICLESYSTEMLODMETHOD_Automatic.

Example: System with 3 LOD levels
        LODDistances(0) = 0.0
        LODDistances(1) = 2500.0
        LODDistances(2) = 5000.0

        In this case, when the system is [   0.0 ..   2499.9] from the camera, LOD level 0 will be used.
                                                                         [2500.0 ..   4999.9] from the camera, LOD level 1 will be used.
                                                                         [5000.0 .. INFINITY] from the camera, LOD level 2 will be used.

### FixedRelativeBoundingBox
- **类型**: `FBox`
- **描述**: Fixed relative bounding box for particle system.

### SecondsBeforeInactive
- **类型**: `float32`
- **描述**: Number of seconds of emitter not being rendered that need to pass before it
no longer gets ticked/ becomes inactive.

### Delay
- **类型**: `float32`
- **描述**: How long this Particle system should delay when ActivateSystem is called on it.

### DelayLow
- **类型**: `float32`
- **描述**: The low end of the emitter delay if using a range.

### SystemUpdateMode
- **类型**: `EParticleSystemUpdateMode`

### LODMethod
- **类型**: `ParticleSystemLODMethod`
- **描述**: The method of LOD level determination to utilize for this particle system
  PARTICLESYSTEMLODMETHOD_Automatic - Automatically set the LOD level, checking every LODDistanceCheckTime seconds.
PARTICLESYSTEMLODMETHOD_DirectSet - LOD level is directly set by the game code.
PARTICLESYSTEMLODMETHOD_ActivateAutomatic - LOD level is determined at Activation time, then left alone unless directly set by game code.

### InsignificantReaction
- **类型**: `EParticleSystemInsignificanceReaction`
- **描述**: The reaction this system takes when all emitters are insignificant.

### OcclusionBoundsMethod
- **类型**: `EParticleSystemOcclusionBoundsMethod`
- **描述**: Which occlusion bounds method to use for this particle system.
EPSOBM_None - Don't determine occlusion for this system.
EPSOBM_ParticleBounds - Use the bounds of the component when determining occlusion.

### MaxSignificanceLevel
- **类型**: `EParticleSignificanceLevel`
- **描述**: The maximum level of significance for emitters in this system. Any emitters with a higher significance will be capped at this significance level.

### MinTimeBetweenTicks
- **类型**: `uint`
- **描述**: Minimum duration between ticks; 33=tick at max. 30FPS, 16=60FPS, 8=120FPS

### InsignificanceDelay
- **类型**: `float32`
- **描述**: Time delay between all emitters becoming insignificant and the systems insignificant reaction.

### MacroUVPosition
- **类型**: `FVector`
- **描述**: Local space position that UVs generated with the ParticleMacroUV material node will be centered on.

### CustomOcclusionBounds
- **类型**: `FBox`
- **描述**: The occlusion bounds to use if OcclusionBoundsMethod is set to EPSOBM_CustomBounds

### NamedMaterialSlots
- **类型**: `TArray<FNamedEmitterMaterial>`
- **描述**: Array of named material slots for use by emitters of this system.
Emitters can use these instead of their own materials by providing the name to the NamedMaterialOverrides property of their required module.
These materials can be overridden using CreateNamedDynamicMaterialInstance() on a ParticleSystemComponent.

### bOrientZAxisTowardCamera
- **类型**: `bool`

### bUseFixedRelativeBoundingBox
- **类型**: `bool`

### bUseRealtimeThumbnail
- **类型**: `bool`

### bUseDelayRange
- **类型**: `bool`

### bAllowManagedTicking
- **类型**: `bool`

### bAutoDeactivate
- **类型**: `bool`

## 方法

### ContainsEmitterType
```angelscript
bool ContainsEmitterType(UClass TypeData)
```
Returns true if this system contains an emitter of the pasesd type.
@ param TypeData - The emitter type to check for. Must be a child class of UParticleModuleTypeDataBase


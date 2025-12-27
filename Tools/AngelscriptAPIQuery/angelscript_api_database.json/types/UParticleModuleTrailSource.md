# UParticleModuleTrailSource

**继承自**: `UParticleModuleTrailBase`

## 属性

### SourceMethod
- **类型**: `ETrail2SourceMethod`
- **描述**: The source method for the trail.

### SourceName
- **类型**: `FName`
- **描述**: The name of the source - either the emitter or Actor.

### SourceStrength
- **类型**: `FRawDistributionFloat`
- **描述**: The strength of the tangent from the source point for each Trail.

### SourceOffsetCount
- **类型**: `int`
- **描述**: SourceOffsetCount
The number of source offsets that can be expected to be found on the instance.
These must be named
        TrailSourceOffset#

### SourceOffsetDefaults
- **类型**: `TArray<FVector>`
- **描述**: Default offsets from the source(s).
If there are < SourceOffsetCount slots, the grabbing of values will simply wrap.

### SelectionMethod
- **类型**: `EParticleSourceSelectionMethod`
- **描述**: Particle selection method, when using the SourceMethod of Particle.

### bLockSourceStength
- **类型**: `bool`

### bInheritRotation
- **类型**: `bool`


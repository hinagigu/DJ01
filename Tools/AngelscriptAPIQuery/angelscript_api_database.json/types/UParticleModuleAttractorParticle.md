# UParticleModuleAttractorParticle

**继承自**: `UParticleModuleAttractorBase`

## 属性

### EmitterName
- **类型**: `FName`
- **描述**: The source emitter for attractors

### Range
- **类型**: `FRawDistributionFloat`
- **描述**: The radial range of the attraction around the source particle.
Particle-life relative.

### Strength
- **类型**: `FRawDistributionFloat`
- **描述**: The strength of the attraction (negative values repel).
Particle-life relative if StrengthByDistance is false.

### SelectionMethod
- **类型**: `EAttractorParticleSelectionMethod`
- **描述**: The method to use when selecting an attractor target particle from the emitter.
One of the following:
Random          - Randomly select a particle from the source emitter.
Sequential  - Select a particle using a sequential order.

### bStrengthByDistance
- **类型**: `bool`

### bAffectBaseVelocity
- **类型**: `bool`

### bRenewSource
- **类型**: `bool`

### bInheritSourceVel
- **类型**: `bool`


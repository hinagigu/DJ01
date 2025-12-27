# UParticleModuleVelocity

**继承自**: `UParticleModuleVelocityBase`

## 属性

### StartVelocity
- **类型**: `FRawDistributionVector`
- **描述**: The velocity to apply to a particle when it is spawned.
Value is retrieved using the EmitterTime of the emitter.

### StartVelocityRadial
- **类型**: `FRawDistributionFloat`
- **描述**: The velocity to apply to a particle along its radial direction.
Direction is determined by subtracting the location of the emitter from the particle location at spawn.
Value is retrieved using the EmitterTime of the emitter.


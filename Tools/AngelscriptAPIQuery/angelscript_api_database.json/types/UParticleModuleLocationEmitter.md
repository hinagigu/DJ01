# UParticleModuleLocationEmitter

**继承自**: `UParticleModuleLocationBase`

## 属性

### EmitterName
- **类型**: `FName`
- **描述**: The name of the emitter to use that the source location for particle.

### SelectionMethod
- **类型**: `ELocationEmitterSelectionMethod`
- **描述**: The method to use when selecting a spawn target particle from the emitter.
Can be one of the following:
        ELESM_Random            Randomly select a particle from the source emitter.
        ELESM_Sequential        Step through each particle from the source emitter in order.

### InheritSourceVelocityScale
- **类型**: `float32`
- **描述**: Amount to scale the source velocity by when inheriting it.

### InheritSourceRotationScale
- **类型**: `float32`
- **描述**: Amount to scale the source rotation by when inheriting it.

### InheritSourceVelocity
- **类型**: `bool`

### bInheritSourceRotation
- **类型**: `bool`


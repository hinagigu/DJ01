# UParticleModuleAcceleration

**继承自**: `UParticleModuleAccelerationBase`

## 属性

### Acceleration
- **类型**: `FRawDistributionVector`
- **描述**: The initial acceleration of the particle.
Value is obtained using the EmitterTime at particle spawn.
Each frame, the current and base velocity of the particle
is then updated using the formula
        velocity += acceleration * DeltaTime
where DeltaTime is the time passed since the last frame.

### bApplyOwnerScale
- **类型**: `bool`


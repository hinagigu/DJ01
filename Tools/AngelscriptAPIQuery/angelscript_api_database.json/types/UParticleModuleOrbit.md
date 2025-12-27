# UParticleModuleOrbit

**继承自**: `UParticleModuleOrbitBase`

## 属性

### ChainMode
- **类型**: `EOrbitChainMode`
- **描述**: Orbit modules will chain together in the order they appear in the module stack.
The combination of a module with the one prior to it is defined by using one
of the following enumerations:
        EOChainMode_Add         Add the values to the previous results
        EOChainMode_Scale       Multiply the values by the previous results
        EOChainMode_Link        'Break' the chain and apply the values from the previous results

### OffsetAmount
- **类型**: `FRawDistributionVector`
- **描述**: The amount to offset the sprite from the particle position.

### OffsetOptions
- **类型**: `FOrbitOptions`
- **描述**: The options associated with the OffsetAmount look-up.

### RotationAmount
- **类型**: `FRawDistributionVector`
- **描述**: The amount (in 'turns') to rotate the offset about the particle position.
        0.0 = no rotation
        0.5     = 180 degree rotation
        1.0 = 360 degree rotation

### RotationOptions
- **类型**: `FOrbitOptions`
- **描述**: The options associated with the RotationAmount look-up.

### RotationRateAmount
- **类型**: `FRawDistributionVector`
- **描述**: The rate (in 'turns') at which to rotate the offset about the particle positon.
        0.0 = no rotation
        0.5     = 180 degree rotation
        1.0 = 360 degree rotation

### RotationRateOptions
- **类型**: `FOrbitOptions`
- **描述**: The options associated with the RotationRateAmount look-up.


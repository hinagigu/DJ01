# UParticleModuleCameraOffset

**继承自**: `UParticleModuleCameraBase`

## 属性

### CameraOffset
- **类型**: `FRawDistributionFloat`
- **描述**: The camera-relative offset to apply to sprite location

### UpdateMethod
- **类型**: `EParticleCameraOffsetUpdateMethod`
- **描述**: How to update the offset for this module.
DirectSet - Set the value directly (overwrite any previous setting)
Additive  - Add the offset of this module to the existing offset
Scalar    - Scale the existing offset by the value of this module

### bSpawnTimeOnly
- **类型**: `bool`


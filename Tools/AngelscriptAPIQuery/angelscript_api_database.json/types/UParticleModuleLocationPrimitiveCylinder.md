# UParticleModuleLocationPrimitiveCylinder

**继承自**: `UParticleModuleLocationPrimitiveBase`

## 属性

### StartRadius
- **类型**: `FRawDistributionFloat`
- **描述**: The radius of the cylinder.

### StartHeight
- **类型**: `FRawDistributionFloat`
- **描述**: The height of the cylinder, centered about the location.

### HeightAxis
- **类型**: `CylinderHeightAxis`
- **描述**: Determine the particle system axis that should represent the height of the cylinder.
Can be one of the following:
  PMLPC_HEIGHTAXIS_X - Orient the height along the particle system X-axis.
  PMLPC_HEIGHTAXIS_Y - Orient the height along the particle system Y-axis.
  PMLPC_HEIGHTAXIS_Z - Orient the height along the particle system Z-axis.

### RadialVelocity
- **类型**: `bool`


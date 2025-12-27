# UPhysicalMaterial

**继承自**: `UObject`

Physical materials are used to define the response of a physical object when interacting dynamically with the world.

## 属性

### Friction
- **类型**: `float32`

### StaticFriction
- **类型**: `float32`

### FrictionCombineMode
- **类型**: `EFrictionCombineMode`

### bOverrideFrictionCombineMode
- **类型**: `bool`

### Restitution
- **类型**: `float32`

### RestitutionCombineMode
- **类型**: `EFrictionCombineMode`

### bOverrideRestitutionCombineMode
- **类型**: `bool`

### Density
- **类型**: `float32`

### SleepLinearVelocityThreshold
- **类型**: `float32`

### SleepAngularVelocityThreshold
- **类型**: `float32`

### SleepCounterThreshold
- **类型**: `int`

### RaiseMassToPower
- **类型**: `float32`

### SurfaceType
- **类型**: `EPhysicalSurface`

### Strength
- **类型**: `FPhysicalMaterialStrength`

### DamageModifier
- **类型**: `FPhysicalMaterialDamageModifier`

### SoftCollisionMode
- **类型**: `EPhysicalMaterialSoftCollisionMode`
- **描述**: For enable soft collision shell thickness mode

### SoftCollisionThickness
- **类型**: `float32`
- **描述**: Thickness of the layer just inside the collision shape in which contact is considered "soft".
              The units depend on SoftCollisionMode

### BaseFrictionImpulse
- **类型**: `float32`
- **描述**: A friction (positional) impulse of at least this magnitude may be applied,
              regardless the normal force. This is analogous to adding only the lateral part of a
              "stickiness" to a material


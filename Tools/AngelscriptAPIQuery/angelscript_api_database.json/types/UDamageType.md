# UDamageType

**继承自**: `UObject`

A DamageType is intended to define and describe a particular form of damage and to provide an avenue
for customizing responses to damage from various sources.

For example, a game could make a DamageType_Fire set it up to ignite the damaged actor.

DamageTypes are never instanced and should be treated as immutable data holders with static code
functionality.  They should never be stateful.

## 属性

### DamageImpulse
- **类型**: `float32`

### DestructibleImpulse
- **类型**: `float32`

### DestructibleDamageSpreadScale
- **类型**: `float32`

### DamageFalloff
- **类型**: `float32`

### bCausedByWorld
- **类型**: `bool`

### bScaleMomentumByMass
- **类型**: `bool`

### bRadialDamageVelChange
- **类型**: `bool`


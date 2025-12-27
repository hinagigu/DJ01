# UParticleModuleCollisionGPU

**继承自**: `UParticleModuleCollisionBase`

## 属性

### Resilience
- **类型**: `FRawDistributionFloat`
- **描述**: The bounciness of the particle.

### ResilienceScaleOverLife
- **类型**: `FRawDistributionFloat`
- **描述**: Scales the bounciness of the particle over its life.

### Friction
- **类型**: `float32`
- **描述**: Friction applied to all particles during a collision or while moving
along a surface.

### RandomSpread
- **类型**: `float32`
- **描述**: Controls how wide the bouncing particles are distributed (0 = disabled).

### RandomDistribution
- **类型**: `float32`
- **描述**: Controls bouncing particles distribution (1 = uniform distribution; 2 = squared distribution).

### RadiusScale
- **类型**: `float32`
- **描述**: Scale applied to the size of the particle to obtain the collision radius.

### RadiusBias
- **类型**: `float32`
- **描述**: Bias applied to the collision radius.

### Response
- **类型**: `EParticleCollisionResponse`
- **描述**: How particles respond to a collision event.

### CollisionMode
- **类型**: `EParticleCollisionMode`


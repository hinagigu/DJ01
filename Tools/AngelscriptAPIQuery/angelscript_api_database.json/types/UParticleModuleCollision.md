# UParticleModuleCollision

**继承自**: `UParticleModuleCollisionBase`

## 属性

### DampingFactor
- **类型**: `FRawDistributionVector`
- **描述**: How much to `slow' the velocity of the particle after a collision.
Value is obtained using the EmitterTime at particle spawn.

### DampingFactorRotation
- **类型**: `FRawDistributionVector`
- **描述**: How much to `slow' the rotation of the particle after a collision.
Value is obtained using the EmitterTime at particle spawn.

### MaxCollisions
- **类型**: `FRawDistributionFloat`
- **描述**: The maximum number of collisions a particle can have.
Value is obtained using the EmitterTime at particle spawn.

### CollisionCompletionOption
- **类型**: `EParticleCollisionComplete`
- **描述**: What to do once a particles MaxCollisions is reached.
One of the following:
EPCC_Kill
        Kill the particle when MaxCollisions is reached
EPCC_Freeze
        Freeze in place, NO MORE UPDATES
EPCC_HaltCollisions,
        Stop collision checks, keep updating everything
EPCC_FreezeTranslation,
        Stop translations, keep updating everything else
EPCC_FreezeRotation,
        Stop rotations, keep updating everything else
EPCC_FreezeMovement
        Stop all movement, keep updating

### CollisionTypes
- **类型**: `TArray<EObjectTypeQuery>`
- **描述**: Which ObjectTypes to collide with

### ParticleMass
- **类型**: `FRawDistributionFloat`
- **描述**: The mass of the particle - for use when bApplyPhysics is true.
Value is obtained using the EmitterTime at particle spawn.

### DirScalar
- **类型**: `float32`
- **描述**: The directional scalar value - used to scale the bounds to
'assist' in avoiding inter-penetration or large gaps.

### VerticalFudgeFactor
- **类型**: `float32`
- **描述**: The fudge factor to use to determine vertical.
True vertical will have a Hit.Normal.Z == 1.0
This will allow for Z components in the range of
[1.0-VerticalFudgeFactor..1.0]
to count as vertical collisions.

### DelayAmount
- **类型**: `FRawDistributionFloat`
- **描述**: How long to delay before checking a particle for collisions.
Value is retrieved using the EmitterTime.
During update, the particle flag IgnoreCollisions will be
set until the particle RelativeTime has surpassed the
DelayAmount.

### MaxCollisionDistance
- **类型**: `float32`
- **描述**: Max distance at which particle collision will occur.

### bApplyPhysics
- **类型**: `bool`

### bIgnoreTriggerVolumes
- **类型**: `bool`

### bPawnsDoNotDecrementCount
- **类型**: `bool`

### bOnlyVerticalNormalsDecrementCount
- **类型**: `bool`

### bDropDetail
- **类型**: `bool`

### bCollideOnlyIfVisible
- **类型**: `bool`

### bIgnoreSourceActor
- **类型**: `bool`


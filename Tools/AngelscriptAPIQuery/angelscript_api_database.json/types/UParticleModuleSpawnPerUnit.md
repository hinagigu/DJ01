# UParticleModuleSpawnPerUnit

**继承自**: `UParticleModuleSpawnBase`

## 属性

### UnitScalar
- **类型**: `float32`
- **描述**: The scalar to apply to the distance traveled.
The value from SpawnPerUnit is divided by this value to give the actual
number of particles per unit.

### MovementTolerance
- **类型**: `float32`
- **描述**: The tolerance for moving vs. not moving w.r.t. the bIgnoreSpawnRateWhenMoving flag.
Ie, if (DistanceMoved < (UnitScalar x MovementTolerance)) then consider it not moving.

### SpawnPerUnit
- **类型**: `FRawDistributionFloat`
- **描述**: The amount to spawn per meter distribution.
The value is retrieved using the EmitterTime.

### MaxFrameDistance
- **类型**: `float32`
- **描述**: The maximum valid movement for a single frame.
If 0.0, then the check is not performed.
Currently, if the distance moved between frames is greater than this
then NO particles will be spawned.
This is primiarily intended to cover cases where the PSystem is
attached to teleporting objects.

### bIgnoreSpawnRateWhenMoving
- **类型**: `bool`

### bIgnoreMovementAlongX
- **类型**: `bool`

### bIgnoreMovementAlongY
- **类型**: `bool`

### bIgnoreMovementAlongZ
- **类型**: `bool`


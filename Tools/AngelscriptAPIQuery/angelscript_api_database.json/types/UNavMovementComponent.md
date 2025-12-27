# UNavMovementComponent

**继承自**: `UMovementComponent`

NavMovementComponent defines base functionality for MovementComponents that move any 'agent' that may be involved in AI pathfinding.

## 属性

### NavAgentProps
- **类型**: `FNavAgentProperties`

### FixedPathBrakingDistance
- **类型**: `float32`
- **描述**: Braking distance override used with acceleration driven path following (bUseAccelerationForPaths)

### bUpdateNavAgentWithOwnersCollision
- **类型**: `bool`

### bUseAccelerationForPaths
- **类型**: `bool`

### bUseFixedBrakingDistanceForPaths
- **类型**: `bool`

## 方法

### IsCrouching
```angelscript
bool IsCrouching()
```
Returns true if currently crouching

### IsFalling
```angelscript
bool IsFalling()
```
Returns true if currently falling (not flying, in a non-fluid volume, and not on the ground)

### IsFlying
```angelscript
bool IsFlying()
```
Returns true if currently flying (moving through a non-fluid volume without resting on the ground)

### IsMovingOnGround
```angelscript
bool IsMovingOnGround()
```
Returns true if currently moving on the ground (e.g. walking or driving)

### IsSwimming
```angelscript
bool IsSwimming()
```
Returns true if currently swimming (moving through a fluid volume)

### StopActiveMovement
```angelscript
void StopActiveMovement()
```
Stops applying further movement (usually zeros acceleration).

### StopMovementKeepPathing
```angelscript
void StopMovementKeepPathing()
```
Stops movement immediately (reset velocity) but keeps following current path


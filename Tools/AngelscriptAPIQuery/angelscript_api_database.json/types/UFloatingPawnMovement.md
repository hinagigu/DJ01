# UFloatingPawnMovement

**继承自**: `UPawnMovementComponent`

FloatingPawnMovement is a movement component that provides simple movement for any Pawn class.
Limits on speed and acceleration are provided, while gravity is not implemented.

Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

## 属性

### Acceleration
- **类型**: `float32`

### Deceleration
- **类型**: `float32`

### TurningBoost
- **类型**: `float32`

### MaxSpeed
- **类型**: `float32`


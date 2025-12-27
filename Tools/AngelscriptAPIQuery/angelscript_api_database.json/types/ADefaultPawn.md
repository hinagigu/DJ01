# ADefaultPawn

**继承自**: `APawn`

DefaultPawn implements a simple Pawn with spherical collision and built-in flying movement.
@see UFloatingPawnMovement

## 属性

### BaseTurnRate
- **类型**: `float32`
- **描述**: Base turn rate, in deg/sec. Other scaling may affect final turn rate.

### BaseLookUpRate
- **类型**: `float32`
- **描述**: Base lookup rate, in deg/sec. Other scaling may affect final lookup rate.

### CollisionComponent
- **类型**: `USphereComponent`

### MeshComponent
- **类型**: `UStaticMeshComponent`

### MovementComponent
- **类型**: `UPawnMovementComponent`

### bAddDefaultMovementBindings
- **类型**: `bool`

## 方法

### LookUpAtRate
```angelscript
void LookUpAtRate(float32 Rate)
```
Called via input to look up at a given rate (or down if Rate is negative).
@param Rate   This is a normalized rate, i.e. 1.0 means 100% of desired turn rate

### MoveForward
```angelscript
void MoveForward(float32 Val)
```
Input callback to move forward in local space (or backward if Val is negative).
@param Val Amount of movement in the forward direction (or backward if negative).
@see APawn::AddMovementInput()

### MoveRight
```angelscript
void MoveRight(float32 Val)
```
Input callback to strafe right in local space (or left if Val is negative).
@param Val Amount of movement in the right direction (or left if negative).
@see APawn::AddMovementInput()

### MoveUp_World
```angelscript
void MoveUp_World(float32 Val)
```
Input callback to move up in world space (or down if Val is negative).
@param Val Amount of movement in the world up direction (or down if negative).
@see APawn::AddMovementInput()

### TurnAtRate
```angelscript
void TurnAtRate(float32 Rate)
```
Called via input to turn at a given rate.
@param Rate  This is a normalized rate, i.e. 1.0 means 100% of desired turn rate


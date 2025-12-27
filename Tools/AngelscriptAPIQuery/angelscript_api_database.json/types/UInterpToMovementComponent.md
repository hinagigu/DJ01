# UInterpToMovementComponent

**继承自**: `UMovementComponent`

Move the root component between a series of points over a given time *

@see UMovementComponent

## 属性

### Duration
- **类型**: `float32`

### bSweep
- **类型**: `bool`

### TeleportType
- **类型**: `ETeleportType`

### BehaviourType
- **类型**: `EInterpToBehaviourType`

### bCheckIfStillInWorld
- **类型**: `bool`

### OnInterpToReverse
- **类型**: `FOnInterpToReverseDelegate__InterpToMovementComponent`

### OnInterpToStop
- **类型**: `FOnInterpToStopDelegate__InterpToMovementComponent`

### OnWaitBeginDelegate
- **类型**: `FOnInterpToWaitBeginDelegate__InterpToMovementComponent`

### OnWaitEndDelegate
- **类型**: `FOnInterpToWaitEndDelegate__InterpToMovementComponent`

### OnResetDelegate
- **类型**: `FOnInterpToResetDelegate__InterpToMovementComponent`

### MaxSimulationTimeStep
- **类型**: `float32`

### SpeedMultiplier
- **类型**: `float32`

### MaxSimulationIterations
- **类型**: `int`

### ControlPoints
- **类型**: `TArray<FInterpControlPoint>`

### bPauseOnImpact
- **类型**: `bool`

### bForceSubStepping
- **类型**: `bool`

## 方法

### AddControlPointPosition
```angelscript
void AddControlPointPosition(FVector Pos, bool bPositionIsRelative)
```
Add a control point that represents a position.

### FinaliseControlPoints
```angelscript
void FinaliseControlPoints()
```
Initialise the control points array. Call after adding control points if they are add after begin play .

### ResetControlPoints
```angelscript
void ResetControlPoints()
```
Clear the control points array and set to stopped.

### RestartMovement
```angelscript
void RestartMovement(float32 InitialDirection)
```
Reset to start. Sets time to zero and direction to 1.

### StopSimulating
```angelscript
void StopSimulating(FHitResult HitResult)
```
Clears the reference to UpdatedComponent, fires stop event, and stops ticking.


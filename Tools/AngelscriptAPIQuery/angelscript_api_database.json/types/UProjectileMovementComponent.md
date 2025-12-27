# UProjectileMovementComponent

**继承自**: `UMovementComponent`

ProjectileMovementComponent updates the position of another component during its tick.

Behavior such as bouncing after impacts and homing toward a target are supported.

Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
If the updated component is simulating physics, only the initial launch parameters (when initial velocity is non-zero)
will affect the projectile, and the physics sim will take over from there.

@see UMovementComponent

## 属性

### InitialSpeed
- **类型**: `float32`

### PreviousHitTime
- **类型**: `float32`
- **描述**: Saved HitResult Time (0 to 1) from previous simulation step. Equal to 1.0 when there was no impact.

### PreviousHitNormal
- **类型**: `FVector`
- **描述**: Saved HitResult Normal from previous simulation step that resulted in an impact. If PreviousHitTime is 1.0, then the hit was not in the last step.

### ProjectileGravityScale
- **类型**: `float32`

### Bounciness
- **类型**: `float32`

### Friction
- **类型**: `float32`

### BounceVelocityStopSimulatingThreshold
- **类型**: `float32`

### MinFrictionFraction
- **类型**: `float32`

### OnProjectileBounce
- **类型**: `FOnProjectileBounceDelegate__ProjectileMovementComponent`

### OnProjectileStop
- **类型**: `FOnProjectileStopDelegate__ProjectileMovementComponent`

### HomingAccelerationMagnitude
- **类型**: `float32`

### MaxSimulationTimeStep
- **类型**: `float32`

### MaxSimulationIterations
- **类型**: `int`

### BounceAdditionalIterations
- **类型**: `int`

### InterpLocationTime
- **类型**: `float32`

### InterpRotationTime
- **类型**: `float32`

### InterpLocationMaxLagDistance
- **类型**: `float32`

### InterpLocationSnapToTargetDistance
- **类型**: `float32`

### ThrottleInterpolationThresholdNotRenderedShortTime
- **类型**: `float32`

### ThrottleInterpolationThresholdNotRenderedLongTime
- **类型**: `float32`

### ThrottleInterpolationSkipFramesRecent
- **类型**: `int`

### ThrottleInterpolationSkipFramesNotRecent
- **类型**: `int`

### MaxSpeed
- **类型**: `float32`

### bRotationFollowsVelocity
- **类型**: `bool`

### bRotationRemainsVertical
- **类型**: `bool`

### bShouldBounce
- **类型**: `bool`

### bInitialVelocityInLocalSpace
- **类型**: `bool`

### bForceSubStepping
- **类型**: `bool`

### bSimulationEnabled
- **类型**: `bool`

### bSweepCollision
- **类型**: `bool`

### bIsHomingProjectile
- **类型**: `bool`

### bBounceAngleAffectsFriction
- **类型**: `bool`

### bIsSliding
- **类型**: `bool`

### bInterpMovement
- **类型**: `bool`

### bInterpRotation
- **类型**: `bool`

### bThrottleInterpolation
- **类型**: `bool`

### bSimulationUseScopedMovement
- **类型**: `bool`

### bInterpolationUseScopedMovement
- **类型**: `bool`

## 方法

### GetHomingTargetComponent
```angelscript
const USceneComponent GetHomingTargetComponent()
```

### SetHomingTargetComponent
```angelscript
void SetHomingTargetComponent(USceneComponent HomingTargetComponent)
```

### IsInterpolationComplete
```angelscript
bool IsInterpolationComplete()
```
Returns whether interpolation is complete because the target has been reached. True when interpolation is disabled.

### IsVelocityUnderSimulationThreshold
```angelscript
bool IsVelocityUnderSimulationThreshold()
```
Returns true if velocity magnitude is less than BounceVelocityStopSimulatingThreshold.

### LimitVelocity
```angelscript
FVector LimitVelocity(FVector NewVelocity)
```
Don't allow velocity magnitude to exceed MaxSpeed, if MaxSpeed is non-zero.

### MoveInterpolationTarget
```angelscript
void MoveInterpolationTarget(FVector NewLocation, FRotator NewRotation)
```
Moves the UpdatedComponent, which is also the interpolation target for the interpolated component. If there is not interpolated component, this simply moves UpdatedComponent.
Use this typically from PostNetReceiveLocationAndRotation() or similar from an Actor.

### ResetInterpolation
```angelscript
void ResetInterpolation()
```
Resets interpolation so that interpolated component snaps back to the initial location/rotation without any additional offsets.

### SetInterpolatedComponent
```angelscript
void SetInterpolatedComponent(USceneComponent Component)
```
Assigns the component that will be used for network interpolation/smoothing. It is expected that this is a component attached somewhere below the UpdatedComponent.
When network updates use MoveInterpolationTarget() to move the UpdatedComponent, the interpolated component's relative offset will be maintained and smoothed over
the course of future component ticks. The current relative location and rotation of the component is saved as the target offset for future interpolation.
@see MoveInterpolationTarget(), bInterpMovement, bInterpRotation

### SetVelocityInLocalSpace
```angelscript
void SetVelocityInLocalSpace(FVector NewVelocity)
```
Sets the velocity to the new value, rotated into Actor space.

### StopSimulating
```angelscript
void StopSimulating(FHitResult HitResult)
```
Clears the reference to UpdatedComponent, fires stop event (OnProjectileStop), and stops ticking (if bAutoUpdateTickRegistration is true).


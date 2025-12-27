# UMovementComponent

**继承自**: `UActorComponent`

MovementComponent is an abstract component class that defines functionality for moving a PrimitiveComponent (our UpdatedComponent) each tick.
Base functionality includes:
   - Restricting movement to a plane or axis.
   - Utility functions for special handling of collision results (SlideAlongSurface(), ComputeSlideVector(), TwoWallAdjust()).
   - Utility functions for moving when there may be initial penetration (SafeMoveUpdatedComponent(), ResolvePenetration()).
   - Automatically registering the component tick and finding a component to move on the owning Actor.
Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

## 属性

### UpdatedPrimitive
- **类型**: `UPrimitiveComponent`
- **描述**: UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent.

### Velocity
- **类型**: `FVector`

### UpdatedComponent
- **类型**: `USceneComponent`

### bUpdateOnlyIfRendered
- **类型**: `bool`

### bAutoUpdateTickRegistration
- **类型**: `bool`

### bTickBeforeOwner
- **类型**: `bool`

### bAutoRegisterUpdatedComponent
- **类型**: `bool`

### bConstrainToPlane
- **类型**: `bool`

### bSnapToPlaneAtStart
- **类型**: `bool`

### bAutoRegisterPhysicsVolumeUpdates
- **类型**: `bool`

### bComponentShouldUpdatePhysicsVolume
- **类型**: `bool`

## 方法

### ConstrainDirectionToPlane
```angelscript
FVector ConstrainDirectionToPlane(FVector Direction)
```
Constrain a direction vector to the plane constraint, if enabled.
@see SetPlaneConstraint

### ConstrainLocationToPlane
```angelscript
FVector ConstrainLocationToPlane(FVector Location)
```
Constrain a position vector to the plane constraint, if enabled.

### ConstrainNormalToPlane
```angelscript
FVector ConstrainNormalToPlane(FVector Normal)
```
Constrain a normal vector (of unit length) to the plane constraint, if enabled.

### GetGravityZ
```angelscript
float32 GetGravityZ()
```
Returns gravity that affects this component

### GetMaxSpeed
```angelscript
float32 GetMaxSpeed()
```
Returns maximum speed of component in current movement mode.

### GetPhysicsVolume
```angelscript
APhysicsVolume GetPhysicsVolume()
```
Returns the PhysicsVolume this MovementComponent is using, or the world's default physics volume if none. *

### GetPlaneConstraintAxisSetting
```angelscript
EPlaneConstraintAxisSetting GetPlaneConstraintAxisSetting()
```
Get the plane constraint axis setting.

### GetPlaneConstraintNormal
```angelscript
FVector GetPlaneConstraintNormal()
```
Returns the normal of the plane that constrains movement, enforced if the plane constraint is enabled.

### GetPlaneConstraintOrigin
```angelscript
FVector GetPlaneConstraintOrigin()
```
Get the plane constraint origin. This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().
@return The origin of the plane that constrains movement, if the plane constraint is enabled.

### IsExceedingMaxSpeed
```angelscript
bool IsExceedingMaxSpeed(float32 MaxSpeed)
```
Returns true if the current velocity is exceeding the given max speed (usually the result of GetMaxSpeed()), within a small error tolerance.
Note that under normal circumstances updates cause by acceleration will not cause this to be true, however external forces or changes in the max speed limit
can cause the max speed to be violated.

### MoveUpdatedComponent
```angelscript
bool MoveUpdatedComponent(FVector Delta, FRotator NewRotation, FHitResult& OutHit, bool bSweep, bool bTeleport)
```
Moves our UpdatedComponent by the given Delta, and sets rotation to NewRotation.
Respects the plane constraint, if enabled.
@return True if some movement occurred, false if no movement occurred. Result of any impact will be stored in OutHit.

### SetPlaneConstraintAxisSetting
```angelscript
void SetPlaneConstraintAxisSetting(EPlaneConstraintAxisSetting NewAxisSetting)
```
Set the plane constraint axis setting.
Changing this setting will modify the current value of PlaneConstraintNormal.

@param  NewAxisSetting New plane constraint axis setting.

### SetPlaneConstraintEnabled
```angelscript
void SetPlaneConstraintEnabled(bool bEnabled)
```
Sets whether or not the plane constraint is enabled.

### SetPlaneConstraintFromVectors
```angelscript
void SetPlaneConstraintFromVectors(FVector Forward, FVector Up)
```
Uses the Forward and Up vectors to compute the plane that constrains movement, enforced if the plane constraint is enabled.

### SetPlaneConstraintNormal
```angelscript
void SetPlaneConstraintNormal(FVector PlaneNormal)
```
Sets the normal of the plane that constrains movement, enforced if the plane constraint is enabled.
Changing the normal automatically sets PlaneConstraintAxisSetting to "Custom".

@param PlaneNormal   The normal of the plane. If non-zero in length, it will be normalized.

### SetPlaneConstraintOrigin
```angelscript
void SetPlaneConstraintOrigin(FVector PlaneOrigin)
```
Sets the origin of the plane that constrains movement, enforced if the plane constraint is enabled.

### SetUpdatedComponent
```angelscript
void SetUpdatedComponent(USceneComponent NewUpdatedComponent)
```
Assign the component we move and update.

### SnapUpdatedComponentToPlane
```angelscript
void SnapUpdatedComponentToPlane()
```
Snap the updated component to the plane constraint, if enabled.

### StopMovementImmediately
```angelscript
void StopMovementImmediately()
```
Stops movement immediately (zeroes velocity, usually zeros acceleration for components with acceleration).


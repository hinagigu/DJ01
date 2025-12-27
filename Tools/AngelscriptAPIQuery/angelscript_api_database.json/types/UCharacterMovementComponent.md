# UCharacterMovementComponent

**继承自**: `UPawnMovementComponent`

CharacterMovementComponent handles movement logic for the associated Character owner.
It supports various movement modes including: walking, falling, swimming, flying, custom.

Movement is affected primarily by current Velocity and Acceleration. Acceleration is updated each frame
based on the input vector accumulated thus far (see UPawnMovementComponent::GetPendingInputVector()).

Networking is fully implemented, with server-client correction and prediction included.

@see ACharacter, UPawnMovementComponent
@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Pawn/Character/

## 属性

### GravityScale
- **类型**: `float32`

### MaxStepHeight
- **类型**: `float32`

### JumpZVelocity
- **类型**: `float32`

### JumpOffJumpZFactor
- **类型**: `float32`

### WorldToGravityTransform
- **类型**: `FQuat`
- **描述**: A cached quaternion representing the rotation from world space to gravity relative space defined by GravityDirection.

### GravityToWorldTransform
- **类型**: `FQuat`
- **描述**: A cached quaternion representing the inverse rotation from world space to gravity relative space defined by GravityDirection.

### CustomMovementMode
- **类型**: `uint8`
- **描述**: Current custom sub-mode if MovementMode is set to Custom.
This is automatically replicated through the Character owner and for client-server movement functions.
@see SetMovementMode()

### NetworkSmoothingMode
- **类型**: `ENetworkSmoothingMode`

### GroundFriction
- **类型**: `float32`

### MaxWalkSpeed
- **类型**: `float32`

### MaxWalkSpeedCrouched
- **类型**: `float32`

### MaxSwimSpeed
- **类型**: `float32`

### MaxFlySpeed
- **类型**: `float32`

### MaxCustomMovementSpeed
- **类型**: `float32`

### MinAnalogWalkSpeed
- **类型**: `float32`

### BrakingFrictionFactor
- **类型**: `float32`

### BrakingFriction
- **类型**: `float32`

### BrakingSubStepTime
- **类型**: `float32`

### BrakingDecelerationWalking
- **类型**: `float32`

### BrakingDecelerationFalling
- **类型**: `float32`

### BrakingDecelerationSwimming
- **类型**: `float32`

### BrakingDecelerationFlying
- **类型**: `float32`

### AirControl
- **类型**: `float32`

### AirControlBoostMultiplier
- **类型**: `float32`

### AirControlBoostVelocityThreshold
- **类型**: `float32`

### FallingLateralFriction
- **类型**: `float32`

### Buoyancy
- **类型**: `float32`

### PerchAdditionalHeight
- **类型**: `float32`

### RotationRate
- **类型**: `FRotator`

### MaxOutOfWaterStepHeight
- **类型**: `float32`

### OutofWaterZ
- **类型**: `float32`

### Mass
- **类型**: `float32`

### StandingDownwardForceScale
- **类型**: `float32`

### InitialPushForceFactor
- **类型**: `float32`

### PushForceFactor
- **类型**: `float32`

### PushForcePointZOffsetFactor
- **类型**: `float32`

### TouchForceFactor
- **类型**: `float32`

### MinTouchForce
- **类型**: `float32`

### MaxTouchForce
- **类型**: `float32`

### RepulsionForce
- **类型**: `float32`

### MaxSimulationTimeStep
- **类型**: `float32`

### MaxSimulationIterations
- **类型**: `int`

### MaxJumpApexAttemptsPerSimulation
- **类型**: `int`

### MaxDepenetrationWithGeometry
- **类型**: `float32`

### MaxDepenetrationWithGeometryAsProxy
- **类型**: `float32`

### MaxDepenetrationWithPawn
- **类型**: `float32`

### MaxDepenetrationWithPawnAsProxy
- **类型**: `float32`

### NetworkSimulatedSmoothLocationTime
- **类型**: `float32`
- **描述**: How long to take to smoothly interpolate from the old pawn position on the client to the corrected one sent by the server. Not used by Linear smoothing.

### NetworkSimulatedSmoothRotationTime
- **类型**: `float32`
- **描述**: How long to take to smoothly interpolate from the old pawn rotation on the client to the corrected one sent by the server. Not used by Linear smoothing.

### ListenServerNetworkSimulatedSmoothLocationTime
- **类型**: `float32`
- **描述**: Similar setting as NetworkSimulatedSmoothLocationTime but only used on Listen servers.

### ListenServerNetworkSimulatedSmoothRotationTime
- **类型**: `float32`
- **描述**: Similar setting as NetworkSimulatedSmoothRotationTime but only used on Listen servers.

### NetProxyShrinkRadius
- **类型**: `float32`
- **描述**: Shrink simulated proxy capsule radius by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.
@see AdjustProxyCapsuleSize()

### NetProxyShrinkHalfHeight
- **类型**: `float32`
- **描述**: Shrink simulated proxy capsule half height by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.
@see AdjustProxyCapsuleSize()

### NetworkMaxSmoothUpdateDistance
- **类型**: `float32`
- **描述**: Maximum distance character is allowed to lag behind server location when interpolating between updates.

### NetworkNoSmoothUpdateDistance
- **类型**: `float32`
- **描述**: Maximum distance beyond which character is teleported to the new server location without any smoothing.

### NetworkMinTimeBetweenClientAckGoodMoves
- **类型**: `float32`
- **描述**: Minimum time on the server between acknowledging good client moves. This can save on bandwidth. Set to 0 to disable throttling.

### NetworkMinTimeBetweenClientAdjustments
- **类型**: `float32`
- **描述**: Minimum time on the server between sending client adjustments when client has exceeded allowable position error.
Should be >= NetworkMinTimeBetweenClientAdjustmentsLargeCorrection (the larger value is used regardless).
This can save on bandwidth. Set to 0 to disable throttling.
@see ServerLastClientAdjustmentTime

### NetworkMinTimeBetweenClientAdjustmentsLargeCorrection
- **类型**: `float32`
- **描述**: Minimum time on the server between sending client adjustments when client has exceeded allowable position error by a large amount (NetworkLargeClientCorrectionDistance).
Should be <= NetworkMinTimeBetweenClientAdjustments (the smaller value is used regardless).
@see NetworkMinTimeBetweenClientAdjustments

### NetworkLargeClientCorrectionDistance
- **类型**: `float32`
- **描述**: If client error is larger than this, sets bNetworkLargeClientCorrection to reduce delay between client adjustments.
@see NetworkMinTimeBetweenClientAdjustments, NetworkMinTimeBetweenClientAdjustmentsLargeCorrection

### LedgeCheckThreshold
- **类型**: `float32`

### JumpOutOfWaterPitch
- **类型**: `float32`

### CurrentFloor
- **类型**: `FFindFloorResult`
- **描述**: Information about the floor the Character is standing on (updated only during walking movement).

### DefaultLandMovementMode
- **类型**: `EMovementMode`

### DefaultWaterMovementMode
- **类型**: `EMovementMode`

### FormerBaseVelocityDecayHalfLife
- **类型**: `float32`

### AvoidanceConsiderationRadius
- **类型**: `float32`

### AvoidanceUID
- **类型**: `int`
- **描述**: No default value, for now it's assumed to be valid if GetAvoidanceManager() returns non-NULL.

### AvoidanceWeight
- **类型**: `float32`

### NavMeshProjectionInterval
- **类型**: `float32`

### NavMeshProjectionInterpSpeed
- **类型**: `float32`

### NavMeshProjectionHeightScaleUp
- **类型**: `float32`

### NavMeshProjectionHeightScaleDown
- **类型**: `float32`

### NavWalkingFloorDistTolerance
- **类型**: `float32`

### bBasedMovementIgnorePhysicsBase
- **类型**: `bool`

### bStayBasedInAir
- **类型**: `bool`

### StayBasedInAirHeight
- **类型**: `float32`

### MovementMode
- **类型**: `EMovementMode`

### MaxAcceleration
- **类型**: `float32`

### PerchRadiusThreshold
- **类型**: `float32`

### bUseSeparateBrakingFriction
- **类型**: `bool`

### bApplyGravityWhileJumping
- **类型**: `bool`

### bUseControllerDesiredRotation
- **类型**: `bool`

### bOrientRotationToMovement
- **类型**: `bool`

### bSweepWhileNavWalking
- **类型**: `bool`

### bEnableScopedMovementUpdates
- **类型**: `bool`

### bEnableServerDualMoveScopedMovementUpdates
- **类型**: `bool`

### bRunPhysicsWithNoController
- **类型**: `bool`

### bForceNextFloorCheck
- **类型**: `bool`

### bCanWalkOffLedges
- **类型**: `bool`

### bCanWalkOffLedgesWhenCrouching
- **类型**: `bool`

### bNetworkSkipProxyPredictionOnNetUpdate
- **类型**: `bool`

### bNetworkAlwaysReplicateTransformUpdateTimestamp
- **类型**: `bool`

### bEnablePhysicsInteraction
- **类型**: `bool`

### bTouchForceScaledToMass
- **类型**: `bool`

### bPushForceScaledToMass
- **类型**: `bool`

### bPushForceUsingZOffset
- **类型**: `bool`

### bScalePushForceToVelocity
- **类型**: `bool`

### bMaintainHorizontalGroundVelocity
- **类型**: `bool`

### bImpartBaseVelocityX
- **类型**: `bool`

### bImpartBaseVelocityY
- **类型**: `bool`

### bImpartBaseVelocityZ
- **类型**: `bool`

### bImpartBaseAngularVelocity
- **类型**: `bool`

### bJustTeleported
- **类型**: `bool`

### bIgnoreClientMovementErrorChecksAndCorrection
- **类型**: `bool`

### bServerAcceptClientAuthoritativePosition
- **类型**: `bool`

### bNotifyApex
- **类型**: `bool`

### bWantsToCrouch
- **类型**: `bool`

### bCrouchMaintainsBaseLocation
- **类型**: `bool`

### bIgnoreBaseRotation
- **类型**: `bool`

### bAlwaysCheckFloor
- **类型**: `bool`

### bUseFlatBaseForFloorChecks
- **类型**: `bool`

### bUseRVOAvoidance
- **类型**: `bool`

### bRequestedMoveUseAcceleration
- **类型**: `bool`

### bAllowPhysicsRotationDuringAnimRootMotion
- **类型**: `bool`

### bProjectNavMeshWalking
- **类型**: `bool`

### bProjectNavMeshOnBothWorldChannels
- **类型**: `bool`

### AvoidanceGroup
- **类型**: `FNavAvoidanceMask`

### GroupsToAvoid
- **类型**: `FNavAvoidanceMask`

### GroupsToIgnore
- **类型**: `FNavAvoidanceMask`

## 方法

### AddForce
```angelscript
void AddForce(FVector Force)
```
Add force to character. Forces are accumulated each tick and applied together
so multiple calls to this function will accumulate.
Forces are scaled depending on timestep, so they can be applied each frame. If you want an
instantaneous force, use AddImpulse.
Adding a force always takes the actor's mass into account.
Note that changing the momentum of characters like this can change the movement mode.

@param       Force                   Force to apply.

### AddImpulse
```angelscript
void AddImpulse(FVector Impulse, bool bVelocityChange)
```
Add impulse to character. Impulses are accumulated each tick and applied together
so multiple calls to this function will accumulate.
An impulse is an instantaneous force, usually applied once. If you want to continually apply
forces each frame, use AddForce().
Note that changing the momentum of characters like this can change the movement mode.

@param       Impulse                         Impulse to apply.
@param       bVelocityChange         Whether or not the impulse is relative to mass.

### CalcVelocity
```angelscript
void CalcVelocity(float32 DeltaTime, float32 Friction, bool bFluid, float32 BrakingDeceleration)
```
Updates Velocity and Acceleration based on the current state, applying the effects of friction and acceleration or deceleration. Does not apply gravity.
This is used internally during movement updates. Normally you don't need to call this from outside code, but you might want to use it for custom movement modes.

@param       DeltaTime                                               time elapsed since last frame.
@param       Friction                                                coefficient of friction when not accelerating, or in the direction opposite acceleration.
@param       bFluid                                                  true if moving through a fluid, causing Friction to always be applied regardless of acceleration.
@param       BrakingDeceleration                             deceleration applied when not accelerating, or when exceeding max velocity.

### ClearAccumulatedForces
```angelscript
void ClearAccumulatedForces()
```
Clears forces accumulated through AddImpulse() and AddForce(), and also pending launch velocity.

### DisableMovement
```angelscript
void DisableMovement()
```
Make movement impossible (sets movement mode to MOVE_None).

### GetAnalogInputModifier
```angelscript
float32 GetAnalogInputModifier()
```
Returns modifier [0..1] based on the magnitude of the last input vector, which is used to modify the acceleration and max speed during movement.

### GetCharacterOwner
```angelscript
ACharacter GetCharacterOwner()
```
Get the Character that owns UpdatedComponent.

### GetCrouchedHalfHeight
```angelscript
float32 GetCrouchedHalfHeight()
```
Returns the collision half-height when crouching (component scale is applied separately)

### GetCurrentAcceleration
```angelscript
FVector GetCurrentAcceleration()
```
Returns current acceleration, computed from input vector each update.

### GetGravityDirection
```angelscript
FVector GetGravityDirection()
```
Returns the current gravity direction.

### GetImpartedMovementBaseVelocity
```angelscript
FVector GetImpartedMovementBaseVelocity()
```
If we have a movement base, get the velocity that should be imparted by that base, usually when jumping off of it.
Only applies the components of the velocity enabled by bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ.

### GetLastUpdateLocation
```angelscript
FVector GetLastUpdateLocation()
```
Returns the location at the end of the last tick.

### GetLastUpdateRequestedVelocity
```angelscript
FVector GetLastUpdateRequestedVelocity()
```
Returns velocity requested by path following

### GetLastUpdateRotation
```angelscript
FRotator GetLastUpdateRotation()
```
Returns the rotation at the end of the last tick.

### GetLastUpdateVelocity
```angelscript
FVector GetLastUpdateVelocity()
```
Returns the velocity at the end of the last tick.

### GetMaxAcceleration
```angelscript
float32 GetMaxAcceleration()
```
Returns maximum acceleration for the current state.

### GetMaxBrakingDeceleration
```angelscript
float32 GetMaxBrakingDeceleration()
```
Returns maximum deceleration for the current state when braking (ie when there is no acceleration).

### GetMaxJumpHeight
```angelscript
float32 GetMaxJumpHeight()
```
Compute the max jump height based on the JumpZVelocity velocity and gravity.
This does not take into account the CharacterOwner's MaxJumpHoldTime.

### GetMaxJumpHeightWithJumpTime
```angelscript
float32 GetMaxJumpHeightWithJumpTime()
```
Compute the max jump height based on the JumpZVelocity velocity and gravity.
This does take into account the CharacterOwner's MaxJumpHoldTime.

### GetMinAnalogSpeed
```angelscript
float32 GetMinAnalogSpeed()
```
Returns maximum acceleration for the current state.

### GetMovementBase
```angelscript
UPrimitiveComponent GetMovementBase()
```
Return PrimitiveComponent we are based on (standing and walking on).

### GetPerchRadiusThreshold
```angelscript
float32 GetPerchRadiusThreshold()
```
Returns The distance from the edge of the capsule within which we don't allow the character to perch on the edge of a surface.

### GetValidPerchRadius
```angelscript
float32 GetValidPerchRadius()
```
Returns the radius within which we can stand on the edge of a surface without falling (if this is a walkable surface).
Simply computed as the capsule radius minus the result of GetPerchRadiusThreshold().

### HasCustomGravity
```angelscript
bool HasCustomGravity()
```
Whether the gravity direction is different from UCharacterMovementComponent::DefaultGravityDirection.

### IsWalkable
```angelscript
bool IsWalkable(FHitResult Hit)
```
Return true if the hit result should be considered a walkable surface for the character.

### IsWalking
```angelscript
bool IsWalking()
```
Returns true if the character is in the 'Walking' movement mode.

### ComputeFloorDistance
```angelscript
void ComputeFloorDistance(FVector CapsuleLocation, float32 LineDistance, float32 SweepDistance, float32 SweepRadius, FFindFloorResult& FloorResult)
```
Compute distance to the floor from bottom sphere of capsule and store the result in FloorResult.
This distance is the swept distance of the capsule to the first point impacted by the lower hemisphere, or distance from the bottom of the capsule in the case of a line trace.
This function does not care if collision is disabled on the capsule (unlike FindFloor).

@param CapsuleLocation                Location where the capsule sweep should originate
@param LineDistance                   If non-zero, max distance to test for a simple line check from the capsule base. Used only if the sweep test fails to find a walkable floor, and only returns a valid result if the impact normal is a walkable normal.
@param SweepDistance                  If non-zero, max distance to use when sweeping a capsule downwards for the test. MUST be greater than or equal to the line distance.
@param SweepRadius                    The radius to use for sweep tests. Should be <= capsule radius.
@param FloorResult                    Result of the floor check

### FindFloor
```angelscript
void FindFloor(FVector CapsuleLocation, FFindFloorResult& FloorResult)
```
Sweeps a vertical trace to find the floor for the capsule at the given location. Will attempt to perch if ShouldComputePerchResult() returns true for the downward sweep result.
No floor will be found if collision is disabled on the capsule!

@param CapsuleLocation                Location where the capsule sweep should originate
@param FloorResult                    Result of the floor check

### GetWalkableFloorAngle
```angelscript
float32 GetWalkableFloorAngle()
```
Get the max angle in degrees of a walkable surface for the character.

### GetWalkableFloorZ
```angelscript
float32 GetWalkableFloorZ()
```
Get the Z component of the normal of the steepest walkable surface for the character. Any lower than this and it is not walkable.

### SetAvoidanceEnabled
```angelscript
void SetAvoidanceEnabled(bool bEnable)
```
Change avoidance state and registers in RVO manager if needed

### SetAvoidanceGroupMask
```angelscript
void SetAvoidanceGroupMask(FNavAvoidanceMask GroupMask)
```

### SetCrouchedHalfHeight
```angelscript
void SetCrouchedHalfHeight(float32 NewValue)
```
Sets collision half-height when crouching and updates dependent computations

### SetGravityDirection
```angelscript
void SetGravityDirection(FVector GravityDir)
```
Set a custom, local gravity direction to use during movement simulation.
The gravity direction must be synchronized by external systems between the autonomous
and authority processes. The gravity direction will be corrected as part of movement
corrections should the movement state diverge.
SetGravityDirection is responsible for initializing cached values used to tranform to
from gravity relative space.
@param GravityDir            A non-zero vector representing the new gravity direction. The vector will be normalized.

### SetGroupsToAvoidMask
```angelscript
void SetGroupsToAvoidMask(FNavAvoidanceMask GroupMask)
```

### SetGroupsToIgnoreMask
```angelscript
void SetGroupsToIgnoreMask(FNavAvoidanceMask GroupMask)
```

### SetMovementMode
```angelscript
void SetMovementMode(EMovementMode NewMovementMode, uint8 NewCustomMode)
```
Change movement mode.

@param NewMovementMode       The new movement mode
@param NewCustomMode         The new custom sub-mode, only applicable if NewMovementMode is Custom.

### SetWalkableFloorAngle
```angelscript
void SetWalkableFloorAngle(float32 InWalkableFloorAngle)
```
Set the max angle in degrees of a walkable surface for the character. Also computes WalkableFloorZ.

### SetWalkableFloorZ
```angelscript
void SetWalkableFloorZ(float32 InWalkableFloorZ)
```
Set the Z component of the normal of the steepest walkable surface for the character. Also computes WalkableFloorAngle.


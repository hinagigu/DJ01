# ACharacter

**继承自**: `APawn`

Characters are Pawns that have a mesh, collision, and built-in movement logic.
They are responsible for all physical interaction between the player or AI and the world, and also implement basic networking and input models.
They are designed for a vertically-oriented player representation that can walk, jump, fly, and swim through the world using CharacterMovementComponent.

@see APawn, UCharacterMovementComponent
@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Pawn/Character/

## 属性

### Mesh
- **类型**: `USkeletalMeshComponent`

### CharacterMovement
- **类型**: `UCharacterMovementComponent`

### CapsuleComponent
- **类型**: `UCapsuleComponent`

### CrouchedEyeHeight
- **类型**: `float32`

### JumpKeyHoldTime
- **类型**: `float32`
- **描述**: Jump key Held Time.
This is the time that the player has held the jump key, in seconds.

### JumpForceTimeRemaining
- **类型**: `float32`
- **描述**: Amount of jump force time remaining, if JumpMaxHoldTime > 0.

### ProxyJumpForceStartedTime
- **类型**: `float32`
- **描述**: Track last time a jump force started for a proxy.

### JumpMaxHoldTime
- **类型**: `float32`

### JumpMaxCount
- **类型**: `int`

### JumpCurrentCount
- **类型**: `int`
- **描述**: Tracks the current number of jumps performed.
This is incremented in CheckJumpInput, used in CanJump_Implementation, and reset in OnMovementModeChanged.
When providing overrides for these methods, it's recommended to either manually
increment / reset this value, or call the Super:: method.

### JumpCurrentCountPreJump
- **类型**: `int`
- **描述**: Represents the current number of jumps performed before CheckJumpInput modifies JumpCurrentCount.
This is set in CheckJumpInput and is used in SetMoveFor and PrepMoveFor instead of JumpCurrentCount
since CheckJumpInput can modify JumpCurrentCount.
When providing overrides for these methods, it's recommended to either manually
set this value, or call the Super:: method.

### OnReachedJumpApex
- **类型**: `FCharacterReachedApexSignature`

### LandedDelegate
- **类型**: `FLandedSignature`

### MovementModeChangedDelegate
- **类型**: `FMovementModeChangedSignature`

### OnCharacterMovementUpdated
- **类型**: `FCharacterMovementUpdatedSignature`

### bIsCrouched
- **类型**: `bool`

### bPressedJump
- **类型**: `bool`

### bWasJumping
- **类型**: `bool`

## 方法

### CacheInitialMeshOffset
```angelscript
void CacheInitialMeshOffset(FVector MeshRelativeLocation, FRotator MeshRelativeRotation)
```
Cache mesh offset from capsule. This is used as the target for network smoothing interpolation, when the mesh is offset with lagged smoothing.
This is automatically called during initialization; call this at runtime if you intend to change the default mesh offset from the capsule.
@see GetBaseTranslationOffset(), GetBaseRotationOffset()

### CanCrouch
```angelscript
bool CanCrouch()
```
@return true if this character is currently able to crouch (and is not currently crouched)

### CanJump
```angelscript
bool CanJump()
```
Check if the character can jump in the current state.

The default implementation may be overridden or extended by implementing the custom CanJump event in Blueprints.

@Return Whether the character can jump in the current state.

### CanJumpInternal
```angelscript
bool CanJumpInternal()
```
Customizable event to check if the character can jump in the current state.
Default implementation returns true if the character is on the ground and not crouching,
has a valid CharacterMovementComponent and CanEverJump() returns true.
Default implementation also allows for 'hold to jump higher' functionality:
As well as returning true when on the ground, it also returns true when GetMaxJumpTime is more
than zero and IsJumping returns true.


@Return Whether the character can jump in the current state.

### ClientAckGoodMove
```angelscript
void ClientAckGoodMove(float32 TimeStamp)
```

### ClientAdjustPosition
```angelscript
void ClientAdjustPosition(float32 TimeStamp, FVector NewLoc, FVector NewVel, UPrimitiveComponent NewBase, FName NewBaseBoneName, bool bHasBase, bool bBaseRelativePosition, uint8 ServerMovementMode)
```

### ClientAdjustRootMotionPosition
```angelscript
void ClientAdjustRootMotionPosition(float32 TimeStamp, float32 ServerMontageTrackPosition, FVector ServerLoc, FVector ServerRotation, float32 ServerVelZ, UPrimitiveComponent ServerBase, FName ServerBoneName, bool bHasBase, bool bBaseRelativePosition, uint8 ServerMovementMode)
```

### ClientCheatFly
```angelscript
void ClientCheatFly()
```

### ClientCheatGhost
```angelscript
void ClientCheatGhost()
```

### ClientCheatWalk
```angelscript
void ClientCheatWalk()
```

### ClientVeryShortAdjustPosition
```angelscript
void ClientVeryShortAdjustPosition(float32 TimeStamp, FVector NewLoc, UPrimitiveComponent NewBase, FName NewBaseBoneName, bool bHasBase, bool bBaseRelativePosition, uint8 ServerMovementMode)
```
Bandwidth saving version, when velocity is zeroed

### Crouch
```angelscript
void Crouch(bool bClientSimulation)
```
Request the character to start crouching. The request is processed on the next update of the CharacterMovementComponent.
@see OnStartCrouch
@see IsCrouched
@see CharacterMovement->WantsToCrouch

### GetAnimRootMotionTranslationScale
```angelscript
float32 GetAnimRootMotionTranslationScale()
```
Returns current value of AnimRootMotionScale

### GetBaseRotationOffset
```angelscript
FRotator GetBaseRotationOffset()
```
Get the saved rotation offset of mesh. This is how much extra rotation is applied from the capsule rotation.

### GetBaseTranslationOffset
```angelscript
FVector GetBaseTranslationOffset()
```
Get the saved translation offset of mesh. This is how much extra offset is applied from the center of the capsule.

### GetCurrentMontage
```angelscript
UAnimMontage GetCurrentMontage()
```
Return current playing Montage *

### HasAnyRootMotion
```angelscript
bool HasAnyRootMotion()
```
True if we are playing root motion from any source right now (anim root motion, root motion source)

### IsJumpProvidingForce
```angelscript
bool IsJumpProvidingForce()
```
True if jump is actively providing a force, such as when the jump key is held and the time it has been held is less than JumpMaxHoldTime.
@see CharacterMovement->IsFalling

### IsPlayingNetworkedRootMotionMontage
```angelscript
bool IsPlayingNetworkedRootMotionMontage()
```
True if we are playing Root Motion right now, through a Montage with RootMotionMode == ERootMotionMode::RootMotionFromMontagesOnly.
This means code path for networked root motion is enabled.

### IsPlayingRootMotion
```angelscript
bool IsPlayingRootMotion()
```
True if we are playing Anim root motion right now

### Jump
```angelscript
void Jump()
```
Make the character jump on the next update.
If you want your character to jump according to the time that the jump key is held,
then you can set JumpMaxHoldTime to some non-zero value. Make sure in this case to
call StopJumping() when you want the jump's z-velocity to stop being applied (such
as on a button up event), otherwise the character will carry on receiving the
velocity until JumpKeyHoldTime reaches JumpMaxHoldTime.

### OnEndCrouch
```angelscript
void OnEndCrouch(float HalfHeightAdjust, float ScaledHalfHeightAdjust)
```
Event when Character stops crouching.
@param       HalfHeightAdjust                difference between default collision half-height, and actual crouched capsule half-height.
@param       ScaledHalfHeightAdjust  difference after component scale is taken in to account.

### OnMovementModeChanged
```angelscript
void OnMovementModeChanged(EMovementMode PrevMovementMode, EMovementMode NewMovementMode, uint8 PrevCustomMode, uint8 NewCustomMode)
```
Called from CharacterMovementComponent to notify the character that the movement mode has changed.
@param       PrevMovementMode        Movement mode before the change
@param       NewMovementMode         New movement mode
@param       PrevCustomMode          Custom mode before the change (applicable if PrevMovementMode is Custom)
@param       NewCustomMode           New custom mode (applicable if NewMovementMode is Custom)

### OnStartCrouch
```angelscript
void OnStartCrouch(float HalfHeightAdjust, float ScaledHalfHeightAdjust)
```
Event when Character crouches.
@param       HalfHeightAdjust                difference between default collision half-height, and actual crouched capsule half-height.
@param       ScaledHalfHeightAdjust  difference after component scale is taken in to account.

### UpdateCustomMovement
```angelscript
void UpdateCustomMovement(float DeltaTime)
```
Event for implementing custom character movement mode. Called by CharacterMovement if MovementMode is set to Custom.
@note C++ code should override UCharacterMovementComponent::PhysCustom() instead.
@see UCharacterMovementComponent::PhysCustom()

### LaunchCharacter
```angelscript
void LaunchCharacter(FVector LaunchVelocity, bool bXYOverride, bool bZOverride)
```
Set a pending launch velocity on the Character. This velocity will be processed on the next CharacterMovementComponent tick,
and will set it to the "falling" state. Triggers the OnLaunched event.
@PARAM LaunchVelocity is the velocity to impart to the Character
@PARAM bXYOverride if true replace the XY part of the Character's velocity instead of adding to it.
@PARAM bZOverride if true replace the Z component of the Character's velocity instead of adding to it.

### OnJumped
```angelscript
void OnJumped()
```
Event fired when the character has just started jumping

### OnLanded
```angelscript
void OnLanded(FHitResult Hit)
```
Called upon landing when falling, to perform actions based on the Hit result.
Note that movement mode is still "Falling" during this event. Current Velocity value is the velocity at the time of landing.
Consider OnMovementModeChanged() as well, as that can be used once the movement mode changes to the new mode (most likely Walking).

@param Hit Result describing the landing that resulted in a valid landing spot.
@see OnMovementModeChanged()

### OnLaunched
```angelscript
void OnLaunched(FVector LaunchVelocity, bool bXYOverride, bool bZOverride)
```
Let blueprint know that we were launched

### OnWalkingOffLedge
```angelscript
void OnWalkingOffLedge(FVector PreviousFloorImpactNormal, FVector PreviousFloorContactNormal, FVector PreviousLocation, float TimeDelta)
```
Event fired when the Character is walking off a surface and is about to fall because CharacterMovement->CurrentFloor became unwalkable.
If CharacterMovement->MovementMode does not change during this event then the character will automatically start falling afterwards.
@note Z velocity is zero during walking movement, and will be here as well. Another velocity can be computed here if desired and will be used when starting to fall.

@param  PreviousFloorImpactNormal Normal of the previous walkable floor.
@param  PreviousFloorContactNormal Normal of the contact with the previous walkable floor.
@param  PreviousLocation     Previous character location before movement off the ledge.
@param  TimeTick     Time delta of movement update resulting in moving off the ledge.

### PlayAnimMontage
```angelscript
float32 PlayAnimMontage(UAnimMontage AnimMontage, float32 InPlayRate, FName StartSectionName)
```
Play Animation Montage on the character mesh. Returns the length of the animation montage in seconds, or 0.f if failed to play. *

### RootMotionDebugClientPrintOnScreen
```angelscript
void RootMotionDebugClientPrintOnScreen(FString InString)
```

### ServerMove
```angelscript
void ServerMove(float32 TimeStamp, FVector InAccel, FVector ClientLoc, uint8 CompressedMoveFlags, uint8 ClientRoll, uint View, UPrimitiveComponent ClientMovementBase, FName ClientBaseBoneName, uint8 ClientMovementMode)
```

### ServerMoveDual
```angelscript
void ServerMoveDual(float32 TimeStamp0, FVector InAccel0, uint8 PendingFlags, uint View0, float32 TimeStamp, FVector InAccel, FVector ClientLoc, uint8 NewFlags, uint8 ClientRoll, uint View, UPrimitiveComponent ClientMovementBase, FName ClientBaseBoneName, uint8 ClientMovementMode)
```

### ServerMoveDualHybridRootMotion
```angelscript
void ServerMoveDualHybridRootMotion(float32 TimeStamp0, FVector InAccel0, uint8 PendingFlags, uint View0, float32 TimeStamp, FVector InAccel, FVector ClientLoc, uint8 NewFlags, uint8 ClientRoll, uint View, UPrimitiveComponent ClientMovementBase, FName ClientBaseBoneName, uint8 ClientMovementMode)
```

### ServerMoveDualNoBase
```angelscript
void ServerMoveDualNoBase(float32 TimeStamp0, FVector InAccel0, uint8 PendingFlags, uint View0, float32 TimeStamp, FVector InAccel, FVector ClientLoc, uint8 NewFlags, uint8 ClientRoll, uint View, uint8 ClientMovementMode)
```

### ServerMoveNoBase
```angelscript
void ServerMoveNoBase(float32 TimeStamp, FVector InAccel, FVector ClientLoc, uint8 CompressedMoveFlags, uint8 ClientRoll, uint View, uint8 ClientMovementMode)
```

### ServerMoveOld
```angelscript
void ServerMoveOld(float32 OldTimeStamp, FVector OldAccel, uint8 OldMoveFlags)
```

### StopAnimMontage
```angelscript
void StopAnimMontage(UAnimMontage AnimMontage)
```
Stop Animation Montage. If nullptr, it will stop what's currently active. The Blend Out Time is taken from the montage asset that is being stopped. *

### StopJumping
```angelscript
void StopJumping()
```
Stop the character from jumping on the next update.
Call this from an input event (such as a button 'up' event) to cease applying
jump Z-velocity. If this is not called, then jump z-velocity will be applied
until JumpMaxHoldTime is reached.

### UnCrouch
```angelscript
void UnCrouch(bool bClientSimulation)
```
Request the character to stop crouching. The request is processed on the next update of the CharacterMovementComponent.
@see OnEndCrouch
@see IsCrouched
@see CharacterMovement->WantsToCrouch


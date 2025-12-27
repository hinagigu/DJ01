# APawn

**继承自**: `AActor`

Pawn is the base class of all actors that can be possessed by players or AI.
They are the physical representations of players and creatures in a level.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Pawn/

## 属性

### BaseEyeHeight
- **类型**: `float32`

### AutoPossessPlayer
- **类型**: `EAutoReceiveInput`
- **描述**: Determines which PlayerController, if any, should automatically possess the pawn when the level starts or when the pawn is spawned.
@see AutoPossessAI

### AutoPossessAI
- **类型**: `EAutoPossessAI`
- **描述**: Determines when the Pawn creates and is possessed by an AI Controller (on level start, when spawned, etc).
Only possible if AIControllerClassRef is set, and ignored if AutoPossessPlayer is enabled.
@see AutoPossessPlayer

### AIControllerClass
- **类型**: `TSubclassOf<AController>`

### PlayerState
- **类型**: `APlayerState`
- **描述**: If Pawn is possessed by a player, points to its Player State.  Needed for network play as controllers are not replicated to clients.

### LastHitBy
- **类型**: `AController`
- **描述**: Controller of the last Actor that caused us damage.

### ReceiveControllerChangedDelegate
- **类型**: `FPawnControllerChangedSignature`

### ReceiveRestartedDelegate
- **类型**: `FPawnRestartedSignature`

### bUseControllerRotationPitch
- **类型**: `bool`

### bUseControllerRotationYaw
- **类型**: `bool`

### bUseControllerRotationRoll
- **类型**: `bool`

### bCanAffectNavigationGeneration
- **类型**: `bool`

### OverrideInputComponentClass
- **类型**: `TSubclassOf<UInputComponent>`

## 方法

### AddControllerPitchInput
```angelscript
void AddControllerPitchInput(float32 Val)
```
Add input (affecting Pitch) to the Controller's ControlRotation, if it is a local PlayerController.
This value is multiplied by the PlayerController's InputPitchScale value.
@param Val Amount to add to Pitch. This value is multiplied by the PlayerController's InputPitchScale value.
@see PlayerController::InputPitchScale

### AddControllerRollInput
```angelscript
void AddControllerRollInput(float32 Val)
```
Add input (affecting Roll) to the Controller's ControlRotation, if it is a local PlayerController.
This value is multiplied by the PlayerController's InputRollScale value.
@param Val Amount to add to Roll. This value is multiplied by the PlayerController's InputRollScale value.
@see PlayerController::InputRollScale

### AddControllerYawInput
```angelscript
void AddControllerYawInput(float32 Val)
```
Add input (affecting Yaw) to the Controller's ControlRotation, if it is a local PlayerController.
This value is multiplied by the PlayerController's InputYawScale value.
@param Val Amount to add to Yaw. This value is multiplied by the PlayerController's InputYawScale value.
@see PlayerController::InputYawScale

### AddMovementInput
```angelscript
void AddMovementInput(FVector WorldDirection, float32 ScaleValue, bool bForce)
```
Add movement input along the given world direction vector (usually normalized) scaled by 'ScaleValue'. If ScaleValue < 0, movement will be in the opposite direction.
Base Pawn classes won't automatically apply movement, it's up to the user to do so in a Tick event. Subclasses such as Character and DefaultPawn automatically handle this input and move.

@param WorldDirection        Direction in world space to apply input
@param ScaleValue            Scale to apply to input. This can be used for analog input, ie a value of 0.5 applies half the normal value, while -1.0 would reverse the direction.
@param bForce                        If true always add the input, ignoring the result of IsMoveInputIgnored().
@see GetPendingMovementInputVector(), GetLastMovementInputVector(), ConsumeMovementInputVector()

### ConsumeMovementInputVector
```angelscript
FVector ConsumeMovementInputVector()
```
Returns the pending input vector and resets it to zero.
This should be used during a movement update (by the Pawn or PawnMovementComponent) to prevent accumulation of control input between frames.
Copies the pending input vector to the saved input vector (GetLastMovementInputVector()).
@return The pending input vector.

### DetachFromControllerPendingDestroy
```angelscript
void DetachFromControllerPendingDestroy()
```
Call this function to detach safely pawn from its controller, knowing that we will be destroyed soon.

### GetBaseAimRotation
```angelscript
FRotator GetBaseAimRotation()
```
Return the aim rotation for the Pawn.
If we have a controller, by default we aim at the player's 'eyes' direction
that is by default the Pawn rotation for AI, and camera (crosshair) rotation for human players.

### GetController
```angelscript
AController GetController()
```
Returns controller for this actor.

### GetControlRotation
```angelscript
FRotator GetControlRotation()
```
Get the rotation of the Controller, often the 'view' rotation of this Pawn.

### GetLastMovementInputVector
```angelscript
FVector GetLastMovementInputVector()
```
Return the last input vector in world space that was processed by ConsumeMovementInputVector(), which is usually done by the Pawn or PawnMovementComponent.
Any user that needs to know about the input that last affected movement should use this function.
For example an animation update would want to use this, since by default the order of updates in a frame is:
PlayerController (device input) -> MovementComponent -> Pawn -> Mesh (animations)

@return The last input vector in world space that was processed by ConsumeMovementInputVector().
@see AddMovementInput(), GetPendingMovementInputVector(), ConsumeMovementInputVector()

### GetLocalViewingPlayerController
```angelscript
APlayerController GetLocalViewingPlayerController()
```
Returns local Player Controller viewing this pawn, whether it is controlling or spectating

### GetMovementComponent
```angelscript
UPawnMovementComponent GetMovementComponent()
```
Return our PawnMovementComponent, if we have one.

### GetNavAgentLocation
```angelscript
FVector GetNavAgentLocation()
```
Basically retrieved pawn's location on navmesh

### GetOverrideInputComponentClass
```angelscript
TSubclassOf<UInputComponent> GetOverrideInputComponentClass()
```

### GetPendingMovementInputVector
```angelscript
FVector GetPendingMovementInputVector()
```
Return the pending input vector in world space. This is the most up-to-date value of the input vector, pending ConsumeMovementInputVector() which clears it,
Usually only a PawnMovementComponent will want to read this value, or the Pawn itself if it is responsible for movement.

@return The pending input vector in world space.
@see AddMovementInput(), GetLastMovementInputVector(), ConsumeMovementInputVector()

### GetPlatformUserId
```angelscript
FPlatformUserId GetPlatformUserId()
```
Returns the Platform User ID of the PlayerController that is controlling this character.

Returns an invalid Platform User ID if this character is not controlled by a local player.

### IsBotControlled
```angelscript
bool IsBotControlled()
```
Returns true if controlled by a bot.

### IsControlled
```angelscript
bool IsControlled()
```

### IsLocallyControlled
```angelscript
bool IsLocallyControlled()
```
Returns true if controlled by a local (not network) Controller.

### IsLocallyViewed
```angelscript
bool IsLocallyViewed()
```
Is this pawn the ViewTarget of a local PlayerController?  Helpful for determining whether the pawn is
visible/critical for any VFX.  NOTE: Technically there may be some cases where locally controlled pawns return
false for this, such as if you are using a remote camera view of some sort.  But generally it will be true for
locally controlled pawns, and it will always be true for pawns that are being spectated in-game or in Replays.

### IsMoveInputIgnored
```angelscript
bool IsMoveInputIgnored()
```
Helper to see if move input is ignored. If our controller is a PlayerController, checks Controller->IsMoveInputIgnored().

### IsPawnControlled
```angelscript
bool IsPawnControlled()
```
Check if this actor is currently being controlled at all (the actor has a valid Controller, which will be false for remote clients)

### IsPlayerControlled
```angelscript
bool IsPlayerControlled()
```
Returns true if controlled by a human player (possessed by a PlayerController).        This returns true for players controlled by remote clients

### PawnMakeNoise
```angelscript
void PawnMakeNoise(float32 Loudness, FVector NoiseLocation, bool bUseNoiseMakerLocation, AActor NoiseMaker)
```
Inform AIControllers that you've made a noise they might hear (they are sent a HearNoise message if they have bHearNoises==true)
The instigator of this sound is the pawn which is used to call MakeNoise.

@param Loudness - is the relative loudness of this noise (range 0.0 to 1.0).  Directly affects the hearing range specified by the AI's HearingThreshold.
@param NoiseLocation - Position of noise source.  If zero vector, use the actor's location.
@param bUseNoiseMakerLocation - If true, use the location of the NoiseMaker rather than NoiseLocation.  If false, use NoiseLocation.
@param NoiseMaker - Which actor is the source of the noise.  Not to be confused with the Noise Instigator, which is responsible for the noise (and is the pawn on which this function is called).  If not specified, the pawn instigating the noise will be used as the NoiseMaker

### ControllerChanged
```angelscript
void ControllerChanged(AController OldController, AController NewController)
```
Event called after a pawn's controller has changed, on the server and owning client. This will happen at the same time as the delegate on GameInstance

### Possessed
```angelscript
void Possessed(AController NewController)
```
Event called when the Pawn is possessed by a Controller. Only called on the server (or in standalone)

### Restarted
```angelscript
void Restarted()
```
Event called after a pawn has been restarted, usually by a possession change. This is called on the server for all pawns and the owning client for player pawns

### Unpossessed
```angelscript
void Unpossessed(AController OldController)
```
Event called when the Pawn is no longer possessed by a Controller. Only called on the server (or in standalone)

### SetCanAffectNavigationGeneration
```angelscript
void SetCanAffectNavigationGeneration(bool bNewValue, bool bForceUpdate)
```
Use SetCanAffectNavigationGeneration to change this value at runtime.
Note that calling this function at runtime will result in any navigation change only if runtime navigation generation is enabled.

### SpawnDefaultController
```angelscript
void SpawnDefaultController()
```
Spawn default controller for this Pawn, and get possessed by it.


# APlayerController

**继承自**: `AController`

PlayerControllers are used by human players to control Pawns.

ControlRotation (accessed via GetControlRotation()), determines the aiming
orientation of the controlled Pawn.

In networked games, PlayerControllers exist on the server for every player-controlled pawn,
and also on the controlling client's machine. They do NOT exist on a client's
machine for pawns controlled by remote players elsewhere on the network.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Controller/PlayerController/

## 属性

### PlayerCameraManager
- **类型**: `APlayerCameraManager`
- **描述**: Camera manager associated with this Player Controller.

### PlayerCameraManagerClass
- **类型**: `TSubclassOf<APlayerCameraManager>`

### bAutoManageActiveCameraTarget
- **类型**: `bool`
- **描述**: True to allow this player controller to manage the camera target for you,
typically by using the possessed pawn as the camera target. Set to false
if you want to manually control the camera target.

### SmoothTargetViewRotationSpeed
- **类型**: `float32`

### CheatManager
- **类型**: `UCheatManager`
- **描述**: Object that manages "cheat" commands.

By default:
      - In Shipping configurations, the manager is always disabled because UE_WITH_CHEAT_MANAGER is 0
  - When playing in the editor, cheats are always enabled
  - In other cases, cheats are enabled by default in single player games but can be forced on with the EnableCheats console command

This behavior can be changed either by overriding APlayerController::EnableCheats or AGameModeBase::AllowCheats.

### CheatClass
- **类型**: `TSubclassOf<UCheatManager>`

### StreamingSourceDebugColor
- **类型**: `FColor`

### ClickEventKeys
- **类型**: `TArray<FKey>`

### DefaultMouseCursor
- **类型**: `EMouseCursor`

### CurrentMouseCursor
- **类型**: `EMouseCursor`
- **描述**: Currently visible mouse cursor

### DefaultClickTraceChannel
- **类型**: `ECollisionChannel`

### CurrentClickTraceChannel
- **类型**: `ECollisionChannel`
- **描述**: Trace channel currently being used for determining what world object was clicked on.

### HitResultTraceDistance
- **类型**: `float32`

### bEnableMotionControls
- **类型**: `bool`

### bPlayerIsWaiting
- **类型**: `bool`

### bShowMouseCursor
- **类型**: `bool`

### bEnableClickEvents
- **类型**: `bool`

### bEnableTouchEvents
- **类型**: `bool`

### bEnableMouseOverEvents
- **类型**: `bool`

### bEnableTouchOverEvents
- **类型**: `bool`

### bForceFeedbackEnabled
- **类型**: `bool`

### bEnableStreamingSource
- **类型**: `bool`

### bStreamingSourceShouldActivate
- **类型**: `bool`

### bStreamingSourceShouldBlockOnSlowStreaming
- **类型**: `bool`

### StreamingSourcePriority
- **类型**: `EStreamingSourcePriority`

### StreamingSourceShapes
- **类型**: `TArray<FStreamingSourceShape>`

### bShouldPerformFullTickWhenPaused
- **类型**: `bool`

### OverridePlayerInputClass
- **类型**: `TSubclassOf<UPlayerInput>`

## 方法

### SetPlayer
```angelscript
void SetPlayer(UPlayer InPlayer)
```

### GetLocalPlayer
```angelscript
ULocalPlayer GetLocalPlayer()
```

### ActivateTouchInterface
```angelscript
void ActivateTouchInterface(UTouchInterface NewTouchInterface)
```
Activates a new touch interface for this player controller

### AddPitchInput
```angelscript
void AddPitchInput(float32 Val)
```
Add Pitch (look up) input. This value is multiplied by InputPitchScale.
@param Val Amount to add to Pitch. This value is multiplied by InputPitchScale.

### AddRollInput
```angelscript
void AddRollInput(float32 Val)
```
Add Roll input. This value is multiplied by InputRollScale.
@param Val Amount to add to Roll. This value is multiplied by InputRollScale.

### AddYawInput
```angelscript
void AddYawInput(float32 Val)
```
Add Yaw (turn) input. This value is multiplied by InputYawScale.
@param Val Amount to add to Yaw. This value is multiplied by InputYawScale.

### CanRestartPlayer
```angelscript
bool CanRestartPlayer()
```
Returns true if this controller thinks it's able to restart. Called from GameModeBase::PlayerCanRestart

### ClearAudioListenerAttenuationOverride
```angelscript
void ClearAudioListenerAttenuationOverride()
```

### ClearAudioListenerOverride
```angelscript
void ClearAudioListenerOverride()
```
Clear any overrides that have been applied to audio listener

### ClientAckTimeDilation
```angelscript
void ClientAckTimeDilation(float32 TimeDilation, int ServerStep)
```
Client receives the time dilation value it needs to use to keep its ServerFrame to LocalFrame offset in sync

### ClientAddTextureStreamingLoc
```angelscript
void ClientAddTextureStreamingLoc(FVector InLoc, float32 Duration, bool bOverrideLocation)
```
Adds a location to the texture streaming system for the specified duration.

### ClientCancelPendingMapChange
```angelscript
void ClientCancelPendingMapChange()
```
Tells client to cancel any pending map change.

### ClientCapBandwidth
```angelscript
void ClientCapBandwidth(int Cap)
```
Set CurrentNetSpeed to the lower of its current value and Cap.

### ClientClearCameraLensEffects
```angelscript
void ClientClearCameraLensEffects()
```
Removes all Camera Lens Effects.

### ClientCommitMapChange
```angelscript
void ClientCommitMapChange()
```
Actually performs the level transition prepared by PrepareMapChange().

### ClientEnableNetworkVoice
```angelscript
void ClientEnableNetworkVoice(bool bEnable)
```
Tell the client to enable or disable voice chat (not muting)
@param bEnable enable or disable voice chat

### ClientEndOnlineSession
```angelscript
void ClientEndOnlineSession()
```
Notify client that the session is about to start

### ClientFlushLevelStreaming
```angelscript
void ClientFlushLevelStreaming()
```
Tells the client to block until all pending level streaming actions are complete
happens at the end of the tick
primarily used to force update the client ASAP at join time

### ClientForceGarbageCollection
```angelscript
void ClientForceGarbageCollection()
```
Forces GC at the end of the tick on the client

### ClientGameEnded
```angelscript
void ClientGameEnded(AActor EndGameFocus, bool bIsWinner)
```
Replicated function called by GameHasEnded().
@param       EndGameFocus - actor to view with camera
@param       bIsWinner - true if this controller is on winning team

### ClientGotoState
```angelscript
void ClientGotoState(FName NewState)
```
Server uses this to force client into NewState .
@Note ALL STATE NAMES NEED TO BE DEFINED IN name table in UnrealNames.h to be correctly replicated (so they are mapped to the same thing on client and server).

### ClientIgnoreLookInput
```angelscript
void ClientIgnoreLookInput(bool bIgnore)
```
Calls IgnoreLookInput on client

### ClientIgnoreMoveInput
```angelscript
void ClientIgnoreMoveInput(bool bIgnore)
```
Calls IgnoreMoveInput on client

### ClientMessage
```angelscript
void ClientMessage(FString S, FName Type, float32 MsgLifeTime)
```
Outputs a message to HUD
@param S - message to display
@param Type - @todo document
@param MsgLifeTime - Optional length of time to display 0 = default time

### ClientMutePlayer
```angelscript
void ClientMutePlayer(FUniqueNetIdRepl PlayerId)
```
Tell the client to mute a player for this controller
@param PlayerId player id to mute

### ClientPlaySound
```angelscript
void ClientPlaySound(USoundBase Sound, float32 VolumeMultiplier, float32 PitchMultiplier)
```
Play sound client-side (so only the client will hear it)
@param Sound - Sound to play
@param VolumeMultiplier - Volume multiplier to apply to the sound
@param PitchMultiplier - Pitch multiplier to apply to the sound

### ClientPlaySoundAtLocation
```angelscript
void ClientPlaySoundAtLocation(USoundBase Sound, FVector Location, float32 VolumeMultiplier, float32 PitchMultiplier)
```
Play sound client-side at the specified location
@param Sound - Sound to play
@param Location - Location to play the sound at
@param VolumeMultiplier - Volume multiplier to apply to the sound
@param PitchMultiplier - Pitch multiplier to apply to the sound

### ClientPrepareMapChange
```angelscript
void ClientPrepareMapChange(FName LevelName, bool bFirst, bool bLast)
```
Asynchronously loads the given level in preparation for a streaming map transition.
the server sends one function per level name since dynamic arrays can't be replicated
@param LevelNames - the names of the level packages to load. LevelNames[0] will be the new persistent (primary) level
@param bFirst - whether this is the first item in the list (so clear the list first)
@param bLast - whether this is the last item in the list (so start preparing the change after receiving it)

### ClientPrestreamTextures
```angelscript
void ClientPrestreamTextures(AActor ForcedActor, float32 ForceDuration, bool bEnableStreaming, int CinematicTextureGroups)
```
Forces the streaming system to disregard the normal logic for the specified duration and
instead always load all mip-levels for all textures used by the specified actor.
@param ForcedActor           - The actor whose textures should be forced into memory.
@param ForceDuration         - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic.
@param bEnableStreaming      - Whether to start (true) or stop (false) streaming
@param CinematicTextureGroups        - Bitfield indicating which texture groups that use extra high-resolution mips

### ClientReceiveLocalizedMessage
```angelscript
void ClientReceiveLocalizedMessage(TSubclassOf<ULocalMessage> Message, int Switch, APlayerState RelatedPlayerState_1, APlayerState RelatedPlayerState_2, UObject OptionalObject)
```
send client localized message id

### ClientRecvServerAckFrame
```angelscript
void ClientRecvServerAckFrame(int LastProcessedInputFrame, int RecvServerFrameNumber, int8 TimeDilation)
```

### ClientRecvServerAckFrameDebug
```angelscript
void ClientRecvServerAckFrameDebug(uint8 NumBuffered, float32 TargetNumBufferedCmds)
```

### ClientRepObjRef
```angelscript
void ClientRepObjRef(UObject Object)
```
Development RPC for testing object reference replication

### ClientReset
```angelscript
void ClientReset()
```
Tell client to reset the PlayerController

### ClientRestart
```angelscript
void ClientRestart(APawn NewPawn)
```
Tell client to restart the level

### ClientRetryClientRestart
```angelscript
void ClientRetryClientRestart(APawn NewPawn)
```
Assign Pawn to player, but avoid calling ClientRestart if we have already accepted this pawn

### ClientReturnToMainMenuWithTextReason
```angelscript
void ClientReturnToMainMenuWithTextReason(FText ReturnReason)
```
Return the client to the main menu gracefully

### ClientSetBlockOnAsyncLoading
```angelscript
void ClientSetBlockOnAsyncLoading()
```
Tells the client to block until all pending level streaming actions are complete.
Happens at the end of the tick primarily used to force update the client ASAP at join time.

### ClientSetCameraFade
```angelscript
void ClientSetCameraFade(bool bEnableFading, FColor FadeColor, FVector2D FadeAlpha, float32 FadeTime, bool bFadeAudio, bool bHoldWhenFinished)
```
Tell client to fade camera
@Param bEnableFading - true if we should apply FadeColor/FadeAmount to the screen
@Param FadeColor - Color to fade to
@Param FadeAlpha - Contains the start fade (X) and end fade (Y) values to apply. A start fade of less than 0 will use the screen's current fade value
@Param FadeTime - length of time for fade to occur over
@Param bFadeAudio - true to apply fading of audio alongside the video
@param bHoldWhenFinished - True for fade to hold at the ToAlpha until fade is disabled

### ClientSetCameraMode
```angelscript
void ClientSetCameraMode(FName NewCamMode)
```
Replicated function to set camera style on client
@param       NewCamMode, name defining the new camera mode

### ClientSetCinematicMode
```angelscript
void ClientSetCinematicMode(bool bInCinematicMode, bool bAffectsMovement, bool bAffectsTurning, bool bAffectsHUD)
```
Called by the server to synchronize cinematic transitions with the client

### ClientSetForceMipLevelsToBeResident
```angelscript
void ClientSetForceMipLevelsToBeResident(UMaterialInterface Material, float32 ForceDuration, int CinematicTextureGroups)
```
Forces the streaming system to disregard the normal logic for the specified duration and
instead always load all mip-levels for all textures used by the specified material.

@param Material              - The material whose textures should be forced into memory.
@param ForceDuration - Number of seconds to keep all mip-levels in memory, disregarding the normal priority logic.
@param CinematicTextureGroups        - Bitfield indicating which texture groups that use extra high-resolution mips

### ClientSetHUD
```angelscript
void ClientSetHUD(TSubclassOf<AHUD> NewHUDClass)
```
Set the client's class of HUD and spawns a new instance of it. If there was already a HUD active, it is destroyed.

### ClientSetSpectatorWaiting
```angelscript
void ClientSetSpectatorWaiting(bool bWaiting)
```
Indicate that the Spectator is waiting to join/respawn.

### ClientSetViewTarget
```angelscript
void ClientSetViewTarget(AActor A, FViewTargetTransitionParams TransitionParams)
```
Set the view target
@param A - new actor to set as view target
@param TransitionParams - parameters to use for controlling the transition

### ClientSpawnGenericCameraLensEffect
```angelscript
void ClientSpawnGenericCameraLensEffect(TSubclassOf<AActor> LensEffectEmitterClass)
```
Spawn a camera lens effect (e.g. blood).

### ClientStartCameraShake
```angelscript
void ClientStartCameraShake(TSubclassOf<UCameraShakeBase> Shake, float32 Scale, ECameraShakePlaySpace PlaySpace, FRotator UserPlaySpaceRot)
```
Play Camera Shake
@param Shake - Camera shake animation to play
@param Scale - Scalar defining how "intense" to play the anim
@param PlaySpace - Which coordinate system to play the shake in (used for CameraAnims within the shake).
@param UserPlaySpaceRot - Matrix used when PlaySpace = CAPS_UserDefined

### ClientStartCameraShakeFromSource
```angelscript
void ClientStartCameraShakeFromSource(TSubclassOf<UCameraShakeBase> Shake, UCameraShakeSourceComponent SourceComponent)
```
Play Camera Shake localized to a given source
@param Shake - Camera shake animation to play
@param SourceComponent - The source from which the camera shakes originates

### ClientStartOnlineSession
```angelscript
void ClientStartOnlineSession()
```
Notify client that the session is starting

### ClientStopCameraShake
```angelscript
void ClientStopCameraShake(TSubclassOf<UCameraShakeBase> Shake, bool bImmediately)
```
Stop camera shake on client.

### ClientStopCameraShakesFromSource
```angelscript
void ClientStopCameraShakesFromSource(UCameraShakeSourceComponent SourceComponent, bool bImmediately)
```
Stop camera shake on client.

### ClientStopForceFeedback
```angelscript
void ClientStopForceFeedback(UForceFeedbackEffect ForceFeedbackEffect, FName Tag)
```
Stops a playing force feedback pattern
@param       ForceFeedbackEffect             If set only patterns from that effect will be stopped
@param       Tag                                             If not none only the pattern with this tag will be stopped

### ClientTeamMessage
```angelscript
void ClientTeamMessage(APlayerState SenderPlayerState, FString S, FName Type, float32 MsgLifeTime)
```
@todo document

### ClientTravelInternal
```angelscript
void ClientTravelInternal(FString URL, ETravelType TravelType, bool bSeamless, FGuid MapPackageGuid)
```
Internal clientside implementation of ClientTravel - use ClientTravel to call this

@param URL                           A string containing the mapname (or IP address) to travel to, along with option key/value pairs
@param TravelType            specifies whether the client should append URL options used in previous travels; if true is specified
                                                     for the bSeamlesss parameter, this value must be TRAVEL_Relative.
@param bSeamless                     Indicates whether to use seamless travel (requires TravelType of TRAVEL_Relative)
@param MapPackageGuid        The GUID of the map package to travel to - this is used to find the file when it has been autodownloaded,
                                                     so it is only needed for clients

### ClientUnmutePlayer
```angelscript
void ClientUnmutePlayer(FUniqueNetIdRepl PlayerId)
```
Tell the client to unmute a player for this controller
@param PlayerId player id to unmute

### ClientUnmutePlayers
```angelscript
void ClientUnmutePlayers(TArray<FUniqueNetIdRepl> PlayerIds)
```
Tell the client to unmute an array of players for this controller
@param PlayerIds player ids to unmute

### ClientVoiceHandshakeComplete
```angelscript
void ClientVoiceHandshakeComplete()
```
Tells the client that the server has all the information it needs and that it
is ok to start sending voice packets. The server will already send voice packets
when this function is called, since it is set server side and then forwarded

NOTE: This is done as an RPC instead of variable replication because ordering matters

### ClientWasKicked
```angelscript
void ClientWasKicked(FText KickReason)
```
Notify client they were kicked from the server

### DeprojectMousePositionToWorld
```angelscript
bool DeprojectMousePositionToWorld(FVector& WorldLocation, FVector& WorldDirection)
```
Convert current mouse 2D position to World Space 3D position and direction. Returns false if unable to determine value. *

### DeprojectScreenPositionToWorld
```angelscript
bool DeprojectScreenPositionToWorld(float32 ScreenX, float32 ScreenY, FVector& WorldLocation, FVector& WorldDirection)
```
Convert 2D screen position to World Space 3D position and direction. Returns false if unable to determine value. *

### GetAsyncPhysicsDataToConsume
```angelscript
const UAsyncPhysicsData GetAsyncPhysicsDataToConsume()
```

### GetAsyncPhysicsDataToWrite
```angelscript
UAsyncPhysicsData GetAsyncPhysicsDataToWrite()
```

### GetDeprecatedInputPitchScale
```angelscript
float32 GetDeprecatedInputPitchScale()
```

### GetDeprecatedInputRollScale
```angelscript
float32 GetDeprecatedInputRollScale()
```

### GetDeprecatedInputYawScale
```angelscript
float32 GetDeprecatedInputYawScale()
```

### GetFocalLocation
```angelscript
FVector GetFocalLocation()
```
Returns the location the PlayerController is focused on.
 If there is a possessed Pawn, returns the Pawn's location.
 If there is a spectator Pawn, returns that Pawn's location.
 Otherwise, returns the PlayerController's spawn location (usually the last known Pawn location after it has died).

### GetHitResultUnderCursorByChannel
```angelscript
bool GetHitResultUnderCursorByChannel(ETraceTypeQuery TraceChannel, bool bTraceComplex, FHitResult& HitResult)
```
Performs a collision query under the mouse cursor, looking on a trace channel

### GetHitResultUnderCursorForObjects
```angelscript
bool GetHitResultUnderCursorForObjects(TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, FHitResult& HitResult)
```
Performs a collision query under the mouse cursor, looking for object types

### GetHitResultUnderFingerByChannel
```angelscript
bool GetHitResultUnderFingerByChannel(ETouchIndex FingerIndex, ETraceTypeQuery TraceChannel, bool bTraceComplex, FHitResult& HitResult)
```
Performs a collision query under the finger, looking on a trace channel

### GetHitResultUnderFingerForObjects
```angelscript
bool GetHitResultUnderFingerForObjects(ETouchIndex FingerIndex, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, FHitResult& HitResult)
```
Performs a collision query under the finger, looking for object types

### GetHUD
```angelscript
AHUD GetHUD()
```
Gets the HUD currently being used by this player controller

### GetInputAnalogKeyState
```angelscript
float32 GetInputAnalogKeyState(FKey Key)
```
Returns the analog value for the given key/button.  If analog isn't supported, returns 1 for down and 0 for up.

### GetInputAnalogStickState
```angelscript
void GetInputAnalogStickState(EControllerAnalogStick WhichStick, float32& StickX, float32& StickY)
```
Retrieves the X and Y displacement of the given analog stick.

### GetInputKeyTimeDown
```angelscript
float32 GetInputKeyTimeDown(FKey Key)
```
Returns how long the given key/button has been down.  Returns 0 if it's up or it just went down this frame.

### GetInputMotionState
```angelscript
void GetInputMotionState(FVector& Tilt, FVector& RotationRate, FVector& Gravity, FVector& Acceleration)
```
Retrieves the current motion state of the player's input device

### GetInputMouseDelta
```angelscript
void GetInputMouseDelta(float32& DeltaX, float32& DeltaY)
```
Retrieves how far the mouse moved this frame.

### GetInputTouchState
```angelscript
void GetInputTouchState(ETouchIndex FingerIndex, float32& LocationX, float32& LocationY, bool& bIsCurrentlyPressed)
```
Retrieves the X and Y screen coordinates of the specified touch key. Returns false if the touch index is not down

### GetInputVectorKeyState
```angelscript
FVector GetInputVectorKeyState(FKey Key)
```
Returns the vector value for the given key/button.

### GetMousePosition
```angelscript
bool GetMousePosition(float32& LocationX, float32& LocationY)
```
Retrieves the X and Y screen coordinates of the mouse cursor. Returns false if there is no associated mouse device

### GetOverridePlayerInputClass
```angelscript
TSubclassOf<UPlayerInput> GetOverridePlayerInputClass()
```

### GetPlatformUserId
```angelscript
FPlatformUserId GetPlatformUserId()
```
Returns the platform user that is assigned to this Player Controller's Local Player.
If there is no local player, then this will return PLATFORMUSERID_NONE

### GetSpectatorPawn
```angelscript
ASpectatorPawn GetSpectatorPawn()
```
Get the Pawn used when spectating. nullptr when not spectating.

### GetStreamingSourceLocationAndRotation
```angelscript
void GetStreamingSourceLocationAndRotation(FVector& OutLocation, FRotator& OutRotation)
```
Gets the streaming source location and rotation.
Default implementation returns APlayerController::GetPlayerViewPoint but can be overriden in child classes.

### GetStreamingSourcePriority
```angelscript
EStreamingSourcePriority GetStreamingSourcePriority()
```
Gets the streaming source priority.
Default implementation returns StreamingSourcePriority but can be overriden in child classes.
@return the streaming source priority.

### GetStreamingSourceShapes
```angelscript
void GetStreamingSourceShapes(TArray<FStreamingSourceShape>& OutShapes)
```
Gets the streaming source priority.
Default implementation returns StreamingSourceShapes but can be overriden in child classes.
@return the streaming source priority.

### GetViewportSize
```angelscript
void GetViewportSize(int& SizeX, int& SizeY)
```
Helper to get the size of the HUD canvas for this player controller.  Returns 0 if there is no HUD

### IsInputKeyDown
```angelscript
bool IsInputKeyDown(FKey Key)
```
Returns true if the given key/button is pressed on the input of the controller (if present)

### IsStreamingSourceEnabled
```angelscript
bool IsStreamingSourceEnabled()
```
Whether the PlayerController should be used as a World Partiton streaming source.
Default implementation returns bEnableStreamingSource but can be overriden in child classes.
@return true if it should.

### ClientPlayForceFeedback
```angelscript
void ClientPlayForceFeedback(UForceFeedbackEffect ForceFeedbackEffect, FName Tag, bool bLooping, bool bIgnoreTimeDilation, bool bPlayWhilePaused)
```
Play a force feedback pattern on the player's controller
@param       ForceFeedbackEffect             The force feedback pattern to play
@param       bLooping                                Whether the pattern should be played repeatedly or be a single one shot
@param       bIgnoreTimeDilation             Whether the pattern should ignore time dilation
@param       bPlayWhilePaused                Whether the pattern should continue to play while the game is paused
@param       Tag                                             A tag that allows stopping of an effect.  If another effect with this Tag is playing, it will be stopped and replaced

### OnServerStartedVisualLogger
```angelscript
void OnServerStartedVisualLogger(bool bIsLogging)
```
Notify from server that Visual Logger is recording, to show that information on client about possible performance issues

### PlayDynamicForceFeedback
```angelscript
void PlayDynamicForceFeedback(float32 Intensity, float32 Duration, bool bAffectsLeftLarge, bool bAffectsLeftSmall, bool bAffectsRightLarge, bool bAffectsRightSmall, EDynamicForceFeedbackAction Action, FLatentActionInfo LatentInfo)
```
Latent action that controls the playing of force feedback
Begins playing when Start is called.  Calling Update or Stop if the feedback is not active will have no effect.
Completed will execute when Stop is called or the duration ends.
When Update is called the Intensity, Duration, and affect values will be updated with the current inputs
@param       Intensity                               How strong the feedback should be.  Valid values are between 0.0 and 1.0
@param       Duration                                How long the feedback should play for.  If the value is negative it will play until stopped
@param   bAffectsLeftLarge           Whether the intensity should be applied to the large left servo
@param   bAffectsLeftSmall           Whether the intensity should be applied to the small left servo
@param   bAffectsRightLarge          Whether the intensity should be applied to the large right servo
@param   bAffectsRightSmall          Whether the intensity should be applied to the small right servo

### PlayHapticEffect
```angelscript
void PlayHapticEffect(UHapticFeedbackEffect_Base HapticEffect, EControllerHand Hand, float32 Scale, bool bLoop)
```
Play a haptic feedback curve on the player's controller
@param       HapticEffect                    The haptic effect to play
@param       Hand                                    Which hand to play the effect on
@param       Scale                                   Scale between 0.0 and 1.0 on the intensity of playback

### ProjectWorldLocationToScreen
```angelscript
bool ProjectWorldLocationToScreen(FVector WorldLocation, FVector2D& ScreenLocation, bool bPlayerViewportRelative)
```
Convert a World Space 3D position into a 2D Screen Space position.
@return true if the world coordinate was successfully projected to the screen.

### ResetControllerLightColor
```angelscript
void ResetControllerLightColor()
```
Resets the light color of the player's controller to default

### ServerAcknowledgePossession
```angelscript
void ServerAcknowledgePossession(APawn P)
```
acknowledge possession of pawn

### ServerBlockPlayer
```angelscript
void ServerBlockPlayer(FUniqueNetIdRepl PlayerId)
```
Tell the client to block a player for this controller
@param PlayerId player id to block

### ServerCamera
```angelscript
void ServerCamera(FName NewMode)
```
change mode of camera

### ServerChangeName
```angelscript
void ServerChangeName(FString S)
```
Change name of server

### ServerCheckClientPossession
```angelscript
void ServerCheckClientPossession()
```
Tells the server to make sure the possessed pawn is in sync with the client.

### ServerCheckClientPossessionReliable
```angelscript
void ServerCheckClientPossessionReliable()
```
Reliable version of ServerCheckClientPossession to be used when there is no likely danger of spamming the network.

### ServerExecRPC
```angelscript
void ServerExecRPC(FString Msg)
```
RPC used by ServerExec. Not intended to be called directly

### ServerMutePlayer
```angelscript
void ServerMutePlayer(FUniqueNetIdRepl PlayerId)
```
Tell the server to mute a player for this controller
@param PlayerId player id to mute

### ServerNotifyLoadedWorld
```angelscript
void ServerNotifyLoadedWorld(FName WorldPackageName)
```
Called to notify the server when the client has loaded a new world via seamless traveling
@param WorldPackageName the name of the world package that was loaded

### ServerPause
```angelscript
void ServerPause()
```
Replicate pause request to the server

### ServerRecvClientInputFrame
```angelscript
void ServerRecvClientInputFrame(int RecvClientInputFrame, TArray<uint8> Data)
```

### ServerRestartPlayer
```angelscript
void ServerRestartPlayer()
```
Attempts to restart this player, generally called from the client upon respawn request.

### ServerSetSpectatorLocation
```angelscript
void ServerSetSpectatorLocation(FVector NewLoc, FRotator NewRot)
```
When spectating, updates spectator location/rotation and pings the server to make sure spectating should continue.

### ServerSetSpectatorWaiting
```angelscript
void ServerSetSpectatorWaiting(bool bWaiting)
```
Indicate that the Spectator is waiting to join/respawn.

### ServerShortTimeout
```angelscript
void ServerShortTimeout()
```
Notifies the server that the client has ticked gameplay code, and should no longer get the extended "still loading" timeout grace period

### ServerToggleAILogging
```angelscript
void ServerToggleAILogging()
```
Used by UGameplayDebuggingControllerComponent to replicate messages for AI debugging in network games.

### ServerUnblockPlayer
```angelscript
void ServerUnblockPlayer(FUniqueNetIdRepl PlayerId)
```
Tell the client to unblock a player for this controller
@param PlayerId player id to unblock

### ServerUnmutePlayer
```angelscript
void ServerUnmutePlayer(FUniqueNetIdRepl PlayerId)
```
Tell the server to unmute a player for this controller
@param PlayerId player id to unmute

### ServerUpdateCamera
```angelscript
void ServerUpdateCamera(FVector CamLoc, int CamPitchAndYaw)
```
If PlayerCamera.bUseClientSideCameraUpdates is set, client will replicate camera positions to the server. // @TODO - combine pitch/yaw into one int, maybe also send location compressed

### ServerVerifyViewTarget
```angelscript
void ServerVerifyViewTarget()
```
Used by client to request server to confirm current viewtarget (server will respond with ClientSetViewTarget() ).

### ServerViewNextPlayer
```angelscript
void ServerViewNextPlayer()
```
Move camera to next player on round ended or spectating

### ServerViewPrevPlayer
```angelscript
void ServerViewPrevPlayer()
```
Move camera to previous player on round ended or spectating

### ServerViewSelf
```angelscript
void ServerViewSelf(FViewTargetTransitionParams TransitionParams)
```
Move camera to current user

### SetAudioListenerAttenuationOverride
```angelscript
void SetAudioListenerAttenuationOverride(USceneComponent AttachToComponent, FVector AttenuationLocationOVerride)
```

### SetAudioListenerOverride
```angelscript
void SetAudioListenerOverride(USceneComponent AttachToComponent, FVector Location, FRotator Rotation)
```
Used to override the default positioning of the audio listener

@param AttachToComponent Optional component to attach the audio listener to
@param Location Depending on whether Component is attached this is either an offset from its location or an absolute position
@param Rotation Depending on whether Component is attached this is either an offset from its rotation or an absolute rotation

### SetCinematicMode
```angelscript
void SetCinematicMode(bool bInCinematicMode, bool bHidePlayer, bool bAffectsHUD, bool bAffectsMovement, bool bAffectsTurning)
```
Server/SP only function for changing whether the player is in cinematic mode.  Updates values of various state variables, then replicates the call to the client
to sync the current cinematic mode.
@param       bInCinematicMode        specify true if the player is entering cinematic mode; false if the player is leaving cinematic mode.
@param       bHidePlayer                     specify true to hide the player's pawn (only relevant if bInCinematicMode is true)
@param       bAffectsHUD                     specify true if we should show/hide the HUD to match the value of bCinematicMode
@param       bAffectsMovement        specify true to disable movement in cinematic mode, enable it when leaving
@param       bAffectsTurning         specify true to disable turning in cinematic mode or enable it when leaving

### SetControllerLightColor
```angelscript
void SetControllerLightColor(FColor Color)
```
Sets the light color of the player's controller
@param       Color                                   The color for the light to be

### SetDeprecatedInputPitchScale
```angelscript
void SetDeprecatedInputPitchScale(float32 NewValue)
```

### SetDeprecatedInputRollScale
```angelscript
void SetDeprecatedInputRollScale(float32 NewValue)
```

### SetDeprecatedInputYawScale
```angelscript
void SetDeprecatedInputYawScale(float32 NewValue)
```

### SetDisableHaptics
```angelscript
void SetDisableHaptics(bool bNewDisabled)
```
Allows the player controller to disable all haptic requests from being fired, e.g. in the case of a level loading

@param       bNewDisabled    If TRUE, the haptics will stop and prevented from being enabled again until set to FALSE

### SetHapticsByValue
```angelscript
void SetHapticsByValue(float32 Frequency, float32 Amplitude, EControllerHand Hand)
```
Sets the value of the haptics for the specified hand directly, using frequency and amplitude.  NOTE:  If a curve is already
playing for this hand, it will be cancelled in favour of the specified values.

@param       Frequency                               The normalized frequency [0.0, 1.0] to play through the haptics system
@param       Amplitude                               The normalized amplitude [0.0, 1.0] to set the haptic feedback to
@param       Hand                                    Which hand to play the effect on

### SetMotionControlsEnabled
```angelscript
void SetMotionControlsEnabled(bool bEnabled)
```

### SetMouseCursorWidget
```angelscript
void SetMouseCursorWidget(EMouseCursor Cursor, UUserWidget CursorWidget)
```
Sets the Widget for the Mouse Cursor to display
@param Cursor - the cursor to set the widget for
@param CursorWidget - the widget to set the cursor to

### SetMouseLocation
```angelscript
void SetMouseLocation(int X, int Y)
```
Positions the mouse cursor in screen space, in pixels.

### SetViewTargetWithBlend
```angelscript
void SetViewTargetWithBlend(AActor NewViewTarget, float32 BlendTime, EViewTargetBlendFunction BlendFunc, float32 BlendExp, bool bLockOutgoing)
```
Set the view target blending with variable control
@param NewViewTarget - new actor to set as view target
@param BlendTime - time taken to blend
@param BlendFunc - Cubic, Linear etc functions for blending
@param BlendExp -  Exponent, used by certain blend functions to control the shape of the curve.
@param bLockOutgoing - If true, lock outgoing viewtarget to last frame's camera position for the remainder of the blend.

### SetVirtualJoystickVisibility
```angelscript
void SetVirtualJoystickVisibility(bool bVisible)
```
Set the virtual joystick visibility.

### StopHapticEffect
```angelscript
void StopHapticEffect(EControllerHand Hand)
```
Stops a playing haptic feedback curve
@param       HapticEffect                    The haptic effect to stop
@param       Hand                                    Which hand to stop the effect for

### StreamingSourceShouldActivate
```angelscript
bool StreamingSourceShouldActivate()
```
Whether the PlayerController streaming source should activate cells after loading.
Default implementation returns bStreamingSourceShouldActivate but can be overriden in child classes.
@return true if it should.

### StreamingSourceShouldBlockOnSlowStreaming
```angelscript
bool StreamingSourceShouldBlockOnSlowStreaming()
```
Whether the PlayerController streaming source should block on slow streaming.
Default implementation returns bStreamingSourceShouldBlockOnSlowStreaming but can be overriden in child classes.
@return true if it should.

### WasInputKeyJustPressed
```angelscript
bool WasInputKeyJustPressed(FKey Key)
```
Returns true if the given key/button was up last frame and down this frame.

### WasInputKeyJustReleased
```angelscript
bool WasInputKeyJustReleased(FKey Key)
```
Returns true if the given key/button was down last frame and up this frame.

### GetPlayerInput
```angelscript
UPlayerInput GetPlayerInput()
```

### PopInputComponent
```angelscript
void PopInputComponent(UInputComponent Component)
```
Remove an input component so it no longer handles input from this player controller.

### PushInputComponent
```angelscript
void PushInputComponent(UInputComponent Component)
```
Push an input component to handle input from this player controller.


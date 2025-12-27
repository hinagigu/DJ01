# __Gameplay

## 方法

### ActivateReverbEffect
```angelscript
void ActivateReverbEffect(UReverbEffect ReverbEffect, FName TagName, float32 Priority, float32 Volume, float32 FadeTime)
```
Activates a Reverb Effect without the need for an Audio Volume
@param ReverbEffect Reverb Effect to use
@param TagName Tag to associate with Reverb Effect
@param Priority Priority of the Reverb Effect
@param Volume Volume level of Reverb Effect
@param FadeTime Time before Reverb Effect is fully active

### AnnounceAccessibleString
```angelscript
void AnnounceAccessibleString(FString AnnouncementString)
```
If accessibility is enabled, have the platform announce a string to the player.
These announcements can be interrupted by system accessibiliity announcements or other accessibility announcement requests.
This should be used judiciously as flooding a player with announcements can be overrwhelming and confusing.
Try to make announcements concise and clear.
NOTE: Currently only supported on Win10, Mac, iOS

### ApplyDamage
```angelscript
float32 ApplyDamage(AActor DamagedActor, float32 BaseDamage, AController EventInstigator, AActor DamageCauser, TSubclassOf<UDamageType> DamageTypeClass)
```
Hurts the specified actor with generic damage.
@param DamagedActor - Actor that will be damaged.
@param BaseDamage - The base damage to apply.
@param EventInstigator - Controller that was responsible for causing this damage (e.g. player who shot the weapon)
@param DamageCauser - Actor that actually caused the damage (e.g. the grenade that exploded)
@param DamageTypeClass - Class that describes the damage that was done.
@return Actual damage the ended up being applied to the actor.

### ApplyPointDamage
```angelscript
float32 ApplyPointDamage(AActor DamagedActor, float32 BaseDamage, FVector HitFromDirection, FHitResult HitInfo, AController EventInstigator, AActor DamageCauser, TSubclassOf<UDamageType> DamageTypeClass)
```
Hurts the specified actor with the specified impact.
@param DamagedActor - Actor that will be damaged.
@param BaseDamage - The base damage to apply.
@param HitFromDirection - Direction the hit came FROM
@param HitInfo - Collision or trace result that describes the hit
@param EventInstigator - Controller that was responsible for causing this damage (e.g. player who shot the weapon)
@param DamageCauser - Actor that actually caused the damage (e.g. the grenade that exploded)
@param DamageTypeClass - Class that describes the damage that was done.
@return Actual damage the ended up being applied to the actor.

### ApplyRadialDamage
```angelscript
bool ApplyRadialDamage(float32 BaseDamage, FVector Origin, float32 DamageRadius, TSubclassOf<UDamageType> DamageTypeClass, TArray<AActor> IgnoreActors, AActor DamageCauser, AController InstigatedByController, bool bDoFullDamage, ECollisionChannel DamagePreventionChannel)
```
Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.
@param BaseDamage - The base damage to apply, i.e. the damage at the origin.
@param Origin - Epicenter of the damage area.
@param DamageRadius - Radius of the damage area, from Origin
@param DamageTypeClass - Class that describes the damage that was done.
@param IgnoreActors - List of Actors to ignore
@param DamageCauser - Actor that actually caused the damage (e.g. the grenade that exploded).  This actor will not be damaged and it will not block damage.
@param InstigatedByController - Controller that was responsible for causing this damage (e.g. player who threw the grenade)
@param bFullDamage - if true, damage not scaled based on distance from Origin
@param DamagePreventionChannel - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel
@return true if damage was applied to at least one actor.

### ApplyRadialDamageWithFalloff
```angelscript
bool ApplyRadialDamageWithFalloff(float32 BaseDamage, float32 MinimumDamage, FVector Origin, float32 DamageInnerRadius, float32 DamageOuterRadius, float32 DamageFalloff, TSubclassOf<UDamageType> DamageTypeClass, TArray<AActor> IgnoreActors, AActor DamageCauser, AController InstigatedByController, ECollisionChannel DamagePreventionChannel)
```
Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.
@param BaseDamage - The base damage to apply, i.e. the damage at the origin.
@param Origin - Epicenter of the damage area.
@param DamageInnerRadius - Radius of the full damage area, from Origin
@param DamageOuterRadius - Radius of the minimum damage area, from Origin
@param DamageFalloff - Falloff exponent of damage from DamageInnerRadius to DamageOuterRadius
@param DamageTypeClass - Class that describes the damage that was done.
@param IgnoreActors - List of Actors to ignore
@param DamageCauser - Actor that actually caused the damage (e.g. the grenade that exploded)
@param InstigatedByController - Controller that was responsible for causing this damage (e.g. player who threw the grenade)
@param bFullDamage - if true, damage not scaled based on distance from Origin
@param DamagePreventionChannel - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel
@return true if damage was applied to at least one actor.

### AreAnyListenersWithinRange
```angelscript
bool AreAnyListenersWithinRange(FVector Location, float32 MaximumRange)
```
Determines if any audio listeners are within range of the specified location
@param Location              The location from which test if a listener is in range
@param MaximumRange  The distance away from Location to test if any listener is within
@note This will always return false if there is no audio device, or the audio device is disabled.

### AreSubtitlesEnabled
```angelscript
bool AreSubtitlesEnabled()
```
Returns whether or not subtitles are currently enabled.
@return true if subtitles are enabled.

### Blueprint_PredictProjectilePath_Advanced
```angelscript
bool Blueprint_PredictProjectilePath_Advanced(FPredictProjectilePathParams PredictParams, FPredictProjectilePathResult& PredictResult)
```
Predict the arc of a virtual projectile affected by gravity with collision checks along the arc.
Returns true if it hit something.

@param PredictParams                          Input params to the trace (start location, velocity, time to simulate, etc).
@param PredictResult                          Output result of the trace (Hit result, array of location/velocity/times for each trace step, etc).
@return                                                       True if hit something along the path (if tracing with collision).

### Blueprint_PredictProjectilePath_ByObjectType
```angelscript
bool Blueprint_PredictProjectilePath_ByObjectType(FHitResult& OutHit, TArray<FVector>& OutPathPositions, FVector& OutLastTraceDestination, FVector StartPos, FVector LaunchVelocity, bool bTracePath, float32 ProjectileRadius, TArray<EObjectTypeQuery> ObjectTypes, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, float32 DrawDebugTime, float32 SimFrequency, float32 MaxSimTime, float32 OverrideGravityZ)
```
Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
Returns true if it hit something.

@param OutPathPositions                       Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something.
@param OutHit                                         Predicted hit result, if the projectile will hit something
@param OutLastTraceDestination        Goal position of the final trace it did. Will not be in the path if there is a hit.
@param StartPos                                       First start trace location
@param LaunchVelocity                         Velocity the "virtual projectile" is launched at
@param bTracePath                                     Trace along the entire path to look for blocking hits
@param ProjectileRadius                       Radius of the virtual projectile to sweep against the environment
@param ObjectTypes                            ObjectTypes to trace against, if bTracePath is true.
@param bTraceComplex                          Use TraceComplex (trace against triangles not primitives)
@param ActorsToIgnore                         Actors to exclude from the traces
@param DrawDebugType                          Debug type (one-frame, duration, persistent)
@param DrawDebugTime                          Duration of debug lines (only relevant for DrawDebugType::Duration)
@param SimFrequency                           Determines size of each sub-step in the simulation (chopping up MaxSimTime)
@param MaxSimTime                                     Maximum simulation time for the virtual projectile.
@param OverrideGravityZ                       Optional override of Gravity (if 0, uses WorldGravityZ)
@return                                                       True if hit something along the path if tracing for collision.

### Blueprint_PredictProjectilePath_ByTraceChannel
```angelscript
bool Blueprint_PredictProjectilePath_ByTraceChannel(FHitResult& OutHit, TArray<FVector>& OutPathPositions, FVector& OutLastTraceDestination, FVector StartPos, FVector LaunchVelocity, bool bTracePath, float32 ProjectileRadius, ECollisionChannel TraceChannel, bool bTraceComplex, TArray<AActor> ActorsToIgnore, EDrawDebugTrace DrawDebugType, float32 DrawDebugTime, float32 SimFrequency, float32 MaxSimTime, float32 OverrideGravityZ)
```
Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
Returns true if it hit something (if tracing with collision).

@param OutPathPositions                       Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something.
@param OutHit                                         Predicted hit result, if the projectile will hit something
@param OutLastTraceDestination        Goal position of the final trace it did. Will not be in the path if there is a hit.
@param StartPos                                       First start trace location
@param LaunchVelocity                         Velocity the "virtual projectile" is launched at
@param bTracePath                                     Trace along the entire path to look for blocking hits
@param ProjectileRadius                       Radius of the virtual projectile to sweep against the environment
@param TraceChannel                           TraceChannel to trace against, if bTracePath is true.
@param bTraceComplex                          Use TraceComplex (trace against triangles not primitives)
@param ActorsToIgnore                         Actors to exclude from the traces
@param DrawDebugType                          Debug type (one-frame, duration, persistent)
@param DrawDebugTime                          Duration of debug lines (only relevant for DrawDebugType::Duration)
@param SimFrequency                           Determines size of each sub-step in the simulation (chopping up MaxSimTime)
@param MaxSimTime                                     Maximum simulation time for the virtual projectile.
@param OverrideGravityZ                       Optional override of Gravity (if 0, uses WorldGravityZ)
@return                                                       True if hit something along the path (if tracing with collision).

### BlueprintSuggestProjectileVelocity
```angelscript
bool BlueprintSuggestProjectileVelocity(FVector& TossVelocity, FVector StartLocation, FVector EndLocation, float32 LaunchSpeed, float32 OverrideGravityZ, ESuggestProjVelocityTraceOption TraceOption, float32 CollisionRadius, bool bFavorHighArc, bool bDrawDebug, bool bAcceptClosestOnNoSolutions)
```
Calculates an launch velocity for a projectile to hit a specified point.
@param TossVelocity                                  (output) Result launch velocity.
@param StartLocation                                 Intended launch location
@param EndLocation                                   Desired landing location
@param LaunchSpeed                                   Desired launch speed
@param OverrideGravityZ                              Optional gravity override.  0 means "do not override".
@param TraceOption                                   Controls whether or not to validate a clear path by tracing along the calculated arc
@param CollisionRadius                               Radius of the projectile (assumed spherical), used when tracing
@param bFavorHighArc                                 If true and there are 2 valid solutions, will return the higher arc.  If false, will favor the lower arc.
@param bDrawDebug                                    When true, a debug arc is drawn (red for an invalid arc, green for a valid arc)
@param bAcceptClosestOnNoSolutions   If target is unreachable and no solutions are possible, provide a velocity that gets as close to the target as possible given this launch speed
@return                                                              Returns false if there is no valid solution or the valid solutions are blocked.  Returns true otherwise.

### BreakHitResult
```angelscript
void BreakHitResult(FHitResult Hit, bool& bBlockingHit, bool& bInitialOverlap, float32& Time, float32& Distance, FVector& Location, FVector& ImpactPoint, FVector& Normal, FVector& ImpactNormal, UPhysicalMaterial& PhysMat, AActor& HitActor, UPrimitiveComponent& HitComponent, FName& HitBoneName, FName& BoneName, int& HitItem, int& ElementIndex, int& FaceIndex, FVector& TraceStart, FVector& TraceEnd)
```
Extracts data from a HitResult.
@param Hit                   The source HitResult.
@param bBlockingHit  True if there was a blocking hit, false otherwise.
@param bInitialOverlap True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector.
@param Time                  'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit.
@param Distance              The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object).
@param Location              Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate.
@param Normal                Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests.
@param ImpactPoint   Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap.
@param ImpactNormal  Normal of the hit in world space, for the object that was hit by the sweep.
@param PhysMat               Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned.
@param HitActor              Actor hit by the trace.
@param HitComponent  PrimitiveComponent hit by the trace.
@param HitBoneName   Name of the bone hit (valid only if we hit a skeletal mesh).
@param BoneName              Name of the trace bone hit (valid only if we hit a skeletal mesh).
@param HitItem               Primitive-specific data recording which item in the primitive was hit
@param ElementIndex  If colliding with a primitive with multiple parts, index of the part that was hit.
@param FaceIndex             If colliding with trimesh or landscape, index of face that was hit.

### CancelAsyncLoading
```angelscript
void CancelAsyncLoading()
```
Cancels all currently queued streaming packages

### ClearSoundMixClassOverride
```angelscript
void ClearSoundMixClassOverride(USoundMix InSoundMixModifier, USoundClass InSoundClass, float32 FadeOutTime)
```
Clears any existing override of the Sound Class Adjuster in the given Sound Mix
@param InSoundMixModifier The sound mix to modify.
@param InSoundClass The sound class in the sound mix to clear overrides from.
@param FadeOutTime The interpolation time to use to go from the current sound class adjuster override values to the non-override values.

### ClearSoundMixModifiers
```angelscript
void ClearSoundMixModifiers()
```
Clear all sound mix modifiers from the audio system

### CreatePlayer
```angelscript
APlayerController CreatePlayer(int ControllerId, bool bSpawnPlayerController)
```
Create a new local player for this game, for cases like local multiplayer.

@param ControllerId             The ID of the physical controller that the should control the newly created player. A value of -1 specifies to use the next available ID
@param bSpawnPlayerController   Whether a player controller should be spawned immediately for this player. If false a player controller will not be created automatically until transition to the next map.
@return                         The created player controller if one is created.

### CreatePlayerFromPlatformUser
```angelscript
APlayerController CreatePlayerFromPlatformUser(FPlatformUserId UserId, bool bSpawnPlayerController)
```
Create a new local player for this game, for cases like local multiplayer.

@param UserId                   The platform user id that should control the newly created player. A valude of PLATFRMUSERID_NONE specifies to use the next available ID
@param bSpawnPlayerController   Whether a player controller should be spawned immediately for this player. If false a player controller will not be created automatically until transition to the next map.
@return                         The created player controller if one is created.

### CreateSaveGameObject
```angelscript
USaveGame CreateSaveGameObject(TSubclassOf<USaveGame> SaveGameClass)
```
Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.
@param       SaveGameClass   Class of SaveGame to create
@return                                      New SaveGame object to write data to

### CreateSound2D
```angelscript
UAudioComponent CreateSound2D(USoundBase Sound, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundConcurrency ConcurrencySettings, bool bPersistAcrossLevelTransition, bool bAutoDestroy)
```
This function allows users to create Audio Components in advance of playback with settings specifically for non-spatialized,
non-distance-attenuated sounds. Audio Components created using this function by default will not have Spatialization applied.
@param Sound - Sound to create.
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far into the sound to begin playback at
@param ConcurrencySettings - Override concurrency settings package to play sound with
@param PersistAcrossLevelTransition - Whether the sound should continue to play when the map it was played in is unloaded
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound finishes
                                              (by completing or stopping), or whether it can be reactivated
@return An audio component to manipulate the created sound

### DeactivateReverbEffect
```angelscript
void DeactivateReverbEffect(FName TagName)
```
Deactivates a Reverb Effect that was applied outside of an Audio Volume

@param TagName Tag associated with Reverb Effect to remove

### DeleteGameInSlot
```angelscript
bool DeleteGameInSlot(FString SlotName, int UserIndex)
```
Delete a save game in a particular slot.
@param SlotName                      Name of save game slot to delete.
@param UserIndex                     The platform user index that identifies the user doing the saving, ignored on some platforms.
@return                                      True if a file was actually able to be deleted. use DoesSaveGameExist to distinguish between delete failures and failure due to file not existing.

### DeprojectSceneCaptureToWorld
```angelscript
bool DeprojectSceneCaptureToWorld(const ASceneCapture2D SceneCapture2D, FVector2D TargetUV, FVector& WorldPosition, FVector& WorldDirection)
```
Transforms the given 2D UV coordinate into a 3D world-space point and direction.
@param SceneCapture2D        Deproject using this scene capture's view.
@param ScreenPosition        UV in scene capture render target to deproject.
@param WorldPosition         (out) Corresponding 3D position on camera near plane, in world space.
@param WorldDirection        (out) World space direction vector away from the camera at the given 2d point.

### DeprojectScreenToWorld
```angelscript
bool DeprojectScreenToWorld(const APlayerController Player, FVector2D ScreenPosition, FVector& WorldPosition, FVector& WorldDirection)
```
Transforms the given 2D screen space coordinate into a 3D world-space point and direction.
@param Player                        Deproject using this player's view.
@param ScreenPosition        2D screen space to deproject.
@param WorldPosition         (out) Corresponding 3D position in world space.
@param WorldDirection        (out) World space direction vector away from the camera at the given 2d point.

### DoesSaveGameExist
```angelscript
bool DoesSaveGameExist(FString SlotName, int UserIndex)
```
See if a save game exists with the specified name.
@param SlotName                      Name of save game slot.
@param UserIndex                     The platform user index that identifies the user doing the saving, ignored on some platforms.

### EnableLiveStreaming
```angelscript
void EnableLiveStreaming(bool Enable)
```
Toggle live DVR streaming.
@param Enable                        If true enable streaming, otherwise disable.

### FindCollisionUV
```angelscript
bool FindCollisionUV(FHitResult Hit, int UVChannel, FVector2D& UV)
```
Try and find the UV for a collision impact. Note this ONLY works if 'Support UV From Hit Results' is enabled in Physics Settings.

### FindNearestActor
```angelscript
AActor FindNearestActor(FVector Origin, TArray<AActor> ActorsToCheck, float32& Distance)
```
Returns an Actor nearest to Origin from ActorsToCheck array.
@param  Origin                  World Location from which the distance is measured.
@param  ActorsToCheck   Array of Actors to examine and return Actor nearest to Origin.
@param  Distance        Distance from Origin to the returned Actor.
@return                         Nearest Actor.

### FlushLevelStreaming
```angelscript
void FlushLevelStreaming()
```
Flushes level streaming in blocking fashion and returns when all sub-levels are loaded / visible / hidden

### GetAccurateRealTime
```angelscript
void GetAccurateRealTime(int& Seconds, float& PartialSeconds)
```
Returns time in seconds since the application was started. Unlike the other time functions this is accurate to the exact time this function is called instead of set once per frame.

### GetActiveSpatialPluginName
```angelscript
FName GetActiveSpatialPluginName()
```
Get currently active Audio Spatialization Plugin name

### GetActorArrayAverageLocation
```angelscript
FVector GetActorArrayAverageLocation(TArray<AActor> Actors)
```
Find the average location (centroid) of an array of Actors

### GetActorArrayBounds
```angelscript
void GetActorArrayBounds(TArray<AActor> Actors, bool bOnlyCollidingComponents, FVector& Center, FVector& BoxExtent)
```
Bind the bounds of an array of Actors

### GetActorOfClass
```angelscript
AActor GetActorOfClass(TSubclassOf<AActor> ActorClass)
```
Find the first Actor in the world of the specified class.
This is a slow operation, use with caution e.g. do not use every frame.
@param  ActorClass      Class of Actor to find. Must be specified or result will be empty.
@return                         Actor of the specified class.

### GetAllActorsOfClass
```angelscript
void GetAllActorsOfClass(TSubclassOf<AActor> ActorClass, TArray<AActor>& OutActors)
```
Find all Actors in the world of the specified class.
This is a slow operation, use with caution e.g. do not use every frame.
@param  ActorClass      Class of Actor to find. Must be specified or result array will be empty.
@param  OutActors       Output array of Actors of the specified class.

### GetAllActorsOfClassWithTag
```angelscript
void GetAllActorsOfClassWithTag(TSubclassOf<AActor> ActorClass, FName Tag, TArray<AActor>& OutActors)
```
Find all Actors in the world of the specified class with the specified tag.
This is a slow operation, use with caution e.g. do not use every frame.
@param  Tag                     Tag to find. Must be specified or result array will be empty.
@param  ActorClass      Class of Actor to find. Must be specified or result array will be empty.
@param  OutActors       Output array of Actors of the specified tag.

### GetAllActorsWithInterface
```angelscript
void GetAllActorsWithInterface(TSubclassOf<UInterface> Interface, TArray<AActor>& OutActors)
```
Find all Actors in the world with the specified interface.
This is a slow operation, use with caution e.g. do not use every frame.
@param  Interface       Interface to find. Must be specified or result array will be empty.
@param  OutActors       Output array of Actors of the specified interface.

### GetAllActorsWithTag
```angelscript
void GetAllActorsWithTag(FName Tag, TArray<AActor>& OutActors)
```
Find all Actors in the world with the specified tag.
This is a slow operation, use with caution e.g. do not use every frame.
@param  Tag                     Tag to find. Must be specified or result array will be empty.
@param  OutActors       Output array of Actors of the specified tag.

### GetAudioTimeSeconds
```angelscript
float GetAudioTimeSeconds()
```
Returns time in seconds since world was brought up for play, IS stopped when game pauses, NOT dilated/clamped.

### GetAvailableSpatialPluginNames
```angelscript
TArray<FName> GetAvailableSpatialPluginNames()
```
Get list of available Audio Spatialization Plugin names

### GetClosestListenerLocation
```angelscript
bool GetClosestListenerLocation(FVector Location, float32 MaximumRange, bool bAllowAttenuationOverride, FVector& ListenerPosition)
```
Finds and returns the position of the closest listener to the specified location
@param Location                                              The location from which we'd like to find the closest listener, in world space.
@param MaximumRange                                  The maximum distance away from Location that a listener can be.
@param bAllowAttenuationOverride             True for the adjusted listener position (if attenuation override is set), false for the raw listener position (for panning)
@param ListenerPosition                              [Out] The position of the closest listener in world space, if found.
@return true if we've successfully found a listener within MaximumRange of Location, otherwise false.
@note This will always return false if there is no audio device, or the audio device is disabled.

### GetCurrentLevelName
```angelscript
FString GetCurrentLevelName(bool bRemovePrefixString)
```
Get the name of the currently-open level.

@param bRemovePrefixString    remove any streaming- or editor- added prefixes from the level name.

### GetCurrentReverbEffect
```angelscript
UReverbEffect GetCurrentReverbEffect()
```
Returns the highest priority reverb settings currently active from any source (Audio Volumes or manual settings).

### GetEnableWorldRendering
```angelscript
bool GetEnableWorldRendering()
```
Returns the world rendering state
@return      Whether the world should be rendered or not

### GetGameInstance
```angelscript
UGameInstance GetGameInstance()
```
Returns the game instance object

### GetGameMode
```angelscript
AGameModeBase GetGameMode()
```
Returns the current GameModeBase or Null if it can't be retrieved, such as on the client

### GetGameState
```angelscript
AGameStateBase GetGameState()
```
Returns the current GameStateBase or Null if it can't be retrieved

### GetGlobalTimeDilation
```angelscript
float32 GetGlobalTimeDilation()
```
Gets the current global time dilation.
@return Current time dilation.

### GetIntOption
```angelscript
int GetIntOption(FString Options, FString Key, int DefaultValue)
```
Find an option in the options string and return it as an integer.
@param Options               The string containing the options.
@param Key                   The key to find the value of in Options.
@return                              The value associated with Key as an integer if Key found in Options string, otherwise DefaultValue.

### GetKeyValue
```angelscript
void GetKeyValue(FString Pair, FString& Key, FString& Value)
```
Break up a key=value pair into its key and value.
@param Pair                  The string containing a pair to split apart.
@param Key                   (out) Key portion of Pair. If no = in string will be the same as Pair.
@param Value                 (out) Value portion of Pair. If no = in string will be empty.

### GetMaxAudioChannelCount
```angelscript
int GetMaxAudioChannelCount()
```
Retrieves the max voice count currently used by the audio engine.

### GetNumLocalPlayerControllers
```angelscript
int GetNumLocalPlayerControllers()
```
Returns the number of fully initialized local players, this will be 0 on dedicated servers.
Indexes up to this can be used as PlayerIndex parameters for the following functions, and you are guaranteed to get a local player controller.

### GetNumPlayerControllers
```angelscript
int GetNumPlayerControllers()
```
Returns the total number of available player controllers, including remote players when called on a server.
Indexes up to this can be used as PlayerIndex parameters for the following functions.

### GetNumPlayerStates
```angelscript
int GetNumPlayerStates()
```
Returns the number of active player states, there is one player state for every connected player even if they are a remote client.
Indexes up to this can be use as PlayerStateIndex parameters for other functions.

### GetObjectClass
```angelscript
UClass GetObjectClass(const UObject Object)
```
Returns the class of a passed in Object, will always be valid if Object is not NULL

### GetPlatformName
```angelscript
FString GetPlatformName()
```
Returns the string name of the current platform, to perform different behavior based on platform.
(Platform names include Windows, Mac, Linux, IOS, Android, consoles, etc.).

### GetPlayerCameraManager
```angelscript
APlayerCameraManager GetPlayerCameraManager(int PlayerIndex)
```
Returns the camera manager for the Player Controller at the specified player index.
This will not include remote clients with no player controller.

@param PlayerIndex   Index in the player controller list, starting first with local players and then available remote ones

### GetPlayerCharacter
```angelscript
ACharacter GetPlayerCharacter(int PlayerIndex)
```
Returns the pawn for the player controller at the specified player index, will return null if the pawn is not a character.
This will not include characters of remote clients with no available player controller, you can iterate the PlayerStates list for that.

@param PlayerIndex   Index in the player controller list, starting first with local players and then available remote ones

### GetPlayerController
```angelscript
APlayerController GetPlayerController(int PlayerIndex)
```
Returns the player controller found while iterating through the local and available remote player controllers.
On a network client, this will only include local players as remote player controllers are not available.
The index will be consistent as long as no new players join or leave, but it will not be the same across different clients and servers.

@param PlayerIndex   Index in the player controller list, starting first with local players and then available remote ones

### GetPlayerControllerFromID
```angelscript
APlayerController GetPlayerControllerFromID(int ControllerID)
```
Returns the player controller with the specified physical controller ID. This only works for local players.

@param ControllerID  Physical controller ID, the same value returned from Get Player Controller ID

### GetPlayerControllerFromPlatformUser
```angelscript
APlayerController GetPlayerControllerFromPlatformUser(FPlatformUserId UserId)
```
Returns the player controller with the specified physical controller ID. This only works for local players.

@param ControllerID  Physical controller ID, the same value returned from Get Player Controller ID

### GetPlayerControllerID
```angelscript
int GetPlayerControllerID(APlayerController Player)
```
Gets what physical controller ID a player is using. This only works for local player controllers.

@param Player        The player controller of the player to get the ID of
@return                      The ID of the passed in player. -1 if there is no physical controller assigned to the passed in player

### GetPlayerPawn
```angelscript
APawn GetPlayerPawn(int PlayerIndex)
```
Returns the pawn for the player controller at the specified player index.
This will not include pawns of remote clients with no available player controller, you can use the player states list for that.

@param PlayerIndex   Index in the player controller list, starting first with local players and then available remote ones

### GetPlayerState
```angelscript
APlayerState GetPlayerState(int PlayerStateIndex)
```
Returns the player state at the given index in the game state's PlayerArray.
This will work on both the client and server and the index will be consistent.
After initial replication, all clients and the server will have access to PlayerStates for all connected players.

@param PlayerStateIndex      Index into the game state's PlayerArray

### GetPlayerStateFromUniqueNetId
```angelscript
APlayerState GetPlayerStateFromUniqueNetId(FUniqueNetIdRepl UniqueId)
```
Returns the player state that matches the passed in online id, or null for an invalid one.
This will work on both the client and server for local and remote players.

@param UniqueId      The player's unique net/online id

### GetRealTimeSeconds
```angelscript
float GetRealTimeSeconds()
```
Returns time in seconds since world was brought up for play, does NOT stop when game pauses, NOT dilated/clamped

### GetStreamingLevel
```angelscript
ULevelStreaming GetStreamingLevel(FName PackageName)
```
Returns level streaming object with specified level package name

### GetSurfaceType
```angelscript
EPhysicalSurface GetSurfaceType(FHitResult Hit)
```
Returns the EPhysicalSurface type of the given Hit.
To edit surface type for your project, use ProjectSettings/Physics/PhysicalSurface section

### GetTimeSeconds
```angelscript
float GetTimeSeconds()
```
Returns time in seconds since world was brought up for play, adjusted by time dilation and IS stopped when game pauses

### GetUnpausedTimeSeconds
```angelscript
float GetUnpausedTimeSeconds()
```
Returns time in seconds since world was brought up for play, adjusted by time dilation and IS NOT stopped when game pauses

### GetViewportMouseCaptureMode
```angelscript
EMouseCaptureMode GetViewportMouseCaptureMode()
```
Returns the current viewport mouse capture mode

### GetViewProjectionMatrix
```angelscript
void GetViewProjectionMatrix(FMinimalViewInfo DesiredView, FMatrix& ViewMatrix, FMatrix& ProjectionMatrix, FMatrix& ViewProjectionMatrix)
```
Returns the View Matrix, Projection Matrix and the View x Projection Matrix for a given view
@param DesiredView                   FMinimalViewInfo struct for a camera.
@param ViewMatrix                    (out) Corresponding View Matrix
@param ProjectionMatrix              (out) Corresponding Projection Matrix
@param ViewProjectionMatrix  (out) Corresponding View x Projection Matrix

### GetWorldDeltaSeconds
```angelscript
float GetWorldDeltaSeconds()
```
Returns the frame delta time in seconds, adjusted by time dilation.

### GetWorldOriginLocation
```angelscript
FIntVector GetWorldOriginLocation()
```
Returns world origin current location.

### GrassOverlappingSphereCount
```angelscript
int GrassOverlappingSphereCount(const UStaticMesh StaticMesh, FVector CenterPosition, float32 Radius)
```
Counts how many grass foliage instances overlap a given sphere.

@param        Mesh                    The static mesh we are interested in counting.
@param        CenterPosition  The center position of the sphere.
@param        Radius                  The radius of the sphere.

@return Number of foliage instances with their mesh set to Mesh that overlap the sphere.

### HasLaunchOption
```angelscript
bool HasLaunchOption(FString OptionToCheck)
```
Checks the commandline to see if the desired option was specified on the commandline (e.g. -demobuild)
@return                               True if the launch option was specified on the commandline, false otherwise

### HasOption
```angelscript
bool HasOption(FString Options, FString InKey)
```
Returns whether a key exists in an options string.
@param Options               The string containing the options.
@param Key                   The key to determine if it exists in Options.
@return                              Whether Key was found in Options.

### IsAnyLocalPlayerCameraWithinRange
```angelscript
bool IsAnyLocalPlayerCameraWithinRange(FVector Location, float32 MaximumRange)
```
Determines if any local player controller's camera is within range of the specified location.
@param Location              The location from which test range
@param MaximumRange  The distance away from Location to test range
@note This will always return false on dedicated servers.

### IsGamePaused
```angelscript
bool IsGamePaused()
```
Returns the game's paused state
@return      Whether the game is currently paused or not

### IsSplitscreenForceDisabled
```angelscript
bool IsSplitscreenForceDisabled()
```
Returns the split screen state
@return      Whether the game viewport is split screen or not

### LoadGameFromSlot
```angelscript
USaveGame LoadGameFromSlot(FString SlotName, int UserIndex)
```
Load the contents from a given slot.
@param SlotName                      Name of the save game slot to load from.
@param UserIndex                     The platform user index that identifies the user doing the saving, ignored on some platforms.
@return                                      Object containing loaded game state (nullptr if load fails)

### LoadStreamLevel
```angelscript
void LoadStreamLevel(FName LevelName, bool bMakeVisibleAfterLoad, bool bShouldBlockOnLoad, FLatentActionInfo LatentInfo)
```
Stream the level (by Name); Calling again before it finishes has no effect

### LoadStreamLevelBySoftObjectPtr
```angelscript
void LoadStreamLevelBySoftObjectPtr(TSoftObjectPtr<UWorld> Level, bool bMakeVisibleAfterLoad, bool bShouldBlockOnLoad, FLatentActionInfo LatentInfo)
```
Stream the level (by Object Reference); Calling again before it finishes has no effect

### MakeHitResult
```angelscript
FHitResult MakeHitResult(bool bBlockingHit, bool bInitialOverlap, float32 Time, float32 Distance, FVector Location, FVector ImpactPoint, FVector Normal, FVector ImpactNormal, UPhysicalMaterial PhysMat, AActor HitActor, UPrimitiveComponent HitComponent, FName HitBoneName, FName BoneName, int HitItem, int ElementIndex, int FaceIndex, FVector TraceStart, FVector TraceEnd)
```
Create a HitResult struct
@param Hit                   The source HitResult.
@param bBlockingHit  True if there was a blocking hit, false otherwise.
@param bInitialOverlap True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector.
@param Time                  'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit.
@param Distance              The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object).
@param Location              Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate.
@param Normal                Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests.
@param ImpactPoint   Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap.
@param ImpactNormal  Normal of the hit in world space, for the object that was hit by the sweep.
@param PhysMat               Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned.
@param HitActor              Actor hit by the trace.
@param HitComponent  PrimitiveComponent hit by the trace.
@param HitBoneName   Name of the bone hit (valid only if we hit a skeletal mesh).
@param BoneName              Name of the trace bone hit (valid only if we hit a skeletal mesh).
@param HitItem               Primitive-specific data recording which item in the primitive was hit
@param ElementIndex  If colliding with a primitive with multiple parts, index of the part that was hit.
@param FaceIndex             If colliding with trimesh or landscape, index of face that was hit.

### ObjectIsA
```angelscript
bool ObjectIsA(const UObject Object, TSubclassOf<UObject> ObjectClass)
```
Returns whether or not the object passed in is of (or inherits from) the class type.
@return True if the object is of (or inherits from) the class type.

### OpenLevel
```angelscript
void OpenLevel(FName LevelName, bool bAbsolute, FString Options)
```
Travel to another level

@param       LevelName                       the level to open
@param       bAbsolute                       if true options are reset, if false options are carried over from current level
@param       Options                         a string of options to use for the travel URL

### OpenLevelBySoftObjectPtr
```angelscript
void OpenLevelBySoftObjectPtr(TSoftObjectPtr<UWorld> Level, bool bAbsolute, FString Options)
```
Travel to another level

@param       Level                           the level to open
@param       bAbsolute                       if true options are reset, if false options are carried over from current level
@param       Options                         a string of options to use for the travel URL

### ParseOption
```angelscript
FString ParseOption(FString Options, FString Key)
```
Find an option in the options string and return it.
@param Options               The string containing the options.
@param Key                   The key to find the value of in Options.
@return                              The value associated with Key if Key found in Options string.

### PlayDialogue2D
```angelscript
void PlayDialogue2D(UDialogueWave Dialogue, FDialogueContext Context, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime)
```
Plays a dialogue directly with no attenuation, perfect for UI.

* Fire and Forget.
* Not Replicated.
@param Dialogue - dialogue to play
@param Context - context the dialogue is to play in
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the dialogue to begin playback at

### PlayDialogueAtLocation
```angelscript
void PlayDialogueAtLocation(UDialogueWave Dialogue, FDialogueContext Context, FVector Location, FRotator Rotation, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundAttenuation AttenuationSettings)
```
Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor.
    Replication is also not handled at this point.
@param Dialogue - dialogue to play
@param Context - context the dialogue is to play in
@param Location - World position to play dialogue at
@param Rotation - World rotation to play dialogue at
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the dialogue to begin playback at
@param AttenuationSettings - Override attenuation settings package to play sound with

### PlaySound2D
```angelscript
void PlaySound2D(USoundBase Sound, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundConcurrency ConcurrencySettings, const AActor OwningActor, bool bIsUISound)
```
Plays a sound directly with no attenuation, perfect for UI sounds.

* Fire and Forget.
* Not Replicated.
@param Sound - Sound to play.
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the sound to begin playback at
@param ConcurrencySettings - Override concurrency settings package to play sound with
@param OwningActor - The actor to use as the "owner" for concurrency settings purposes.
                                             Allows PlaySound calls to do a concurrency limit per owner.
@param bIsUISound - True if sound is UI related, else false

### PlaySoundAtLocation
```angelscript
void PlaySoundAtLocation(USoundBase Sound, FVector Location, FRotator Rotation, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundAttenuation AttenuationSettings, USoundConcurrency ConcurrencySettings, const AActor OwningActor, const UInitialActiveSoundParams InitialParams)
```
Plays a sound at the given location. This is a fire and forget sound and does not travel with any actor.
Replication is also not handled at this point.
@param Sound - sound to play
@param Location - World position to play sound at
@param Rotation - World rotation to play sound at
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the sound to begin playback at
@param AttenuationSettings - Override attenuation settings package to play sound with
@param ConcurrencySettings - Override concurrency settings package to play sound with
@param OwningActor - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls
                                             to do a concurrency limit per owner.

### PlayWorldCameraShake
```angelscript
void PlayWorldCameraShake(TSubclassOf<UCameraShakeBase> Shake, FVector Epicenter, float32 InnerRadius, float32 OuterRadius, float32 Falloff, bool bOrientShakeTowardsEpicenter)
```
Plays an in-world camera shake that affects all nearby local players, with distance-based attenuation. Does not replicate.
@param WorldContextObject - Object that we can obtain a world context from
@param Shake - Camera shake asset to use
@param Epicenter - location to place the effect in world space
@param InnerRadius - Cameras inside this radius are ignored
@param OuterRadius - Cameras outside of InnerRadius and inside this are effected
@param Falloff - Affects falloff of effect as it nears OuterRadius
@param bOrientShakeTowardsEpicenter - Changes the rotation of shake to point towards epicenter instead of forward

### PopSoundMixModifier
```angelscript
void PopSoundMixModifier(USoundMix InSoundMixModifier)
```
Pop a sound mix modifier from the audio system
    @param InSoundMixModifier The Sound Mix Modifier to remove from the system

### PrimeAllSoundsInSoundClass
```angelscript
void PrimeAllSoundsInSoundClass(USoundClass InSoundClass)
```
Primes the sound waves in the given USoundClass, caching the first chunk of streamed audio.

### PrimeSound
```angelscript
void PrimeSound(USoundBase InSound)
```
Primes the sound, caching the first chunk of streamed audio.

### ProjectWorldToScreen
```angelscript
bool ProjectWorldToScreen(const APlayerController Player, FVector WorldPosition, FVector2D& ScreenPosition, bool bPlayerViewportRelative)
```
Transforms the given 3D world-space point into a its 2D screen space coordinate.
@param Player                        Project using this player's view.
@param WorldPosition         World position to project.
@param ScreenPosition        (out) Corresponding 2D position in screen space
@param bPlayerViewportRelative       Should this be relative to the player viewport subregion (useful when using player attached widgets in split screen)

### PushSoundMixModifier
```angelscript
void PushSoundMixModifier(USoundMix InSoundMixModifier)
```
Push a sound mix modifier onto the audio system
@param InSoundMixModifier The Sound Mix Modifier to add to the system

### RebaseLocalOriginOntoZero
```angelscript
FVector RebaseLocalOriginOntoZero(FVector WorldLocation)
```
Returns origin based position for local world location.

### RebaseZeroOriginOntoLocal
```angelscript
FVector RebaseZeroOriginOntoLocal(FVector WorldLocation)
```
Returns local location for origin based position.

### RemovePlayer
```angelscript
void RemovePlayer(APlayerController Player, bool bDestroyPawn)
```
Removes a local player from this game.

@param Player                        The player controller of the player to be removed
@param bDestroyPawn          Whether the controlled pawn should be deleted as well

### SaveGameToSlot
```angelscript
bool SaveGameToSlot(USaveGame SaveGameObject, FString SlotName, int UserIndex)
```
Save the contents of the SaveGameObject to a platform-specific save slot/file.
@note This will write out all non-transient properties, the SaveGame property flag is not checked

@param SaveGameObject        Object that contains data about the save game that we want to write out
@param SlotName                      Name of save game slot to save to.
@param UserIndex                     The platform user index that identifies the user doing the saving, ignored on some platforms.
@return                                      Whether we successfully saved this information

### SetActiveSpatialPluginByName
```angelscript
bool SetActiveSpatialPluginByName(FName InPluginName)
```
Get list of available Audio Spatialization Plugins

### SetBaseSoundMix
```angelscript
void SetBaseSoundMix(USoundMix InSoundMix)
```
Set the sound mix of the audio system for special EQing

### SetEnableWorldRendering
```angelscript
void SetEnableWorldRendering(bool bEnable)
```
Enabled rendering of the world
@param       bEnable         Whether the world should be rendered or not

### SetForceDisableSplitscreen
```angelscript
void SetForceDisableSplitscreen(bool bDisable)
```
Enables split screen
@param       bDisable                Whether the viewport should split screen between local players or not

### SetGamePaused
```angelscript
bool SetGamePaused(bool bPaused)
```
Sets the game's paused state
@param       bPaused         Whether the game should be paused or not
@return      Whether the game was successfully paused/unpaused

### SetGlobalListenerFocusParameters
```angelscript
void SetGlobalListenerFocusParameters(float32 FocusAzimuthScale, float32 NonFocusAzimuthScale, float32 FocusDistanceScale, float32 NonFocusDistanceScale, float32 FocusVolumeScale, float32 NonFocusVolumeScale, float32 FocusPriorityScale, float32 NonFocusPriorityScale)
```
Sets the global listener focus parameters, which will scale focus behavior of sounds based on their focus azimuth
settings in their attenuation settings.

* Fire and Forget.
* Not Replicated.
@param FocusAzimuthScale - An angle scale value used to scale the azimuth angle that defines where sounds are in-focus.
@param NonFocusAzimuthScale- An angle scale value used to scale the azimuth angle that defines where sounds are out-of-focus.
@param FocusDistanceScale - A distance scale value to use for sounds which are in-focus. Values < 1.0 will reduce perceived
                                                        distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds.
@param NonFocusDistanceScale - A distance scale value to use for sounds which are out-of-focus. Values < 1.0 will reduce
                                                               perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds.
@param FocusVolumeScale- A volume attenuation value to use for sounds which are in-focus.
@param NonFocusVolumeScale- A volume attenuation value to use for sounds which are out-of-focus.
@param FocusPriorityScale - A priority scale value (> 0.0) to use for sounds which are in-focus. Values < 1.0 will reduce
                                                        the priority of in-focus sounds, values > 1.0 will increase the priority of in-focus sounds.
@param NonFocusPriorityScale - A priority scale value (> 0.0) to use for sounds which are out-of-focus. Values < 1.0 will
                                                               reduce the priority of sounds out-of-focus sounds, values > 1.0 will increase the priority of
                                                               out-of-focus sounds.

### SetGlobalPitchModulation
```angelscript
void SetGlobalPitchModulation(float32 PitchModulation, float32 TimeSec)
```
Sets a global pitch modulation scalar that will apply to all non-UI sounds

* Fire and Forget.
* Not Replicated.
@param PitchModulation - A pitch modulation value to globally set.
@param TimeSec - A time value to linearly interpolate the global modulation pitch over from it's current value.

### SetGlobalTimeDilation
```angelscript
void SetGlobalTimeDilation(float32 TimeDilation)
```
Sets the global time dilation.
@param       TimeDilation    value to set the global time dilation to

### SetMaxAudioChannelsScaled
```angelscript
void SetMaxAudioChannelsScaled(float32 MaxChannelCountScale)
```
Sets the max number of voices (also known as "channels") dynamically by percentage. E.g. if you want to temporarily
reduce voice count by 50%, use 0.50. Later, you can return to the original max voice count by using 1.0.
@param MaxChannelCountScale The percentage of the original voice count to set the max number of voices to

### SetPlayerControllerID
```angelscript
void SetPlayerControllerID(APlayerController Player, int ControllerId)
```
Sets what physical controller ID a player should be using. This only works for local player controllers.

@param Player                        The player controller of the player to change the controller ID of
@param ControllerId          The controller ID to assign to this player

### SetPlayerPlatformUserId
```angelscript
void SetPlayerPlatformUserId(APlayerController PlayerController, FPlatformUserId UserId)
```
Sets what platform user id a player should be using. This only works for local player controllers.

@param Player                        The player controller of the player to change the platform user of
@param PlatformUserId        The platform user id to assign this player

### SetSoundClassDistanceScale
```angelscript
void SetSoundClassDistanceScale(USoundClass SoundClass, float32 DistanceAttenuationScale, float32 TimeSec)
```
Linearly interpolates the attenuation distance scale value from it's current attenuation distance override value
(1.0f it not overridden) to its new attenuation distance override, over the given amount of time

* Fire and Forget.
* Not Replicated.
@param SoundClass - Sound class to to use to set the attenuation distance scale on.
@param DistanceAttenuationScale - A scalar for the attenuation distance used for computing distance attenuation.
@param TimeSec - A time value to linearly interpolate from the current distance attenuation scale value to the new value.

### SetSoundMixClassOverride
```angelscript
void SetSoundMixClassOverride(USoundMix InSoundMixModifier, USoundClass InSoundClass, float32 Volume, float32 Pitch, float32 FadeInTime, bool bApplyToChildren)
```
Overrides the sound class adjuster in the given sound mix. If the sound class does not exist in the input sound mix,
    the sound class adjuster will be added to the list of active sound mix modifiers.
@param InSoundMixModifier The sound mix to modify.
@param InSoundClass The sound class to override (or add) in the sound mix.
@param Volume The volume scale to set the sound class adjuster to.
@param Pitch The pitch scale to set the sound class adjuster to.
@param FadeInTime The interpolation time to use to go from the current sound class adjuster values to the new values.
@param bApplyToChildren Whether or not to apply this override to the sound class' children or to just the specified sound class.

### SetSubtitlesEnabled
```angelscript
void SetSubtitlesEnabled(bool bEnabled)
```
Will set subtitles to be enabled or disabled.
@param bEnabled will enable subtitle drawing if true, disable if false.

### SetViewportMouseCaptureMode
```angelscript
void SetViewportMouseCaptureMode(EMouseCaptureMode MouseCaptureMode)
```
Sets the current viewport mouse capture mode

### SetWorldOriginLocation
```angelscript
void SetWorldOriginLocation(FIntVector NewLocation)
```
Requests a new location for a world origin.

### SpawnDecalAtLocation
```angelscript
UDecalComponent SpawnDecalAtLocation(UMaterialInterface DecalMaterial, FVector DecalSize, FVector Location, FRotator Rotation, float32 LifeSpan)
```
Spawns a decal at the given location and rotation, fire and forget. Does not replicate.
@param DecalMaterial - decal's material
@param DecalSize - size of decal
@param Location - location to place the decal in world space
@param Rotation - rotation to place the decal in world space
@param LifeSpan - destroy decal component after time runs out (0 = infinite)

### SpawnDecalAttached
```angelscript
UDecalComponent SpawnDecalAttached(UMaterialInterface DecalMaterial, FVector DecalSize, USceneComponent AttachToComponent, FName AttachPointName, FVector Location, FRotator Rotation, EAttachLocation LocationType, float32 LifeSpan)
```
Spawns a decal attached to and following the specified component. Does not replicate.
@param DecalMaterial - decal's material
@param DecalSize - size of decal
@param AttachComponent - Component to attach to.
@param AttachPointName - Optional named point within the AttachComponent to spawn the emitter at
@param Location - Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world position that will be translated to a relative offset
@param Rotation - Depending on the value of LocationType this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a realative offset
@param LocationType - Specifies whether Location is a relative offset or an absolute world position
@param LifeSpan - destroy decal component after time runs out (0 = infinite)

### SpawnDialogue2D
```angelscript
UAudioComponent SpawnDialogue2D(UDialogueWave Dialogue, FDialogueContext Context, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, bool bAutoDestroy)
```
Spawns a DialogueWave, a special type of Asset that requires Context data in order to resolve a specific SoundBase,
which is then passed on to the new Audio Component. Audio Components created using this function by default will not
have Spatialization applied. Sound instances will begin playing upon spawning this Audio Component.

* Not Replicated.
@param Dialogue - dialogue to play
@param Context - context the dialogue is to play in
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the dialogue to begin playback at
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound
                                              finishes (by completing or stopping) or whether it can be reactivated
@return An audio component to manipulate the spawned sound

### SpawnDialogueAtLocation
```angelscript
UAudioComponent SpawnDialogueAtLocation(UDialogueWave Dialogue, FDialogueContext Context, FVector Location, FRotator Rotation, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundAttenuation AttenuationSettings, bool bAutoDestroy)
```
Spawns a DialogueWave, a special type of Asset that requires Context data in order to resolve a specific SoundBase,
which is then passed on to the new Audio Component. This function allows users to create and play Audio Components at a
specific World Location and Rotation. Useful for spatialized and/or distance-attenuated dialogue.
@param Dialogue - Dialogue to play
@param Context - Context the dialogue is to play in
@param Location - World position to play dialogue at
@param Rotation - World rotation to play dialogue at
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far into the dialogue to begin playback at
@param AttenuationSettings - Override attenuation settings package to play sound with
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound finishes
                                             (by completing or stopping) or whether it can be reactivated
@return Audio Component to manipulate the playing dialogue with

### SpawnDialogueAttached
```angelscript
UAudioComponent SpawnDialogueAttached(UDialogueWave Dialogue, FDialogueContext Context, USceneComponent AttachToComponent, FName AttachPointName, FVector Location, FRotator Rotation, EAttachLocation LocationType, bool bStopWhenAttachedToDestroyed, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundAttenuation AttenuationSettings, bool bAutoDestroy)
```
Spawns a DialogueWave, a special type of Asset that requires Context data in order to resolve a specific SoundBase,
    which is then passed on to the new Audio Component. This function allows users to create and play Audio Components
    attached to a specific Scene Component. Useful for spatialized and/or distance-attenuated dialogue that needs to
    follow another object in space.
@param Dialogue - dialogue to play
@param Context - context the dialogue is to play in
@param AttachComponent - Component to attach to.
@param AttachPointName - Optional named point within the AttachComponent to play the sound at
@param Location - Depending on the value of Location Type this is either a relative offset from the
                                     attach component/point or an absolute world position that will be translated to a relative offset
@param Rotation - Depending on the value of Location Type this is either a relative offset from the
                                     attach component/point or an absolute world rotation that will be translated to a relative offset
@param LocationType - Specifies whether Location is a relative offset or an absolute world position
@param bStopWhenAttachedToDestroyed - Specifies whether the sound should stop playing when the owner its attached
                                                                             to is destroyed.
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the dialogue to begin playback at
@param AttenuationSettings - Override attenuation settings package to play sound with
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound finishes
                                             (by completing or stopping) or whether it can be reactivated
@return Audio Component to manipulate the playing dialogue with

### SpawnEmitterAtLocation
```angelscript
UParticleSystemComponent SpawnEmitterAtLocation(UParticleSystem EmitterTemplate, FVector Location, FRotator Rotation, FVector Scale, bool bAutoDestroy, EPSCPoolMethod PoolingMethod, bool bAutoActivateSystem)
```
Plays the specified effect at the given location and rotation, fire and forget. The system will go away when the effect is complete. Does not replicate.
@param WorldContextObject - Object that we can obtain a world context from
@param EmitterTemplate - particle system to create
@param Location - location to place the effect in world space
@param Rotation - rotation to place the effect in world space
@param Scale - scale to create the effect at
@param bAutoDestroy - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated
@param PoolingMethod - Method used for pooling this component. Defaults to none.
@param bAutoActivate - Whether the component will be automatically activated on creation.

### SpawnEmitterAttached
```angelscript
UParticleSystemComponent SpawnEmitterAttached(UParticleSystem EmitterTemplate, USceneComponent AttachToComponent, FName AttachPointName, FVector Location, FRotator Rotation, FVector Scale, EAttachLocation LocationType, bool bAutoDestroy, EPSCPoolMethod PoolingMethod, bool bAutoActivate)
```
Plays the specified effect attached to and following the specified component. The system will go away when the effect is complete. Does not replicate.
@param EmitterTemplate - particle system to create
@param AttachComponent - Component to attach to.
@param AttachPointName - Optional named point within the AttachComponent to spawn the emitter at
@param Location - Depending on the value of LocationType this is either a relative offset from the attach component/point or an absolute world location that will be translated to a relative offset (if LocationType is KeepWorldPosition).
@param Rotation - Depending on the value of LocationType this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a relative offset (if LocationType is KeepWorldPosition).
@param Scale - Depending on the value of LocationType this is either a relative scale from the attach component or an absolute world scale that will be translated to a relative scale (if LocationType is KeepWorldPosition).
@param LocationType - Specifies whether Location is a relative offset or an absolute world position
@param bAutoDestroy - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated
@param PoolingMethod - Method used for pooling this component. Defaults to none.
@param bAutoActivate - Whether the component will be automatically activated on creation.

### SpawnForceFeedbackAtLocation
```angelscript
UForceFeedbackComponent SpawnForceFeedbackAtLocation(UForceFeedbackEffect ForceFeedbackEffect, FVector Location, FRotator Rotation, bool bLooping, float32 IntensityMultiplier, float32 StartTime, UForceFeedbackAttenuation AttenuationSettings, bool bAutoDestroy)
```
Plays a force feedback effect at the given location. This is a fire and forget effect and does not travel with any actor. Replication is also not handled at this point.
@param ForceFeedbackEffect - effect to play
@param Location - World position to center the effect at
@param Rotation - World rotation to center the effect at
@param IntensityMultiplier - Intensity multiplier
@param StartTime - How far in to the feedback effect to begin playback at
@param AttenuationSettings - Override attenuation settings package to play effect with
@param bAutoDestroy - Whether the returned force feedback component will be automatically cleaned up when the feedback pattern finishes (by completing or stopping) or whether it can be reactivated
@return Force Feedback Component to manipulate the playing feedback effect with

### SpawnForceFeedbackAttached
```angelscript
UForceFeedbackComponent SpawnForceFeedbackAttached(UForceFeedbackEffect ForceFeedbackEffect, USceneComponent AttachToComponent, FName AttachPointName, FVector Location, FRotator Rotation, EAttachLocation LocationType, bool bStopWhenAttachedToDestroyed, bool bLooping, float32 IntensityMultiplier, float32 StartTime, UForceFeedbackAttenuation AttenuationSettings, bool bAutoDestroy)
```
Plays a force feedback effect attached to and following the specified component. This is a fire and forget effect. Replication is also not handled at this point.
@param ForceFeedbackEffect - effect to play
@param AttachComponent - Component to attach to.
@param AttachPointName - Optional named point within the AttachComponent to attach to
@param Location - Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world position that will be translated to a relative offset
@param Rotation - Depending on the value of Location Type this is either a relative offset from the attach component/point or an absolute world rotation that will be translated to a relative offset
@param LocationType - Specifies whether Location is a relative offset or an absolute world position
@param bStopWhenAttachedToDestroyed - Specifies whether the feedback effect should stop playing when the owner of the attach to component is destroyed.
@param IntensityMultiplier - Intensity multiplier
@param StartTime - How far in to the feedback effect to begin playback at
@param AttenuationSettings - Override attenuation settings package to play effect with
@param bAutoDestroy - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated
@return Force Feedback Component to manipulate the playing feedback effect with

### SpawnSound2D
```angelscript
UAudioComponent SpawnSound2D(USoundBase Sound, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundConcurrency ConcurrencySettings, bool bPersistAcrossLevelTransition, bool bAutoDestroy)
```
This function allows users to create Audio Components with settings specifically for non-spatialized,
non-distance-attenuated sounds. Audio Components created using this function by default will not have
Spatialization applied. Sound instances will begin playing upon spawning this Audio Component.

* Not Replicated.
@param Sound - Sound to play.
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the sound to begin playback at
@param ConcurrencySettings - Override concurrency settings package to play sound with
@param PersistAcrossLevelTransition - Whether the sound should continue to play when the map it was played in is unloaded
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound finishes
                                              (by completing or stopping) or whether it can be reactivated
@return An audio component to manipulate the spawned sound

### SpawnSoundAtLocation
```angelscript
UAudioComponent SpawnSoundAtLocation(USoundBase Sound, FVector Location, FRotator Rotation, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundAttenuation AttenuationSettings, USoundConcurrency ConcurrencySettings, bool bAutoDestroy)
```
Spawns a sound at the given location. This does not travel with any actor. Replication is also not handled at this point.
@param Sound - sound to play
@param Location - World position to play sound at
@param Rotation - World rotation to play sound at
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the sound to begin playback at
@param AttenuationSettings - Override attenuation settings package to play sound with
@param ConcurrencySettings - Override concurrency settings package to play sound with
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound finishes
                                              (by completing or stopping) or whether it can be reactivated
@return An audio component to manipulate the spawned sound

### SpawnSoundAttached
```angelscript
UAudioComponent SpawnSoundAttached(USoundBase Sound, USceneComponent AttachToComponent, FName AttachPointName, FVector Location, FRotator Rotation, EAttachLocation LocationType, bool bStopWhenAttachedToDestroyed, float32 VolumeMultiplier, float32 PitchMultiplier, float32 StartTime, USoundAttenuation AttenuationSettings, USoundConcurrency ConcurrencySettings, bool bAutoDestroy)
```
This function allows users to create and play Audio Components attached to a specific Scene Component.
Useful for spatialized and/or distance-attenuated sounds that need to follow another object in space.
@param Sound - sound to play
@param AttachComponent - Component to attach to.
@param AttachPointName - Optional named point within the AttachComponent to play the sound at
@param Location - Depending on the value of Location Type this is either a relative offset from
                                     the attach component/point or an absolute world position that will be translated to a relative offset
@param Rotation - Depending on the value of Location Type this is either a relative offset from
                                     the attach component/point or an absolute world rotation that will be translated to a relative offset
@param LocationType - Specifies whether Location is a relative offset or an absolute world position
@param bStopWhenAttachedToDestroyed - Specifies whether the sound should stop playing when the
                                                                             owner of the attach to component is destroyed.
@param VolumeMultiplier - A linear scalar multiplied with the volume, in order to make the sound louder or softer.
@param PitchMultiplier - A linear scalar multiplied with the pitch.
@param StartTime - How far in to the sound to begin playback at
@param AttenuationSettings - Override attenuation settings package to play sound with
@param ConcurrencySettings - Override concurrency settings package to play sound with
@param bAutoDestroy - Whether the returned audio component will be automatically cleaned up when the sound finishes
                                             (by completing or stopping) or whether it can be reactivated
@return An audio component to manipulate the spawned sound

### SuggestProjectileVelocity_CustomArc
```angelscript
bool SuggestProjectileVelocity_CustomArc(FVector& OutLaunchVelocity, FVector StartPos, FVector EndPos, float32 OverrideGravityZ, float32 ArcParam)
```
Returns the launch velocity needed for a projectile at rest at StartPos to land on EndPos.
Assumes a medium arc (e.g. 45 deg on level ground). Projectile velocity is variable and unconstrained.
Does no tracing.

@param OutLaunchVelocity                      Returns the launch velocity required to reach the EndPos
@param StartPos                                       Start position of the simulation
@param EndPos                                         Desired end location for the simulation
@param OverrideGravityZ                       Optional override of WorldGravityZ
@param ArcParam                                       Change height of arc between 0.0-1.0 where 0.5 is the default medium arc, 0 is up, and 1 is directly toward EndPos.

### SuggestProjectileVelocity_MovingTarget
```angelscript
bool SuggestProjectileVelocity_MovingTarget(FVector& OutLaunchVelocity, FVector ProjectileStartLocation, AActor TargetActor, FVector TargetLocationOffset, float GravityZOverride, float TimeToTarget, EDrawDebugTrace DrawDebugType, float32 DrawDebugTime, FLinearColor DrawDebugColor)
```
Returns a launch velocity need for a projectile to hit the TargetActor in TimeToTarget seconds based on the TargetActor's current velocity.
This assumes the projectile is only accelerated by gravity (i.e. no outside forces), and that the TargetActor is moving at a constant velocity.

@param OutLaunchVelocity                     The launch velocity returned from this calculation
@param ProjectileStartLocation       Location the projectile is launched from
@param TargetActor                           Actor that the projectile should hit in TimeToTarget seconds
@param TargetLocationOffset          Offset to apply to the location the projectile is aiming for
@param GravityZOverride                      Optional override of WorldGravityZ
@param TimeToTarget                          Time (in seconds) between the projectile being launched and the projectile hitting the TargetActor - clamped to be at least 0.1

### UnloadStreamLevel
```angelscript
void UnloadStreamLevel(FName LevelName, FLatentActionInfo LatentInfo, bool bShouldBlockOnUnload)
```
Unload a streamed in level (by Name)

### UnloadStreamLevelBySoftObjectPtr
```angelscript
void UnloadStreamLevelBySoftObjectPtr(TSoftObjectPtr<UWorld> Level, FLatentActionInfo LatentInfo, bool bShouldBlockOnUnload)
```
Unload a streamed in level (by Object Reference)

### UnRetainAllSoundsInSoundClass
```angelscript
void UnRetainAllSoundsInSoundClass(USoundClass InSoundClass)
```
Iterate through all sound waves and releases handles to retained chunks. (If the chunk is not being played it will be up for eviction)

### AsyncLoadGameFromSlot
```angelscript
void AsyncLoadGameFromSlot(FString SlotName, int UserIndex, FAsyncLoadGameFromSlotDynamicDelegate Delegate)
```
Schedule an async load of a specific slot. UAsyncActionHandleSaveGame::AsyncLoadGameFromSlot is the blueprint version of this.
This will do the platform-specific read on a worker thread, the serialize and creation on the game thread, and then will call the passed in delegate
The passed in delegate will be copied to a worker thread so make sure any payload is thread safe to copy by value

@param SlotName                      Name of the save game slot to load from.
@param UserIndex                     For some platforms, master user index to identify the user doing the loading.
@param LoadedDelegate        Delegate that will be called on game thread when load succeeds or fails.

### AsyncSaveGameToSlot
```angelscript
void AsyncSaveGameToSlot(USaveGame SaveGameObject, FString SlotName, int UserIndex, FAsyncSaveGameToSlotDynamicDelegate Delegate)
```
Schedule an async save to a specific slot. UAsyncActionHandleSaveGame::AsyncSaveGameToSlot is the blueprint version of this.
This will do the serialize on the game thread, the platform-specific write on a worker thread, then call the complete delegate on the game thread.
The passed in delegate will be copied to a worker thread so make sure any payload is thread safe to copy by value.

@param SaveGameObject        Object that contains data about the save game that we want to write out.
@param SlotName                      Name of the save game slot to load from.
@param UserIndex                     For some platforms, master user index to identify the user doing the loading.
@param SavedDelegate         Delegate that will be called on game thread when save succeeds or fails.


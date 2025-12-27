# AGameModeBase

**继承自**: `AInfo`

The GameModeBase defines the game being played. It governs the game rules, scoring, what actors
are allowed to exist in this game type, and who may enter the game.

It is only instanced on the server and will never exist on the client.

A GameModeBase actor is instantiated when the level is initialized for gameplay in
C++ UGameEngine::LoadMap().

The class of this GameMode actor is determined by (in order) either the URL ?game=xxx,
the GameMode Override value set in the World Settings, or the DefaultGameMode entry set
in the game's Project Settings.

@see https://docs.unrealengine.com/latest/INT/Gameplay/Framework/GameMode/index.html

## 属性

### OptionsString
- **类型**: `FString`
- **描述**: Save options string and parse it when needed

### GameSessionClass
- **类型**: `TSubclassOf<AGameSession>`

### GameStateClass
- **类型**: `TSubclassOf<AGameStateBase>`

### PlayerControllerClass
- **类型**: `TSubclassOf<APlayerController>`

### PlayerStateClass
- **类型**: `TSubclassOf<APlayerState>`

### HUDClass
- **类型**: `TSubclassOf<AHUD>`

### DefaultPawnClass
- **类型**: `TSubclassOf<APawn>`

### SpectatorClass
- **类型**: `TSubclassOf<ASpectatorPawn>`

### ReplaySpectatorPlayerControllerClass
- **类型**: `TSubclassOf<APlayerController>`

### ServerStatReplicatorClass
- **类型**: `TSubclassOf<AServerStatReplicator>`

### DefaultPlayerName
- **类型**: `FText`
- **描述**: The default player name assigned to players that join with no name specified.

### GameNetDriverReplicationSystem
- **类型**: `EReplicationSystem`

### bUseSeamlessTravel
- **类型**: `bool`

### bStartPlayersAsSpectators
- **类型**: `bool`

### bPauseable
- **类型**: `bool`

## 方法

### CanSpectate
```angelscript
bool CanSpectate(APlayerController Viewer, APlayerState ViewTarget)
```
Return whether Viewer is allowed to spectate from the point of view of ViewTarget.

### ChangeName
```angelscript
void ChangeName(AController Controller, FString NewName, bool bNameChange)
```
Sets the name for a controller
@param Controller    The controller of the player to change the name of
@param NewName               The name to set the player to
@param bNameChange   Whether the name is changing or if this is the first time it has been set

### ChoosePlayerStart
```angelscript
AActor ChoosePlayerStart(AController Player)
```
Return the 'best' player start for this player to spawn from
Default implementation looks for a random unoccupied spot

@param Player is the controller for whom we are choosing a playerstart
@returns AActor chosen as player start (usually a PlayerStart)

### FindPlayerStart
```angelscript
AActor FindPlayerStart(AController Player, FString IncomingName)
```
Return the specific player start actor that should be used for the next spawn
This will either use a previously saved startactor, or calls ChoosePlayerStart

@param Player The AController for whom we are choosing a Player Start
@param IncomingName Specifies the tag of a Player Start to use
@returns Actor chosen as player start (usually a PlayerStart)

### GetDefaultPawnClassForController
```angelscript
UClass GetDefaultPawnClassForController(AController InController)
```
Returns default pawn class for given controller

### GetNumPlayers
```angelscript
int GetNumPlayers()
```
Returns number of active human players, excluding spectators

### GetNumSpectators
```angelscript
int GetNumSpectators()
```
Returns number of human players currently spectating

### HandleStartingNewPlayer
```angelscript
void HandleStartingNewPlayer(APlayerController NewPlayer)
```
Signals that a player is ready to enter the game, which may start it up

### HasMatchEnded
```angelscript
bool HasMatchEnded()
```
Returns true if the match can be considered ended

### HasMatchStarted
```angelscript
bool HasMatchStarted()
```
Returns true if the match start callbacks have been called

### InitializeHUDForPlayer
```angelscript
void InitializeHUDForPlayer(APlayerController NewPlayer)
```
Initialize the AHUD object for a player. Games can override this to do something different

### InitStartSpot
```angelscript
void InitStartSpot(AActor StartSpot, AController NewPlayer)
```
Called from RestartPlayerAtPlayerStart, can be used to initialize the start spawn actor

### K2_FindPlayerStart
```angelscript
AActor K2_FindPlayerStart(AController Player, FString IncomingName)
```
Return the specific player start actor that should be used for the next spawn
This will either use a previously saved startactor, or calls ChoosePlayerStart

@param Player The AController for whom we are choosing a Player Start
@param IncomingName Specifies the tag of a Player Start to use
@returns Actor chosen as player start (usually a PlayerStart)

### OnChangeName
```angelscript
void OnChangeName(AController Other, FString NewName, bool bNameChange)
```
Overridable event for GameMode blueprint to respond to a change name call
@param Controller    The controller of the player to change the name of
@param NewName               The name to set the player to
@param bNameChange   Whether the name is changing or if this is the first time it has been set

### OnLogout
```angelscript
void OnLogout(AController ExitingController)
```
Implementable event when a Controller with a PlayerState leaves the game.

### OnRestartPlayer
```angelscript
void OnRestartPlayer(AController NewPlayer)
```
Implementable event called at the end of RestartPlayer

### OnSwapPlayerControllers
```angelscript
void OnSwapPlayerControllers(APlayerController OldPC, APlayerController NewPC)
```
Called when a PlayerController is swapped to a new one during seamless travel

### OnPostLogin
```angelscript
void OnPostLogin(APlayerController NewPlayer)
```
Notification that a player has successfully logged in, and has been given a player controller

### MustSpectate
```angelscript
bool MustSpectate(APlayerController NewPlayerController)
```
Returns true if NewPlayerController may only join the server as a spectator.

### PlayerCanRestart
```angelscript
bool PlayerCanRestart(APlayerController Player)
```
Returns true if it's valid to call RestartPlayer. By default will call Player->CanRestartPlayer

### ResetLevel
```angelscript
void ResetLevel()
```
Overridable function called when resetting level. This is used to reset the game state while staying in the same map
Default implementation calls Reset() on all actors except GameMode and Controllers

### RestartPlayer
```angelscript
void RestartPlayer(AController NewPlayer)
```
Tries to spawn the player's pawn, at the location returned by FindPlayerStart

### RestartPlayerAtPlayerStart
```angelscript
void RestartPlayerAtPlayerStart(AController NewPlayer, AActor StartSpot)
```
Tries to spawn the player's pawn at the specified actor's location

### RestartPlayerAtTransform
```angelscript
void RestartPlayerAtTransform(AController NewPlayer, FTransform SpawnTransform)
```
Tries to spawn the player's pawn at a specific location

### ReturnToMainMenuHost
```angelscript
void ReturnToMainMenuHost()
```
Return to main menu, and disconnect any players

### ShouldReset
```angelscript
bool ShouldReset(AActor ActorToReset)
```
Overridable function to determine whether an Actor should have Reset called when the game has Reset called on it.
Default implementation returns true
@param ActorToReset The actor to make a determination for
@return true if ActorToReset should have Reset() called on it while restarting the game,
                false if the GameMode will manually reset it or if the actor does not need to be reset

### SpawnDefaultPawnAtTransform
```angelscript
APawn SpawnDefaultPawnAtTransform(AController NewPlayer, FTransform SpawnTransform)
```
Called during RestartPlayer to actually spawn the player's pawn, when using a transform
@param       NewPlayer - Controller for whom this pawn is spawned
@param       SpawnTransform - Transform at which to spawn pawn
@return      a pawn of the default pawn class

### SpawnDefaultPawnFor
```angelscript
APawn SpawnDefaultPawnFor(AController NewPlayer, AActor StartSpot)
```
Called during RestartPlayer to actually spawn the player's pawn, when using a start spot
@param       NewPlayer - Controller for whom this pawn is spawned
@param       StartSpot - Actor at which to spawn pawn
@return      a pawn of the default pawn class

### StartPlay
```angelscript
void StartPlay()
```
Transitions to calls BeginPlay on actors.


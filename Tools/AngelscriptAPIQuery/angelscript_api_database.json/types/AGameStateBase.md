# AGameStateBase

**继承自**: `AInfo`

GameStateBase is a class that manages the game's global state, and is spawned by GameModeBase.
It exists on both the client and the server and is fully replicated.

## 属性

### GameModeClass
- **类型**: `TSubclassOf<AGameModeBase>`
- **描述**: Class of the server's game mode, assigned by GameModeBase.

### AuthorityGameMode
- **类型**: `AGameModeBase`
- **描述**: Instance of the current game mode, exists only on the server. For non-authority clients, this will be NULL.

### SpectatorClass
- **类型**: `TSubclassOf<ASpectatorPawn>`
- **描述**: Class used by spectators, assigned by GameModeBase.

### PlayerArray
- **类型**: `TArray<TObjectPtr<APlayerState>>`
- **描述**: Array of all PlayerStates, maintained on both server and clients (PlayerStates are always relevant)

### ServerWorldTimeSecondsUpdateFrequency
- **类型**: `float32`
- **描述**: Frequency that the server updates the replicated TimeSeconds from the world. Set to zero to disable periodic updates.

## 方法

### GetPlayerRespawnDelay
```angelscript
float32 GetPlayerRespawnDelay(AController Controller)
```
Returns how much time needs to be spent before a player can respawn

### GetPlayerStartTime
```angelscript
float32 GetPlayerStartTime(AController Controller)
```
Returns the time that should be used as when a player started

### GetServerWorldTimeSeconds
```angelscript
float GetServerWorldTimeSeconds()
```
Returns the simulated TimeSeconds on the server, will be synchronized on client and server

### HasBegunPlay
```angelscript
bool HasBegunPlay()
```
Returns true if the world has started play (called BeginPlay on actors)

### HasMatchEnded
```angelscript
bool HasMatchEnded()
```
Returns true if the match can be considered ended. Defaults to false.

### HasMatchStarted
```angelscript
bool HasMatchStarted()
```
Returns true if the world has started match (called MatchStarted callbacks)


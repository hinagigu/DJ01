# AGameMode

**继承自**: `AGameModeBase`

GameMode is a subclass of GameModeBase that behaves like a multiplayer match-based game.
It has default behavior for picking spawn points and match state.
If you want a simpler base, inherit from GameModeBase instead.

## 属性

### NumBots
- **类型**: `int`
- **描述**: number of non-human players (AI controlled but participating as a player).

### MinRespawnDelay
- **类型**: `float32`

### NumTravellingPlayers
- **类型**: `int`
- **描述**: Number of players that are still traveling from a previous map

### InactivePlayerStateLifeSpan
- **类型**: `float32`
- **描述**: Time a playerstate will stick around in an inactive state after a player logout

### MaxInactivePlayers
- **类型**: `int`
- **描述**: The maximum number of inactive players before we kick the oldest ones out

### bDelayedStart
- **类型**: `bool`

## 方法

### AbortMatch
```angelscript
void AbortMatch()
```
Report that a match has failed due to unrecoverable error

### EndMatch
```angelscript
void EndMatch()
```
Transition from InProgress to WaitingPostMatch. You can call this manually, will also get called if ReadyToEndMatch returns true

### GetMatchState
```angelscript
FName GetMatchState()
```
Returns the current match state, this is an accessor to protect the state machine flow

### IsMatchInProgress
```angelscript
bool IsMatchInProgress()
```
Returns true if the match state is InProgress or other gameplay state

### OnSetMatchState
```angelscript
void OnSetMatchState(FName NewState)
```
Implementable event to respond to match state changes

### ReadyToEndMatch
```angelscript
bool ReadyToEndMatch()
```
Returns true if ready to End Match. Games should override this

### ReadyToStartMatch
```angelscript
bool ReadyToStartMatch()
```
Returns true if ready to Start Match. Games should override this

### RestartGame
```angelscript
void RestartGame()
```
Restart the game, by default travel to the current map

### Say
```angelscript
void Say(FString Msg)
```
Exec command to broadcast a string to all players

### StartMatch
```angelscript
void StartMatch()
```
Transition from WaitingToStart to InProgress. You can call this manually, will also get called if ReadyToStartMatch returns true


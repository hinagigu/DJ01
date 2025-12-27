# APlayerState

**继承自**: `AInfo`

A PlayerState is created for every player on a server (or in a standalone game).
PlayerStates are replicated to all clients, and contain network game relevant information about the player, such as playername, score, etc.

## 属性

### OnPawnSet
- **类型**: `FOnPlayerStatePawnSet`

### PawnPrivate
- **类型**: `APawn`
- **描述**: The pawn that is controlled by by this player state.

### bIsSpectator
- **类型**: `bool`

### bIsABot
- **类型**: `bool`

### bShouldUpdateReplicatedPing
- **类型**: `bool`

## 方法

### GetUniqueId
```angelscript
FUniqueNetIdRepl GetUniqueId()
```
Gets the online unique id for a player. If a player is logged in this will be consistent across all clients and servers.

### GetCompressedPing
```angelscript
uint8 GetCompressedPing()
```
Gets the literal value of the compressed Ping value (Ping = PingInMS / 4).

### GetPawn
```angelscript
APawn GetPawn()
```
Return the pawn controlled by this Player State.

### GetPingInMilliseconds
```angelscript
float32 GetPingInMilliseconds()
```
Returns the ping (in milliseconds)

Returns ExactPing if available (local players or when running on the server), and
the replicated CompressedPing (converted back to milliseconds) otherwise.

Note that replication of CompressedPing is controlled by bShouldUpdateReplicatedPing,
and if disabled then this will return 0 or a stale value on clients for player states
that aren't related to local players

### GetPlayerController
```angelscript
APlayerController GetPlayerController()
```
Return the player controller that created this player state, or null for remote clients

### GetPlayerId
```angelscript
int GetPlayerId()
```
Gets the literal value of PlayerId.

### GetPlayerName
```angelscript
FString GetPlayerName()
```
returns current player name

### GetScore
```angelscript
float32 GetScore()
```
Gets the literal value of Score.

### IsABot
```angelscript
bool IsABot()
```
Gets the literal value of bIsABot.

### IsOnlyASpectator
```angelscript
bool IsOnlyASpectator()
```
Gets the literal value of bOnlySpectator.

### IsSpectator
```angelscript
bool IsSpectator()
```
Gets the literal value of bIsSpectator.

### CopyProperties
```angelscript
void CopyProperties(APlayerState NewPlayerState)
```
* Can be implemented in Blueprint Child to move more properties from old to new PlayerState when traveling to a new level
*
* @param NewPlayerState         New PlayerState, which we fill with the current properties

### OverrideWith
```angelscript
void OverrideWith(APlayerState OldPlayerState)
```
* Can be implemented in Blueprint Child to move more properties from old to new PlayerState when reconnecting
*
* @param OldPlayerState         Old PlayerState, which we use to fill the new one with


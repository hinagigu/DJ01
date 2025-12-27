# ALobbyBeaconClient

**继承自**: `AOnlineBeaconClient`

A beacon client used for quality timings to a specified session

## 方法

### ClientAckJoiningServer
```angelscript
void ClientAckJoiningServer()
```

### ClientJoinGame
```angelscript
void ClientJoinGame()
```
Tell the client to join the game

### ClientLoginComplete
```angelscript
void ClientLoginComplete(FUniqueNetIdRepl InUniqueId, bool bWasSuccessful)
```
Client notification result for a single login attempt

@param InUniqueId id of player involved
@param bWasSuccessful result of the login attempt

### ClientPlayerJoined
```angelscript
void ClientPlayerJoined(FText NewPlayerName, FUniqueNetIdRepl InUniqueId)
```
Client notification that another player has joined the lobby

@param NewPlayerName display name of new player
@param InUniqueId unique id of new player

### ClientPlayerLeft
```angelscript
void ClientPlayerLeft(FUniqueNetIdRepl InUniqueId)
```
Client notification that another player has left the lobby

@param InUniqueId unique id of new player

### ClientWasKicked
```angelscript
void ClientWasKicked(FText KickReason)
```
This was client was kicked by the server

@param KickReason reason the server kicked the local player

### ServerCheat
```angelscript
void ServerCheat(FString Msg)
```
Run a cheat command on the server

### ServerDisconnectFromLobby
```angelscript
void ServerDisconnectFromLobby()
```
Make a graceful disconnect with the server

### ServerKickPlayer
```angelscript
void ServerKickPlayer(FUniqueNetIdRepl PlayerToKick, FText Reason)
```
Make a request to kick a given player

@param PlayerToKick player kick request
@param Reason reason for the kick to tell client if this succeeds

### ServerLoginPlayer
```angelscript
void ServerLoginPlayer(FString InSessionId, FUniqueNetIdRepl InUniqueId, FString UrlString)
```
Attempt to login a single local player with the lobby beacon

@param InSessionId session id that the client is expecting to connect with
@param InUniqueId unique id of the new player
@param UrlString URL containing player options (name, etc)

### ServerNotifyJoiningServer
```angelscript
void ServerNotifyJoiningServer()
```
Make a graceful request to actually join the server

### ServerSetPartyOwner
```angelscript
void ServerSetPartyOwner(FUniqueNetIdRepl InUniqueId, FUniqueNetIdRepl InPartyOwnerId)
```
Make a request to set the party owner for the given player

@param InUniqueId id of the requesting player
@param PartyOwnerUniqueId id the party owner


# UCommonSession_HostSessionRequest

**继承自**: `UObject`

A request object that stores the parameters used when hosting a gameplay session

## 属性

### OnlineMode
- **类型**: `ECommonSessionOnlineMode`
- **描述**: Indicates if the session is a full online session or a different type

### bUseLobbies
- **类型**: `bool`
- **描述**: True if this request should create a player-hosted lobbies if available

### ModeNameForAdvertisement
- **类型**: `FString`
- **描述**: String used during matchmaking to specify what type of game mode this is

### MapID
- **类型**: `FPrimaryAssetId`
- **描述**: The map that will be loaded at the start of gameplay, this needs to be a valid Primary Asset top-level map

### ExtraArgs
- **类型**: `TMap<FString,FString>`
- **描述**: Extra arguments passed as URL options to the game

### MaxPlayerCount
- **类型**: `int`
- **描述**: Maximum players allowed per gameplay session


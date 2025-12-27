# UCommonSession_SearchSessionRequest

**继承自**: `UObject`

Request object describing a session search, this object will be updated once the search has completed

## 属性

### OnlineMode
- **类型**: `ECommonSessionOnlineMode`
- **描述**: Indicates if the this is looking for full online games or a different type like LAN

### bUseLobbies
- **类型**: `bool`
- **描述**: True if this request should look for player-hosted lobbies if they are available, false will only search for registered server sessions

### Results
- **类型**: `TArray<TObjectPtr<UCommonSession_SearchResult>>`
- **描述**: List of all found sessions, will be valid when OnSearchFinished is called

### K2_OnSearchFinished
- **类型**: `FCommonSession_FindSessionsFinishedDynamic`


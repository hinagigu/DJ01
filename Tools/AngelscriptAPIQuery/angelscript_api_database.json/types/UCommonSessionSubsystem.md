# UCommonSessionSubsystem

**继承自**: `UGameInstanceSubsystem`

Game subsystem that handles requests for hosting and joining online games.
One subsystem is created for each game instance and can be accessed from blueprints or C++ code.
If a game-specific subclass exists, this base subsystem will not be created.

## 属性

### K2_OnUserRequestedSessionEvent
- **类型**: `FCommonSessionOnUserRequestedSession_Dynamic`

### K2_OnJoinSessionCompleteEvent
- **类型**: `FCommonSessionOnJoinSessionComplete_Dynamic`

### K2_OnCreateSessionCompleteEvent
- **类型**: `FCommonSessionOnCreateSessionComplete_Dynamic`

### K2_OnSessionInformationChangedEvent
- **类型**: `FCommonSessionOnSessionInformationChanged_Dynamic`

## 方法

### CleanUpSessions
```angelscript
void CleanUpSessions()
```
Clean up any active sessions, called from cases like returning to the main menu

### CreateOnlineHostSessionRequest
```angelscript
UCommonSession_HostSessionRequest CreateOnlineHostSessionRequest()
```
Creates a host session request with default options for online games, this can be modified after creation

### CreateOnlineSearchSessionRequest
```angelscript
UCommonSession_SearchSessionRequest CreateOnlineSearchSessionRequest()
```
Creates a session search object with default options to look for default online games, this can be modified after creation

### FindSessions
```angelscript
void FindSessions(APlayerController SearchingPlayer, UCommonSession_SearchSessionRequest Request)
```
Queries online system for the list of joinable sessions matching the search request

### HostSession
```angelscript
void HostSession(APlayerController HostingPlayer, UCommonSession_HostSessionRequest Request)
```
Creates a new online game using the session request information, if successful this will start a hard map transfer

### JoinSession
```angelscript
void JoinSession(APlayerController JoiningPlayer, UCommonSession_SearchResult Request)
```
Starts process to join an existing session, if successful this will connect to the specified server

### QuickPlaySession
```angelscript
void QuickPlaySession(APlayerController JoiningOrHostingPlayer, UCommonSession_HostSessionRequest Request)
```
Starts a process to look for existing sessions or create a new one if no viable sessions are found


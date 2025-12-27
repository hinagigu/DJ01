# ADJ01PlayerController

**继承自**: `ACommonPlayerController`

ADJ01PlayerController

     The base player controller class used by this project.

## 方法

### GetDJ01AbilitySystemComponent
```angelscript
UDJ01AbilitySystemComponent GetDJ01AbilitySystemComponent()
```
获取玩家的 AbilitySystemComponent (从 PlayerState 获取)

### GetDJ01HUD
```angelscript
ADJ01HUD GetDJ01HUD()
```

### GetDJ01PlayerState
```angelscript
ADJ01PlayerState GetDJ01PlayerState()
```

### GetIsAutoRunning
```angelscript
bool GetIsAutoRunning()
```

### OnEndAutoRun
```angelscript
void OnEndAutoRun()
```

### OnStartAutoRun
```angelscript
void OnStartAutoRun()
```

### ServerCheat
```angelscript
void ServerCheat(FString Msg)
```
Run a cheat command on the server.

### ServerCheatAll
```angelscript
void ServerCheatAll(FString Msg)
```
Run a cheat command on the server for all players.

### SetIsAutoRunning
```angelscript
void SetIsAutoRunning(bool bEnabled)
```

### TryToRecordClientReplay
```angelscript
bool TryToRecordClientReplay()
```
Call from game state logic to start recording an automatic client replay if ShouldRecordClientReplay returns true


# ADJ01GameMode

**继承自**: `AModularGameModeBase`

ADJ01GameMode

     The base game mode class used by this project.

## 方法

### GetPawnDataForController
```angelscript
const UDJ01PawnData GetPawnDataForController(const AController InController)
```

### RequestPlayerRestartNextFrame
```angelscript
void RequestPlayerRestartNextFrame(AController Controller, bool bForceReset)
```
Restart (respawn) the specified player or bot next frame
- If bForceReset is true, the controller will be reset this frame (abandoning the currently possessed pawn, if any)


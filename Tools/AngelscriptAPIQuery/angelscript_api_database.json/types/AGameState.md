# AGameState

**继承自**: `AGameStateBase`

GameState is a subclass of GameStateBase that behaves like a multiplayer match-based game.
It is tied to functionality in GameMode.

## 属性

### MatchState
- **类型**: `FName`
- **描述**: What match state we are currently in

### PreviousMatchState
- **类型**: `FName`
- **描述**: Previous map state, used to handle if multiple transitions happen per frame

### ElapsedTime
- **类型**: `int`
- **描述**: Elapsed game time since match has started.


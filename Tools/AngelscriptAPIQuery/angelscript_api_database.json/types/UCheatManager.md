# UCheatManager

**继承自**: `UObject`

Cheat Manager is a central blueprint to implement test and debug code and actions that are not to ship with the game.
As the Cheat Manager is not instanced in shipping builds, it is for debugging purposes only

## 属性

### DebugCameraControllerClass
- **类型**: `TSubclassOf<ADebugCameraController>`

## 方法

### ChangeSize
```angelscript
void ChangeSize(float32 F)
```
Scale the player's size to be F * default size.

### DamageTarget
```angelscript
void DamageTarget(float32 DamageAmount)
```
Damage the actor you're looking at (sourced from the player).

### DestroyTarget
```angelscript
void DestroyTarget()
```
Destroy the actor you're looking at.

### DisableDebugCamera
```angelscript
void DisableDebugCamera()
```
Switch controller from debug camera back to normal controller

### EnableDebugCamera
```angelscript
void EnableDebugCamera()
```
Switch controller to debug camera without locking gameplay and with locking local player controller input

### Fly
```angelscript
void Fly()
```
Pawn can fly.

### FreezeFrame
```angelscript
void FreezeFrame(float32 Delay)
```
Pause the game for Delay seconds.

### GetPlayerController
```angelscript
APlayerController GetPlayerController()
```

### Ghost
```angelscript
void Ghost()
```
Pawn no longer collides with the world, and can fly

### God
```angelscript
void God()
```
Invulnerability cheat.

### PlayersOnly
```angelscript
void PlayersOnly()
```
Freeze everything in the level except for players.

### EndPlay
```angelscript
void EndPlay()
```
This is the End Play event for the CheatManager

### InitCheatManager
```angelscript
void InitCheatManager()
```
BP implementable event for when CheatManager is created to allow any needed initialization.

### ServerToggleAILogging
```angelscript
void ServerToggleAILogging()
```

### Slomo
```angelscript
void Slomo(float32 NewTimeDilation)
```
Modify time dilation to change apparent speed of passage of time. e.g. "Slomo 0.1" makes everything move very slowly, while "Slomo 10" makes everything move very fast.

### Teleport
```angelscript
void Teleport()
```
Teleport to surface player is looking at.

### Walk
```angelscript
void Walk()
```
Return to walking movement mode from Fly or Ghost cheat.


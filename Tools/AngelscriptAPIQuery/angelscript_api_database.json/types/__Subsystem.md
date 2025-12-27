# __Subsystem

## 方法

### GetEngineSubsystem
```angelscript
UEngineSubsystem GetEngineSubsystem(TSubclassOf<UEngineSubsystem> Class)
```
Get a Game Instance Subsystem from the Game Instance associated with the provided context

### GetGameInstanceSubsystem
```angelscript
UGameInstanceSubsystem GetGameInstanceSubsystem(TSubclassOf<UGameInstanceSubsystem> Class)
```
Get a Game Instance Subsystem from the Game Instance associated with the provided context

### GetLocalPlayerSubsystem
```angelscript
ULocalPlayerSubsystem GetLocalPlayerSubsystem(TSubclassOf<ULocalPlayerSubsystem> Class)
```
Get a Local Player Subsystem from the Local Player associated with the provided context

### GetLocalPlayerSubsystemFromLocalPlayer
```angelscript
ULocalPlayerSubsystem GetLocalPlayerSubsystemFromLocalPlayer(ULocalPlayer LocalPlayer, TSubclassOf<ULocalPlayerSubsystem> Class)
```
Get a Local Player Subsystem from the Local Player associated with the provided context

### GetLocalPlayerSubsystemFromPlayerController
```angelscript
ULocalPlayerSubsystem GetLocalPlayerSubsystemFromPlayerController(APlayerController PlayerController, TSubclassOf<ULocalPlayerSubsystem> Class)
```
Get a Local Player Subsystem from the LocalPlayer associated with the provided context
If the player controller isn't associated to a LocalPlayer nullptr is returned

### GetWorldSubsystem
```angelscript
UWorldSubsystem GetWorldSubsystem(TSubclassOf<UWorldSubsystem> Class)
```
Get a World Subsystem from the World associated with the provided context


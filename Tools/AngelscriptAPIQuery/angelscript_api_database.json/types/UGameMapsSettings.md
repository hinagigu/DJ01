# UGameMapsSettings

**继承自**: `UObject`

## 属性

### EditorStartupMap
- **类型**: `FSoftObjectPath`
- **描述**: If set, this map will be loaded when the Editor starts up.

### EditorTemplateMapOverrides
- **类型**: `TArray<FTemplateMapInfoOverride>`
- **描述**: Map templates that should show up in the new level dialog. This will completely override the default maps chosen by the default editor

### LocalMapOptions
- **类型**: `FString`
- **描述**: The default options that will be appended to a map being loaded.

### TransitionMap
- **类型**: `FSoftObjectPath`
- **描述**: The map loaded when transition from one map to another.

### bUseSplitscreen
- **类型**: `bool`
- **描述**: Whether the screen should be split or not when multiple local players are present

### TwoPlayerSplitscreenLayout
- **类型**: `ETwoPlayerSplitScreenType`
- **描述**: The viewport layout to use if the screen should be split and there are two local players

### ThreePlayerSplitscreenLayout
- **类型**: `EThreePlayerSplitScreenType`
- **描述**: The viewport layout to use if the screen should be split and there are three local players

### FourPlayerSplitscreenLayout
- **类型**: `EFourPlayerSplitScreenType`
- **描述**: The viewport layout to use if the screen should be split and there are three local players

### bOffsetPlayerGamepadIds
- **类型**: `bool`
- **描述**: If enabled, this will make so that gamepads start being assigned to the second controller ID in local multiplayer games.
In PIE sessions with multiple windows, this has the same effect as enabling "Route 1st Gamepad to 2nd Client"

### GameInstanceClass
- **类型**: `FSoftClassPath`
- **描述**: The class to use when instantiating the transient GameInstance class

### GameDefaultMap
- **类型**: `FSoftObjectPath`
- **描述**: The map that will be loaded by default when no other map is loaded.

### ServerDefaultMap
- **类型**: `FSoftObjectPath`
- **描述**: The map that will be loaded by default when no other map is loaded (DEDICATED SERVER).

### GlobalDefaultGameMode
- **类型**: `FSoftClassPath`
- **描述**: GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL).

### GlobalDefaultServerGameMode
- **类型**: `FSoftClassPath`
- **描述**: GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL) (DEDICATED SERVERS)
If not set, the GlobalDefaultGameMode value will be used.

### GameModeMapPrefixes
- **类型**: `TArray<FGameModeName>`
- **描述**: Overrides the GameMode to use when loading a map that starts with a specific prefix

### GameModeClassAliases
- **类型**: `TArray<FGameModeName>`
- **描述**: List of GameModes to load when game= is specified in the URL (e.g. "DM" could be an alias for "MyProject.MyGameModeMP_DM")

## 方法

### GetSkipAssigningGamepadToPlayer1
```angelscript
bool GetSkipAssigningGamepadToPlayer1()
```

### SetSkipAssigningGamepadToPlayer1
```angelscript
void SetSkipAssigningGamepadToPlayer1(bool bSkipFirstPlayer)
```
Modify "Skip Assigning Gamepad to Player 1" GameMapsSettings option
@param bSkipFirstPlayer              If set connected game pads will only be assigned to the second and subsequent players
@note This value is saved to local config when changed.


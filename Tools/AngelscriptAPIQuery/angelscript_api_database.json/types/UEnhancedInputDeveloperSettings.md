# UEnhancedInputDeveloperSettings

**继承自**: `UDeveloperSettingsBackedByCVars`

Developer settings for Enhanced Input

## 属性

### DefaultMappingContexts
- **类型**: `TArray<FDefaultContextSetting>`
- **描述**: Array of any input mapping contexts that you want to be applied by default to the Enhanced Input local player subsystem.
NOTE: These mapping context's can only be from your game's root content directory, not plugins.

### DefaultWorldSubsystemMappingContexts
- **类型**: `TArray<FDefaultContextSetting>`
- **描述**: Array of any input mapping contexts that you want to be applied by default to the Enhanced Input world subsystem.
NOTE: These mapping context's can only be from your game's root content directory, not plugins.

### PlatformSettings
- **类型**: `FPerPlatformSettings`
- **描述**: Platform specific settings for Enhanced Input.
@see UEnhancedInputPlatformSettings

### UserSettingsClass
- **类型**: `TSoftClassPtr<UEnhancedInputUserSettings>`
- **描述**: The class that should be used for the User Settings by each Enhanced Input subsystem.
An instance of this class will be spawned by each Enhanced Input subsytem as a place to store
user settings such as keymappings, accessibility settings, etc. Subclass this to add more custom
options to your game.

Note: This is a new experimental feature!

### DefaultPlayerMappableKeyProfileClass
- **类型**: `TSoftClassPtr<UEnhancedPlayerMappableKeyProfile>`
- **描述**: The default class for the player mappable key profile, used to store the key mappings set by the player in the user settings.

Note: This is a new experimental feature!

### DefaultWorldInputClass
- **类型**: `TSoftClassPtr<UEnhancedPlayerInput>`
- **描述**: The default player input class that the Enhanced Input world subsystem will use.

### bSendTriggeredEventsWhenInputIsFlushed
- **类型**: `bool`

### bEnableUserSettings
- **类型**: `bool`

### bEnableDefaultMappingContexts
- **类型**: `bool`

### bShouldOnlyTriggerLastActionInChord
- **类型**: `bool`

### bLogOnDeprecatedConfigUsed
- **类型**: `bool`

### bEnableWorldSubsystem
- **类型**: `bool`

### bShouldLogAllWorldSubsystemInputs
- **类型**: `bool`


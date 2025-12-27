# UInputSettings

**继承自**: `UObject`

Project wide settings for input handling

@see https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

## 属性

### AxisConfig
- **类型**: `TArray<FInputAxisConfigEntry>`
- **描述**: List of Axis Properties

### PlatformSettings
- **类型**: `FPerPlatformSettings`
- **描述**: Platform specific settings for Input.
@see UInputPlatformSettings

### ExcludedAutocorrectOS
- **类型**: `TArray<FString>`
- **描述**: Disables autocorrect for these operating systems, even if autocorrect is enabled. Use the format "[platform] [osversion]"
(e.g., "iOS 11.2" or "Android 6"). More specific versions will disable autocorrect for fewer devices ("iOS 11" will disable
autocorrect for all devices running iOS 11, but "iOS 11.2.2" will not disable autocorrect for devices running 11.2.1).

### ExcludedAutocorrectCultures
- **类型**: `TArray<FString>`
- **描述**: Disables autocorrect for these cultures, even if autocorrect is turned on. These should be ISO-compliant language and country codes, such as "en" or "en-US".

### ExcludedAutocorrectDeviceModels
- **类型**: `TArray<FString>`
- **描述**: Disables autocorrect for these device models, even if autocorrect is turned in. Model IDs listed here will match against the start of the device's
model (e.g., "SM-" will match all device model IDs that start with "SM-"). This is currently only supported on Android devices.

### DefaultViewportMouseCaptureMode
- **类型**: `EMouseCaptureMode`
- **描述**: The default mouse capture mode for the game viewport

### DefaultViewportMouseLockMode
- **类型**: `EMouseLockMode`
- **描述**: The default mouse lock state behavior when the viewport acquires capture

### FOVScale
- **类型**: `float32`
- **描述**: The scaling value to multiply the field of view by

### DoubleClickTime
- **类型**: `float32`
- **描述**: If a key is pressed twice in this amount of time it is considered a "double click"

### DefaultPlayerInputClass
- **类型**: `TSoftClassPtr<UPlayerInput>`
- **描述**: Default class type for player input object. May be overridden by player controller.

### DefaultInputComponentClass
- **类型**: `TSoftClassPtr<UInputComponent>`
- **描述**: Default class type for pawn input components.

### DefaultTouchInterface
- **类型**: `FSoftObjectPath`
- **描述**: The default on-screen touch input interface for the game (can be null to disable the onscreen interface)

### ConsoleKeys
- **类型**: `TArray<FKey>`
- **描述**: The keys which open the console.

### bAltEnterTogglesFullscreen
- **类型**: `bool`

### bF11TogglesFullscreen
- **类型**: `bool`

### bUseMouseForTouch
- **类型**: `bool`

### bEnableMouseSmoothing
- **类型**: `bool`

### bEnableFOVScaling
- **类型**: `bool`

### bCaptureMouseOnLaunch
- **类型**: `bool`

### bEnableLegacyInputScales
- **类型**: `bool`

### bEnableMotionControls
- **类型**: `bool`

### bFilterInputByPlatformUser
- **类型**: `bool`

### bEnableInputDeviceSubsystem
- **类型**: `bool`

### bShouldFlushPressedKeysOnViewportFocusLost
- **类型**: `bool`

### bEnableDynamicComponentInputBinding
- **类型**: `bool`

### bAlwaysShowTouchInterface
- **类型**: `bool`

### bShowConsoleOnFourFingerTap
- **类型**: `bool`

### bEnableGestureRecognizer
- **类型**: `bool`

### bUseAutocorrect
- **类型**: `bool`

### ActionMappings
- **类型**: `TArray<FInputActionKeyMapping>`

### AxisMappings
- **类型**: `TArray<FInputAxisKeyMapping>`

### SpeechMappings
- **类型**: `TArray<FInputActionSpeechMapping>`

## 方法

### GetUniqueActionName
```angelscript
FName GetUniqueActionName(FName BaseActionMappingName)
```

### GetUniqueAxisName
```angelscript
FName GetUniqueAxisName(FName BaseAxisMappingName)
```

### GetActionMappings
```angelscript
TArray<FInputActionKeyMapping> GetActionMappings()
```

### GetAxisMappings
```angelscript
TArray<FInputAxisKeyMapping> GetAxisMappings()
```

### GetSpeechMappings
```angelscript
TArray<FInputActionSpeechMapping> GetSpeechMappings()
```

### DoesActionExist
```angelscript
bool DoesActionExist(FName InActionName)
```

### DoesAxisExist
```angelscript
bool DoesAxisExist(FName InAxisName)
```

### DoesSpeechExist
```angelscript
bool DoesSpeechExist(FName InSpeechName)
```

### AddActionMapping
```angelscript
void AddActionMapping(FInputActionKeyMapping KeyMapping, bool bForceRebuildKeymaps)
```
Programmatically add an action mapping to the project defaults

### AddAxisMapping
```angelscript
void AddAxisMapping(FInputAxisKeyMapping KeyMapping, bool bForceRebuildKeymaps)
```
Programmatically add an axis mapping to the project defaults

### ForceRebuildKeymaps
```angelscript
void ForceRebuildKeymaps()
```
When changes are made to the default mappings, push those changes out to PlayerInput key maps

### GetActionMappingByName
```angelscript
void GetActionMappingByName(FName InActionName, TArray<FInputActionKeyMapping>& OutMappings)
```

### GetActionNames
```angelscript
void GetActionNames(TArray<FName>& ActionNames)
```
Populate a list of all defined action names

### GetAxisMappingByName
```angelscript
void GetAxisMappingByName(FName InAxisName, TArray<FInputAxisKeyMapping>& OutMappings)
```
Retrieve all axis mappings by a certain name.

### GetAxisNames
```angelscript
void GetAxisNames(TArray<FName>& AxisNames)
```
Populate a list of all defined axis names

### RemoveActionMapping
```angelscript
void RemoveActionMapping(FInputActionKeyMapping KeyMapping, bool bForceRebuildKeymaps)
```
Programmatically remove an action mapping to the project defaults

### RemoveAxisMapping
```angelscript
void RemoveAxisMapping(FInputAxisKeyMapping KeyMapping, bool bForceRebuildKeymaps)
```
Programmatically remove an axis mapping to the project defaults

### SaveKeyMappings
```angelscript
void SaveKeyMappings()
```
Flush the current mapping values to the config file


# UCommonInputSettings

**继承自**: `UDeveloperSettings`

## 属性

### InputData
- **类型**: `TSoftClassPtr<UCommonUIInputData>`
- **描述**: Create a derived asset from UCommonUIInputData to store Input data for your game.

### PlatformInput
- **类型**: `FPerPlatformSettings`

### bEnableInputMethodThrashingProtection
- **类型**: `bool`

### InputMethodThrashingLimit
- **类型**: `int`

### InputMethodThrashingWindowInSeconds
- **类型**: `float`

### InputMethodThrashingCooldownInSeconds
- **类型**: `float`

### bAllowOutOfFocusDeviceInput
- **类型**: `bool`

### bEnableDefaultInputConfig
- **类型**: `bool`
- **描述**: Controls whether a default Input Config will be set when the active CommonActivatableWidgets do not specify a desired one.
Disable this if you want to control the Input Mode via alternative means.

### bEnableEnhancedInputSupport
- **类型**: `bool`
- **描述**: Controls if Enhanced Input Support plugin-wide. Requires restart due to caching.

### bEnableAutomaticGamepadTypeDetection
- **类型**: `bool`
- **描述**: Controls automatic detection of the gamepad type.
Disable this if you want to manually control the gamepad type using the UCommonInputSubsystem::SetGamepadInputType() function.

### ActionDomainTable
- **类型**: `TSoftObjectPtr<UCommonInputActionDomainTable>`
- **描述**: Create a derived asset from UCommonInputActionDomainTable to store ordered ActionDomain data for your game


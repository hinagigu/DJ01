# UCommonUIInputSettings

**继承自**: `UObject`

Project-wide input settings for UI input actions

## 属性

### bLinkCursorToGamepadFocus
- **类型**: `bool`
- **描述**: True to have the mouse pointer automatically moved to the center of whatever widget is currently focused while using a gamepad.

### UIActionProcessingPriority
- **类型**: `int`
- **描述**: The input priority of the input components that process UI input actions.
The lower the value, the higher the priority of the component.

By default, this value is incredibly high to ensure UI action processing priority over game elements.
Adjust as needed for the UI input components to be processed at the appropriate point in the input stack in your project.

NOTE: When the active input mode is ECommonInputMode::Menu, ALL input components with lower priority than this will be fully blocked.
              Thus, if any game agent input components are registered with higher priority than this, behavior will not match expectation.

### InputActions
- **类型**: `TArray<FUIInputAction>`
- **描述**: All UI input action mappings for the project

### AnalogCursorSettings
- **类型**: `FCommonAnalogCursorSettings`


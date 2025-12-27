# UCommonInputBaseControllerData

**继承自**: `UObject`

Derive from this class to store the Input data. It is referenced in the Common Input Settings, found in the project settings UI.

## 属性

### SetButtonImageHeightTo
- **类型**: `int`

### InputType
- **类型**: `ECommonInputType`

### GamepadName
- **类型**: `FName`

### GamepadDisplayName
- **类型**: `FText`

### GamepadCategory
- **类型**: `FText`

### GamepadPlatformName
- **类型**: `FText`

### GamepadHardwareIdMapping
- **类型**: `TArray<FInputDeviceIdentifierPair>`

### ControllerTexture
- **类型**: `TSoftObjectPtr<UTexture2D>`

### ControllerButtonMaskTexture
- **类型**: `TSoftObjectPtr<UTexture2D>`

### InputBrushDataMap
- **类型**: `TArray<FCommonInputKeyBrushConfiguration>`

### InputBrushKeySets
- **类型**: `TArray<FCommonInputKeySetBrushConfiguration>`


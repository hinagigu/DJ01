# UCommonUIInputData

**继承自**: `UObject`

Derive from this class to store the Input data. It is referenced in the Common Input Settings, found in the project settings UI.

## 属性

### DefaultClickAction
- **类型**: `FDataTableRowHandle`

### DefaultBackAction
- **类型**: `FDataTableRowHandle`

### DefaultHoldData
- **类型**: `TSoftClassPtr<UCommonUIHoldData>`
- **描述**: Newly created CommonButton widgets will use these hold values by default if bRequiresHold is true.
Inherits from UCommonUIHoldData.

### EnhancedInputClickAction
- **类型**: `UInputAction`

### EnhancedInputBackAction
- **类型**: `UInputAction`


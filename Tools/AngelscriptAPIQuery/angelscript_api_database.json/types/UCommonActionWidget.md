# UCommonActionWidget

**继承自**: `UWidget`

A widget that shows a platform-specific icon for the given input action.

## 属性

### OnInputMethodChanged
- **类型**: `FOnInputMethodChanged__CommonActionWidget`

### ProgressMaterialBrush
- **类型**: `FSlateBrush`

### ProgressMaterialParam
- **类型**: `FName`

### DesignTimeKey
- **类型**: `FKey`

### IconRimBrush
- **类型**: `FSlateBrush`

### InputActions
- **类型**: `TArray<FDataTableRowHandle>`

### EnhancedInputAction
- **类型**: `UInputAction`

## 方法

### GetDisplayText
```angelscript
FText GetDisplayText()
```

### GetIcon
```angelscript
FSlateBrush GetIcon()
```
End UWidet

### IsHeldAction
```angelscript
bool IsHeldAction()
```

### SetEnhancedInputAction
```angelscript
void SetEnhancedInputAction(UInputAction InInputAction)
```

### SetIconRimBrush
```angelscript
void SetIconRimBrush(FSlateBrush InIconRimBrush)
```

### SetInputAction
```angelscript
void SetInputAction(FDataTableRowHandle InputActionRow)
```

### SetInputActions
```angelscript
void SetInputActions(TArray<FDataTableRowHandle> NewInputActions)
```


# UCommonUISubsystemBase

**继承自**: `UGameInstanceSubsystem`

## 方法

### GetEnhancedInputActionButtonIcon
```angelscript
FSlateBrush GetEnhancedInputActionButtonIcon(const UInputAction InputAction, const ULocalPlayer LocalPlayer)
```
Gets Action Button Icon for given action and player, enhanced input API currently does not allow input type specification

### GetInputActionButtonIcon
```angelscript
FSlateBrush GetInputActionButtonIcon(FDataTableRowHandle InputActionRowHandle, ECommonInputType InputType, FName GamepadName)
```
Gets Action Button Icon for current gamepad


# UCommonPlayerInputKey

**继承自**: `UCommonUserWidget`

## 属性

### BoundKeyFallback
- **类型**: `FKey`

### InputTypeOverride
- **类型**: `ECommonInputType`

### IsHoldKeybindValue
- **类型**: `bool`

### bShowTimeCountDown
- **类型**: `bool`

### HoldProgressBrush
- **类型**: `FSlateBrush`
- **描述**: Material for showing Progress

### KeyBindTextBorder
- **类型**: `FSlateBrush`
- **描述**: The key bind text border.

### bShowUnboundStatus
- **类型**: `bool`
- **描述**: Should this keybinding widget display information that it is currently unbound?

### KeyBindTextFont
- **类型**: `FSlateFontInfo`
- **描述**: The font to apply at each size

### CountdownTextFont
- **类型**: `FSlateFontInfo`
- **描述**: The font to apply at each size

### PercentageMaterialParameterName
- **类型**: `FName`
- **描述**: The material parameter name for hold percentage in the HoldKeybindImage

### BoundAction
- **类型**: `FName`

### AxisScale
- **类型**: `float32`

### PresetNameOverride
- **类型**: `FName`

### ForcedHoldKeybindStatus
- **类型**: `ECommonKeybindForcedHoldStatus`

### BoundKey
- **类型**: `FKey`

## 方法

### IsHoldKeybind
```angelscript
bool IsHoldKeybind()
```
Get whether this keybind is a hold action.

### SetAxisScale
```angelscript
void SetAxisScale(float32 NewValue)
```
Set the axis scale value for this keybind

### SetBoundAction
```angelscript
void SetBoundAction(FName NewBoundAction)
```
Set the bound action for our keybind

### SetBoundKey
```angelscript
void SetBoundKey(FKey NewBoundAction)
```
Set the bound key for our keybind

### SetForcedHoldKeybindStatus
```angelscript
void SetForcedHoldKeybindStatus(ECommonKeybindForcedHoldStatus InForcedHoldKeybindStatus)
```
Force this keybind to be a hold keybind

### SetPresetNameOverride
```angelscript
void SetPresetNameOverride(FName NewValue)
```
Set the preset name override value for this keybind.

### SetShowProgressCountDown
```angelscript
void SetShowProgressCountDown(bool bShow)
```
Force this keybind to be a hold keybind

### UpdateKeybindWidget
```angelscript
void UpdateKeybindWidget()
```
Update the key and associated display based on our current Boundaction


# UCommonButtonBase

**继承自**: `UCommonUserWidget`

Button that disables itself when not active. Also updates actions for CommonActionWidget if bound to display platform-specific icons.

## 属性

### ClickEvent
- **类型**: `FWidgetEventField`

### MinWidth
- **类型**: `int`

### MinHeight
- **类型**: `int`

### bHideInputAction
- **类型**: `bool`

### PressedSlateSoundOverride
- **类型**: `FSlateSound`

### HoveredSlateSoundOverride
- **类型**: `FSlateSound`

### SelectedPressedSlateSoundOverride
- **类型**: `FSlateSound`

### SelectedHoveredSlateSoundOverride
- **类型**: `FSlateSound`

### LockedPressedSlateSoundOverride
- **类型**: `FSlateSound`

### LockedHoveredSlateSoundOverride
- **类型**: `FSlateSound`

### HoldData
- **类型**: `TSubclassOf<UCommonUIHoldData>`

### bSimulateHoverOnTouchInput
- **类型**: `bool`

### InputPriority
- **类型**: `int`

### OnSelectedChangedBase
- **类型**: `FCommonSelectedStateChangedBase`

### OnButtonBaseClicked
- **类型**: `FCommonButtonBaseClicked`

### OnButtonBaseDoubleClicked
- **类型**: `FCommonButtonBaseClicked`

### OnButtonBaseHovered
- **类型**: `FCommonButtonBaseClicked`

### OnButtonBaseUnhovered
- **类型**: `FCommonButtonBaseClicked`

### bIsPersistentBinding
- **类型**: `bool`
- **描述**: DANGER! Be very, very careful with this. Unless you absolutely know what you're doing, this is not the property you're looking for.

True to register the action bound to this button as a "persistent" binding. False (default) will register a standard activation-based binding.
A persistent binding ignores the standard ruleset for UI input routing - the binding will be live immediately upon construction of the button.

### InputModeOverride
- **类型**: `ECommonInputMode`
- **描述**: Set this to Game for special cases where an input action needs to be set for an in-game button.

### InputActionWidget
- **类型**: `UCommonActionWidget`
- **描述**: Optionally bound widget for visualization behavior of an input action;
NOTE: If specified, will visualize according to the following algorithm:
If TriggeringEnhancedInputAction is specified, visualize it else:
If TriggeringInputAction is specified, visualize it else:
If TriggeredInputAction is specified, visualize it else:
Visualize the default click action while hovered

### bApplyAlphaOnDisable
- **类型**: `bool`

### bLocked
- **类型**: `bool`

### bSelectable
- **类型**: `bool`

### bShouldSelectUponReceivingFocus
- **类型**: `bool`

### bInteractableWhenSelected
- **类型**: `bool`

### bToggleable
- **类型**: `bool`

### bTriggerClickedAfterSelection
- **类型**: `bool`

### bDisplayInputActionWhenNotInteractable
- **类型**: `bool`

### bHideInputActionWithKeyboard
- **类型**: `bool`

### bShouldUseFallbackDefaultInputAction
- **类型**: `bool`

### bRequiresHold
- **类型**: `bool`

### ClickMethod
- **类型**: `EButtonClickMethod`

### TouchMethod
- **类型**: `EButtonTouchMethod`

### PressMethod
- **类型**: `EButtonPressMethod`

### TriggeringInputAction
- **类型**: `FDataTableRowHandle`

### TriggeringEnhancedInputAction
- **类型**: `UInputAction`

## 方法

### OnClicked
```angelscript
void OnClicked()
```

### OnDeselected
```angelscript
void OnDeselected()
```

### OnDisabled
```angelscript
void OnDisabled()
```

### OnDoubleClicked
```angelscript
void OnDoubleClicked()
```

### OnEnabled
```angelscript
void OnEnabled()
```

### BP_OnFocusLost
```angelscript
void BP_OnFocusLost()
```

### BP_OnFocusReceived
```angelscript
void BP_OnFocusReceived()
```

### OnHovered
```angelscript
void OnHovered()
```

### OnInputActionTriggered
```angelscript
void OnInputActionTriggered()
```

### OnInputMethodChanged
```angelscript
void OnInputMethodChanged(ECommonInputType CurrentInputType)
```

### OnLockClicked
```angelscript
void OnLockClicked()
```

### OnLockDoubleClicked
```angelscript
void OnLockDoubleClicked()
```

### OnLockedChanged
```angelscript
void OnLockedChanged(bool bIsLocked)
```

### OnPressed
```angelscript
void OnPressed()
```

### OnReleased
```angelscript
void OnReleased()
```

### OnSelected
```angelscript
void OnSelected()
```

### OnUnhovered
```angelscript
void OnUnhovered()
```

### ClearSelection
```angelscript
void ClearSelection()
```

### DisableButtonWithReason
```angelscript
void DisableButtonWithReason(FText DisabledReason)
```
Disables this button with a reason (use instead of SetIsEnabled)

### GetCurrentButtonPadding
```angelscript
void GetCurrentButtonPadding(FMargin& OutButtonPadding)
```
@return The current button padding that corresponds to the current size and selection state

### GetCurrentCustomPadding
```angelscript
void GetCurrentCustomPadding(FMargin& OutCustomPadding)
```
@return The custom padding that corresponds to the current size and selection state

### GetCurrentTextStyle
```angelscript
UCommonTextStyle GetCurrentTextStyle()
```
@return The text style that corresponds to the current size and selection state

### GetCurrentTextStyleClass
```angelscript
TSubclassOf<UCommonTextStyle> GetCurrentTextStyleClass()
```
@return The class of the text style that corresponds to the current size and selection state

### GetEnhancedInputAction
```angelscript
UInputAction GetEnhancedInputAction()
```
Gets the appropriate enhanced input action that is set

### GetInputAction
```angelscript
bool GetInputAction(FDataTableRowHandle& InputActionRow)
```
Gets the appropriate input action that is set

### GetIsFocusable
```angelscript
bool GetIsFocusable()
```
Gets the bIsFocusable flag

### GetLocked
```angelscript
bool GetLocked()
```
@returns True if the button is currently locked, False otherwise

### GetSelected
```angelscript
bool GetSelected()
```
@returns True if the button is currently in a selected state, False otherwise

### GetShouldSelectUponReceivingFocus
```angelscript
bool GetShouldSelectUponReceivingFocus()
```
Get whether the button should become selected upon receiving focus or not

### GetSingleMaterialStyleMID
```angelscript
UMaterialInstanceDynamic GetSingleMaterialStyleMID()
```
Returns the dynamic instance of the material being used for this button, if it is using a single material style.

### GetStyle
```angelscript
UCommonButtonStyle GetStyle()
```
@Returns Current button style

### IsInteractionEnabled
```angelscript
bool IsInteractionEnabled()
```
Is this button currently interactable? (use instead of GetIsEnabled)

### IsPressed
```angelscript
bool IsPressed()
```
Is this button currently pressed?

### OnActionComplete
```angelscript
void OnActionComplete()
```
Callback fired when hold events complete

### OnActionProgress
```angelscript
void OnActionProgress(float HeldPercent)
```
Callback fired continously during hold interactions

### OnCurrentTextStyleChanged
```angelscript
void OnCurrentTextStyleChanged()
```
Allows derived classes to take action when the current text style has changed

### OnTriggeredInputActionChanged
```angelscript
void OnTriggeredInputActionChanged(FDataTableRowHandle NewTriggeredAction)
```
Callback fired when input action datatable row changes

### OnTriggeringEnhancedInputActionChanged
```angelscript
void OnTriggeringEnhancedInputActionChanged(const UInputAction InInputAction)
```
Callback fired when enhanced input action changes

### OnTriggeringInputActionChanged
```angelscript
void OnTriggeringInputActionChanged(FDataTableRowHandle NewTriggeredAction)
```
Callback fired when triggered input action datatable row changes

### SetClickMethod
```angelscript
void SetClickMethod(EButtonClickMethod InClickMethod)
```
Set the click method for mouse interaction

### SetHideInputAction
```angelscript
void SetHideInputAction(bool bInHideInputAction)
```

### SetHoveredSoundOverride
```angelscript
void SetHoveredSoundOverride(USoundBase Sound)
```

### SetInputActionProgressMaterial
```angelscript
void SetInputActionProgressMaterial(FSlateBrush InProgressMaterialBrush, FName InProgressMaterialParam)
```

### SetIsFocusable
```angelscript
void SetIsFocusable(bool bInIsFocusable)
```
Updates the bIsFocusable flag

### SetIsInteractableWhenSelected
```angelscript
void SetIsInteractableWhenSelected(bool bInInteractableWhenSelected)
```
Change whether this widget is selectable at all. If false and currently selected, will deselect.

### SetIsInteractionEnabled
```angelscript
void SetIsInteractionEnabled(bool bInIsInteractionEnabled)
```
Change whether this widget is selectable at all. If false and currently selected, will deselect.

### SetIsLocked
```angelscript
void SetIsLocked(bool bInIsLocked)
```
Change whether this widget is locked. If locked, the button can be focusable and responsive to mouse input but will not broadcast OnClicked events.

### SetIsSelectable
```angelscript
void SetIsSelectable(bool bInIsSelectable)
```
Change whether this widget is selectable at all. If false and currently selected, will deselect.

### SetIsSelected
```angelscript
void SetIsSelected(bool InSelected, bool bGiveClickFeedback)
```
Change the selected state manually.
@param bGiveClickFeedback    If true, the button may give user feedback as if it were clicked. IE: Play a click sound, trigger animations as if it were clicked.

### SetIsToggleable
```angelscript
void SetIsToggleable(bool bInIsToggleable)
```
Change whether this widget is toggleable. If toggleable, clicking when selected will deselect.

### SetLockedHoveredSoundOverride
```angelscript
void SetLockedHoveredSoundOverride(USoundBase Sound)
```

### SetLockedPressedSoundOverride
```angelscript
void SetLockedPressedSoundOverride(USoundBase Sound)
```

### SetMinDimensions
```angelscript
void SetMinDimensions(int InMinWidth, int InMinHeight)
```
Sets the minimum dimensions of this button

### SetPressedSoundOverride
```angelscript
void SetPressedSoundOverride(USoundBase Sound)
```

### SetPressMethod
```angelscript
void SetPressMethod(EButtonPressMethod InPressMethod)
```
Set the click method for keyboard/gamepad button press interaction

### SetSelectedHoveredSoundOverride
```angelscript
void SetSelectedHoveredSoundOverride(USoundBase Sound)
```

### SetSelectedInternal
```angelscript
void SetSelectedInternal(bool bInSelected, bool bAllowSound, bool bBroadcast)
```
Internal method to allow the selected state to be set regardless of selectability or toggleability

### SetSelectedPressedSoundOverride
```angelscript
void SetSelectedPressedSoundOverride(USoundBase Sound)
```

### SetShouldSelectUponReceivingFocus
```angelscript
void SetShouldSelectUponReceivingFocus(bool bInShouldSelectUponReceivingFocus)
```
Set whether the button should become selected upon receiving focus or not; Only settable for buttons that are selectable

### SetShouldUseFallbackDefaultInputAction
```angelscript
void SetShouldUseFallbackDefaultInputAction(bool bInShouldUseFallbackDefaultInputAction)
```
Change whether this widget should use the fallback default input action.

### SetStyle
```angelscript
void SetStyle(TSubclassOf<UCommonButtonStyle> InStyle)
```
Sets the style of this button, rebuilds the internal styling

### SetTouchMethod
```angelscript
void SetTouchMethod(EButtonTouchMethod InTouchMethod)
```
Set the click method for touch interaction

### SetTriggeredInputAction
```angelscript
void SetTriggeredInputAction(FDataTableRowHandle InputActionRow)
```
Updates the current triggered action

### SetTriggeringEnhancedInputAction
```angelscript
void SetTriggeringEnhancedInputAction(UInputAction InInputAction)
```
Updates the current triggering enhanced input action, requires enhanced input enabled in CommonUI settings

### SetTriggeringInputAction
```angelscript
void SetTriggeringInputAction(FDataTableRowHandle InputActionRow)
```
Updates the current triggering action

### StopDoubleClickPropagation
```angelscript
void StopDoubleClickPropagation()
```
Unless this is called, we will assume the double click should be converted into a normal click.


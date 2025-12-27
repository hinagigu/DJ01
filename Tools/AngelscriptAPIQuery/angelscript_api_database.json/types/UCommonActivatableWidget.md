# UCommonActivatableWidget

**继承自**: `UCommonUserWidget`

The base for widgets that are capable of being "activated" and "deactivated" during their lifetime without being otherwise modified or destroyed.

This is generally desired for one or more of the following purposes:
    - This widget can turn on/off without being removed from the hierarchy (or otherwise reconstructing the underlying SWidgets), so Construct/Destruct are insufficient
    - You'd like to be able to "go back" from this widget, whether that means back a breadcrumb, closing a modal, or something else. This is built-in here.
    - This widget's place in the hierarchy is such that it defines a meaningful node-point in the tree of activatable widgets through which input is routed to all widgets.

By default, an activatable widget:
    - Is not automatically activated upon construction
    - Does not register to receive back actions (or any other actions, for that matter)
    - If classified as a back handler, is automatically deactivated (but not destroyed) when it receives a back action

Note that removing an activatable widget from the UI (i.e. triggering Destruct()) will always deactivate it, even if the UWidget is not destroyed.
Re-constructing the underlying SWidget will only result in re-activation if auto-activate is enabled.

## 属性

### bIsBackHandler
- **类型**: `bool`
- **描述**: True to receive "Back" actions automatically. Custom back handler behavior can be provided, default is to deactivate.

### bIsBackActionDisplayedInActionBar
- **类型**: `bool`
- **描述**: True to receive "Back" actions automatically. Custom back handler behavior can be provided, default is to deactivate.

### bAutoActivate
- **类型**: `bool`
- **描述**: True to automatically activate upon construction

### bSupportsActivationFocus
- **类型**: `bool`
- **描述**: True if this widget is a candidate to receive/route focus or specify a desired UIInputConfig when active.
Primary reason for disabling is for utility sub-widgets within a larger screen that possess actions, but are never
intended to be involved in navigation or dictate changes to the active UI input config.

### bIsModal
- **类型**: `bool`
- **描述**: True to have this widget be treated as a root node for input routing, regardless of its actual parentage.
Should seldom be needed, but useful in cases where a child widget should prevent all action processing by parents, even though they remain active (ex: modal popup menu).

### bAutoRestoreFocus
- **类型**: `bool`
- **描述**: True to prefer automatically restoring focus to the widget that was focused when this widget last became the non-leafmost-active-widget.
If true and a valid restoration candidate exists, we'll use that. If it doesn't, we rely on GetDesiredFocusTarget()
If false, we simply always rely on GetDesiredFocusTarget()

### bOverrideActionDomain
- **类型**: `bool`

### InputMapping
- **类型**: `UInputMappingContext`
- **描述**: Optional mapping context to be applied & removed on activation & deactivation respectfully.

### InputMappingPriority
- **类型**: `int`
- **描述**: Enhanced Input priority. Higher priority input mappings will be prioritized over mappings with a lower priority.

### ActionDomainOverride
- **类型**: `TSoftObjectPtr<UCommonInputActionDomain>`

### BP_OnWidgetActivated
- **类型**: `FOnWidgetActivationChanged`

### BP_OnWidgetDeactivated
- **类型**: `FOnWidgetActivationChanged`

### bIsActive
- **类型**: `bool`

### bSetVisibilityOnActivated
- **类型**: `bool`

### ActivatedVisibility
- **类型**: `ESlateVisibility`

### bSetVisibilityOnDeactivated
- **类型**: `bool`

### DeactivatedVisibility
- **类型**: `ESlateVisibility`

## 方法

### ActivateWidget
```angelscript
void ActivateWidget()
```

### BindVisibilityToActivation
```angelscript
void BindVisibilityToActivation(UCommonActivatableWidget ActivatableWidget)
```
Bind our visibility to the activation of another widget, useful for making mouse collisions behave similiar to console navigation w.r.t activation
Will immediately update visibility based on the bound widget activation & visibilites set by SetBindVisibilities.

@param       ActivatableWidget               - The widget whose activation / deactivation will modify our visibility

### BP_GetDesiredFocusTarget
```angelscript
UWidget BP_GetDesiredFocusTarget()
```
Implement to provide the desired widget to focus if/when this activatable becomes the primary active widget.
Note: This is a fallback used only if the native class parentage does not provide a target.

### GetDesiredInputConfig
```angelscript
FUIInputConfig GetDesiredInputConfig()
```
Implement to provide the input config to use when this widget is activated. Keep in mind when all widgets
are deactivated, CommonUI will not attempt to automatically restore the input config to before any widget was active.
Note: This is a fallback used only if the native class parentage does not provide an input config.

### OnActivated
```angelscript
void OnActivated()
```

### OnDeactivated
```angelscript
void OnDeactivated()
```

### OnHandleBackAction
```angelscript
bool OnHandleBackAction()
```
Override in BP implementations to provide custom behavior when receiving a back action
Note: Only called if native code in the base class hasn't handled it in NativeOnHandleBackAction

### ClearFocusRestorationTarget
```angelscript
void ClearFocusRestorationTarget()
```
Clears the cached focus target that's set when bAutoRestoreFocus is true

### DeactivateWidget
```angelscript
void DeactivateWidget()
```

### GetDesiredFocusTarget
```angelscript
UWidget GetDesiredFocusTarget()
```
Returns the desired widget to focus when this Widget Activates.

### IsActivated
```angelscript
bool IsActivated()
```

### RequestRefreshFocus
```angelscript
void RequestRefreshFocus()
```
Ask for focus to be re-set to our current DesiredFocusTarget,
but only if our node is currently the leaf-most active node (no stealing!).
This is useful for complex cases like: the buttons animate in from off-screen,
or the buttons are deeply nested in a multi-switcher hierarchy and it would be burdensome
to wrap each element in a CommonActivatableWidget.

### SetBindVisibilities
```angelscript
void SetBindVisibilities(ESlateVisibility OnActivatedVisibility, ESlateVisibility OnDeactivatedVisibility, bool bInAllActive)
```
Visibilities to use for when bound widgets in BindVisibilityToActivation are activated.

@param       OnActivatedVisibility   - Visibility for when bound widgets are active
@param       OnDeactivatedVisibility - Visibility for when bound widgets are not active, not used if this widget has activation / deactivation visibilities
@param       bInAllActive                    - True if we should switch to activated visibility only when all bound widgets are active


# UWidget

**继承自**: `UVisual`

This is the base class for all wrapped Slate controls that are exposed to UObjects.

## 属性

### Slot
- **类型**: `UPanelSlot`

### FlowDirectionPreference
- **类型**: `EFlowDirectionPreference`

### AccessibleBehavior
- **类型**: `ESlateAccessibleBehavior`
- **描述**: Whether or not the widget is accessible, and how to describe it. If set to custom, additional customization options will appear.

### AccessibleSummaryBehavior
- **类型**: `ESlateAccessibleBehavior`
- **描述**: How to describe this widget when it's being presented through a summary of a parent widget. If set to custom, additional customization options will appear.

### PixelSnapping
- **类型**: `EWidgetPixelSnapping`

### Navigation
- **类型**: `UWidgetNavigation`

### ToolTipWidget
- **类型**: `UWidget`

### bIsEnabled
- **类型**: `bool`

### ToolTipText
- **类型**: `FText`

### RenderTransformPivot
- **类型**: `FVector2D`

### bOverride_Cursor
- **类型**: `bool`

### bOverrideAccessibleDefaults
- **类型**: `bool`

### bCanChildrenBeAccessible
- **类型**: `bool`

### AccessibleText
- **类型**: `FText`

### AccessibleSummaryText
- **类型**: `FText`

### bIsVolatile
- **类型**: `bool`

### Cursor
- **类型**: `EMouseCursor`

## 方法

### ForceLayoutPrepass
```angelscript
void ForceLayoutPrepass()
```
Forces a pre-pass.  A pre-pass caches the desired size of the widget hierarchy owned by this widget.
One pre-pass already happens for every widget before Tick occurs.  You only need to perform another
pre-pass if you are adding child widgets this frame and want them to immediately be visible this frame.

### ForceVolatile
```angelscript
void ForceVolatile(bool bForce)
```
Sets the forced volatility of the widget.

### GetAccessibleSummaryText
```angelscript
FText GetAccessibleSummaryText()
```
Gets the accessible summary text from the underlying Slate accessible widget.
@return The accessible summary text of the underlying Slate accessible widget. Returns an empty text if
accessibility is dsabled or the underlying accessible widget is invalid.

### GetAccessibleText
```angelscript
FText GetAccessibleText()
```
Gets the accessible text from the underlying Slate accessible widget
@return The accessible text of the underlying Slate accessible widget. Returns an empty text if
accessibility is dsabled or the underlying accessible widget is invalid.

### GetCachedGeometry
```angelscript
FGeometry GetCachedGeometry()
```
Gets the last geometry used to Tick the widget.  This data may not exist yet if this call happens prior to
the widget having been ticked/painted, or it may be out of date, or a frame behind.

We recommend not to use this data unless there's no other way to solve your problem.  Normally in Slate we
try and handle these issues by making a dependent widget part of the hierarchy, as to avoid frame behind
or what are referred to as hysteresis problems, both caused by depending on geometry from the previous frame
being used to advise how to layout a dependent object the current frame.

### GetClipping
```angelscript
EWidgetClipping GetClipping()
```
Gets the clipping state of this widget.

### GetDesiredSize
```angelscript
FVector2D GetDesiredSize()
```
Gets the widgets desired size.
NOTE: The underlying Slate widget must exist and be valid, also at least one pre-pass must
      have occurred before this value will be of any use.

@return The widget's desired size

### GetGameInstance
```angelscript
UGameInstance GetGameInstance()
```
Gets the game instance associated with this UI.
@return a pointer to the owning game instance

### GetIsEnabled
```angelscript
bool GetIsEnabled()
```
Gets the current enabled status of the widget

### GetOwningLocalPlayer
```angelscript
ULocalPlayer GetOwningLocalPlayer()
```
Gets the local player associated with this UI.
@return The owning local player.

### GetOwningPlayer
```angelscript
APlayerController GetOwningPlayer()
```
Gets the player controller associated with this UI.
@return The player controller that owns the UI.

### GetPaintSpaceGeometry
```angelscript
FGeometry GetPaintSpaceGeometry()
```

### GetParent
```angelscript
UPanelWidget GetParent()
```
Gets the parent widget

### GetRenderOpacity
```angelscript
float32 GetRenderOpacity()
```
Gets the current visibility of the widget.

### GetRenderTransformAngle
```angelscript
float32 GetRenderTransformAngle()
```

### GetTickSpaceGeometry
```angelscript
FGeometry GetTickSpaceGeometry()
```

### GetVisibility
```angelscript
ESlateVisibility GetVisibility()
```
Gets the current visibility of the widget.

### HasAnyUserFocus
```angelscript
bool HasAnyUserFocus()
```
Returns true if this widget is focused by any user.

### HasFocusedDescendants
```angelscript
bool HasFocusedDescendants()
```
Returns true if any descendant widget is focused by any user.

### HasKeyboardFocus
```angelscript
bool HasKeyboardFocus()
```
Checks to see if this widget currently has the keyboard focus

@return  True if this widget has keyboard focus

### HasMouseCapture
```angelscript
bool HasMouseCapture()
```
Checks to see if this widget is the current mouse captor
@return  True if this widget has captured the mouse

### HasMouseCaptureByUser
```angelscript
bool HasMouseCaptureByUser(int UserIndex, int PointerIndex)
```
Checks to see if this widget is the current mouse captor
     @param User index to check for capture
     @param Optional pointer index to check for capture
     @return  True if this widget has captured the mouse with given user and pointer

### HasUserFocus
```angelscript
bool HasUserFocus(APlayerController PlayerController)
```
Returns true if this widget is focused by a specific user.

### HasUserFocusedDescendants
```angelscript
bool HasUserFocusedDescendants(APlayerController PlayerController)
```
Returns true if any descendant widget is focused by a specific user.

### InvalidateLayoutAndVolatility
```angelscript
void InvalidateLayoutAndVolatility()
```
Invalidates the widget from the view of a layout caching widget that may own this widget.
will force the owning widget to redraw and cache children on the next paint pass.

### IsHovered
```angelscript
bool IsHovered()
```
Returns true if the widget is currently being hovered by a pointer device

### IsInViewport
```angelscript
bool IsInViewport()
```
@return true if the widget was added to the viewport using AddToViewport or AddToPlayerScreen.

### IsRendered
```angelscript
bool IsRendered()
```
Returns true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible and the Render Opacity is greater than 0.

### IsVisible
```angelscript
bool IsVisible()
```
Returns true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible.

### AddFieldValueChangedDelegate
```angelscript
void AddFieldValueChangedDelegate(FFieldNotificationId FieldId, FFieldValueChangedDynamicDelegate Delegate)
```

### BroadcastFieldValueChanged
```angelscript
void BroadcastFieldValueChanged(FFieldNotificationId FieldId)
```

### RemoveFieldValueChangedDelegate
```angelscript
void RemoveFieldValueChangedDelegate(FFieldNotificationId FieldId, FFieldValueChangedDynamicDelegate Delegate)
```

### RemoveFromParent
```angelscript
void RemoveFromParent()
```
Removes the widget from its parent widget.  If this widget was added to the player's screen or the viewport
it will also be removed from those containers.

### ResetCursor
```angelscript
void ResetCursor()
```
Resets the cursor to use on the widget, removing any customization for it.

### SetAllNavigationRules
```angelscript
void SetAllNavigationRules(EUINavigationRule Rule, FName WidgetToFocus)
```
Sets the widget navigation rules for all directions. This can only be called on widgets that are in a widget tree.
@param Rule The rule to use when navigation is taking place
@param WidgetToFocus When using the Explicit rule, focus on this widget

### SetClipping
```angelscript
void SetClipping(EWidgetClipping InClipping)
```
Sets the clipping state of this widget.

### SetCursor
```angelscript
void SetCursor(EMouseCursor InCursor)
```
Sets the cursor to show over the widget.

### SetFocus
```angelscript
void SetFocus()
```
Sets the focus to this widget for the owning user

### SetIsEnabled
```angelscript
void SetIsEnabled(bool bInIsEnabled)
```
Sets the current enabled status of the widget

### SetKeyboardFocus
```angelscript
void SetKeyboardFocus()
```
Sets the focus to this widget.

### SetNavigationRuleBase
```angelscript
void SetNavigationRuleBase(EUINavigation Direction, EUINavigationRule Rule)
```
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for non Explicit, non Custom and non CustomBoundary Rules.
@param Direction
@param Rule The rule to use when navigation is taking place

### SetNavigationRuleCustom
```angelscript
void SetNavigationRuleCustom(EUINavigation Direction, FCustomWidgetNavigationDelegate InCustomDelegate)
```
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for Custom Rule.
@param Direction
@param InCustomDelegate Custom Delegate that will be called

### SetNavigationRuleCustomBoundary
```angelscript
void SetNavigationRuleCustomBoundary(EUINavigation Direction, FCustomWidgetNavigationDelegate InCustomDelegate)
```
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for CustomBoundary Rule.
@param Direction
@param InCustomDelegate Custom Delegate that will be called

### SetNavigationRuleExplicit
```angelscript
void SetNavigationRuleExplicit(EUINavigation Direction, UWidget InWidget)
```
Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree. This works only for Explicit Rule.
@param Direction
@param InWidget Focus on this widget instance

### SetRenderOpacity
```angelscript
void SetRenderOpacity(float32 InOpacity)
```
Sets the visibility of the widget.

### SetRenderScale
```angelscript
void SetRenderScale(FVector2D Scale)
```

### SetRenderShear
```angelscript
void SetRenderShear(FVector2D Shear)
```

### SetRenderTransform
```angelscript
void SetRenderTransform(FWidgetTransform InTransform)
```

### SetRenderTransformAngle
```angelscript
void SetRenderTransformAngle(float32 Angle)
```

### SetRenderTransformPivot
```angelscript
void SetRenderTransformPivot(FVector2D Pivot)
```

### SetRenderTranslation
```angelscript
void SetRenderTranslation(FVector2D Translation)
```

### SetToolTip
```angelscript
void SetToolTip(UWidget Widget)
```
Sets a custom widget as the tooltip of the widget.

### SetToolTipText
```angelscript
void SetToolTipText(FText InToolTipText)
```
Sets the tooltip text for the widget.

### SetUserFocus
```angelscript
void SetUserFocus(APlayerController PlayerController)
```
Sets the focus to this widget for a specific user (if setting focus for the owning user, prefer SetFocus())

### SetVisibility
```angelscript
void SetVisibility(ESlateVisibility InVisibility)
```
Sets the visibility of the widget.

### GetRenderTransform
```angelscript
FWidgetTransform GetRenderTransform()
```


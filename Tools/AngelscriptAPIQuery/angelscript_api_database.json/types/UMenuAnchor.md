# UMenuAnchor

**继承自**: `UContentWidget`

The Menu Anchor allows you to specify an location that a popup menu should be anchored to,
and should be summoned from.
* Single Child
* Popup

## 属性

### MenuClass
- **类型**: `TSubclassOf<UUserWidget>`

### OnGetMenuContentEvent
- **类型**: `FGetWidget__Widget`

### OnGetUserMenuContentEvent
- **类型**: `FGetUserWidget__MenuAnchor`
- **描述**: Called when the menu content is requested to allow a more customized handling over what to display

### ShouldFitInWindow
- **类型**: `bool`

### ShouldDeferPaintingAfterWindowContent
- **类型**: `bool`

### UseApplicationMenuStack
- **类型**: `bool`

### OnMenuOpenChanged
- **类型**: `FOnMenuOpenChangedEvent`

### bFitInWindow
- **类型**: `bool`

### Placement
- **类型**: `EMenuPlacement`

## 方法

### Close
```angelscript
void Close()
```
Closes the menu if it is currently open.

### FitInWindow
```angelscript
void FitInWindow(bool bFit)
```

### GetMenuPosition
```angelscript
FVector2D GetMenuPosition()
```
Returns the current menu position

### HasOpenSubMenus
```angelscript
bool HasOpenSubMenus()
```
Returns whether this menu has open submenus

### IsOpen
```angelscript
bool IsOpen()
```
Returns true if the popup is open; false otherwise.

### Open
```angelscript
void Open(bool bFocusMenu)
```
Opens the menu if it is not already open

### SetPlacement
```angelscript
void SetPlacement(EMenuPlacement InPlacement)
```
TODO UMG Add Set MenuClass

### ShouldOpenDueToClick
```angelscript
bool ShouldOpenDueToClick()
```
Returns true if we should open the menu due to a click. Sometimes we should not, if
the same MouseDownEvent that just closed the menu is about to re-open it because it
happens to land on the button.

### ToggleOpen
```angelscript
void ToggleOpen(bool bFocusOnOpen)
```
Toggles the menus open state.

@param bFocusOnOpen  Should we focus the popup as soon as it opens?


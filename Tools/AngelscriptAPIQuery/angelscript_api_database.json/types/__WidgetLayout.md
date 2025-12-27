# __WidgetLayout

## 方法

### GetMousePositionOnPlatform
```angelscript
FVector2D GetMousePositionOnPlatform()
```
Gets the platform's mouse cursor position.  This is the 'absolute' desktop location of the mouse.

### GetMousePositionOnViewport
```angelscript
FVector2D GetMousePositionOnViewport()
```
Gets the platform's mouse cursor position in the local space of the viewport widget.

### GetMousePositionScaledByDPI
```angelscript
bool GetMousePositionScaledByDPI(APlayerController Player, float32& LocationX, float32& LocationY)
```
Gets the mouse position of the player controller, scaled by the DPI.  If you're trying to go from raw mouse screenspace coordinates
to fullscreen widget space, you'll need to transform the mouse into DPI Scaled space.  This function performs that scaling.

MousePositionScaledByDPI = MousePosition * (1 / ViewportScale).
        //UE_DEPRECATED(4.17, "Use GetMousePositionOnViewport() instead.  Optionally and for more options, you can use GetViewportWidgetGeometry and GetPlayerScreenWidgetGeometry are newly introduced to give you the geometry of the viewport and the player screen for widgets to help convert between spaces.")

### GetPlayerScreenWidgetGeometry
```angelscript
FGeometry GetPlayerScreenWidgetGeometry(APlayerController PlayerController)
```
Gets the geometry of the widget holding all widgets added to the "Player Screen". You
can use this geometry to convert between absolute and local space of widgets held on this
widget.

### GetViewportScale
```angelscript
float32 GetViewportScale()
```
Gets the current DPI Scale being applied to the viewport and all the Widgets.

### GetViewportSize
```angelscript
FVector2D GetViewportSize()
```
Gets the size of the game viewport.

### GetViewportWidgetGeometry
```angelscript
FGeometry GetViewportWidgetGeometry()
```
Gets the geometry of the widget holding all widgets added to the "Viewport".  You
can use this geometry to convert between absolute and local space of widgets held on this
widget.

### ProjectWorldLocationToWidgetPosition
```angelscript
bool ProjectWorldLocationToWidgetPosition(APlayerController PlayerController, FVector WorldLocation, FVector2D& ScreenPosition, bool bPlayerViewportRelative)
```
Gets the projected world to screen position for a player, then converts it into a widget
position, which takes into account any quality scaling.
@param PlayerController The player controller to project the position in the world to their screen.
@param WorldLocation The world location to project from.
@param ScreenPosition The position in the viewport with quality scale removed and DPI scale remove.
@param bPlayerViewportRelative Should this be relative to the player viewport subregion (useful when using player attached widgets in split screen or when aspect-ratio constrained)
@return true if the position projects onto the screen.

### RemoveAllWidgets
```angelscript
void RemoveAllWidgets()
```
Removes all widgets from the viewport.

### SlotAsBorderSlot
```angelscript
UBorderSlot SlotAsBorderSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Border Slot, allowing you to manipulate layout information.
@param Widget The child widget of a border panel.

### SlotAsCanvasSlot
```angelscript
UCanvasPanelSlot SlotAsCanvasSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Canvas Slot, allowing you to manipulate layout information.
@param Widget The child widget of a canvas panel.

### SlotAsGridSlot
```angelscript
UGridSlot SlotAsGridSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Grid Slot, allowing you to manipulate layout information.
@param Widget The child widget of a grid panel.

### SlotAsHorizontalBoxSlot
```angelscript
UHorizontalBoxSlot SlotAsHorizontalBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Horizontal Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Horizontal Box.

### SlotAsOverlaySlot
```angelscript
UOverlaySlot SlotAsOverlaySlot(UWidget Widget)
```
Gets the slot object on the child widget as a Overlay Slot, allowing you to manipulate layout information.
@param Widget The child widget of a overlay panel.

### SlotAsSafeBoxSlot
```angelscript
USafeZoneSlot SlotAsSafeBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Safe Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Safe Box.

### SlotAsScaleBoxSlot
```angelscript
UScaleBoxSlot SlotAsScaleBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Scale Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Scale Box.

### SlotAsScrollBoxSlot
```angelscript
UScrollBoxSlot SlotAsScrollBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Scroll Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Scroll Box.

### SlotAsSizeBoxSlot
```angelscript
USizeBoxSlot SlotAsSizeBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Size Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Size Box.

### SlotAsUniformGridSlot
```angelscript
UUniformGridSlot SlotAsUniformGridSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Uniform Grid Slot, allowing you to manipulate layout information.
@param Widget The child widget of a uniform grid panel.

### SlotAsVerticalBoxSlot
```angelscript
UVerticalBoxSlot SlotAsVerticalBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Vertical Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Vertical Box.

### SlotAsWidgetSwitcherSlot
```angelscript
UWidgetSwitcherSlot SlotAsWidgetSwitcherSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Widget Switcher Slot, allowing you to manipulate its information.
@param Widget The child widget of a Widget Switcher Slot.

### SlotAsWrapBoxSlot
```angelscript
UWrapBoxSlot SlotAsWrapBoxSlot(UWidget Widget)
```
Gets the slot object on the child widget as a Wrap Box Slot, allowing you to manipulate its information.
@param Widget The child widget of a Wrap Box.


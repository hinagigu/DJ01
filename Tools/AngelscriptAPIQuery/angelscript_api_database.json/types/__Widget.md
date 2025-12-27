# __Widget

## 方法

### CancelDragDrop
```angelscript
void CancelDragDrop()
```
Cancels any current drag drop operation.

### CaptureMouse
```angelscript
FEventReply CaptureMouse(FEventReply& Reply, UWidget CapturingWidget)
```

### ClearUserFocus
```angelscript
FEventReply ClearUserFocus(FEventReply& Reply, bool bInAllUsers)
```

### DetectDrag
```angelscript
FEventReply DetectDrag(FEventReply& Reply, UWidget WidgetDetectingDrag, FKey DragKey)
```
Ask Slate to detect if a user starts dragging in this widget later.  Slate internally tracks the movement
and if it surpasses the drag threshold, Slate will send an OnDragDetected event to the widget.

@param WidgetDetectingDrag  Detect dragging in this widget
@param DragKey                      This button should be pressed to detect the drag

### DetectDragIfPressed
```angelscript
FEventReply DetectDragIfPressed(FPointerEvent PointerEvent, UWidget WidgetDetectingDrag, FKey DragKey)
```
Given the pointer event, emit the DetectDrag reply if the provided key was pressed.
If the DragKey is a touch key, that will also automatically work.
@param PointerEvent  The pointer device event coming in.
@param WidgetDetectingDrag  Detect dragging in this widget.
@param DragKey                      This button should be pressed to detect the drag, won't emit the DetectDrag FEventReply unless this is pressed.

### DismissAllMenus
```angelscript
void DismissAllMenus()
```
Closes any popup menu

### DrawBox
```angelscript
void DrawBox(FPaintContext& Context, FVector2D Position, FVector2D Size, USlateBrushAsset Brush, FLinearColor Tint)
```
Draws a box

### DrawLine
```angelscript
void DrawLine(FPaintContext& Context, FVector2D PositionA, FVector2D PositionB, FLinearColor Tint, bool bAntiAlias, float32 Thickness)
```
Draws a line.

@param PositionA             Starting position of the line in local space.
@param PositionB             Ending position of the line in local space.
@param Tint                  Color to render the line.
@param bAntialias    Whether the line should be antialiased.
@param Thickness             How many pixels thick this line should be.

### DrawLines
```angelscript
void DrawLines(FPaintContext& Context, TArray<FVector2D> Points, FLinearColor Tint, bool bAntiAlias, float32 Thickness)
```
Draws several line segments.

@param Points                Line pairs, each line needs to be 2 separate points in the array.
@param Tint                  Color to render the line.
@param bAntialias    Whether the line should be antialiased.
@param Thickness             How many pixels thick this line should be.

### DrawSpline
```angelscript
void DrawSpline(FPaintContext& Context, FVector2D Start, FVector2D StartDir, FVector2D End, FVector2D EndDir, FLinearColor Tint, float32 Thickness)
```
Draws a hermite spline.

@param Start                 Starting position of the spline in local space.
@param StartDir              The direction of the spline from the start point.
@param End                   Ending position of the spline in local space.
@param EndDir                The direction of the spline to the end point.
@param Tint                  Color to render the spline.
@param Thickness             How many pixels thick this spline should be.

### DrawTextFormatted
```angelscript
void DrawTextFormatted(FPaintContext& Context, FText Text, FVector2D Position, UFont Font, float32 FontSize, FName FontTypeFace, FLinearColor Tint)
```
Draws text.

@param Text                  The string to draw.
@param Position              The starting position where the text is drawn in local space.
@param Tint                  Color to render the line.

### EndDragDrop
```angelscript
FEventReply EndDragDrop(FEventReply& Reply)
```
An event should return FReply::Handled().EndDragDrop() to request that the current drag/drop operation be terminated.

### GetAllWidgetsOfClass
```angelscript
void GetAllWidgetsOfClass(TArray<UUserWidget>& FoundWidgets, TSubclassOf<UUserWidget> WidgetClass, bool TopLevelOnly)
```
Find all widgets of a certain class.
@param FoundWidgets The widgets that were found matching the filter.
@param WidgetClass The widget class to filter by.
@param TopLevelOnly Only the widgets that are direct children of the viewport will be returned.

### GetAllWidgetsWithInterface
```angelscript
void GetAllWidgetsWithInterface(TArray<UUserWidget>& FoundWidgets, TSubclassOf<UInterface> Interface, bool TopLevelOnly)
```
Find all widgets in the world with the specified interface.
This is a slow operation, use with caution e.g. do not use every frame.
@param Interface The interface to find. Must be specified or result array will be empty.
@param FoundWidgets Output array of widgets that implement the specified interface.
@param TopLevelOnly Only the widgets that are direct children of the viewport will be returned.

### GetBrushResource
```angelscript
UObject GetBrushResource(FSlateBrush Brush)
```
Gets the resource object on a brush.  This could be a UTexture2D or a UMaterialInterface.

### GetBrushResourceAsMaterial
```angelscript
UMaterialInterface GetBrushResourceAsMaterial(FSlateBrush Brush)
```
Gets the brush resource as a material.

### GetBrushResourceAsTexture2D
```angelscript
UTexture2D GetBrushResourceAsTexture2D(FSlateBrush Brush)
```
Gets the brush resource as a texture 2D.

### GetDragDroppingContent
```angelscript
UDragDropOperation GetDragDroppingContent()
```
Returns the drag and drop operation that is currently occurring if any, otherwise nothing.

### GetDynamicMaterial
```angelscript
UMaterialInstanceDynamic GetDynamicMaterial(FSlateBrush& Brush)
```
Gets the material that allows changes to parameters at runtime.  The brush must already have a material assigned to it,
if it does it will automatically be converted to a MID.

@return A material that supports dynamic input from the game.

### GetInputEventFromCharacterEvent
```angelscript
FInputEvent GetInputEventFromCharacterEvent(FCharacterEvent Event)
```

### GetInputEventFromKeyEvent
```angelscript
FInputEvent GetInputEventFromKeyEvent(FKeyEvent Event)
```

### GetInputEventFromNavigationEvent
```angelscript
FInputEvent GetInputEventFromNavigationEvent(FNavigationEvent Event)
```

### GetInputEventFromPointerEvent
```angelscript
FInputEvent GetInputEventFromPointerEvent(FPointerEvent Event)
```

### GetKeyEventFromAnalogInputEvent
```angelscript
FKeyEvent GetKeyEventFromAnalogInputEvent(FAnalogInputEvent Event)
```

### GetSafeZonePadding
```angelscript
void GetSafeZonePadding(FVector4& SafePadding, FVector2D& SafePaddingScale, FVector4& SpillOverPadding)
```
Gets the amount of padding that needs to be added when accounting for the safe zone on TVs.

### Handled
```angelscript
FEventReply Handled()
```
The event reply to use when you choose to handle an event.  This will prevent the event
from continuing to bubble up / down the widget hierarchy.

### IsDragDropping
```angelscript
bool IsDragDropping()
```
Returns true if a drag/drop event is occurring that a widget can handle.

### LockMouse
```angelscript
FEventReply LockMouse(FEventReply& Reply, UWidget CapturingWidget)
```

### MakeBrushFromAsset
```angelscript
FSlateBrush MakeBrushFromAsset(USlateBrushAsset BrushAsset)
```
Creates a Slate Brush from a Slate Brush Asset

@return A new slate brush using the asset's brush.

### MakeBrushFromMaterial
```angelscript
FSlateBrush MakeBrushFromMaterial(UMaterialInterface Material, int Width, int Height)
```
Creates a Slate Brush from a Material.  Materials don't have an implicit size, so providing a widget and height
is required to hint slate with how large the image wants to be by default.

@return A new slate brush using the material.

### MakeBrushFromTexture
```angelscript
FSlateBrush MakeBrushFromTexture(UTexture2D Texture, int Width, int Height)
```
Creates a Slate Brush from a Texture2D

@param Width  When less than or equal to zero, the Width of the brush will default to the Width of the Texture
@param Height  When less than or equal to zero, the Height of the brush will default to the Height of the Texture

@return A new slate brush using the texture.

### NoResourceBrush
```angelscript
FSlateBrush NoResourceBrush()
```
Creates a Slate Brush that wont draw anything, the "Null Brush".

@return A new slate brush that wont draw anything.

### ReleaseMouseCapture
```angelscript
FEventReply ReleaseMouseCapture(FEventReply& Reply)
```

### RestorePreviousWindowTitleBarState
```angelscript
void RestorePreviousWindowTitleBarState()
```

### SetBrushResourceToMaterial
```angelscript
void SetBrushResourceToMaterial(FSlateBrush& Brush, UMaterialInterface Material)
```
Sets the resource on a brush to be a Material.

### SetBrushResourceToTexture
```angelscript
void SetBrushResourceToTexture(FSlateBrush& Brush, UTexture2D Texture)
```
Sets the resource on a brush to be a UTexture2D.

### SetColorVisionDeficiencyType
```angelscript
void SetColorVisionDeficiencyType(EColorVisionDeficiency Type, float32 Severity, bool CorrectDeficiency, bool ShowCorrectionWithDeficiency)
```
Apply color deficiency correction settings to the game window
@param Type The type of color deficiency correction to apply.
@param Severity Intensity of the color deficiency correction effect, from 0 to 1.
@param CorrectDeficiency Shifts the color spectrum to the visible range based on the current deficiency type.
@param ShowCorrectionWithDeficiency If you're correcting the color deficiency, you can use this to visualize what the correction looks like with the deficiency.

### SetFocusToGameViewport
```angelscript
void SetFocusToGameViewport()
```

### SetHardwareCursor
```angelscript
bool SetHardwareCursor(EMouseCursor CursorShape, FName CursorName, FVector2D HotSpot)
```
Loads or sets a hardware cursor from the content directory in the game.

### SetInputMode_GameAndUIEx
```angelscript
void SetInputMode_GameAndUIEx(APlayerController PlayerController, UWidget InWidgetToFocus, EMouseLockMode InMouseLockMode, bool bHideCursorDuringCapture, bool bFlushInput)
```
Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input / player controller gets a chance.

Note: This means that any bound Input events in the widget will be called.

### SetInputMode_GameOnly
```angelscript
void SetInputMode_GameOnly(APlayerController PlayerController, bool bFlushInput)
```
Setup an input mode that allows only player input / player controller to respond to user input.

Note: Any bound Input Events in this widget will be called.

### SetInputMode_UIOnlyEx
```angelscript
void SetInputMode_UIOnlyEx(APlayerController PlayerController, UWidget InWidgetToFocus, EMouseLockMode InMouseLockMode, bool bFlushInput)
```
Setup an input mode that allows only the UI to respond to user input.

Note: This means that any bound Input Events in the widget will not be called!

### SetMousePosition
```angelscript
FEventReply SetMousePosition(FEventReply& Reply, FVector2D NewMousePosition)
```

### SetUserFocus
```angelscript
FEventReply SetUserFocus(FEventReply& Reply, UWidget FocusWidget, bool bInAllUsers)
```

### SetWindowTitleBarCloseButtonActive
```angelscript
void SetWindowTitleBarCloseButtonActive(bool bActive)
```

### SetWindowTitleBarOnCloseClickedDelegate
```angelscript
void SetWindowTitleBarOnCloseClickedDelegate(FOnGameWindowCloseButtonClickedDelegate__WidgetBlueprintLibrary Delegate)
```

### SetWindowTitleBarState
```angelscript
void SetWindowTitleBarState(UWidget TitleBarContent, EWindowTitleBarMode Mode, bool bTitleBarDragEnabled, bool bWindowButtonsVisible, bool bTitleBarVisible)
```

### Unhandled
```angelscript
FEventReply Unhandled()
```
The event reply to use when you choose not to handle an event.

### UnlockMouse
```angelscript
FEventReply UnlockMouse(FEventReply& Reply)
```


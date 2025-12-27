# UWidgetComponent

**继承自**: `UMeshComponent`

The widget component provides a surface in the 3D environment on which to render widgets normally rendered to the screen.
Widgets are first rendered to a render target, then that render target is displayed in the world.

Material Properties set by this component on whatever material overrides the default.
SlateUI [Texture]
BackColor [Vector]
TintColorAndOpacity [Vector]
OpacityFromTexture [Scalar]

## 属性

### Space
- **类型**: `EWidgetSpace`
- **描述**: The coordinate space in which to render the widget

### TimingPolicy
- **类型**: `EWidgetTimingPolicy`
- **描述**: How this widget should deal with timing, pausing, etc.

### WidgetClass
- **类型**: `TSubclassOf<UUserWidget>`
- **描述**: The class of User Widget to create and display an instance of

### bManuallyRedraw
- **类型**: `bool`
- **描述**: Should we wait to be told to redraw to actually draw?

### bUseInvalidationInWorldSpace
- **类型**: `bool`
- **描述**: Use the invalidation system to update this widget.
Only valid in World space. In Screen space, the widget is updated by the viewport owners.

### bDrawAtDesiredSize
- **类型**: `bool`
- **描述**: Causes the render target to automatically match the desired size.

WARNING: If you change this every frame, it will be very expensive. If you need
   that effect, you should keep the outer widget's sized locked and dynamically
   scale or resize some inner widget.

### bReceiveHardwareInput
- **类型**: `bool`
- **描述**: Register with the viewport for hardware input from the true mouse and keyboard.  These widgets
will more or less react like regular 2D widgets in the viewport, e.g. they can and will steal focus
from the viewport.

WARNING: If you are making a VR game, definitely do not change this to true.  This option should ONLY be used
if you're making what would otherwise be a normal menu for a game, just in 3D.  If you also need the game to
remain responsive and for the player to be able to interact with UI and move around the world (such as a keypad on a door),
use the WidgetInteractionComponent instead.

### bWindowFocusable
- **类型**: `bool`
- **描述**: Is the virtual window created to host the widget focusable?

### bApplyGammaCorrection
- **类型**: `bool`
- **描述**: Widget components that appear in the world will be gamma corrected by the 3D renderer.
In some cases, widget components are blitted directly into the backbuffer, in which case gamma correction should be enabled.

### OpacityFromTexture
- **类型**: `float32`
- **描述**: Sets the amount of opacity from the widget's UI texture to use when rendering the translucent or masked UI to the viewport (0.0-1.0)

### BlendMode
- **类型**: `EWidgetBlendMode`
- **描述**: The blend mode for the widget.

### bIsTwoSided
- **类型**: `bool`
- **描述**: Is the component visible from behind?

### SharedLayerName
- **类型**: `FName`
- **描述**: Layer Name the widget will live on

### LayerZOrder
- **类型**: `int`
- **描述**: ZOrder the layer will be created on, note this only matters on the first time a new layer is created, subsequent additions to the same layer will use the initially defined ZOrder

## 方法

### GetCurrentDrawSize
```angelscript
FVector2D GetCurrentDrawSize()
```
Returns the "actual" draw size of the quad in the world

### GetCylinderArcAngle
```angelscript
float32 GetCylinderArcAngle()
```
Defines the curvature of the widget component when using EWidgetGeometryMode::Cylinder; ignored otherwise.

### GetDrawAtDesiredSize
```angelscript
bool GetDrawAtDesiredSize()
```

### GetDrawSize
```angelscript
FVector2D GetDrawSize()
```
Returns the "specified" draw size of the quad in the world

### GetGeometryMode
```angelscript
EWidgetGeometryMode GetGeometryMode()
```
@see EWidgetGeometryMode, @see GetCylinderArcAngle()

### GetManuallyRedraw
```angelscript
bool GetManuallyRedraw()
```
@see bManuallyRedraw

### GetMaterialInstance
```angelscript
UMaterialInstanceDynamic GetMaterialInstance()
```
Returns the dynamic material instance used to render the user widget

### GetOwnerPlayer
```angelscript
ULocalPlayer GetOwnerPlayer()
```
Gets the local player that owns this widget component.

### GetPivot
```angelscript
FVector2D GetPivot()
```
Returns the pivot point where the UI is rendered about the origin.

### GetRedrawTime
```angelscript
float32 GetRedrawTime()
```

### GetRenderTarget
```angelscript
UTextureRenderTarget2D GetRenderTarget()
```
Returns the render target to which the user widget is rendered

### GetTickWhenOffscreen
```angelscript
bool GetTickWhenOffscreen()
```
Gets whether the widget ticks when offscreen or not

### GetTwoSided
```angelscript
bool GetTwoSided()
```
Gets whether the widget is two-sided or not

### GetUserWidgetObject
```angelscript
UUserWidget GetUserWidgetObject()
```
Returns the user widget object displayed by this component

### GetWidget
```angelscript
UUserWidget GetWidget()
```
Gets the widget that is used by this Widget Component. It will be null if a Slate Widget was set using SetSlateWidget function.

### GetWidgetSpace
```angelscript
EWidgetSpace GetWidgetSpace()
```

### GetWindowFocusable
```angelscript
bool GetWindowFocusable()
```
@see bWindowFocusable

### GetWindowVisiblility
```angelscript
EWindowVisibility GetWindowVisiblility()
```
Gets the visibility of the virtual window created to host the widget focusable.

### IsWidgetVisible
```angelscript
bool IsWidgetVisible()
```
Returns true if the the Slate window is visible and that the widget is also visible, false otherwise.

### RequestRenderUpdate
```angelscript
void RequestRenderUpdate()
```
Requests that the widget have it's render target updated, if TickMode is disabled, this will force a tick to happen to update the render target.

### SetBackgroundColor
```angelscript
void SetBackgroundColor(FLinearColor NewBackgroundColor)
```
Sets the background color and opacityscale for this widget

### SetCylinderArcAngle
```angelscript
void SetCylinderArcAngle(float32 InCylinderArcAngle)
```
Defines the curvature of the widget component when using EWidgetGeometryMode::Cylinder; ignored otherwise.

### SetDrawAtDesiredSize
```angelscript
void SetDrawAtDesiredSize(bool bInDrawAtDesiredSize)
```

### SetDrawSize
```angelscript
void SetDrawSize(FVector2D Size)
```
Sets the draw size of the quad in the world

### SetGeometryMode
```angelscript
void SetGeometryMode(EWidgetGeometryMode InGeometryMode)
```

### SetManuallyRedraw
```angelscript
void SetManuallyRedraw(bool bUseManualRedraw)
```
@see bManuallyRedraw

### SetOwnerPlayer
```angelscript
void SetOwnerPlayer(ULocalPlayer LocalPlayer)
```
Sets the local player that owns this widget component.  Setting the owning player controls
which player's viewport the widget appears on in a split screen scenario.  Additionally it
forwards the owning player to the actual UserWidget that is spawned.

### SetPivot
```angelscript
void SetPivot(FVector2D InPivot)
```

### SetRedrawTime
```angelscript
void SetRedrawTime(float32 InRedrawTime)
```

### SetTickMode
```angelscript
void SetTickMode(ETickMode InTickMode)
```
Sets the Tick mode of the Widget Component.

### SetTickWhenOffscreen
```angelscript
void SetTickWhenOffscreen(bool bWantTickWhenOffscreen)
```
Sets whether the widget ticks when offscreen or not

### SetTintColorAndOpacity
```angelscript
void SetTintColorAndOpacity(FLinearColor NewTintColorAndOpacity)
```
Sets the tint color and opacity scale for this widget

### SetTwoSided
```angelscript
void SetTwoSided(bool bWantTwoSided)
```
Sets whether the widget is two-sided or not

### SetWidget
```angelscript
void SetWidget(UUserWidget Widget)
```
Sets the widget to use directly. This function will keep track of the widget till the next time it's called
    with either a newer widget or a nullptr

### SetWidgetSpace
```angelscript
void SetWidgetSpace(EWidgetSpace NewSpace)
```

### SetWindowFocusable
```angelscript
void SetWindowFocusable(bool bInWindowFocusable)
```
@see bWindowFocusable

### SetWindowVisibility
```angelscript
void SetWindowVisibility(EWindowVisibility InVisibility)
```
Sets the visibility of the virtual window created to host the widget focusable.


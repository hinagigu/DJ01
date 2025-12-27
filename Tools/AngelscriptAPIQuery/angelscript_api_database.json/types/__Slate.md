# __Slate

## 方法

### AbsoluteToLocal
```angelscript
FVector2D AbsoluteToLocal(FGeometry Geometry, FVector2D AbsoluteCoordinate)
```
Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

@return Transforms AbsoluteCoordinate into the local space of this Geometry.

### AbsoluteToViewport
```angelscript
void AbsoluteToViewport(FVector2D AbsoluteDesktopCoordinate, FVector2D& PixelPosition, FVector2D& ViewportPosition)
```
Translates absolute coordinate in desktop space of the geometry provided into local viewport coordinates.

@param PixelPosition The position in the game's viewport, usable for line traces and
other uses where you need a coordinate in the space of viewport resolution units.
@param ViewportPosition The position in the space of other widgets in the viewport.  Like if you wanted
to add another widget to the viewport at the same position in viewport space as this location, this is
what you would use.

### EqualEqual_SlateBrush
```angelscript
bool EqualEqual_SlateBrush(FSlateBrush A, FSlateBrush B)
```
Returns whether brushes A and B are identical.

### GetAbsoluteSize
```angelscript
FVector2D GetAbsoluteSize(FGeometry Geometry)
```
Returns the size of the geometry in absolute space.

### GetLocalSize
```angelscript
FVector2D GetLocalSize(FGeometry Geometry)
```
Returns the size of the geometry in local space.

### GetLocalTopLeft
```angelscript
FVector2D GetLocalTopLeft(FGeometry Geometry)
```
Returns the local top/left of the geometry in local space.

### IsUnderLocation
```angelscript
bool IsUnderLocation(FGeometry Geometry, FVector2D AbsoluteCoordinate)
```
Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

@return true if the provided location in absolute coordinates is within the bounds of this geometry.

### LocalToAbsolute
```angelscript
FVector2D LocalToAbsolute(FGeometry Geometry, FVector2D LocalCoordinate)
```
Translates local coordinates into absolute coordinates

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

@return  Absolute coordinates

### LocalToViewport
```angelscript
void LocalToViewport(FGeometry Geometry, FVector2D LocalCoordinate, FVector2D& PixelPosition, FVector2D& ViewportPosition)
```
Translates local coordinate of the geometry provided into local viewport coordinates.

@param PixelPosition The position in the game's viewport, usable for line traces and
other uses where you need a coordinate in the space of viewport resolution units.
@param ViewportPosition The position in the space of other widgets in the viewport.  Like if you wanted
to add another widget to the viewport at the same position in viewport space as this location, this is
what you would use.

### ScreenToViewport
```angelscript
void ScreenToViewport(FVector2D ScreenPosition, FVector2D& ViewportPosition)
```
Translates a screen position in pixels into the local space of the viewport widget.

### ScreenToWidgetAbsolute
```angelscript
void ScreenToWidgetAbsolute(FVector2D ScreenPosition, FVector2D& AbsoluteCoordinate, bool bIncludeWindowPosition)
```
Translates a screen position in pixels into absolute application coordinates.
If bIncludeWindowPosition is true, then this method will also remove the game window's position (useful when in windowed mode).

### ScreenToWidgetLocal
```angelscript
void ScreenToWidgetLocal(FGeometry Geometry, FVector2D ScreenPosition, FVector2D& LocalCoordinate, bool bIncludeWindowPosition)
```
Translates a screen position in pixels into the local space of a widget with the given geometry.
If bIncludeWindowPosition is true, then this method will also remove the game window's position (useful when in windowed mode).

### TransformScalarAbsoluteToLocal
```angelscript
float32 TransformScalarAbsoluteToLocal(FGeometry Geometry, float32 AbsoluteScalar)
```

### TransformScalarLocalToAbsolute
```angelscript
float32 TransformScalarLocalToAbsolute(FGeometry Geometry, float32 LocalScalar)
```

### TransformVectorAbsoluteToLocal
```angelscript
FVector2D TransformVectorAbsoluteToLocal(FGeometry Geometry, FVector2D AbsoluteVector)
```

### TransformVectorLocalToAbsolute
```angelscript
FVector2D TransformVectorLocalToAbsolute(FGeometry Geometry, FVector2D LocalVector)
```


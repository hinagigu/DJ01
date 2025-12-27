# AHUD

**继承自**: `AActor`

Base class of the heads-up display. This has a canvas and a debug canvas on which primitives can be drawn.
It also contains a list of simple hit boxes that can be used for simple item click detection.
A method of rendering debug text is also included.
Provides some simple methods for rendering text, textures, rectangles and materials which can also be accessed from blueprints.
@see UCanvas
@see FHUDHitBox
@see FDebugTextInfo

## 属性

### PlayerOwner
- **类型**: `APlayerController`
- **描述**: PlayerController which owns this HUD.

### bLostFocusPaused
- **类型**: `bool`

### bShowHUD
- **类型**: `bool`

### bShowDebugInfo
- **类型**: `bool`

### bShowHitBoxDebugInfo
- **类型**: `bool`

### bShowOverlays
- **类型**: `bool`

### bEnableDebugTextShadow
- **类型**: `bool`

## 方法

### AddDebugText
```angelscript
void AddDebugText(FString DebugText, AActor SrcActor, float32 Duration, FVector Offset, FVector DesiredOffset, FColor TextColor, bool bSkipOverwriteCheck, bool bAbsoluteLocation, bool bKeepAttachedToActor, UFont InFont, float32 FontScale, bool bDrawShadow)
```
Add debug text for a specific actor to be displayed via DrawDebugTextList().  If the debug text is invalid then it will
attempt to remove any previous entries via RemoveDebugText().

@param DebugText                             Text to draw
@param SrcActor                              Actor to which this relates
@param Duration                              Duration to display the string
@param Offset                                Initial offset to render text
@param DesiredOffset                 Desired offset to render text - the text will move to this location over the given duration
@param TextColor                     Color of text to render
@param bSkipOverwriteCheck   skips the check to see if there is already debug text for the given actor
@param bAbsoluteLocation     use an absolute world location
@param bKeepAttachedToActor  if this is true the text will follow the actor, otherwise it will be drawn at the location when the call was made
@param InFont                                font to use
@param FontScale                     scale
@param bDrawShadow                   Draw shadow on this string

### AddHitBox
```angelscript
void AddHitBox(FVector2D Position, FVector2D Size, FName InName, bool bConsumesInput, int Priority)
```
Add a hitbox to the hud
@param Position                      Coordinates of the top left of the hit box.
@param Size                          Size of the hit box.
@param Name                          Name of the hit box.
@param bConsumesInput        Whether click processing should continue if this hit box is clicked.
@param Priority                      The priority of the box used for layering. Larger values are considered first.  Equal values are considered in the order they were added.

### Deproject
```angelscript
void Deproject(float32 ScreenX, float32 ScreenY, FVector& WorldPosition, FVector& WorldDirection)
```
Transforms a 2D screen location into a 3D location and direction

### DrawLine
```angelscript
void DrawLine(float32 StartScreenX, float32 StartScreenY, float32 EndScreenX, float32 EndScreenY, FLinearColor LineColor, float32 LineThickness)
```
Draws a 2D line on the HUD.
@param StartScreenX          Screen-space X coordinate of start of the line.
@param StartScreenY          Screen-space Y coordinate of start of the line.
@param EndScreenX            Screen-space X coordinate of end of the line.
@param EndScreenY            Screen-space Y coordinate of end of the line.
@param LineColor                     Color to draw line
@param LineThickness         Thickness of the line to draw

### DrawMaterial
```angelscript
void DrawMaterial(UMaterialInterface Material, float32 ScreenX, float32 ScreenY, float32 ScreenW, float32 ScreenH, float32 MaterialU, float32 MaterialV, float32 MaterialUWidth, float32 MaterialVHeight, float32 Scale, bool bScalePosition, float32 Rotation, FVector2D RotPivot)
```
Draws a material-textured quad on the HUD.
@param Material                      Material to use
@param ScreenX                       Screen-space X coordinate of upper left corner of the quad.
@param ScreenY                       Screen-space Y coordinate of upper left corner of the quad.
@param ScreenW                       Screen-space width of the quad (in pixels).
@param ScreenH                       Screen-space height of the quad (in pixels).
@param MaterialU                     Texture-space U coordinate of upper left corner of the quad
@param MaterialV                     Texture-space V coordinate of upper left corner of the quad.
@param MaterialUWidth        Texture-space width of the quad (in normalized UV distance).
@param MaterialVHeight       Texture-space height of the quad (in normalized UV distance).
@param Scale                         Amount to scale the entire texture (horizontally and vertically)
@param bScalePosition        Whether the "Scale" parameter should also scale the position of this draw call.
@param Rotation                      Amount to rotate this quad
@param RotPivot                      Location (as proportion of quad, 0-1) to rotate about

### DrawMaterialSimple
```angelscript
void DrawMaterialSimple(UMaterialInterface Material, float32 ScreenX, float32 ScreenY, float32 ScreenW, float32 ScreenH, float32 Scale, bool bScalePosition)
```
Draws a material-textured quad on the HUD.  Assumes UVs such that the entire material is shown.
@param Material                      Material to use
@param ScreenX                       Screen-space X coordinate of upper left corner of the quad.
@param ScreenY                       Screen-space Y coordinate of upper left corner of the quad.
@param ScreenW                       Screen-space width of the quad (in pixels).
@param ScreenH                       Screen-space height of the quad (in pixels).
@param Scale                         Amount to scale the entire texture (horizontally and vertically)
@param bScalePosition        Whether the "Scale" parameter should also scale the position of this draw call.

### DrawMaterialTriangle
```angelscript
void DrawMaterialTriangle(UMaterialInterface Material, FVector2D V0_Pos, FVector2D V1_Pos, FVector2D V2_Pos, FVector2D V0_UV, FVector2D V1_UV, FVector2D V2_UV, FLinearColor V0_Color, FLinearColor V1_Color, FLinearColor V2_Color)
```

### DrawRect
```angelscript
void DrawRect(FLinearColor RectColor, float32 ScreenX, float32 ScreenY, float32 ScreenW, float32 ScreenH)
```
Draws a colored untextured quad on the HUD.
@param RectColor                     Color of the rect. Can be translucent.
@param ScreenX                       Screen-space X coordinate of upper left corner of the quad.
@param ScreenY                       Screen-space Y coordinate of upper left corner of the quad.
@param ScreenW                       Screen-space width of the quad (in pixels).
@param ScreenH                       Screen-space height of the quad (in pixels).

### DrawText
```angelscript
void DrawText(FString Text, FLinearColor TextColor, float32 ScreenX, float32 ScreenY, UFont Font, float32 Scale, bool bScalePosition)
```
Draws a string on the HUD.
@param Text                          String to draw
@param TextColor                     Color to draw string
@param ScreenX                       Screen-space X coordinate of upper left corner of the string.
@param ScreenY                       Screen-space Y coordinate of upper left corner of the string.
@param Font                          Font to draw text.  If NULL, default font is chosen.
@param Scale                         Scale multiplier to control size of the text.
@param bScalePosition        Whether the "Scale" parameter should also scale the position of this draw call.

### DrawTexture
```angelscript
void DrawTexture(UTexture Texture, float32 ScreenX, float32 ScreenY, float32 ScreenW, float32 ScreenH, float32 TextureU, float32 TextureV, float32 TextureUWidth, float32 TextureVHeight, FLinearColor TintColor, EBlendMode BlendMode, float32 Scale, bool bScalePosition, float32 Rotation, FVector2D RotPivot)
```
Draws a textured quad on the HUD.
@param Texture                       Texture to draw.
@param ScreenX                       Screen-space X coordinate of upper left corner of the quad.
@param ScreenY                       Screen-space Y coordinate of upper left corner of the quad.
@param ScreenW                       Screen-space width of the quad (in pixels).
@param ScreenH                       Screen-space height of the quad (in pixels).
@param TextureU                      Texture-space U coordinate of upper left corner of the quad
@param TextureV                      Texture-space V coordinate of upper left corner of the quad.
@param TextureUWidth         Texture-space width of the quad (in normalized UV distance).
@param TextureVHeight        Texture-space height of the quad (in normalized UV distance).
@param TintColor                     Vertex color for the quad.
@param BlendMode                     Controls how to blend this quad with the scene. Translucent by default.
@param Scale                         Amount to scale the entire texture (horizontally and vertically)
@param bScalePosition        Whether the "Scale" parameter should also scale the position of this draw call.
@param Rotation                      Amount to rotate this quad
@param RotPivot                      Location (as proportion of quad, 0-1) to rotate about

### DrawTextureSimple
```angelscript
void DrawTextureSimple(UTexture Texture, float32 ScreenX, float32 ScreenY, float32 Scale, bool bScalePosition)
```
Draws a textured quad on the HUD. Assumes 1:1 texel density.
@param Texture                       Texture to draw.
@param ScreenX                       Screen-space X coordinate of upper left corner of the quad.
@param ScreenY                       Screen-space Y coordinate of upper left corner of the quad.
@param Scale                         Scale multiplier to control size of the text.
@param bScalePosition        Whether the "Scale" parameter should also scale the position of this draw call.

### GetActorsInSelectionRectangle
```angelscript
void GetActorsInSelectionRectangle(TSubclassOf<AActor> ClassFilter, FVector2D FirstPoint, FVector2D SecondPoint, TArray<AActor>& OutActors, bool bIncludeNonCollidingComponents, bool bActorMustBeFullyEnclosed)
```
Returns the array of actors inside a selection rectangle, with a class filter.

Sample usage:

      TArray<AStaticMeshActor*> ActorsInSelectionRect;
             Canvas->GetActorsInSelectionRectangle<AStaticMeshActor>(FirstPoint,SecondPoint,ActorsInSelectionRect);


@param FirstPoint                                    The first point, or anchor of the marquee box. Where the dragging of the marquee started in screen space.
@param SecondPoint                                   The second point, where the mouse cursor currently is / the other point of the box selection, in screen space.
@return OutActors                                    The actors that are within the selection box according to selection rule
@param bIncludeNonCollidingComponents        Whether to include even non-colliding components of the actor when determining its bounds
@param bActorMustBeFullyEnclosed     The Selection rule: whether the selection box can partially intersect Actor, or must fully enclose the Actor.

### GetOwningPawn
```angelscript
APawn GetOwningPawn()
```
Returns the Pawn for this HUD's player.

### GetOwningPlayerController
```angelscript
APlayerController GetOwningPlayerController()
```
Returns the PlayerController for this HUD's player.

### GetTextSize
```angelscript
void GetTextSize(FString Text, float32& OutWidth, float32& OutHeight, UFont Font, float32 Scale)
```
Returns the width and height of a string.
@param Text                          String to draw
@param OutWidth                      Returns the width in pixels of the string.
@param OutHeight                     Returns the height in pixels of the string.
@param Font                          Font to draw text.  If NULL, default font is chosen.
@param Scale                         Scale multiplier to control size of the text.

### Project
```angelscript
FVector Project(FVector Location, bool bClampToZeroPlane)
```
Transforms a 3D world-space vector into 2D screen coordinates
@param Location                      The world-space position to transform
@param bClampToZeroPlane     If true, 2D screen coordinates behind the viewing plane (-Z) will have Z set to 0 (leaving X and Y alone)
@return The transformed vector

### DrawHUD
```angelscript
void DrawHUD(int SizeX, int SizeY)
```
Hook to allow blueprints to do custom HUD drawing. @see bSuppressNativeHUD to control HUD drawing in base class.
Note:  the canvas resource used for drawing is only valid during this event, it will not be valid if drawing functions are called later (e.g. after a Delay node).

### HitBoxBeginCursorOver
```angelscript
void HitBoxBeginCursorOver(FName BoxName)
```
Called when a hit box is moused over.

### HitBoxClick
```angelscript
void HitBoxClick(FName BoxName)
```
Called when a hit box is clicked on. Provides the name associated with that box.

### HitBoxEndCursorOver
```angelscript
void HitBoxEndCursorOver(FName BoxName)
```
Called when a hit box no longer has the mouse over it.

### HitBoxRelease
```angelscript
void HitBoxRelease(FName BoxName)
```
Called when a hit box is unclicked. Provides the name associated with that box.

### RemoveAllDebugStrings
```angelscript
void RemoveAllDebugStrings()
```
Remove all debug strings added via AddDebugText

### RemoveDebugText
```angelscript
void RemoveDebugText(AActor SrcActor, bool bLeaveDurationText)
```
Remove debug strings for the given actor

@param       SrcActor                        Actor whose string you wish to remove
@param       bLeaveDurationText      when true text that has a finite duration will be removed, otherwise all will be removed for given actor


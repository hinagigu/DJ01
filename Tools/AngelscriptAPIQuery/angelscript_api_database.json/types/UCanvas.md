# UCanvas

**继承自**: `UObject`

A drawing canvas.

## 方法

### Deproject
```angelscript
void Deproject(FVector2D ScreenPosition, FVector& WorldOrigin, FVector& WorldDirection)
```
Performs a deprojection of a screen space coordinate using the projection matrix set up for the Canvas.

@param ScreenPosition                        Screen space position to deproject to the World.
@param WorldOrigin                           Vector which is the world position of the screen space position.
@param WorldDirection                        Vector which can be used in a trace to determine what is "behind" the screen space position. Useful for object picking.

### DrawBorder
```angelscript
void DrawBorder(UTexture BorderTexture, UTexture BackgroundTexture, UTexture LeftBorderTexture, UTexture RightBorderTexture, UTexture TopBorderTexture, UTexture BottomBorderTexture, FVector2D ScreenPosition, FVector2D ScreenSize, FVector2D CoordinatePosition, FVector2D CoordinateSize, FLinearColor RenderColor, FVector2D BorderScale, FVector2D BackgroundScale, float32 Rotation, FVector2D PivotPoint, FVector2D CornerSize)
```
Draws a 3x3 grid border with tiled frame and tiled interior on the Canvas.

@param BorderTexture                         Texture to use for border.
@param BackgroundTexture                     Texture to use for border background.
@param LeftBorderTexture                     Texture to use for the tiling left border.
@param RightBorderTexture            Texture to use for the tiling right border.
@param TopBorderTexture                      Texture to use for the tiling top border.
@param BottomBorderTexture           Texture to use for the tiling bottom border.
@param ScreenPosition                        Screen space position to render the texture.
@param ScreenSize                            Screen space size to render the texture.
@param CoordinatePosition            Normalized UV starting coordinate to use when rendering the border texture.
@param CoordinateSize                        Normalized UV size coordinate to use when rendering the border texture.
@param RenderColor                           Color to tint the border.
@param BorderScale                           Scale of the border.
@param BackgroundScale                       Scale of the background.
@param Rotation                                      Rotation, in degrees, to render the texture.
@param PivotPoint                            Normalized pivot point to use when rotating the texture.
@param CornerSize                            Frame corner size in percent of frame texture (should be < 0.5f).

### DrawBox
```angelscript
void DrawBox(FVector2D ScreenPosition, FVector2D ScreenSize, float32 Thickness, FLinearColor RenderColor)
```
Draws an unfilled box on the Canvas.

@param ScreenPosition                        Screen space position to render the text.
@param ScreenSize                            Screen space size to render the texture.
@param Thickness                                     How many pixels thick the box lines should be.

### DrawLine
```angelscript
void DrawLine(FVector2D ScreenPositionA, FVector2D ScreenPositionB, float32 Thickness, FLinearColor RenderColor)
```
Draws a line on the Canvas.

@param ScreenPositionA               Starting position of the line in screen space.
@param ScreenPositionB               Ending position of the line in screen space.
@param Thickness                             How many pixels thick this line should be.
@param RenderColor                   Color to render the line.

### DrawMaterial
```angelscript
void DrawMaterial(UMaterialInterface RenderMaterial, FVector2D ScreenPosition, FVector2D ScreenSize, FVector2D CoordinatePosition, FVector2D CoordinateSize, float32 Rotation, FVector2D PivotPoint)
```
Draws a material on the Canvas.

@param RenderMaterial                        Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas.
@param ScreenPosition                        Screen space position to render the texture.
@param ScreenSize                            Screen space size to render the texture.
@param CoordinatePosition            Normalized UV starting coordinate to use when rendering the texture.
@param CoordinateSize                        Normalized UV size coordinate to use when rendering the texture.
@param Rotation                                      Rotation, in degrees, to render the texture.
@param PivotPoint                            Normalized pivot point to use when rotating the texture.

### DrawMaterialTriangles
```angelscript
void DrawMaterialTriangles(UMaterialInterface RenderMaterial, TArray<FCanvasUVTri> Triangles)
```
Draws a set of triangles on the Canvas.

@param RenderMaterial                        Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas.
@param Triangles                                     Triangles to render.

### DrawPolygon
```angelscript
void DrawPolygon(UTexture RenderTexture, FVector2D ScreenPosition, FVector2D Radius, int NumberOfSides, FLinearColor RenderColor)
```
Draws a polygon on the Canvas.

@param RenderTexture                         Texture to use when rendering the triangles. If no texture is set, then the default white texture is used.
@param ScreenPosition                        Screen space position to render the text.
@param Radius                                        How large in pixels this polygon should be.
@param NumberOfSides                         How many sides this polygon should have. This should be above or equal to three.
@param RenderColor                           Color to tint the polygon.

### DrawText
```angelscript
void DrawText(UFont RenderFont, FString RenderText, FVector2D ScreenPosition, FVector2D Scale, FLinearColor RenderColor, float32 Kerning, FLinearColor ShadowColor, FVector2D ShadowOffset, bool bCentreX, bool bCentreY, bool bOutlined, FLinearColor OutlineColor)
```
Draws text on the Canvas.

@param RenderFont                            Font to use when rendering the text. If this is null, then a default engine font is used.
@param RenderText                            Text to render on the Canvas.
@param ScreenPosition                        Screen space position to render the text.
@param RenderColor                           Color to render the text.
@param Kerning                                       Horizontal spacing adjustment to modify the spacing between each letter.
@param ShadowColor                           Color to render the shadow of the text.
@param ShadowOffset                          Pixel offset relative to the screen space position to render the shadow of the text.
@param bCentreX                                      If true, then interpret the screen space position X coordinate as the center of the rendered text.
@param bCentreY                                      If true, then interpret the screen space position Y coordinate as the center of the rendered text.
@param bOutlined                                     If true, then the text should be rendered with an outline.
@param OutlineColor                          Color to render the outline for the text.

### DrawTexture
```angelscript
void DrawTexture(UTexture RenderTexture, FVector2D ScreenPosition, FVector2D ScreenSize, FVector2D CoordinatePosition, FVector2D CoordinateSize, FLinearColor RenderColor, EBlendMode BlendMode, float32 Rotation, FVector2D PivotPoint)
```
Draws a texture on the Canvas.

@param RenderTexture                         Texture to use when rendering. If no texture is set then this will use the default white texture.
@param ScreenPosition                        Screen space position to render the texture.
@param ScreenSize                            Screen space size to render the texture.
@param CoordinatePosition            Normalized UV starting coordinate to use when rendering the texture.
@param CoordinateSize                        Normalized UV size coordinate to use when rendering the texture.
@param RenderColor                           Color to use when rendering the texture.
@param BlendMode                                     Blending mode to use when rendering the texture.
@param Rotation                                      Rotation, in degrees, to render the texture.
@param PivotPoint                            Normalized pivot point to use when rotating the texture.

### DrawTriangles
```angelscript
void DrawTriangles(UTexture RenderTexture, TArray<FCanvasUVTri> Triangles)
```
Draws a set of triangles on the Canvas.

@param RenderTexture                         Texture to use when rendering the triangles. If no texture is set, then the default white texture is used.
@param Triangles                                     Triangles to render.

### Project
```angelscript
FVector Project(FVector WorldLocation)
```
Performs a projection of a world space coordinates using the projection matrix set up for the Canvas.

@param WorldLocation                         World space location to project onto the Canvas rendering plane.
@return                                                      Returns a vector where X, Y defines a screen space position representing the world space location.

### WrappedTextSize
```angelscript
FVector2D WrappedTextSize(UFont RenderFont, FString RenderText)
```
Returns the wrapped text size in screen space coordinates.

@param RenderFont                            Font to use when determining the size of the text. If this is null, then a default engine font is used.
@param RenderText                            Text to determine the size of.
@return                                                      Returns the screen space size of the text.

### ClippedTextSize
```angelscript
FVector2D ClippedTextSize(UFont RenderFont, FString RenderText, FVector2D Scale)
```
Returns the clipped text size in screen space coordinates.

@param RenderFont                            Font to use when determining the size of the text. If this is null, then a default engine font is used.
@param RenderText                            Text to determine the size of.
@param Scale                                         Scale of the font to use when determining the size of the text.
@return                                                      Returns the screen space size of the text.


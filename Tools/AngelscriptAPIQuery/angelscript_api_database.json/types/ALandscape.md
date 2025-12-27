# ALandscape

**继承自**: `ALandscapeProxy`

## 属性

### bAreNewLandscapeActorsSpatiallyLoaded
- **类型**: `bool`
- **描述**: Landscape actor has authority on default streaming behavior for new actors : LandscapeStreamingProxies & LandscapeSplineActors

### bCanHaveLayersContent
- **类型**: `bool`

## 方法

### ForceLayersFullUpdate
```angelscript
void ForceLayersFullUpdate()
```

### GetTargetLayerNames
```angelscript
TArray<FName> GetTargetLayerNames(bool bInIncludeVisibilityLayer)
```
Retrieves the names of valid paint layers on this landscape (editor-only : returns nothing at runtime)
@Param bInIncludeVisibilityLayer whether the visibility layer's name should be included in the list or not
@return the list of paint layer names

### RenderHeightmap
```angelscript
bool RenderHeightmap(FTransform InWorldTransform, FBox2D InExtents, UTextureRenderTarget2D OutRenderTarget)
```
Render the final heightmap in the requested top-down window as one -atlased- texture in the provided render target 2D
 Can be called at runtime.
@param InWorldTransform World transform of the area where the texture should be rendered
@param InExtents Extents of the area where the texture should be rendered (local to InWorldTransform). If size is zero, then the entire loaded landscape will be exported.
@param OutRenderTarget Render target in which the texture will be rendered. The size/format of the render target will be respected.
@return false in case of failure (e.g. invalid inputs, incompatible render target format...)

### RenderWeightmap
```angelscript
bool RenderWeightmap(FTransform InWorldTransform, FBox2D InExtents, FName InWeightmapLayerName, UTextureRenderTarget2D OutRenderTarget)
```
Render the final weightmap for the requested layer, in the requested top-down window, as one -atlased- texture in the provided render target 2D
 Can be called at runtime.
@param InWorldTransform World transform of the area where the texture should be rendered
@param InExtents Extents of the area where the texture should be rendered (local to InWorldTransform). If size is zero, then the entire loaded landscape will be exported.
@param InWeightmapLayerName Weightmap layer that is being requested to render
@param OutRenderTarget Render target in which the texture will be rendered. The size/format of the render target will be respected.
@return false in case of failure (e.g. invalid inputs, incompatible render target format...)

### RenderWeightmaps
```angelscript
bool RenderWeightmaps(FTransform InWorldTransform, FBox2D InExtents, TArray<FName> InWeightmapLayerNames, UTextureRenderTarget OutRenderTarget)
```
Render the final weightmaps for the requested layers, in the requested top-down window, as one -atlased- texture in the provided render target (2D or 2DArray)
 Can be called at runtime.
@param InWorldTransform World transform of the area where the texture should be rendered
@param InExtents Extents of the area where the texture should be rendered (local to InWorldTransform). If size is zero, then the entire loaded landscape will be exported.
@param InWeightmapLayerNames List of weightmap layers that are being requested to render
@param OutRenderTarget Render target in which the texture will be rendered. The size/format of the render target will be respected.
 - If a UTextureRenderTarget2D is passed, the requested layers will be packed in the RGBA channels in order (up to the number of channels available with the render target's format).
 - If a UTextureRenderTarget2DArray is passed, the requested layers will be packed in the RGBA channels of each slice (up to the number of channels * slices available with the render target's format and number of slices).
@return false in case of failure (e.g. invalid inputs, incompatible render target format...)


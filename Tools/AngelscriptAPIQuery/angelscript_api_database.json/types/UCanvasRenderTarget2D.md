# UCanvasRenderTarget2D

**继承自**: `UTextureRenderTarget2D`

CanvasRenderTarget2D is 2D render target which exposes a Canvas interface to allow you to draw elements onto
it directly.  Use CreateCanvasRenderTarget2D() to create a render target texture by unique name, then
bind a function to the OnCanvasRenderTargetUpdate delegate which will be called when the render target is
updated.  If you need to repaint your canvas every single frame, simply call UpdateResource() on it from a Tick
function.  Also, remember to hold onto your new canvas render target with a reference so that it doesn't get
garbage collected.

## 属性

### OnCanvasRenderTargetUpdate
- **类型**: `FOnCanvasRenderTargetUpdate`

## 方法

### GetSampleCount
```angelscript
ETextureRenderTargetSampleCount GetSampleCount()
```

### GetSize
```angelscript
void GetSize(int& Width, int& Height)
```
Gets a specific render target's size from the global map of canvas render targets.

@param       Width   Output variable for the render target's width
@param       Height  Output variable for the render target's height

### Update
```angelscript
void Update(UCanvas Canvas, int Width, int Height)
```
Allows a Blueprint to implement how this Canvas Render Target 2D should be updated.

@param       Canvas                          Canvas object that can be used to paint to the render target
@param       Width                           Width of the render target.
@param       Height                          Height of the render target.

### SetSampleCount
```angelscript
void SetSampleCount(ETextureRenderTargetSampleCount InSampleCount)
```

### UpdateResource
```angelscript
void UpdateResource()
```
Updates the the canvas render target texture's resource. This is where the render target will create or
find a canvas object to use.  It also calls UpdateResourceImmediate() to clear the render target texture
from the deferred rendering list, to stop the texture from being cleared the next frame. From there it
will ask the rendering thread to set up the RHI viewport. The canvas is then set up for rendering and
then the user's update delegate is called.  The canvas is then flushed and the RHI resolves the
texture to make it available for rendering.


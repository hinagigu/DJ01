# __UCanvasRenderTarget2D

## 方法

### CreateCanvasRenderTarget2D
```angelscript
UCanvasRenderTarget2D CreateCanvasRenderTarget2D(TSubclassOf<UCanvasRenderTarget2D> CanvasRenderTarget2DClass, int Width, int Height)
```
Creates a new canvas render target and initializes it to the specified dimensions

@param       WorldContextObject      The world where this render target will be rendered for
@param       CanvasRenderTarget2DClass       Class of the render target.  Unless you want to use a special sub-class, you can simply pass UCanvasRenderTarget2D::StaticClass() here.
@param       Width                           Width of the render target.
@param       Height                          Height of the render target.

@return                                              Returns the instanced render target.

### StaticClass
```angelscript
UClass StaticClass()
```


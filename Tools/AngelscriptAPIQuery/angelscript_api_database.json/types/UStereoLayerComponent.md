# UStereoLayerComponent

**继承自**: `USceneComponent`

A geometry layer within the stereo rendered viewport.

## 属性

### AdditionalFlags
- **类型**: `TArray<FName>`

### StereoLayerType
- **类型**: `EStereoLayerType`

### Shape
- **类型**: `UStereoLayerShape`

### bLiveTexture
- **类型**: `bool`

### bSupportsDepth
- **类型**: `bool`

### bNoAlphaChannel
- **类型**: `bool`

### bQuadPreserveTextureRatio
- **类型**: `bool`

## 方法

### GetLeftTexture
```angelscript
UTexture GetLeftTexture()
```
@return the texture mapped to the stereo layer for left eye, if stereoscopic layer textures are supported on the platform.

### GetPriority
```angelscript
int GetPriority()
```
@return the render priority

### GetQuadSize
```angelscript
FVector2D GetQuadSize()
```
@return the height and width of the rendered quad

### GetTexture
```angelscript
UTexture GetTexture()
```
@return the texture mapped to the stereo layer.

### GetUVRect
```angelscript
FBox2D GetUVRect()
```
@return the UV coordinates mapped to the quad face

### MarkTextureForUpdate
```angelscript
void MarkTextureForUpdate()
```
Manually mark the stereo layer texture for updating

### SetLeftTexture
```angelscript
void SetLeftTexture(UTexture InTexture)
```
Change the texture displayed on the stereo layer for left eye, if stereoscopic layer textures are supported on the platform.
@param       InTexture: new Texture2D

### SetPriority
```angelscript
void SetPriority(int InPriority)
```
Change the layer's render priority, higher priorities render on top of lower priorities
@param       InPriority: Priority value

### SetQuadSize
```angelscript
void SetQuadSize(FVector2D InQuadSize)
```
Change the quad size. This is the unscaled height and width, before component scale is applied.
@param       InQuadSize: new quad size.

### SetTexture
```angelscript
void SetTexture(UTexture InTexture)
```
Change the texture displayed on the stereo layer.

If stereoscopic layer textures are supported on the platform and LeftTexture is set, this property controls the texture for the right eye.
@param       InTexture: new Texture2D

### SetUVRect
```angelscript
void SetUVRect(FBox2D InUVRect)
```
Change the UV coordinates mapped to the quad face
@param       InUVRect: Min and Max UV coordinates


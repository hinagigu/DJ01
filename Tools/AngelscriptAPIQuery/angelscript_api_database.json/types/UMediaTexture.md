# UMediaTexture

**继承自**: `UTexture`

Implements a texture asset for rendering video tracks from UMediaPlayer assets.

note: derives directly from UTexture, not from UTexture2D or UTexture2DDynamic
   maybe should have been UTexture2DDynamic?

## 属性

### AddressX
- **类型**: `TextureAddress`

### AddressY
- **类型**: `TextureAddress`

### AutoClear
- **类型**: `bool`

### ClearColor
- **类型**: `FLinearColor`

### EnableGenMips
- **类型**: `bool`

### NumMips
- **类型**: `uint8`

### NewStyleOutput
- **类型**: `bool`

### CurrentAspectRatio
- **类型**: `float32`
- **描述**: Current aspect ratio

### CurrentOrientation
- **类型**: `MediaTextureOrientation`
- **描述**: Current media orientation

## 方法

### GetAspectRatio
```angelscript
float32 GetAspectRatio()
```
Gets the current aspect ratio of the texture.

@return Texture aspect ratio.
@see GetHeight, GetWidth

### GetHeight
```angelscript
int GetHeight()
```
Gets the current height of the texture.

@return Texture height (in pixels).
@see GetAspectRatio, GetWidth

### GetMediaPlayer
```angelscript
UMediaPlayer GetMediaPlayer()
```
Get the media player that provides the video samples.

@return The texture's media player, or nullptr if not set.
@see SetMediaPlayer

### GetTextureNumMips
```angelscript
int GetTextureNumMips()
```
Gets the current numbe of mips of the texture.

@return Number of mips.

### GetWidth
```angelscript
int GetWidth()
```
Gets the current width of the texture.

@return Texture width (in pixels).
@see GetAspectRatio, GetHeight

### SetMediaPlayer
```angelscript
void SetMediaPlayer(UMediaPlayer NewMediaPlayer)
```
Set the media player that provides the video samples.

@param NewMediaPlayer The player to set.
@see GetMediaPlayer

### UpdateResource
```angelscript
void UpdateResource()
```
Creates a new resource for the texture, and updates any cached references to the resource.
This obviously is just an override to expose to blueprints.


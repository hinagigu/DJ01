# UMediaPlateComponent

**继承自**: `UActorComponent`

This is a component for AMediaPlate that can play and show media in the world.

## 属性

### bPlayOnOpen
- **类型**: `bool`

### bAutoPlay
- **类型**: `bool`
- **描述**: If set then start playing when this object is active.

### bEnableAudio
- **类型**: `bool`
- **描述**: If set then enable audio.

### StartTime
- **类型**: `float32`

### SoundComponent
- **类型**: `UMediaSoundComponent`
- **描述**: Holds the component to play sound.

### StaticMeshComponent
- **类型**: `UStaticMeshComponent`
- **描述**: Holds the component for the mesh.

### Letterboxes
- **类型**: `TArray<TObjectPtr<UStaticMeshComponent>>`
- **描述**: Holds the component for the mesh.

### MediaPlaylist
- **类型**: `UMediaPlaylist`
- **描述**: What media playlist to play.

### PlaylistIndex
- **类型**: `int`
- **描述**: The current index of the source in the play list being played.

### CacheSettings
- **类型**: `FMediaSourceCacheSettings`
- **描述**: Override the default cache settings.

### bPlayOnlyWhenVisible
- **类型**: `bool`

### VisibleMipsTilesCalculations
- **类型**: `EMediaTextureVisibleMipsTiles`
- **描述**: Visible mips and tiles calculation mode for the supported mesh types in MediaPlate. (Player restart on change.)

### MipMapBias
- **类型**: `float32`
- **描述**: Media texture mip map bias shared between the (image sequence) loader and the media texture sampler.

### bEnableMipMapUpscaling
- **类型**: `bool`
- **描述**: If true then enable the use of MipLevelToUpscale as defined below.

### MipLevelToUpscale
- **类型**: `int`
- **描述**: With exr playback, upscale into lower quality mips from this specified level. All levels including and above the specified value will be fully read.

### bAdaptivePoleMipUpscaling
- **类型**: `bool`
- **描述**: If true then Media Plate will attempt to load and upscale lower quality mips and display those at the poles (Sphere object only).

### MediaTextureSettings
- **类型**: `FMediaTextureResourceSettings`
- **描述**: Exposes Media Texture settings via Media Plate component.

### bIsMediaPlatePlaying
- **类型**: `bool`

### bLoop
- **类型**: `bool`

### bIsAspectRatioAuto
- **类型**: `bool`

## 方法

### Close
```angelscript
void Close()
```
Call this to close the media.

### GetIsAspectRatioAuto
```angelscript
bool GetIsAspectRatioAuto()
```
Gets whether automatic aspect ratio is enabled.

### GetLetterboxAspectRatio
```angelscript
float32 GetLetterboxAspectRatio()
```
Call this to get the aspect ratio of the screen.

### GetLoop
```angelscript
bool GetLoop()
```
Call this to see if we want to loop.

### GetMediaPlayer
```angelscript
UMediaPlayer GetMediaPlayer()
```
Call this get our media player.

### GetMediaTexture
```angelscript
UMediaTexture GetMediaTexture(int Index)
```
Call this get our media texture.

### GetMeshRange
```angelscript
FVector2D GetMeshRange()
```
Return the arc size in degrees used for visible mips and tiles calculations, specific to the sphere.

### IsMediaPlatePlaying
```angelscript
bool IsMediaPlatePlaying()
```
Call this to see if the media plate is playing.

### Open
```angelscript
void Open()
```
Call this to open the media.

### Pause
```angelscript
void Pause()
```
Call this to pause playback.
Play can be called to resume playback.

### Play
```angelscript
void Play()
```
Call this to start playing.
Open must be called before this.

### Rewind
```angelscript
bool Rewind()
```
Rewinds the media to the beginning.

This is the same as seeking to zero time.

@return                              True if rewinding, false otherwise.

### Seek
```angelscript
bool Seek(FTimespan Time)
```
Call this to seek to the specified playback time.

@param Time                  Time to seek to.
@return                              True on success, false otherwise.

### SetIsAspectRatioAuto
```angelscript
void SetIsAspectRatioAuto(bool bInIsAspectRatioAuto)
```
Sets whether automatic aspect ratio is enabled.

### SetLetterboxAspectRatio
```angelscript
void SetLetterboxAspectRatio(float32 AspectRatio)
```
Call this to set the aspect ratio of the screen.

### SetLoop
```angelscript
void SetLoop(bool bInLoop)
```
Call this enable/disable looping.

### SetMeshRange
```angelscript
void SetMeshRange(FVector2D InMeshRange)
```
Set the arc size in degrees used for visible mips and tiles calculations, specific to the sphere.

### SetPlayOnlyWhenVisible
```angelscript
void SetPlayOnlyWhenVisible(bool bInPlayOnlyWhenVisible)
```
Call this to set bPlayOnlyWhenVisible.


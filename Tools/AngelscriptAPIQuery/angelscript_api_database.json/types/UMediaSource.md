# UMediaSource

**继承自**: `UObject`

Abstract base class for media sources.

Media sources describe the location and/or settings of media objects that can
be played in a media player, such as a video file on disk, a video stream on
the internet, or a web cam attached to or built into the target device. The
location is encoded as a media URL string, whose URI scheme and optional file
extension will be used to locate a suitable media player.

## 方法

### GetUrl
```angelscript
FString GetUrl()
```
Get the media source's URL string (must be implemented in child classes).

@return The media URL.
@see GetProxies

### SetMediaOptionBool
```angelscript
void SetMediaOptionBool(FName Key, bool Value)
```
Set a boolean parameter to pass to the player.

### SetMediaOptionFloat
```angelscript
void SetMediaOptionFloat(FName Key, float32 Value)
```
Set a float parameter to pass to the player.

### SetMediaOptionInt64
```angelscript
void SetMediaOptionInt64(FName Key, int64 Value)
```
Set an integer64 parameter to pass to the player.

### SetMediaOptionString
```angelscript
void SetMediaOptionString(FName Key, FString Value)
```
Set a string parameter to pass to the player.

### Validate
```angelscript
bool Validate()
```
Validate the media source settings (must be implemented in child classes).

@return true if validation passed, false otherwise.


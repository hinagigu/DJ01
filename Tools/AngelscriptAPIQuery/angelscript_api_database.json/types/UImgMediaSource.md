# UImgMediaSource

**继承自**: `UBaseMediaSource`

Media source for EXR image sequences.

Image sequence media sources point to a directory that contains a series of
image files in which each image represents a single frame of the sequence.
BMP, EXR, PNG and JPG images are currently supported. EXR image sequences
are optimized for performance. The first frame of an image sequence is used
to determine the image dimensions (all formats) and frame rate (EXR only).

The image sequence directory may contain sub-directories, which are called
'proxies'. Proxies can be used to provide alternative media for playback
during development and testing of a game. One common scenario is the use
of low resolution versions of image sequence media on computers that are
too slow or don't have enough storage to play the original high-res media.

## 属性

### FrameRateOverride
- **类型**: `FFrameRate`

### ProxyOverride
- **类型**: `FString`

### bFillGapsInSequence
- **类型**: `bool`

## 方法

### AddTargetObject
```angelscript
void AddTargetObject(AActor InActor)
```
This object is using our img sequence.

@param InActor Object using our img sequence.

### GetProxies
```angelscript
void GetProxies(TArray<FString>& OutProxies)
```
Get the names of available proxy directories.

@param OutProxies Will contain the names of available proxy directories, if any.
@see GetSequencePath

### GetSequencePath
```angelscript
FString GetSequencePath()
```
Get the path to the image sequence directory to be played. Supported tokens will be expanded.

@return The file path.
@see SetSequencePath

### RemoveTargetObject
```angelscript
void RemoveTargetObject(AActor InActor)
```
This object is no longer using our img sequence.

@param InActor Object no longer using our img sequence.

### SetSequencePath
```angelscript
void SetSequencePath(FString Path)
```
Set the path to the image sequence directory this source represents.

@param Path The path to an image file in the desired directory.
@see GetSequencePath

### SetTokenizedSequencePath
```angelscript
void SetTokenizedSequencePath(FString Path)
```
Set the path to the image sequence directory this source represents.

@param Path The path to the desired image sequence directory. May contain supported tokens.
@see GetSequencePath


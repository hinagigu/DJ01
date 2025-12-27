# UFileMediaSource

**继承自**: `UBaseMediaSource`

## 属性

### PrecacheFile
- **类型**: `bool`

### FilePath
- **类型**: `FString`

## 方法

### SetFilePath
```angelscript
void SetFilePath(FString Path)
```
Set the path to the media file that this source represents.

Automatically converts full paths to media sources that reside in the
Engine's or project's /Content/Movies directory into relative paths.

@param Path The path to set.
@see FilePath, GetFilePath


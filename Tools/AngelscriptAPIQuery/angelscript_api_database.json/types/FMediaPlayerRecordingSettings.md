# FMediaPlayerRecordingSettings

## 属性

### bActive
- **类型**: `bool`
- **描述**: Whether this MediaPlayer is active and its event will be recorded when the 'Record' button is pressed.

### bRecordMediaFrame
- **类型**: `bool`
- **描述**: Whether this MediaPlayer is active and the image frame will be recorded when the 'Record' button is pressed.

### BaseFilename
- **类型**: `FString`
- **描述**: How to name each frame.

### NumerationStyle
- **类型**: `EMediaPlayerRecordingNumerationStyle`
- **描述**: How to numerate the filename.

### ImageFormat
- **类型**: `EMediaPlayerRecordingImageFormat`
- **描述**: The image format we wish to record to.

### CompressionQuality
- **类型**: `int`
- **描述**: An image format specific compression setting.
For EXRs, either 0 (Default) or 1 (Uncompressed)
For PNGs & JPEGs, 0 (Default) or a value between 1 (worst quality, best compression) and 100 (best quality, worst compression)

### bResetAlpha
- **类型**: `bool`
- **描述**: If the format support it, set the alpha to 1 (or 255).
@note Removing alpha increase the memory foot print.

## 方法

### opAssign
```angelscript
FMediaPlayerRecordingSettings& opAssign(FMediaPlayerRecordingSettings Other)
```


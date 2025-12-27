# UUserDefinedImageCaptureProtocol

**继承自**: `UUserDefinedCaptureProtocol`

A blueprintable capture protocol tailored to capturing and exporting frames as images

## 属性

### Format
- **类型**: `EDesiredImageFormat`

### bEnableCompression
- **类型**: `bool`

### CompressionQuality
- **类型**: `int`

## 方法

### GenerateFilenameForBuffer
```angelscript
FString GenerateFilenameForBuffer(UTexture Buffer, FCapturedPixelsID StreamID)
```
* Generate a filename for the specified buffer using this protocol's file name formatter
*
* @param Buffer          The desired buffer to generate a filename for
* @param StreamID        The ID of the stream for this buffer (e.g. a composition pass name)
* @return A fully qualified file name

### GenerateFilenameForCurrentFrame
```angelscript
FString GenerateFilenameForCurrentFrame()
```
* Generate a filename for the current frame using this protocol's file name formatter
*
* @return A fully qualified file name for the current frame number

### WriteImageToDisk
```angelscript
void WriteImageToDisk(FCapturedPixels PixelData, FCapturedPixelsID StreamID, FFrameMetrics FrameMetrics, bool bCopyImageData)
```
* Generate a filename for the current frame using this protocol's file name formatter
*
* @return A fully qualified file name for the current frame number


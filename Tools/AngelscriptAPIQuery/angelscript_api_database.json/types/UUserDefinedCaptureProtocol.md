# UUserDefinedCaptureProtocol

**继承自**: `UMovieSceneImageCaptureProtocolBase`

A blueprintable capture protocol that defines how to capture frames from the engine

## 方法

### GenerateFilename
```angelscript
FString GenerateFilename(FFrameMetrics InFrameMetrics)
```
Generate a filename for the current frame

### GetCurrentFrameMetrics
```angelscript
FFrameMetrics GetCurrentFrameMetrics()
```
Access this protocol's current frame metrics

### OnBeginFinalize
```angelscript
void OnBeginFinalize()
```
Called when this protocol is going to be shut down - should not capture any more frames

### OnCanFinalize
```angelscript
bool OnCanFinalize()
```
Called to check whether this protocol has finished any pending tasks, and can now be shut down

### OnCaptureFrame
```angelscript
void OnCaptureFrame()
```
Called when this protocol should capture the current frame

### OnFinalize
```angelscript
void OnFinalize()
```
Called to complete finalization of this protocol

### OnPauseCapture
```angelscript
void OnPauseCapture()
```
Called when this protocol should temporarily stop capturing frames

### OnPixelsReceived
```angelscript
void OnPixelsReceived(FCapturedPixels Pixels, FCapturedPixelsID ID, FFrameMetrics FrameMetrics)
```
Called when pixels have been received for the specified stream name

### OnPreTick
```angelscript
void OnPreTick()
```
Called before the capture process itself is ticked, before each frame is set up for capture
Useful for any pre-frame set up or resetting the previous frame's state

### OnSetup
```angelscript
bool OnSetup()
```
Called once at the start of the capture process, but before any warmup frames
@return true if this protocol set up successfully, false otherwise

### OnStartCapture
```angelscript
void OnStartCapture()
```
Called when this protocol should start capturing frames

### OnTick
```angelscript
void OnTick()
```
Called after the capture process itself is ticked, after the frame is set up for capture, but before most actors have ticked

### OnWarmUp
```angelscript
void OnWarmUp()
```
Called when the capture process is warming up. Protocols may transition from either an initialized, or capturing state to warm-up

### ResolveBuffer
```angelscript
void ResolveBuffer(UTexture Buffer, FCapturedPixelsID BufferID)
```
* Resolve the specified buffer and pass it directly to the specified handler when done (does not pass to any bound streams)
*
* @param Buffer          The desired buffer to save
* @param BufferID        The ID of this buffer that is passed to the pixel handler (e.g. a composition pass name).

### StartCapturingFinalPixels
```angelscript
void StartCapturingFinalPixels(FCapturedPixelsID StreamID)
```
Instruct this protocol to start capturing LDR final pixels (including slate widgets and burn-ins)

@param StreamID        The identifier to use for the final pixels buffer

### StopCapturingFinalPixels
```angelscript
void StopCapturingFinalPixels()
```
Instruct this protocol to stop capturing LDR final pixels


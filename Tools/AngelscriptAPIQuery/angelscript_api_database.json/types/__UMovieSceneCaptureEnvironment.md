# __UMovieSceneCaptureEnvironment

## 方法

### FindAudioCaptureProtocol
```angelscript
UMovieSceneAudioCaptureProtocolBase FindAudioCaptureProtocol()
```
Attempt to locate a capture protocol - may not be in a capturing state

### FindImageCaptureProtocol
```angelscript
UMovieSceneImageCaptureProtocolBase FindImageCaptureProtocol()
```
Attempt to locate a capture protocol - may not be in a capturing state

### GetCaptureElapsedTime
```angelscript
float32 GetCaptureElapsedTime()
```
Get the total elapsed time of the current capture in seconds

### GetCaptureFrameNumber
```angelscript
int GetCaptureFrameNumber()
```
Get the frame number of the current capture

### IsCaptureInProgress
```angelscript
bool IsCaptureInProgress()
```
Return true if there is any capture currently active (even in a warm-up state).
Useful for checking whether to do certain operations in BeginPlay

### StaticClass
```angelscript
UClass StaticClass()
```


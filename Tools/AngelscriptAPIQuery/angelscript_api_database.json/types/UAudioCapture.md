# UAudioCapture

**继承自**: `UAudioGenerator`

Class which opens up a handle to an audio capture device.
Allows other objects to get audio buffers from the capture device.

## 方法

### GetAudioCaptureDeviceInfo
```angelscript
bool GetAudioCaptureDeviceInfo(FAudioCaptureDeviceInfo& OutInfo)
```
Returns the audio capture device info

### IsCapturingAudio
```angelscript
bool IsCapturingAudio()
```
Returns true if capturing audio

### StartCapturingAudio
```angelscript
void StartCapturingAudio()
```
Starts capturing audio

### StopCapturingAudio
```angelscript
void StopCapturingAudio()
```
Stops capturing audio


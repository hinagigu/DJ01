# UTimecodeProvider

**继承自**: `UObject`

A class responsible of fetching a timecode from a source.
Note, FApp::GetTimecode and FApp::GetTimecodeFramerate should be used to retrieve
the current system Timecode and Framerate.

## 属性

### FrameDelay
- **类型**: `float32`
- **描述**: Number of frames to subtract from the qualified frame time when GetDelayedQualifiedFrameTime or GetDelayedTimecode is called.
@see GetDelayedQualifiedFrameTime, GetDelayedTimecode

## 方法

### FetchAndUpdate
```angelscript
void FetchAndUpdate()
```
Update the state of the provider. Call it to ensure timecode and state are updated.
It is suggested to fetch timecode from its source and cache it for the getters.

### FetchTimecode
```angelscript
bool FetchTimecode(FQualifiedFrameTime& OutFrameTime)
```
Fetch current timecode from its source. e.g. From hardware/network/file/etc.
It is recommended to cache the fetched timecode.

### GetDelayedQualifiedFrameTime
```angelscript
FQualifiedFrameTime GetDelayedQualifiedFrameTime()
```
Return current frame time with FrameDelay applied.
Only assume valid when GetSynchronizationState() returns Synchronized.

### GetDelayedTimecode
```angelscript
FTimecode GetDelayedTimecode()
```
Return the delayed frame time converted into a timecode value.

### GetFrameRate
```angelscript
FFrameRate GetFrameRate()
```
Return the frame rate of the frame time.

### GetQualifiedFrameTime
```angelscript
FQualifiedFrameTime GetQualifiedFrameTime()
```
Return current frame time.
Since it may be called several times per frame, it is suggested to return a cached value.

### GetSynchronizationState
```angelscript
ETimecodeProviderSynchronizationState GetSynchronizationState()
```
The state of the TimecodeProvider and if it's currently synchronized and the Timecode and FrameRate getters are valid.

### GetTimecode
```angelscript
FTimecode GetTimecode()
```
Return the frame time converted into a timecode value.


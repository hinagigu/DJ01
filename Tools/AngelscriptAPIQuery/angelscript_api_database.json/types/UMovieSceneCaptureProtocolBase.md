# UMovieSceneCaptureProtocolBase

**继承自**: `UObject`

A capture protocol responsible for dealing with captured frames using some custom method (writing out to disk, streaming, etc)

A typical process for capture consits of the following process:
    Setup -> [ Warm up -> [ Capture Frame ] ] -> Begin Finalize -> [ HasFinishedProcessing ] -> Finalize

## 方法

### GetState
```angelscript
EMovieSceneCaptureProtocolState GetState()
```
Get the current state of this capture protocol

### IsCapturing
```angelscript
bool IsCapturing()
```
Check whether we can capture a frame from this protocol


# UReplaySubsystem

**继承自**: `UGameInstanceSubsystem`

## 属性

### bLoadDefaultMapOnStop
- **类型**: `bool`
- **描述**: Whether to reload the default map when StopReplay is called.

## 方法

### GetActiveReplayName
```angelscript
FString GetActiveReplayName()
```
Get current recording/playing replay name

@return FString Name of relpay (session id, file name, etc)

### GetReplayCurrentTime
```angelscript
float32 GetReplayCurrentTime()
```
Get current recording/playing replay time

@return float Current recording/playback time in seconds

### IsPlaying
```angelscript
bool IsPlaying()
```

### IsRecording
```angelscript
bool IsRecording()
```

### RequestCheckpoint
```angelscript
void RequestCheckpoint()
```
Request a checkpoint write, if currently recording.


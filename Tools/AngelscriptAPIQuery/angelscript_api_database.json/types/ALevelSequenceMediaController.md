# ALevelSequenceMediaController

**继承自**: `AActor`

Replicated actor class that is responsible for instigating various cinematic assets (Media, Audio, Level Sequences) in a synchronized fasion

## 属性

### ServerStartTimeSeconds
- **类型**: `float32`
- **描述**: Replicated time at which the server started the sequence (taken from AGameStateBase::GetServerWorldTimeSeconds)

### Sequence
- **类型**: `ALevelSequenceActor`

### MediaComponent
- **类型**: `UMediaComponent`

## 方法

### GetMediaComponent
```angelscript
UMediaComponent GetMediaComponent()
```
Access this actor's media component

### GetSequence
```angelscript
ALevelSequenceActor GetSequence()
```
Access this actor's Level Sequence Actor

### Play
```angelscript
void Play()
```

### SynchronizeToServer
```angelscript
void SynchronizeToServer(float32 DesyncThresholdSeconds)
```
Forcibly synchronize the sequence to the server's position if it has diverged by more than the specified threshold


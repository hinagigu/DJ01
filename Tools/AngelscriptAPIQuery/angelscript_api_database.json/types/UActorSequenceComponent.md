# UActorSequenceComponent

**继承自**: `UActorComponent`

Movie scene animation embedded within an actor.

## 属性

### PlaybackSettings
- **类型**: `FMovieSceneSequencePlaybackSettings`

### Sequence
- **类型**: `UActorSequence`
- **描述**: Embedded actor sequence data

### SequencePlayer
- **类型**: `UActorSequencePlayer`

## 方法

### PauseSequence
```angelscript
void PauseSequence()
```
Calls the Pause function on the SequencePlayer if its valid.

### PlaySequence
```angelscript
void PlaySequence()
```
Calls the Play function on the SequencePlayer if its valid.

### StopSequence
```angelscript
void StopSequence()
```
Calls the Stop function on the SequencePlayer if its valid.


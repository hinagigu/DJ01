# __SequenceRecorder

## 方法

### IsRecordingSequence
```angelscript
bool IsRecordingSequence()
```
Are we currently recording a sequence

### StartRecordingSequence
```angelscript
void StartRecordingSequence(TArray<AActor> ActorsToRecord)
```
Start recording the passed-in actors to a level sequence.
@param       ActorsToRecord  The actors to record

### StopRecordingSequence
```angelscript
void StopRecordingSequence()
```
Stop recording the current sequence, if any


# UTakeRecorderPanel

**继承自**: `UObject`

Take recorder UI panel interop object

## 方法

### CanStartRecording
```angelscript
bool CanStartRecording(FText& OutErrorText)
```
Whether the panel is ready to start recording

### ClearPendingTake
```angelscript
void ClearPendingTake()
```
* Clear the pending take level sequence

### GetFrameRate
```angelscript
FFrameRate GetFrameRate()
```
Access the frame rate for this take

### GetLastRecordedLevelSequence
```angelscript
ULevelSequence GetLastRecordedLevelSequence()
```
Access the last level sequence that was recorded

### GetLevelSequence
```angelscript
ULevelSequence GetLevelSequence()
```
Access the level sequence for this take

### GetMode
```angelscript
ETakeRecorderPanelMode GetMode()
```
Get the mode that the panel is currently in

### GetSources
```angelscript
UTakeRecorderSources GetSources()
```
Access the sources that are to be (or were) used for recording this take

### GetTakeMetaData
```angelscript
UTakeMetaData GetTakeMetaData()
```
Access take meta data for this take

### SetFrameRate
```angelscript
void SetFrameRate(FFrameRate InFrameRate)
```
Set the frame rate for this take

### SetFrameRateFromTimecode
```angelscript
void SetFrameRateFromTimecode(bool bInFromTimecode)
```
Set if the frame rate is set from the Timecode frame rate

### SetupForEditing
```angelscript
void SetupForEditing(UTakePreset TakePreset)
```
Setup this panel as an editor for the specified take preset asset.

### SetupForRecording_LevelSequence
```angelscript
void SetupForRecording_LevelSequence(ULevelSequence LevelSequenceAsset)
```
Setup this panel such that it is ready to start recording using the specified
level sequence asset as a template for the recording.

### SetupForRecording_TakePreset
```angelscript
void SetupForRecording_TakePreset(UTakePreset TakePresetAsset)
```
Setup this panel such that it is ready to start recording using the specified
take preset as a template for the recording.

### SetupForRecordingInto_LevelSequence
```angelscript
void SetupForRecordingInto_LevelSequence(ULevelSequence LevelSequenceAsset)
```
Setup this panel such that it is ready to start recording using the specified
level sequence asset to record into.

### SetupForViewing
```angelscript
void SetupForViewing(ULevelSequence LevelSequenceAsset)
```
Setup this panel as a viewer for a previously recorded take.

### StartRecording
```angelscript
void StartRecording()
```
Start recording with the current take

### StopRecording
```angelscript
void StopRecording()
```
Stop recording with the current take


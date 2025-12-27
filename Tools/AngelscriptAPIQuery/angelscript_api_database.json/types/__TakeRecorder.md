# __TakeRecorder

## 方法

### CancelRecording
```angelscript
void CancelRecording()
```
Cancel recording if there is a recorder currently active

### GetActiveRecorder
```angelscript
UTakeRecorder GetActiveRecorder()
```
Retrieve the currently active recorder, or None if there none are active

### GetDefaultParameters
```angelscript
FTakeRecorderParameters GetDefaultParameters()
```
Get the default recorder parameters according to the project and user settings

### GetTakeRecorderPanel
```angelscript
UTakeRecorderPanel GetTakeRecorderPanel()
```
Get the currently open take recorder panel, if one is open

### IsRecording
```angelscript
bool IsRecording()
```
Check whether a recording is currently active

### IsTakeRecorderEnabled
```angelscript
bool IsTakeRecorderEnabled()
```
Is the Take Recorder enabled in the build

### OpenTakeRecorderPanel
```angelscript
UTakeRecorderPanel OpenTakeRecorderPanel()
```
Get the currently open take recorder panel, if one is open, opening a new one if not

### SetDefaultParameters
```angelscript
void SetDefaultParameters(FTakeRecorderParameters DefaultParameters)
```
Set the default recorder parameters

### SetOnTakeRecorderPanelChanged
```angelscript
void SetOnTakeRecorderPanelChanged(FOnTakeRecorderPanelChanged OnTakeRecorderPanelChanged)
```
Called when a Take Panel is constructed or destroyed.

### StartRecording
```angelscript
UTakeRecorder StartRecording(ULevelSequence LevelSequence, UTakeRecorderSources Sources, UTakeMetaData MetaData, FTakeRecorderParameters Parameters)
```
Start a new recording using the specified parameters. Will fail if a recording is currently in progress

@param LevelSequence         The base level sequence to use for the recording. Will be played back during the recording and duplicated to create the starting point for the resulting asset.
@param Sources               The sources to use for the recording
@param MetaData              Meta-data pertaining to this recording, duplicated into the resulting recorded sequence
@param Parameters            Configurable parameters for this recorder instance
@return The recorder responsible for the recording, or None if a a recording could not be started

### StopRecording
```angelscript
void StopRecording()
```
Stop recording if there is a recorder currently active


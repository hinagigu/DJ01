# UTakeMetaData

**继承自**: `UObject`

Take meta-data that is stored on ULevelSequence assets that are recorded through the Take Recorder.
Meta-data is retrieved through ULevelSequence::FindMetaData<UTakeMetaData>()

## 方法

### GenerateAssetPath
```angelscript
FString GenerateAssetPath(FString PathFormatString)
```
Generate the desired asset path for this take meta-data

### GetDescription
```angelscript
FString GetDescription()
```
@return The user-provided description for this take

### GetDuration
```angelscript
FFrameTime GetDuration()
```
@return The duration for this take

### GetFrameRate
```angelscript
FFrameRate GetFrameRate()
```
@return The frame-rate for this take

### GetFrameRateFromTimecode
```angelscript
bool GetFrameRateFromTimecode()
```
@return Get if we get frame rate from time code

### GetLevelOrigin
```angelscript
ULevel GetLevelOrigin()
```
@return The Map used to create this recording

### GetLevelPath
```angelscript
FString GetLevelPath()
```
@return The AssetPath of the Level used to create a Recorded Level Sequence

### GetPresetOrigin
```angelscript
UTakePreset GetPresetOrigin()
```
@return The preset on which the take was originally based

### GetSlate
```angelscript
FString GetSlate()
```
@return The slate for this take

### GetTakeNumber
```angelscript
int GetTakeNumber()
```
@return The take number for this take

### GetTimecodeIn
```angelscript
FTimecode GetTimecodeIn()
```
@return The timecode in for this take

### GetTimecodeOut
```angelscript
FTimecode GetTimecodeOut()
```
@return The timecode out for this take

### GetTimestamp
```angelscript
FDateTime GetTimestamp()
```
@return The timestamp for this take

### IsLocked
```angelscript
bool IsLocked()
```
Check whether this take is locked

### Lock
```angelscript
void Lock()
```
Lock this take, causing it to become read-only

### Recorded
```angelscript
bool Recorded()
```
Check if this take was recorded (as opposed
to being setup for recording)

### SetDescription
```angelscript
void SetDescription(FString InDescription)
```
Set this take's user-provided description
@note: Only valid for takes that have not been locked

### SetDuration
```angelscript
void SetDuration(FFrameTime InDuration)
```
Set this take's duration
@note: Only valid for takes that have not been locked

### SetFrameRate
```angelscript
void SetFrameRate(FFrameRate InFrameRate)
```
Set this take's frame-rate
@note: Only valid for takes that have not been locked

### SetFrameRateFromTimecode
```angelscript
void SetFrameRateFromTimecode(bool InFromTimecode)
```
Set if we get frame rate from time code

### SetLevelOrigin
```angelscript
void SetLevelOrigin(ULevel InLevelOrigin)
```
Set the map used to create this recording

### SetPresetOrigin
```angelscript
void SetPresetOrigin(UTakePreset InPresetOrigin)
```
Set the preset on which the take is based
@note: Only valid for takes that have not been locked

### SetSlate
```angelscript
void SetSlate(FString InSlate, bool bEmitChanged)
```
Set the slate for this take and reset its take number to 1
@param bEmitChanged Whether or not to send a slate changed event
@note: Only valid for takes that have not been locked

### SetTakeNumber
```angelscript
void SetTakeNumber(int InTakeNumber, bool bEmitChanged)
```
Set this take's take number. Take numbers are always clamped to be >= 1.
@param bEmitChanged Whether or not to send a take number changed event
@note: Only valid for takes that have not been locked

### SetTimecodeIn
```angelscript
void SetTimecodeIn(FTimecode InTimecodeIn)
```
Set this take's timecode in
@note: Only valid for takes that have not been locked

### SetTimecodeOut
```angelscript
void SetTimecodeOut(FTimecode InTimecodeOut)
```
Set this take's timecode out
@note: Only valid for takes that have not been locked

### SetTimestamp
```angelscript
void SetTimestamp(FDateTime InTimestamp)
```
Set this take's timestamp
@note: Only valid for takes that have not been locked

### Unlock
```angelscript
void Unlock()
```
Unlock this take if it is read-only, allowing it to be modified once again


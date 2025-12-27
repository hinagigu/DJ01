# __USequencerScriptingRangeExtensions

## 方法

### GetEndFrame
```angelscript
int GetEndFrame(FSequencerScriptingRange Range)
```
Get the ending frame for the specified range, if it has one. Defined as the first subsequent frame that is outside of the range.

@param Range       The range to get the end from

### GetEndSeconds
```angelscript
float32 GetEndSeconds(FSequencerScriptingRange Range)
```
Get the ending time for the specified range in seconds, if it has one. Defined as the first time that is outside of the range.

@param Range       The range to get the end from

### GetStartFrame
```angelscript
int GetStartFrame(FSequencerScriptingRange Range)
```
Get the starting frame for the specified range, if it has one. Defined as the first valid frame that is inside the range.

@param Range       The range to get the start from

### GetStartSeconds
```angelscript
float32 GetStartSeconds(FSequencerScriptingRange Range)
```
Get the starting time for the specified range in seconds, if it has one. Defined as the first valid time that is inside the range.

@param Range       The range to get the start from

### HasEnd
```angelscript
bool HasEnd(FSequencerScriptingRange Range)
```
Check whether this range has an end

@param Range       The range to check

### HasStart
```angelscript
bool HasStart(FSequencerScriptingRange Range)
```
Check whether this range has a start

@param Range       The range to check

### RemoveEnd
```angelscript
void RemoveEnd(FSequencerScriptingRange& Range)
```
Remove the end from this range, making it infinite

@param Range       The range to remove the end from

### RemoveStart
```angelscript
void RemoveStart(FSequencerScriptingRange& Range)
```
Remove the start from this range, making it infinite

@param Range       The range to remove the start from

### SetEndFrame
```angelscript
void SetEndFrame(FSequencerScriptingRange& Range, int End)
```
Set the ending frame for the specified range. Interpreted as the first subsequent frame that is outside of the range.

@param Range       The range to set the end on

### SetEndSeconds
```angelscript
void SetEndSeconds(FSequencerScriptingRange& Range, float32 End)
```
Set the ending time for the specified range in seconds. Interpreted as the first time that is outside of the range.

@param Range       The range to set the end on

### SetStartFrame
```angelscript
void SetStartFrame(FSequencerScriptingRange& Range, int Start)
```
Set the starting frame for the specified range. Interpreted as the first valid frame that is inside the range.

@param Range       The range to set the start on

### SetStartSeconds
```angelscript
void SetStartSeconds(FSequencerScriptingRange& Range, float32 Start)
```
Set the starting time for the specified range in seconds. Interpreted as the first valid time that is inside the range.

@param Range       The range to set the start on

### StaticClass
```angelscript
UClass StaticClass()
```


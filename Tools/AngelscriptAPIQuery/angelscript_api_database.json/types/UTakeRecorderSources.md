# UTakeRecorderSources

**继承自**: `UObject`

A list of sources to record for any given take. Stored as meta-data on ULevelSequence through ULevelSequence::FindMetaData<UTakeRecorderSources>

## 方法

### AddSource
```angelscript
UTakeRecorderSource AddSource(TSubclassOf<UTakeRecorderSource> InSourceType)
```
Add a new source to this source list of the templated type

@param InSourceType    The class type of the source to add
@return An instance of the specified source type

### GetSourcesCopy
```angelscript
TArray<UTakeRecorderSource> GetSourcesCopy()
```
Retrieves a copy of the list of sources that are being recorded. This is intended for Blueprint usages which cannot
use TArrayView.
DO NOT MODIFY THIS ARRAY, modifications will be lost.

### RemoveSource
```angelscript
void RemoveSource(UTakeRecorderSource InSource)
```
Remove the specified source from this list

@param InSource        The source to remove

### StartRecordingSource
```angelscript
void StartRecordingSource(TArray<UTakeRecorderSource> InSources, FQualifiedFrameTime CurrentFrameTime)
```
Calls the recording initialization flows on each of the specified sources.


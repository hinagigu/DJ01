# USequenceRecorderActorGroup

**继承自**: `UObject`

## 属性

### GroupName
- **类型**: `FName`

### SequenceName
- **类型**: `FString`
- **描述**: The base name of the sequence to record to. This name will also be used to auto-generate any assets created by this recording.

### SequenceRecordingBasePath
- **类型**: `FDirectoryPath`
- **描述**: Base path for this recording. Sub-assets will be created in subdirectories as specified

### bSpecifyTargetLevelSequence
- **类型**: `bool`
- **描述**: Whether we should specify the target level sequence or auto-create it

### TargetLevelSequence
- **类型**: `ULevelSequence`
- **描述**: The level sequence to record into

### bDuplicateTargetLevelSequence
- **类型**: `bool`
- **描述**: Whether we should duplicate the target level sequence and record into the duplicate

### bRecordTargetLevelSequenceLength
- **类型**: `bool`
- **描述**: Whether we should record to the length of the target level sequence


# USequenceRecorderSettings

**继承自**: `UObject`

## 属性

### bCreateLevelSequence
- **类型**: `bool`
- **描述**: Whether to create a level sequence when recording. Actors and animations will be inserted into this sequence

### bImmersiveMode
- **类型**: `bool`
- **描述**: Whether to maximize the viewport when recording

### SequenceLength
- **类型**: `float32`
- **描述**: The length of the recorded sequence

### RecordingDelay
- **类型**: `float32`
- **描述**: Delay that we will use before starting recording

### bAllowLooping
- **类型**: `bool`
- **描述**: Allow the recording to be looped. Subsequence recorded assets will be saved to unique filenames.

### GlobalTimeDilation
- **类型**: `float32`
- **描述**: Global Time dilation to set the world to when recording starts. Useful for playing back a scene in slow motion.

### bIgnoreTimeDilation
- **类型**: `bool`
- **描述**: Should Sequence Recorder ignore global time dilation? If true recorded animations will only be as long as they would have been without global time dilation.

### AnimationSubDirectory
- **类型**: `FString`
- **描述**: The name of the subdirectory animations will be placed in. Leave this empty to place into the same directory as the sequence base path

### RecordAudio
- **类型**: `EAudioRecordingMode`
- **描述**: Whether to record audio alongside animation or not

### AudioGain
- **类型**: `float32`
- **描述**: Gain in decibels to apply to recorded audio

### bSplitAudioChannelsIntoSeparateTracks
- **类型**: `bool`
- **描述**: Whether or not to split mic channels into separate audio tracks. If not true, a max of 2 input channels is supported.

### bReplaceRecordedAudio
- **类型**: `bool`
- **描述**: Replace existing recorded audio with any newly recorded audio

### AudioTrackName
- **类型**: `FText`
- **描述**: Name of the recorded audio track name

### AudioSubDirectory
- **类型**: `FString`
- **描述**: The name of the subdirectory audio will be placed in. Leave this empty to place into the same directory as the sequence base path

### bRecordNearbySpawnedActors
- **类型**: `bool`
- **描述**: Whether to record nearby spawned actors. If an actor matches a class in the ActorFilter, this state will be bypassed.

### NearbyActorRecordingProximity
- **类型**: `float32`
- **描述**: Proximity to currently recorded actors to record newly spawned actors.

### bRecordWorldSettingsActor
- **类型**: `bool`
- **描述**: Whether to record the world settings actor in the sequence (some games use this to attach world SFX)

### bReduceKeys
- **类型**: `bool`
- **描述**: Whether to remove keyframes within a tolerance from the recorded tracks

### bAutoSaveAsset
- **类型**: `bool`
- **描述**: Whether to auto-save asset when recording is completed. Defaults to false

### ActorFilter
- **类型**: `FSequenceRecorderActorFilter`
- **描述**: Filter to check spawned actors against to see if they should be recorded

### DefaultAnimationSettings
- **类型**: `FAnimationRecordingSettings`
- **描述**: Default animation settings which are used to initialize all new actor recording's animation settings

### bRecordSequencerSpawnedActors
- **类型**: `bool`
- **描述**: Whether to record actors that are spawned by sequencer itself (this is usually disabled as results can be unexpected)

### ClassesAndPropertiesToRecord
- **类型**: `TArray<FPropertiesToRecordForClass>`
- **描述**: The properties to record for specified classes. Component classes specified here will be recorded. If an actor does not contain one of these classes it will be ignored.

### ActorsAndPropertiesToRecord
- **类型**: `TArray<FPropertiesToRecordForActorClass>`
- **描述**: The properties to record for specified actors. Actor classes specified here will be recorded. If an actor does not contain one of these properties it will be ignored.

### PerActorSettings
- **类型**: `TArray<FSettingsForActorClass>`
- **描述**: Settings applied to actors of a specified class


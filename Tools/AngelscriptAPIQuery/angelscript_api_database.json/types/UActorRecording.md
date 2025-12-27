# UActorRecording

**继承自**: `USequenceRecordingBase`

## 属性

### ActorSettings
- **类型**: `FActorRecordingSettings`

### bActive
- **类型**: `bool`
- **描述**: Whether this actor is active and to be recorded when the 'Record' button is pressed.

### bCreateLevelSequence
- **类型**: `bool`
- **描述**: Whether to create a level sequence for this actor recording

### TargetLevelSequence
- **类型**: `ULevelSequence`
- **描述**: The level sequence to record into

### TargetName
- **类型**: `FText`
- **描述**: Optional target name to record to. If not specified, the actor label will be used

### TakeNumber
- **类型**: `uint`
- **描述**: Specify the take number for the new recording

### bSpecifyTargetAnimation
- **类型**: `bool`
- **描述**: Whether we should specify the target animation or auto-create it

### TargetAnimation
- **类型**: `UAnimSequence`
- **描述**: The target animation we want to record to

### AnimationSettings
- **类型**: `FAnimationRecordingSettings`
- **描述**: The settings to apply to this actor's animation

### bRecordToPossessable
- **类型**: `bool`
- **描述**: Whether to record to 'possessable' (i.e. level-owned) or 'spawnable' (i.e. sequence-owned) actors. Defaults to the global setting.

### ActorToRecord
- **类型**: `TSoftObjectPtr<AActor>`
- **描述**: The actor we want to record


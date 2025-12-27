# ULevelSequenceBurnIn

**继承自**: `UUserWidget`

Base class for level sequence burn ins

## 属性

### FrameInformation
- **类型**: `FLevelSequencePlayerSnapshot`
- **描述**: Snapshot of frame information.

### LevelSequenceActor
- **类型**: `ALevelSequenceActor`
- **描述**: The actor to get our burn in frames from

## 方法

### GetSettingsClass
```angelscript
TSubclassOf<ULevelSequenceBurnInInitSettings> GetSettingsClass()
```
Get the settings class to use for this burn in

### SetSettings
```angelscript
void SetSettings(UObject InSettings)
```
Called when this burn in is receiving its settings


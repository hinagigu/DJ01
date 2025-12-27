# FDialogueContextMapping

## 属性

### Context
- **类型**: `FDialogueContext`
- **描述**: The context of the dialogue.

### SoundWave
- **类型**: `USoundWave`
- **描述**: The soundwave to play for this dialogue.

### LocalizationKeyFormat
- **类型**: `FString`
- **描述**: The format string to use when generating the localization key for this context. This must be unique within the owner dialogue wave.
Available format markers:
  * {ContextHash} - A hash generated from the speaker and target voices.

## 方法

### opAssign
```angelscript
FDialogueContextMapping& opAssign(FDialogueContextMapping Other)
```


# USubmixEffectDynamicsProcessorPreset

**继承自**: `USoundEffectSubmixPreset`

## 属性

### Settings
- **类型**: `FSubmixEffectDynamicsProcessorSettings`

## 方法

### ResetKey
```angelscript
void ResetKey()
```

### SetAudioBus
```angelscript
void SetAudioBus(UAudioBus AudioBus)
```
Sets the source key input as the provided AudioBus' output.  If no object is provided, key is set
to effect's input.

### SetExternalSubmix
```angelscript
void SetExternalSubmix(USoundSubmix Submix)
```
Sets the source key input as the provided Submix's output.  If no object is provided, key is set
to effect's input.

### SetSettings
```angelscript
void SetSettings(FSubmixEffectDynamicsProcessorSettings Settings)
```


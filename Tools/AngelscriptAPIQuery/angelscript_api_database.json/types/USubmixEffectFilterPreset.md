# USubmixEffectFilterPreset

**继承自**: `USoundEffectSubmixPreset`

USubmixEffectFilterPreset
Class which processes audio streams and uses parameters defined in the preset class.

## 属性

### Settings
- **类型**: `FSubmixEffectFilterSettings`

## 方法

### SetFilterAlgorithm
```angelscript
void SetFilterAlgorithm(ESubmixFilterAlgorithm InAlgorithm)
```
Sets the filter algorithm

### SetFilterCutoffFrequency
```angelscript
void SetFilterCutoffFrequency(float32 InFrequency)
```
Sets the base filter cutoff frequency

### SetFilterCutoffFrequencyMod
```angelscript
void SetFilterCutoffFrequencyMod(float32 InFrequency)
```
Sets the mod filter cutoff frequency

### SetFilterQ
```angelscript
void SetFilterQ(float32 InQ)
```
Sets the filter Q

### SetFilterQMod
```angelscript
void SetFilterQMod(float32 InQ)
```
Sets the filter Q

### SetFilterType
```angelscript
void SetFilterType(ESubmixFilterType InType)
```
Sets the filter type

### SetSettings
```angelscript
void SetSettings(FSubmixEffectFilterSettings InSettings)
```
Set all filter effect settings


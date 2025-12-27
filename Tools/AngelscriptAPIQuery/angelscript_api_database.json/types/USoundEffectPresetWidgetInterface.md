# USoundEffectPresetWidgetInterface

**继承自**: `UAudioPanelWidgetInterface`

## 方法

### GetClass
```angelscript
TSubclassOf<USoundEffectPreset> GetClass()
```
Returns the class of Preset the widget supports

### OnConstructed
```angelscript
void OnConstructed(USoundEffectPreset Preset)
```
Called when the preset widget is constructed

### OnPropertyChanged
```angelscript
void OnPropertyChanged(USoundEffectPreset Preset, FName PropertyName)
```
Called when the preset object is changed


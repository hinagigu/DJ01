# USourceEffectMotionFilterPreset

**继承自**: `USoundEffectSourcePreset`

USourceEffectMotionFilterPreset
This code exposes your preset settings and effect class to the editor.
And allows for a handle to setting/updating effect settings dynamically.

## 属性

### Settings
- **类型**: `FSourceEffectMotionFilterSettings`

## 方法

### SetSettings
```angelscript
void SetSettings(FSourceEffectMotionFilterSettings InSettings)
```
Change settings of your effect from blueprints. Will broadcast changes to active instances.


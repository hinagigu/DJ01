# AAudioVolume

**继承自**: `AVolume`

## 属性

### Settings
- **类型**: `FReverbSettings`

### AmbientZoneSettings
- **类型**: `FInteriorSettings`

### Priority
- **类型**: `float32`

### bEnabled
- **类型**: `bool`

### SubmixSendSettings
- **类型**: `TArray<FAudioVolumeSubmixSendSettings>`

### SubmixOverrideSettings
- **类型**: `TArray<FAudioVolumeSubmixOverrideSettings>`

## 方法

### SetEnabled
```angelscript
void SetEnabled(bool bNewEnabled)
```

### SetInteriorSettings
```angelscript
void SetInteriorSettings(FInteriorSettings NewInteriorSettings)
```

### SetPriority
```angelscript
void SetPriority(float32 NewPriority)
```

### SetReverbSettings
```angelscript
void SetReverbSettings(FReverbSettings NewReverbSettings)
```

### SetSubmixOverrideSettings
```angelscript
void SetSubmixOverrideSettings(TArray<FAudioVolumeSubmixOverrideSettings> NewSubmixOverrideSettings)
```

### SetSubmixSendSettings
```angelscript
void SetSubmixSendSettings(TArray<FAudioVolumeSubmixSendSettings> NewSubmixSendSettings)
```


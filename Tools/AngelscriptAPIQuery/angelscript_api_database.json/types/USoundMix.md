# USoundMix

**继承自**: `UObject`

## 属性

### EQPriority
- **类型**: `float32`

### EQSettings
- **类型**: `FAudioEQEffect`

### SoundClassEffects
- **类型**: `TArray<FSoundClassAdjuster>`

### InitialDelay
- **类型**: `float32`
- **描述**: Initial delay in seconds before the mix is applied.

### FadeInTime
- **类型**: `float32`
- **描述**: Time taken in seconds for the mix to fade in.

### Duration
- **类型**: `float32`
- **描述**: Duration of mix, negative means it will be applied until another mix is set.

### FadeOutTime
- **类型**: `float32`
- **描述**: Time taken in seconds for the mix to fade out.

### bApplyEQ
- **类型**: `bool`


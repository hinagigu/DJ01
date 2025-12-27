# USoundBase

**继承自**: `UObject`

The base class for a playable sound object

## 属性

### SoundClassObject
- **类型**: `USoundClass`

### VirtualizationMode
- **类型**: `EVirtualizationMode`

### ConcurrencySet
- **类型**: `TSet<TObjectPtr<USoundConcurrency>>`

### ConcurrencyOverrides
- **类型**: `FSoundConcurrencySettings`

### Duration
- **类型**: `float32`
- **描述**: Duration of sound in seconds.

### MaxDistance
- **类型**: `float32`
- **描述**: The max distance of the asset, as determined by attenuation settings.

### TotalSamples
- **类型**: `float32`
- **描述**: Total number of samples (in the thousands). Useful as a metric to analyze the relative size of a given sound asset in content browser.

### Priority
- **类型**: `float32`

### AttenuationSettings
- **类型**: `USoundAttenuation`
- **描述**: Attenuation settings package for the sound

### SoundSubmixObject
- **类型**: `USoundSubmixBase`

### SoundSubmixSends
- **类型**: `TArray<FSoundSubmixSendInfo>`

### SourceEffectChain
- **类型**: `USoundEffectSourcePresetChain`

### BusSends
- **类型**: `TArray<FSoundSourceBusSendInfo>`

### PreEffectBusSends
- **类型**: `TArray<FSoundSourceBusSendInfo>`

### AssetUserData
- **类型**: `TArray<TObjectPtr<UAssetUserData>>`
- **描述**: Array of user data stored with the asset

### AudioPropertiesSheet
- **类型**: `UAudioPropertiesSheetAssetBase`

### AudioPropertiesBindings
- **类型**: `UAudioPropertiesBindings`

### bDebug
- **类型**: `bool`

### bOverrideConcurrency
- **类型**: `bool`

### bEnableBusSends
- **类型**: `bool`

### bEnableBaseSubmix
- **类型**: `bool`

### bEnableSubmixSends
- **类型**: `bool`

### bBypassVolumeScaleForPriority
- **类型**: `bool`


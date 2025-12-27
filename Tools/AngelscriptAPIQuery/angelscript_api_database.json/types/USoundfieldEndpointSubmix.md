# USoundfieldEndpointSubmix

**继承自**: `USoundSubmixBase`

Sound Submix class meant for sending soundfield-encoded audio to an external endpoint, such as a hardware binaural renderer that supports ambisonics.

## 属性

### SoundfieldEndpointType
- **类型**: `FName`
- **描述**: Currently used format.

### EndpointSettings
- **类型**: `USoundfieldEndpointSettingsBase`

### EncodingSettings
- **类型**: `USoundfieldEncodingSettingsBase`

### SoundfieldEffectChain
- **类型**: `TArray<TObjectPtr<USoundfieldEffectBase>>`


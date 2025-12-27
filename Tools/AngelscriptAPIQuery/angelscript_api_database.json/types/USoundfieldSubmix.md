# USoundfieldSubmix

**继承自**: `USoundSubmixWithParentBase`

Sound Submix class meant for use with soundfield formats, such as Ambisonics.

## 属性

### SoundfieldEncodingFormat
- **类型**: `FName`
- **描述**: Currently used format.

### EncodingSettings
- **类型**: `USoundfieldEncodingSettingsBase`
- **描述**: Which encoding settings to use the sound field.

### SoundfieldEffectChain
- **类型**: `TArray<TObjectPtr<USoundfieldEffectBase>>`
- **描述**: Soundfield effect chain to use for the sound field.


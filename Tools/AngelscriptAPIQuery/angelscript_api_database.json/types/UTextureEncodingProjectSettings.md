# UTextureEncodingProjectSettings

**继承自**: `UDeveloperSettings`

Encoding can either use the "Final" or "Fast" speeds, for supported encoders (e.g. Oodle)
Encode speed settings have no effect on encoders that don't support encode speed, currently limited to Oodle.

## 属性

### FinalRDOLambda
- **类型**: `int8`
- **描述**: Ignored if UsesRDO is false. This value is used if a given texture is using "Default" LossyCompressionAmount.
Otherwise, the value of LossyCompressionAmount is translated in to a fixed lambda (see UsesRDO tooltip).

Low values (1) represent highest quality (least distortion) results.

### FinalEffortLevel
- **类型**: `ETextureEncodeEffort`
- **描述**: Specifies how much time to take trying for better encoding results.

### FinalUniversalTiling
- **类型**: `ETextureUniversalTiling`
- **描述**: Specifies how to assume textures are laid out on disc. This only applies to Oodle with RDO
enabled. 256 KB is a good middle ground. Enabling this will decrease the on-disc
sizes of textures for platforms with exposed texture tiling (i.e. consoles), but will slightly increase
sizes of textures for platforms with opaque tiling (i.e. desktop).

### FastRDOLambda
- **类型**: `int8`
- **描述**: Ignored if UsesRDO is false. This value is used if a given texture is using "Default" LossyCompressionAmount.
Otherwise, the value of LossyCompressionAmount is translated in to a fixed lambda (see UsesRDO tooltip).

Low values (1) represent highest quality (least distortion) results.

### FastEffortLevel
- **类型**: `ETextureEncodeEffort`
- **描述**: Specifies how much time to take trying for better encode results.

### FastUniversalTiling
- **类型**: `ETextureUniversalTiling`
- **描述**: Specifies how to assume textures are laid out on disc. This only applies to Oodle with RDO
enabled. 256 KB is a good middle ground. Enabling this will decrease the on-disc
sizes of textures for platforms with exposed texture tiling (i.e. consoles), but will slightly increase
sizes of textures for platforms with opaque tiling (i.e. desktop).

### CookUsesSpeed
- **类型**: `ETextureEncodeSpeed`
- **描述**: Which encode speed non interactive editor sessions will use (i.e. commandlets)

### EditorUsesSpeed
- **类型**: `ETextureEncodeSpeed`
- **描述**: Which encode speed everything else uses.

### bSharedLinearTextureEncoding
- **类型**: `bool`

### bFinalUsesRDO
- **类型**: `bool`

### bFastUsesRDO
- **类型**: `bool`


# UMaterialEditorInstanceConstant

**继承自**: `UObject`

## 属性

### PhysMaterial
- **类型**: `UPhysicalMaterial`
- **描述**: Physical material to use for this graphics material. Used for sounds, effects etc.

### Parent
- **类型**: `UMaterialInterface`
- **描述**: since the Parent may point across levels and the property editor needs to import this text, it must be marked lazy so it doesn't set itself to NULL in FindImportedObject

### ParameterGroups
- **类型**: `TArray<FEditorParameterGroup>`

### RefractionDepthBias
- **类型**: `float32`
- **描述**: This is the refraction depth bias, larger values offset distortion to prevent closer objects from rendering into the distorted surface at acute viewing angles but increases the disconnect between surface and where the refraction starts.

### SubsurfaceProfile
- **类型**: `USubsurfaceProfile`

### BasePropertyOverrides
- **类型**: `FMaterialInstanceBasePropertyOverrides`

### LightmassSettings
- **类型**: `FLightmassParameterizedMaterialSettings`
- **描述**: The Lightmass override settings for this object.

### NaniteOverrideMaterial
- **类型**: `UMaterialInterface`
- **描述**: An override material which will be used instead of this one when rendering with nanite.

### bOverrideSubsurfaceProfile
- **类型**: `bool`

### bUseOldStyleMICEditorGroups
- **类型**: `bool`

### bNaniteOverride
- **类型**: `bool`


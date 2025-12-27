# FLightmassParameterizedMaterialSettings

Structure for 'parameterized' Lightmass settings

## 属性

### CastShadowAsMasked
- **类型**: `FLightmassBooleanParameterValue`
- **描述**: If true, forces translucency to cast static shadows as if the material were masked.

### EmissiveBoost
- **类型**: `FLightmassScalarParameterValue`
- **描述**: Scales the emissive contribution of this material to static lighting.

### DiffuseBoost
- **类型**: `FLightmassScalarParameterValue`
- **描述**: Scales the diffuse contribution of this material to static lighting.

### ExportResolutionScale
- **类型**: `FLightmassScalarParameterValue`
- **描述**: Scales the resolution that this material's attributes were exported at.
This is useful for increasing material resolution when details are needed.

## 方法

### opAssign
```angelscript
FLightmassParameterizedMaterialSettings& opAssign(FLightmassParameterizedMaterialSettings Other)
```


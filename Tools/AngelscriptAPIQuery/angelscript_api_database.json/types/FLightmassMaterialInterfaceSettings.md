# FLightmassMaterialInterfaceSettings

UMaterial interface settings for Lightmass

## 属性

### DiffuseBoost
- **类型**: `float32`
- **描述**: Scales the diffuse contribution of this material to static lighting.

### ExportResolutionScale
- **类型**: `float32`
- **描述**: Scales the resolution that this material's attributes were exported at.
This is useful for increasing material resolution when details are needed.

### bCastShadowAsMasked
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FLightmassMaterialInterfaceSettings& opAssign(FLightmassMaterialInterfaceSettings Other)
```


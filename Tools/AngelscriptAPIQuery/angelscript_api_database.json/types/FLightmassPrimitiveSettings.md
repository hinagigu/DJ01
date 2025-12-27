# FLightmassPrimitiveSettings

Per-object settings for Lightmass

## 属性

### EmissiveBoost
- **类型**: `float32`
- **描述**: Scales the emissive contribution of all materials applied to this object.

### DiffuseBoost
- **类型**: `float32`
- **描述**: Scales the diffuse contribution of all materials applied to this object.

### FullyOccludedSamplesFraction
- **类型**: `float32`
- **描述**: Fraction of samples taken that must be occluded in order to reach full occlusion.

### bUseTwoSidedLighting
- **类型**: `bool`

### bShadowIndirectOnly
- **类型**: `bool`

### bUseEmissiveForStaticLighting
- **类型**: `bool`

### bUseVertexNormalForHemisphereGather
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FLightmassPrimitiveSettings& opAssign(FLightmassPrimitiveSettings Other)
```


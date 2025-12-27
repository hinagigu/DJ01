# FMaterialInstanceBasePropertyOverrides

Properties from the base material that can be overridden in material instances.

## 属性

### BlendMode
- **类型**: `EBlendMode`
- **描述**: The blend mode

### ShadingModel
- **类型**: `EMaterialShadingModel`
- **描述**: The shading model

### OpacityMaskClipValue
- **类型**: `float32`
- **描述**: If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue.

### DisplacementScaling
- **类型**: `FDisplacementScaling`

### MaxWorldPositionOffsetDisplacement
- **类型**: `float32`
- **描述**: The maximum World Position Offset distance. Zero means no maximum.

### bOverride_OpacityMaskClipValue
- **类型**: `bool`

### bOverride_BlendMode
- **类型**: `bool`

### bOverride_ShadingModel
- **类型**: `bool`

### bOverride_DitheredLODTransition
- **类型**: `bool`

### bOverride_CastDynamicShadowAsMasked
- **类型**: `bool`

### bOverride_TwoSided
- **类型**: `bool`

### bOverride_bIsThinSurface
- **类型**: `bool`

### bOverride_OutputTranslucentVelocity
- **类型**: `bool`

### bOverride_bHasPixelAnimation
- **类型**: `bool`

### bOverride_bEnableTessellation
- **类型**: `bool`

### bOverride_DisplacementScaling
- **类型**: `bool`

### bOverride_MaxWorldPositionOffsetDisplacement
- **类型**: `bool`

### TwoSided
- **类型**: `bool`

### bIsThinSurface
- **类型**: `bool`

### DitheredLODTransition
- **类型**: `bool`

### bCastDynamicShadowAsMasked
- **类型**: `bool`

### bOutputTranslucentVelocity
- **类型**: `bool`

### bHasPixelAnimation
- **类型**: `bool`

### bEnableTessellation
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMaterialInstanceBasePropertyOverrides& opAssign(FMaterialInstanceBasePropertyOverrides Other)
```


# FNiagaraRibbonUVSettings

Defines settings for UV behavior for a UV channel on ribbons.

## 属性

### DistributionMode
- **类型**: `ENiagaraRibbonUVDistributionMode`
- **描述**: Specifies how ribbon UVs are distributed along the length of a ribbon.

### LeadingEdgeMode
- **类型**: `ENiagaraRibbonUVEdgeMode`
- **描述**: Specifies how UVs transition into life at the leading edge of the ribbon.

### TrailingEdgeMode
- **类型**: `ENiagaraRibbonUVEdgeMode`
- **描述**: Specifies how UVs transition out of life at the trailing edge of the ribbon.

### TilingLength
- **类型**: `float32`
- **描述**: Specifies the length in world units to use when tiling UVs across the ribbon when using one of the tiled distribution modes.

### Offset
- **类型**: `FVector2D`
- **描述**: Specifies an additional offset which is applied to the UV range

### Scale
- **类型**: `FVector2D`
- **描述**: Specifies an additional scaler which is applied to the UV range.

### bEnablePerParticleUOverride
- **类型**: `bool`

### bEnablePerParticleVRangeOverride
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraRibbonUVSettings& opAssign(FNiagaraRibbonUVSettings Other)
```


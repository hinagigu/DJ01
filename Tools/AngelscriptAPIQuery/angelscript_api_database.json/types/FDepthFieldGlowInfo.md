# FDepthFieldGlowInfo

Info for glow when using depth field rendering

## 属性

### GlowColor
- **类型**: `FLinearColor`
- **描述**: Base color to use for the glow

### GlowOuterRadius
- **类型**: `FVector2D`
- **描述**: If bEnableGlow, outline glow outer radius (0 to 1, 0.5 is edge of character silhouette)
glow influence will be 0 at GlowOuterRadius.X and 1 at GlowOuterRadius.Y

### GlowInnerRadius
- **类型**: `FVector2D`
- **描述**: If bEnableGlow, outline glow inner radius (0 to 1, 0.5 is edge of character silhouette)
glow influence will be 1 at GlowInnerRadius.X and 0 at GlowInnerRadius.Y

### bEnableGlow
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FDepthFieldGlowInfo& opAssign(FDepthFieldGlowInfo Other)
```


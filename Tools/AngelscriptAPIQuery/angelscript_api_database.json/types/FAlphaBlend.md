# FAlphaBlend

Alpha Blend class that supports different blend options as well as custom curves

## 属性

### CustomCurve
- **类型**: `UCurveFloat`
- **描述**: If you're using Custom BlendOption, you can specify curve

### BlendTime
- **类型**: `float32`
- **描述**: Blend Time

### BlendOption
- **类型**: `EAlphaBlendOption`
- **描述**: Type of blending used (Linear, Cubic, etc.)

## 方法

### opAssign
```angelscript
FAlphaBlend& opAssign(FAlphaBlend Other)
```


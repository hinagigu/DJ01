# UCurveLinearColorAtlas

**继承自**: `UTexture2D`

Manages gradient LUT textures for registered actors and assigns them to the corresponding materials on the actor

## 属性

### TextureSize
- **类型**: `uint`

### TextureHeight
- **类型**: `uint`

### GradientCurves
- **类型**: `TArray<TObjectPtr<UCurveLinearColor>>`
- **描述**: Height of the lookup textures

### bSquareResolution
- **类型**: `bool`

### bDisableAllAdjustments
- **类型**: `bool`

## 方法

### GetCurvePosition
```angelscript
bool GetCurvePosition(UCurveLinearColor InCurve, float32& Position)
```


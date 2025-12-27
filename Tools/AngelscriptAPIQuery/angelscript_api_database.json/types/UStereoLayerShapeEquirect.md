# UStereoLayerShapeEquirect

**继承自**: `UStereoLayerShape`

## 属性

### LeftUVRect
- **类型**: `FBox2D`

### RightUVRect
- **类型**: `FBox2D`

### LeftScale
- **类型**: `FVector2D`

### RightScale
- **类型**: `FVector2D`

### LeftBias
- **类型**: `FVector2D`

### RightBias
- **类型**: `FVector2D`

### Radius
- **类型**: `float32`

## 方法

### SetEquirectProps
```angelscript
void SetEquirectProps(FEquirectProps InScaleBiases)
```
Set Equirect layer properties: UVRect, Scale, and Bias
@param       LeftScale: Scale for left eye
@param       LeftBias: Bias for left eye
@param       RightScale: Scale for right eye
@param       RightBias: Bias for right eye
@param       Radius: Sphere radius


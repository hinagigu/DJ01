# UBillboardComponent

**继承自**: `UPrimitiveComponent`

A 2d texture that will be rendered always facing the camera.

## 属性

### ScreenSize
- **类型**: `float32`

### U
- **类型**: `float32`

### UL
- **类型**: `float32`

### V
- **类型**: `float32`

### VL
- **类型**: `float32`

### bUseInEditorScaling
- **类型**: `bool`

### Sprite
- **类型**: `UTexture2D`

### bIsScreenSizeScaled
- **类型**: `bool`

### OpacityMaskRefVal
- **类型**: `float32`

## 方法

### SetOpacityMaskRefVal
```angelscript
void SetOpacityMaskRefVal(float32 RefVal)
```
Changed the opacity masked used by this component

### SetSprite
```angelscript
void SetSprite(UTexture2D NewSprite)
```
Change the sprite texture used by this component

### SetSpriteAndUV
```angelscript
void SetSpriteAndUV(UTexture2D NewSprite, int NewU, int NewUL, int NewV, int NewVL)
```
Change the sprite texture and the UV's used by this component

### SetUV
```angelscript
void SetUV(int NewU, int NewUL, int NewV, int NewVL)
```
Change the sprite's UVs


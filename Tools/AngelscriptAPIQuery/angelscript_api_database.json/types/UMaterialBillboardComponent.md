# UMaterialBillboardComponent

**继承自**: `UPrimitiveComponent`

A 2d material that will be rendered always facing the camera.

## 属性

### Elements
- **类型**: `TArray<FMaterialSpriteElement>`

## 方法

### AddElement
```angelscript
void AddElement(UMaterialInterface Material, UCurveFloat DistanceToOpacityCurve, bool bSizeIsInScreenSpace, float32 BaseSizeX, float32 BaseSizeY, UCurveFloat DistanceToSizeCurve)
```
Adds an element to the sprite.

### SetElements
```angelscript
void SetElements(TArray<FMaterialSpriteElement> NewElements)
```
Set all elements of this material billboard component


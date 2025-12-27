# UCommonLazyImage

**继承自**: `UImage`

A special Image widget that can show unloaded images and takes care of the loading for you!

UCommonLazyImage is another wrapper for SLoadGuard, but it only handles image loading and
a throbber during loading.

If this class changes to show any text, by default it will have CoreStyle styling

## 属性

### bShowLoading
- **类型**: `bool`

### LoadingBackgroundBrush
- **类型**: `FSlateBrush`

### OnLoadingStateChanged
- **类型**: `FOnLoadGuardStateChangedDynamic`

## 方法

### IsLoading
```angelscript
bool IsLoading()
```

### SetBrushFromLazyDisplayAsset
```angelscript
void SetBrushFromLazyDisplayAsset(TSoftObjectPtr<UObject> LazyObject, bool bMatchTextureSize)
```
Set the brush from a string asset ref only - expects the referenced asset to be a texture or material.

### SetBrushFromLazyMaterial
```angelscript
void SetBrushFromLazyMaterial(TSoftObjectPtr<UMaterialInterface> LazyMaterial)
```
Set the brush from a lazy material asset pointer - will load the material as needed.

### SetBrushFromLazyTexture
```angelscript
void SetBrushFromLazyTexture(TSoftObjectPtr<UTexture2D> LazyTexture, bool bMatchSize)
```
Set the brush from a lazy texture asset pointer - will load the texture as needed.

### SetMaterialTextureParamName
```angelscript
void SetMaterialTextureParamName(FName TextureParamName)
```
Establishes the name of the texture parameter on the currently applied brush material to which textures should be applied.
Does nothing if the current brush resource object is not a material.

Note: that this is cleared out automatically if/when a new material is established on the brush.
You must call this function again after doing so if the new material has a texture param.


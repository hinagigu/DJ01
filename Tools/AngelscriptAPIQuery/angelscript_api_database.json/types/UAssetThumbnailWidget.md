# UAssetThumbnailWidget

**继承自**: `UWidget`

This widget can be given an asset and it will render its thumbnail. Editor-only.

## 属性

### AssetToShow
- **类型**: `FAssetData`
- **描述**: The asset of which to show the thumbnail.

### ThumbnailSettings
- **类型**: `FAssetThumbnailWidgetSettings`

## 方法

### GetResolution
```angelscript
FIntPoint GetResolution()
```
Gets the resolution of the rendered thumbnail.

### SetAsset
```angelscript
void SetAsset(FAssetData AssetData)
```

### SetAssetByObject
```angelscript
void SetAssetByObject(UObject Object)
```

### SetResolution
```angelscript
void SetResolution(FIntPoint InResolution)
```
Sets the resolution for the rendered thumbnail.

### SetThumbnailSettings
```angelscript
void SetThumbnailSettings(FAssetThumbnailWidgetSettings InThumbnailSettings)
```


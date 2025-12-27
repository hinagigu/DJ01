# ALandscapeBlueprintBrushBase

**继承自**: `AActor`

## 属性

### UpdateOnPropertyChange
- **类型**: `bool`

### AffectHeightmap
- **类型**: `bool`

### AffectWeightmap
- **类型**: `bool`

### AffectVisibilityLayer
- **类型**: `bool`

### AffectedWeightmapLayers
- **类型**: `TArray<FName>`

## 方法

### GetBlueprintRenderDependencies
```angelscript
void GetBlueprintRenderDependencies(TArray<UObject>& OutStreamableAssets)
```

### Initialize
```angelscript
void Initialize(FTransform InLandscapeTransform, FIntPoint InLandscapeSize, FIntPoint InLandscapeRenderTargetSize)
```

### RenderLayer
```angelscript
UTextureRenderTarget2D RenderLayer(FLandscapeBrushParameters InParameters)
```

### RequestLandscapeUpdate
```angelscript
void RequestLandscapeUpdate(bool bInUserTriggered)
```


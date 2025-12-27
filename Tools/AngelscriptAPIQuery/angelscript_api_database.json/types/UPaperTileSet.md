# UPaperTileSet

**继承自**: `UObject`

A tile set is a collection of tiles pulled from a texture that can be used to fill out a tile map.

@see UPaperTileMap, UPaperTileMapComponent

## 属性

### TileSize
- **类型**: `FIntPoint`

### TileSheet
- **类型**: `UTexture2D`

### AdditionalSourceTextures
- **类型**: `TArray<TObjectPtr<UTexture>>`
- **描述**: Additional source textures for other slots

### BorderMargin
- **类型**: `FIntMargin`

### PerTileSpacing
- **类型**: `FIntPoint`

### DrawingOffset
- **类型**: `FIntPoint`

### BackgroundColor
- **类型**: `FLinearColor`
- **描述**: The background color displayed in the tile set viewer

### PerTileData
- **类型**: `TArray<FPaperTileMetadata>`
- **描述**: Per-tile information


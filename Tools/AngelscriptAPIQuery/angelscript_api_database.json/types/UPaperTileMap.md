# UPaperTileMap

**继承自**: `UObject`

A tile map is a 2D grid with a defined width and height (in tiles).  There can be multiple layers, each of which can specify which tile should appear in each cell of the map for that layer.

## 属性

### MapWidth
- **类型**: `int`

### MapHeight
- **类型**: `int`

### TileWidth
- **类型**: `int`

### TileHeight
- **类型**: `int`

### PixelsPerUnrealUnit
- **类型**: `float32`
- **描述**: The scaling factor between pixels and Unreal units (cm) (e.g., 0.64 would make a 64 pixel wide tile take up 100 cm)

### SeparationPerTileX
- **类型**: `float32`
- **描述**: The Z-separation incurred as you travel in X (not strictly applied, batched tiles will be put at the same Z level)

### SeparationPerTileY
- **类型**: `float32`
- **描述**: The Z-separation incurred as you travel in Y (not strictly applied, batched tiles will be put at the same Z level)

### SeparationPerLayer
- **类型**: `float32`

### Material
- **类型**: `UMaterialInterface`

### TileLayers
- **类型**: `TArray<TObjectPtr<UPaperTileLayer>>`

### CollisionThickness
- **类型**: `float32`

### SpriteCollisionDomain
- **类型**: `ESpriteCollisionMode`

### ProjectionMode
- **类型**: `ETileMapProjectionMode`

### HexSideLength
- **类型**: `int`
- **描述**: The vertical height of the sides of the hex cell for a tile.
Note: This value should already be included as part of the TileHeight, and is purely cosmetic; it only affects how the tile cursor preview is drawn.

### AssetImportData
- **类型**: `UAssetImportData`
- **描述**: Importing data and options used for this tile map

### BackgroundColor
- **类型**: `FLinearColor`
- **描述**: The background color displayed in the tile map editor

### TileGridColor
- **类型**: `FLinearColor`
- **描述**: The color of the tile grid

### MultiTileGridColor
- **类型**: `FLinearColor`
- **描述**: The color of the multi tile grid

### MultiTileGridWidth
- **类型**: `int`
- **描述**: Number of tiles the multi tile grid spans horizontally. 0 removes vertical lines

### MultiTileGridHeight
- **类型**: `int`
- **描述**: Number of tiles the multi tile grid spans vertically. 0 removes horizontal lines

### MultiTileGridOffsetX
- **类型**: `int`
- **描述**: Number of tiles the multi tile grid is shifted to the right

### MultiTileGridOffsetY
- **类型**: `int`
- **描述**: Number of tiles the multi tile grid is shifted downwards

### LayerGridColor
- **类型**: `FLinearColor`
- **描述**: The color of the layer grid


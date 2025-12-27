# UPaperTileMapComponent

**继承自**: `UMeshComponent`

A component that handles rendering and collision for a single instance of a UPaperTileMap asset.

This component is created when you drag a tile map asset from the content browser into a Blueprint, or
contained inside of the actor created when you drag one into the level.

NOTE: This is an beta preview class.  While not considered production-ready, it is a step beyond
'experimental' and is being provided as a preview of things to come:
 - We will try to provide forward-compatibility for content you create.
 - The classes may change significantly in the future.
 - The code is in an early state and may not meet the desired polish / quality bar.
 - There is probably no documentation or example content yet.
 - They will be promoted out of 'beta' when they are production ready.

@see UPrimitiveComponent, UPaperTileMap

## 属性

### UseSingleLayerIndex
- **类型**: `int`
- **描述**: The index of the single layer to use if enabled

### bUseSingleLayer
- **类型**: `bool`
- **描述**: Should we draw a single layer?

### bShowPerTileGridWhenSelected
- **类型**: `bool`
- **描述**: Should this component show a tile grid when the component is selected?

### bShowPerLayerGridWhenSelected
- **类型**: `bool`
- **描述**: Should this component show an outline around each layer when the component is selected?

### bShowOutlineWhenUnselected
- **类型**: `bool`
- **描述**: Should this component show an outline around the first layer when the component is not selected?

### bShowPerTileGridWhenUnselected
- **类型**: `bool`
- **描述**: Should this component show a tile grid when the component is not selected?

### bShowPerLayerGridWhenUnselected
- **类型**: `bool`
- **描述**: Should this component show an outline around each layer when the component is not selected?

### TileMap
- **类型**: `UPaperTileMap`

## 方法

### AddNewLayer
```angelscript
UPaperTileLayer AddNewLayer()
```
Creates and adds a new layer to the tile map
Note: This will only work on components that own their own tile map (OwnsTileMap returns true), you cannot modify standalone tile map assets

### CreateNewTileMap
```angelscript
void CreateNewTileMap(int MapWidth, int MapHeight, int TileWidth, int TileHeight, float32 PixelsPerUnrealUnit, bool bCreateLayer)
```
Creates a new tile map of the specified size, replacing the TileMap reference (or dropping the previous owned one)

@param MapWidth Width of the map (in tiles)
@param MapHeight Height of the map (in tiles)
@param TileWidth Width of one tile (in pixels)
@param TileHeight Height of one tile (in pixels)
@param bCreateLayer Should an empty layer be created?

### GetLayerColor
```angelscript
FLinearColor GetLayerColor(int Layer)
```
Gets the per-layer color multiplier for a specific layer (multiplied with the tile map color and passed to the material as a vertex color)

### GetMapSize
```angelscript
void GetMapSize(int& MapWidth, int& MapHeight, int& NumLayers)
```
Returns the size of the tile map

### GetTile
```angelscript
FPaperTileInfo GetTile(int X, int Y, int Layer)
```
Returns the contents of a specified tile cell

### GetTileCenterPosition
```angelscript
FVector GetTileCenterPosition(int TileX, int TileY, int LayerIndex, bool bWorldSpace)
```
Returns the position of the center of the specified tile

### GetTileCornerPosition
```angelscript
FVector GetTileCornerPosition(int TileX, int TileY, int LayerIndex, bool bWorldSpace)
```
Returns the position of the top left corner of the specified tile

### GetTileMapColor
```angelscript
FLinearColor GetTileMapColor()
```
Gets the tile map global color multiplier (multiplied with the per-layer color and passed to the material as a vertex color)

### GetTilePolygon
```angelscript
void GetTilePolygon(int TileX, int TileY, TArray<FVector>& Points, int LayerIndex, bool bWorldSpace)
```
Returns the polygon for the specified tile (will be 4 or 6 vertices as a rectangle, diamond, or hexagon)

### MakeTileMapEditable
```angelscript
void MakeTileMapEditable()
```
Makes the tile map asset pointed to by this component editable.  Nothing happens if it was already instanced, but
if the tile map is an asset reference, it is cloned to make a unique instance.

### OwnsTileMap
```angelscript
bool OwnsTileMap()
```
Does this component own the tile map (is it instanced instead of being an asset reference)?

### RebuildCollision
```angelscript
void RebuildCollision()
```
Rebuilds collision for the tile map

### ResizeMap
```angelscript
void ResizeMap(int NewWidthInTiles, int NewHeightInTiles)
```
Resizes the tile map (Note: This will only work on components that own their own tile map (OwnsTileMap returns true), you cannot modify standalone tile map assets)

### SetDefaultCollisionThickness
```angelscript
void SetDefaultCollisionThickness(float32 Thickness, bool bRebuildCollision)
```
Sets the default thickness for any layers that don't override the collision thickness
Note: This will only work on components that own their own tile map (OwnsTileMap returns true), you cannot modify standalone tile map assets

### SetLayerCollision
```angelscript
void SetLayerCollision(int Layer, bool bHasCollision, bool bOverrideThickness, float32 CustomThickness, bool bOverrideOffset, float32 CustomOffset, bool bRebuildCollision)
```
Sets the collision thickness for a specific layer
Note: This will only work on components that own their own tile map (OwnsTileMap returns true), you cannot modify standalone tile map assets

### SetLayerColor
```angelscript
void SetLayerColor(FLinearColor NewColor, int Layer)
```
Sets the per-layer color multiplier for a specific layer (multiplied with the tile map color and passed to the material as a vertex color)
Note: This will only work on components that own their own tile map (OwnsTileMap returns true), you cannot modify standalone tile map assets

### SetTile
```angelscript
void SetTile(int X, int Y, int Layer, FPaperTileInfo NewValue)
```
Modifies the contents of a specified tile cell (Note: This will only work on components that own their own tile map (OwnsTileMap returns true), you cannot modify standalone tile map assets)
Note: Does not update collision by default, call RebuildCollision after all edits have been done in a frame if necessary

### SetTileMap
```angelscript
bool SetTileMap(UPaperTileMap NewTileMap)
```
Change the PaperTileMap used by this instance.

### SetTileMapColor
```angelscript
void SetTileMapColor(FLinearColor NewColor)
```
Sets the tile map global color multiplier (multiplied with the per-layer color and passed to the material as a vertex color)


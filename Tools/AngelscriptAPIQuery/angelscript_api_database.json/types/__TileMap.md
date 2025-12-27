# __TileMap

## 方法

### BreakTile
```angelscript
void BreakTile(FPaperTileInfo Tile, int& TileIndex, UPaperTileSet& TileSet, bool& bFlipH, bool& bFlipV, bool& bFlipD)
```
Breaks out the information for a tile

### GetTileTransform
```angelscript
FTransform GetTileTransform(FPaperTileInfo Tile)
```
Returns the transform for a tile

### GetTileUserData
```angelscript
FName GetTileUserData(FPaperTileInfo Tile)
```
Returns the user data name for the specified tile, or NAME_None if there is no user-specified data

### MakeTile
```angelscript
FPaperTileInfo MakeTile(int TileIndex, UPaperTileSet TileSet, bool bFlipH, bool bFlipV, bool bFlipD)
```
Creates a tile from the specified information


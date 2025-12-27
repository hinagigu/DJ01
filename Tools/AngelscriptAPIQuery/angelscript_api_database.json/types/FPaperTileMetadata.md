# FPaperTileMetadata

Information about a single tile in a tile set

## 属性

### UserDataName
- **类型**: `FName`

### CollisionData
- **类型**: `FSpriteGeometryCollection`
- **描述**: Collision data for the tile

### TerrainMembership
- **类型**: `uint8`
- **描述**: Indexes into the Terrains array of the owning tile set, in counterclockwise order starting from top-left
0xFF indicates no membership.

## 方法

### opAssign
```angelscript
FPaperTileMetadata& opAssign(FPaperTileMetadata Other)
```


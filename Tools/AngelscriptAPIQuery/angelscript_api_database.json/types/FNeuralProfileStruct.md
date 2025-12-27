# FNeuralProfileStruct

struct with all the settings we want in UNeuralProfile, separate to make it easer to pass this data around in the engine.

## 属性

### InputFormat
- **类型**: `ENeuralProfileFormat`

### OutputFormat
- **类型**: `ENeuralProfileFormat`

### RuntimeType
- **类型**: `ENeuralProfileRuntimeType`

### NNEModelData
- **类型**: `UObject`

### InputDimension
- **类型**: `FIntVector4`

### OutputDimension
- **类型**: `FIntVector4`

### BatchSizeOverride
- **类型**: `int`

### TileSize
- **类型**: `ENeuralModelTileType`
- **描述**: Total tiles used. Each tile will be executed by 1 batch

### TileOverlap
- **类型**: `FIntPoint`
- **描述**: Tile border overlaps (Left|Right, Top|Bottom). The larger this value, the more tiles are required to cover the whole screen when TileSize is Auto.

### TileOverlapResolveType
- **类型**: `ETileOverlapResolveType`

## 方法

### opAssign
```angelscript
FNeuralProfileStruct& opAssign(FNeuralProfileStruct Other)
```


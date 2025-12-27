# FVirtualTextureSpacePoolConfig

Settings for a single virtual texture physical pool.

## 属性

### Formats
- **类型**: `TArray<EPixelFormat>`
- **描述**: Formats of the layers in the physical pool. Leave empty to match any format.

### MinTileSize
- **类型**: `int`
- **描述**: Minimum tile size to match (including tile border).

### MaxTileSize
- **类型**: `int`
- **描述**: Maximum tile size to match (including tile border). Set to 0 to match any tile size.

### SizeInMegabyte
- **类型**: `int`
- **描述**: Upper limit size in megabytes to allocate for the pool. The allocator will allocate as close as possible below this limit.

### bEnableResidencyMipMapBias
- **类型**: `bool`
- **描述**: Enable MipMapBias based on pool residency tracking.

### bAllowSizeScale
- **类型**: `bool`
- **描述**: Allow the size to allocate for the pool to be scaled by scalability settings.

### MinScaledSizeInMegabyte
- **类型**: `int`
- **描述**: Lower limit of size in megabytes to allocate for the pool after size scaling.

### MaxScaledSizeInMegabyte
- **类型**: `int`
- **描述**: Upper limit of size in megabytes to allocate for the pool after size scaling. Set to 0 to ignore.

## 方法

### opAssign
```angelscript
FVirtualTextureSpacePoolConfig& opAssign(FVirtualTextureSpacePoolConfig Other)
```


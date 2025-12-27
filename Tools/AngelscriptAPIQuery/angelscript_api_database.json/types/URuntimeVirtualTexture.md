# URuntimeVirtualTexture

**继承自**: `UObject`

Runtime virtual texture UObject

## 属性

### MaterialType
- **类型**: `ERuntimeVirtualTextureMaterialType`

### bCompressTextures
- **类型**: `bool`

### bUseLowQualityCompression
- **类型**: `bool`

### bClearTextures
- **类型**: `bool`
- **描述**: Enable clear before rendering a page of the virtual texture. Disabling this can be an optimization if you know that the texture will always be fully covered by rendering.

### bSinglePhysicalSpace
- **类型**: `bool`
- **描述**: Enable page table channel packing. This reduces page table memory and update cost but can reduce the ability to share physical memory with other virtual textures.

### bPrivateSpace
- **类型**: `bool`
- **描述**: Enable private page table allocation. This can reduce total page table memory allocation but can also reduce the total number of virtual textures supported.

### bAdaptive
- **类型**: `bool`
- **描述**: Enable sparse adaptive page tables. This supports larger tile counts but adds an indirection cost when sampling the virtual texture. It is recommended only when very large virtual resolutions are necessary.

### bContinuousUpdate
- **类型**: `bool`
- **描述**: Enable continuous update of the virtual texture pages. This round-robin updates already mapped pages and can help fix pages that are mapped before dependent textures are fully streamed in.

### RemoveLowMips
- **类型**: `int`
- **描述**: Number of low mips to cut from the virtual texture. This can reduce peak virtual texture update cost but will also increase the probability of mip shimmering.

### LODGroup
- **类型**: `TextureGroup`

### TileCount
- **类型**: `int`

### TileSize
- **类型**: `int`

### TileBorderSize
- **类型**: `int`

## 方法

### GetPageTableSize
```angelscript
int GetPageTableSize()
```
Public getter for virtual texture page table size. This is only different from GetTileCount() when using an adaptive page table.

### GetSize
```angelscript
int GetSize()
```
Public getter for virtual texture size. This is derived from the TileCount and TileSize.

### GetTileBorderSize
```angelscript
int GetTileBorderSize()
```
Public getter for virtual texture tile border size

### GetTileCount
```angelscript
int GetTileCount()
```
Public getter for virtual texture tile count

### GetTileSize
```angelscript
int GetTileSize()
```
Public getter for virtual texture tile size


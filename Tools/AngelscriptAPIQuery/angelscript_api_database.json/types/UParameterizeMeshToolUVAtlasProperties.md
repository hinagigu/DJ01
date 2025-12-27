# UParameterizeMeshToolUVAtlasProperties

**继承自**: `UInteractiveToolPropertySet`

Settings for the UVAtlas Automatic UV Generation Method

## 属性

### IslandStretch
- **类型**: `float32`
- **描述**: Maximum amount of stretch, from none to unbounded. If zero stretch is specified, each triangle will likely be its own UV island.

### NumIslands
- **类型**: `int`
- **描述**: Hint at number of UV islands. The default of 0 means it is determined automatically.

### TextureResolution
- **类型**: `int`
- **描述**: Expected resolution of the output textures; this controls spacing left between UV islands to avoid interpolation artifacts.

### bUsePolygroups
- **类型**: `bool`
- **描述**: Generate new UVs based on polygroups from specified layer.

### bLayoutUDIMPerPolygroup
- **类型**: `bool`
- **描述**: Layout resulting islands on UDIMs based on polygroups.


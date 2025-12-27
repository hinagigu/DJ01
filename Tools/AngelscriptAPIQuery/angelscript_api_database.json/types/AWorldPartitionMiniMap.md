# AWorldPartitionMiniMap

**继承自**: `AInfo`

A mini map to preview the world in world partition window. (editor-only)

## 属性

### ExcludedDataLayers
- **类型**: `TSet<FActorDataLayer>`
- **描述**: Datalayers excluded from MiniMap rendering

### WorldUnitsPerPixel
- **类型**: `int`
- **描述**: Target world units per pixel for the minimap texture.
May not end up being the final minimap accuracy if the resulting texture resolution is unsupported.

### BuilderCellSize
- **类型**: `int`
- **描述**: Size of the loading region that will be used when iterating over the whole map during the minimap build process.
A smaller size may help reduce blurriness as it will put less pressure on various graphics pools, at the expanse of an increase in processing time.

### CaptureSource
- **类型**: `ESceneCaptureSource`
- **描述**: Specifies which component of the scene rendering should be output to the minimap texture.

### CaptureWarmupFrames
- **类型**: `uint`
- **描述**: Number of frames to render before each capture in order to warmup various rendering systems (VT/Nanite/etc).


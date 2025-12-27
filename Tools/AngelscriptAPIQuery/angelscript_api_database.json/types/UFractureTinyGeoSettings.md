# UFractureTinyGeoSettings

**继承自**: `UFractureToolSettings`

Settings controlling how geometry is selected and merged into neighboring geometry

## 属性

### MergeType
- **类型**: `EMergeType`
- **描述**: Whether to merge small geometry, or small clusters

### bOnFractureLevel
- **类型**: `bool`
- **描述**: Only consider bones at the current Fracture Level

### bOnlyClusters
- **类型**: `bool`
- **描述**: Only auto-consider clusters for merging. Note that leaf nodes can still be consider if manually selected.

### bOnlySameParent
- **类型**: `bool`
- **描述**: Only merge to neighbors with the same parent in the hierarchy

### NeighborSelection
- **类型**: `ENeighborSelectionMethod`

### bOnlyToConnected
- **类型**: `bool`
- **描述**: Only merge pieces that are connected in the proximity graph. If unchecked, connected pieces will still be favored, but if none are available the closest disconnected piece can be merged.

### UseBoneSelection
- **类型**: `EUseBoneSelection`
- **描述**: Options for using the current bone selection

### SelectionMethod
- **类型**: `EGeometrySelectionMethod`

### MinVolumeCubeRoot
- **类型**: `float`
- **描述**: If size (cube root of volume) is less than this value, geometry should be merged into neighbors -- i.e. a value of 2 merges geometry smaller than a 2x2x2 cube

### RelativeVolume
- **类型**: `float`
- **描述**: If cube root of volume relative to the overall shape's cube root of volume is less than this, the geometry should be merged into its neighbors.
      (Note: This is a bit different from the histogram viewer's "Relative Size," which instead shows values relative to the largest rigid bone.)


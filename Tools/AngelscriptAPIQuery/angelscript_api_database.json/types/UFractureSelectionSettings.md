# UFractureSelectionSettings

**继承自**: `UFractureToolSettings`

Settings controlling how geometry is selected

## 属性

### MouseSelectionMethod
- **类型**: `EMouseSelectionMethod`

### VolumeSelectionMethod
- **类型**: `EVolumeSelectionMethod`
- **描述**: What values to use when filtering by volume.  Note all values are presented as cube roots to give more intuitive scales (e.g., to select bones with volume less than a 10x10x10 cube, choose CubeRootOfVolume and MaxVolume=10, rather than needing to multiply out to 1000)

### SelectionOperation
- **类型**: `ESelectionOperation`
- **描述**: How to update the selection from the filter

### MinVolume
- **类型**: `float`
- **描述**: Sets the minimum volume (as computed by the Volume Selection Method) that should be included in the filter

### MaxVolume
- **类型**: `float`
- **描述**: Sets the maximum volume (as computed by the Volume Selection Method) that should be included in the filter

### MinVolumeFrac
- **类型**: `float`
- **描述**: Sets the minimum volume (as computed by the Volume Selection Method) that should be included in the filter

### MaxVolumeFrac
- **类型**: `float`
- **描述**: Sets the maximum volume (as computed by the Volume Selection Method) that should be included in the filter

### KeepFraction
- **类型**: `float`
- **描述**: Fraction of bones to keep in the selection: If less than 1, bones will be randomly excluded from the selection filter

### RandomSeed
- **类型**: `int`
- **描述**: Seed to use for randomization when deciding which bones to keep w/ the Keep Fraction


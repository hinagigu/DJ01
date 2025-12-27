# UIterativeOffsetProperties

**继承自**: `UInteractiveToolPropertySet`

Properties for Iterative Offsetting

## 属性

### Steps
- **类型**: `int`
- **描述**: Number of Offsetting iterations

### bOffsetBoundaries
- **类型**: `bool`
- **描述**: Control whether the boundary is allowed to move

### SmoothingPerStep
- **类型**: `float32`
- **描述**: Amount of smoothing applied per Offset step

### bReprojectSmooth
- **类型**: `bool`
- **描述**: Reproject smooth vertices onto non-smoothed Offset Surface at each step (expensive but better-preserves uniform distance)


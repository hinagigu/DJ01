# UFractureMeshCutSettings

**继承自**: `UFractureToolSettings`

## 属性

### CutDistribution
- **类型**: `EMeshCutDistribution`
- **描述**: How to arrange the mesh cuts in space

### NumberToScatter
- **类型**: `int`
- **描述**: Number of meshes to random scatter

### GridX
- **类型**: `int`
- **描述**: Number of meshes to add to grid in X

### GridY
- **类型**: `int`
- **描述**: Number of meshes to add to grid in Y

### GridZ
- **类型**: `int`
- **描述**: Number of meshes to add to grid in Z

### Variability
- **类型**: `float32`
- **描述**: Magnitude of random displacement to cutting meshes

### MinScaleFactor
- **类型**: `float32`
- **描述**: Minimum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max

### MaxScaleFactor
- **类型**: `float32`
- **描述**: Maximum scale factor to apply to cutting meshes. A random scale will be chosen between Min and Max

### bRandomOrientation
- **类型**: `bool`
- **描述**: Whether to randomly vary the orientation of the cutting meshes

### RollRange
- **类型**: `float32`
- **描述**: Roll will be chosen between -Range and +Range

### PitchRange
- **类型**: `float32`
- **描述**: Pitch will be chosen between -Range and +Range

### YawRange
- **类型**: `float32`
- **描述**: Yaw will be chosen between -Range and +Range


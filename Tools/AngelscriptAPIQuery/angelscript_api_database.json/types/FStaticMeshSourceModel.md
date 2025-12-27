# FStaticMeshSourceModel

Source model from which a renderable static mesh is built.

## 属性

### BuildSettings
- **类型**: `FMeshBuildSettings`
- **描述**: Settings applied when building the mesh.

### ReductionSettings
- **类型**: `FMeshReductionSettings`
- **描述**: Reduction settings to apply when building render data.

### ScreenSize
- **类型**: `FPerPlatformFloat`
- **描述**: ScreenSize to display this LOD.
The screen size is based around the projected diameter of the bounding
sphere of the model. i.e. 0.5 means half the screen's maximum dimension.


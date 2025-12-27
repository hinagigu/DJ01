# UNiagaraRibbonRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### Material
- **类型**: `UMaterialInterface`
- **描述**: UNiagaraRendererProperties Interface END

### MaterialUserParamBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: Use the UMaterialInterface bound to this user variable if it is set to a valid value. If this is bound to a valid value and Material is also set, UserParamBinding wins.

### UV0Settings
- **类型**: `FNiagaraRibbonUVSettings`

### UV1Settings
- **类型**: `FNiagaraRibbonUVSettings`

### FacingMode
- **类型**: `ENiagaraRibbonFacingMode`

### MaxNumRibbons
- **类型**: `int`

### DrawDirection
- **类型**: `ENiagaraRibbonDrawDirection`
- **描述**: Controls the order the ribbon segments will be rendered.

### Shape
- **类型**: `ENiagaraRibbonShapeMode`
- **描述**: Shape of the ribbon, from flat plane, multiplane, 3d tube, and custom shapes.

### WidthSegmentationCount
- **类型**: `int`
- **描述**: Tessellation factor to apply to the width of the ribbon.
Ranges from 1 to 16. Greater values increase amount of tessellation.

### MultiPlaneCount
- **类型**: `int`
- **描述**: Number of planes in multiplane shape. Evenly distributed from 0-90 or 0-180 degrees off camera facing depending on setting

### TubeSubdivisions
- **类型**: `int`
- **描述**: Number of vertices/faces in a tube.

### CustomVertices
- **类型**: `TArray<FNiagaraRibbonShapeCustomVertex>`
- **描述**: Vertices for a cross section of the ribbon in custom shape mode.

### TessellationMode
- **类型**: `ENiagaraRibbonTessellationMode`
- **描述**: Defines the tessellation mode allowing custom tessellation parameters or disabling tessellation entirely.

### CurveTension
- **类型**: `float32`
- **描述**: Defines the curve tension, or how long the curve's tangents are.
Ranges from 0 to 1. The higher the value, the sharper the curve becomes.

### TessellationFactor
- **类型**: `int`
- **描述**: Custom tessellation factor.
Ranges from 1 to 16. Greater values increase amount of tessellation.

### TessellationAngle
- **类型**: `float32`
- **描述**: Defines the angle in degrees at which tessellation occurs.
Ranges from 1 to 180. Smaller values increase amount of tessellation.
If set to 0, use the maximum tessellation set above.

### MaterialParameters
- **类型**: `FNiagaraRendererMaterialParameters`
- **描述**: If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.

### bEnableAccurateGeometry
- **类型**: `bool`

### bUseMaterialBackfaceCulling
- **类型**: `bool`

### bUseGeometryNormals
- **类型**: `bool`

### bUseGPUInit
- **类型**: `bool`

### bUseConstantFactor
- **类型**: `bool`

### bScreenSpaceTessellation
- **类型**: `bool`

### bCastShadows
- **类型**: `bool`


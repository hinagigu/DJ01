# UWeldMeshEdgesToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### Tolerance
- **类型**: `float32`
- **描述**: Edges are considered matching if both pairs of endpoint vertices are closer than this distance

### bOnlyUnique
- **类型**: `bool`
- **描述**: Only merge unambiguous pairs that have unique duplicate-edge matches

### bResolveTJunctions
- **类型**: `bool`
- **描述**: If enabled, after an initial attempt at Welding, attempt to resolve remaining open edges in T-junction configurations via edge splits, and then retry Weld

### AttrWeldingMode
- **类型**: `EWeldMeshEdgesAttributeUIMode`
- **描述**: Controls split-attribute welding performed after the Mesh weld.  Applies to normals, tangents, UVs and colors.

### SplitNormalThreshold
- **类型**: `float32`
- **描述**: Threshold on the angle between normals used to determine if split normals should be merged

### SplitTangentsThreshold
- **类型**: `float32`
- **描述**: Threshold on the angle between tangent used to determine if split tangents should be merged

### SplitUVThreshold
- **类型**: `float32`
- **描述**: Threshold uv-distance used to determine if split UVs should be merged

### SplitColorThreshold
- **类型**: `float32`
- **描述**: Threshold color-distance used to determine if split colors should be merged


# UMeshTangentsToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### CalculationMethod
- **类型**: `EMeshTangentsType`
- **描述**: Method used for calculating the tangents

### bShowTangents
- **类型**: `bool`
- **描述**: Display the mesh tangents

### bShowNormals
- **类型**: `bool`
- **描述**: Display the mesh normals

### LineLength
- **类型**: `float32`
- **描述**: Length of lines used for displaying tangents and/or normals

### LineThickness
- **类型**: `float32`
- **描述**: Thickness of lines used for displaying tangents and/or normals

### bShowDegenerates
- **类型**: `bool`
- **描述**: Display tangents and/or normals for degenerate triangles

### bCompareWithMikkt
- **类型**: `bool`
- **描述**: Display difference between FastMikkTSpace tangents and MikkTSpace tangents.
This is only available if the FastMikkTSpace Calculation Method is selected.

### CompareWithMikktThreshold
- **类型**: `float32`
- **描述**: Minimum angle difference in degrees for a FastMikkTSpace tangent to be considered different to a MikkTSpace tangent.
This is only available if a Compare with MikkT is enabled and the FastMikkTSpace Calculation Method is selected.


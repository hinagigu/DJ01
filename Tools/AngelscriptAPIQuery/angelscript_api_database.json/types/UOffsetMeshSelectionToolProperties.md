# UOffsetMeshSelectionToolProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### OffsetDistance
- **类型**: `float`
- **描述**: The Extrusion Distance used in Fixed Input Mode

### Direction
- **类型**: `EOffsetMeshSelectionDirectionMode`
- **描述**: Control how the Offset Area should be displaced

### NumSubdivisions
- **类型**: `int`
- **描述**: Specify the number of subdivisions along the sides of the Extrusion

### CreaseAngle
- **类型**: `float`
- **描述**: Specify the Crease Angle used to split the sides of the Extrusion into separate Groups

### bShellsToSolids
- **类型**: `bool`
- **描述**: If the Offset Area has a fully open border, this option determines if Extrusion will create a Solid mesh or leave the base "open"

### bInferGroupsFromNbrs
- **类型**: `bool`
- **描述**: Control whether a single Group should be generated along the sides of the Extrusion, or multiple Groups based on the adjacent Groups around the Offset Area border

### bGroupPerSubdivision
- **类型**: `bool`
- **描述**: Control whether a new Group is generated for each Subdivision

### bReplaceSelectionGroups
- **类型**: `bool`
- **描述**: Control whether groups in the Offset Area are mapped to new Groups, or replaced with a single new Group

### UVScale
- **类型**: `float`
- **描述**: The automatically-generated UVs on the sides of the Extrusion are scaled by this value

### bUVIslandPerGroup
- **类型**: `bool`
- **描述**: Control whether a separate UV island should be generated for each output Group on the sides of the Extrusion, or a single UV island wrapping around the entire "tube"

### bInferMaterialID
- **类型**: `bool`
- **描述**: Control whether SetMaterialID is assigned to all triangles along the sides of the Extrusion, or if MaterialIDs should be inferred from the Offset Area

### SetMaterialID
- **类型**: `int`
- **描述**: Constant Material ID used when MaterialIDs are not being inferred, or no adjacent MaterialID exists

### bShowInputMaterials
- **类型**: `bool`
- **描述**: Control whether the original Mesh Materials should be shown, or a visualization of the Offset Groups


# USubdividePolyToolProperties

**继承自**: `UInteractiveToolPropertySet`

Properties

## 属性

### SubdivisionLevel
- **类型**: `int`
- **描述**: Number of iterations/levels of subdivision to perform

### SubdivisionScheme
- **类型**: `ESubdivisionScheme`

### BoundaryScheme
- **类型**: `ESubdivisionBoundaryScheme`
- **描述**: How to treat mesh boundaries

### NormalComputationMethod
- **类型**: `ESubdivisionOutputNormals`

### UVComputationMethod
- **类型**: `ESubdivisionOutputUVs`

### bNewPolyGroups
- **类型**: `bool`
- **描述**: Assign a new PolyGroup ID to each newly created face

### bRenderGroups
- **类型**: `bool`
- **描述**: Display each PolyGroup with an auto-generated color

### bRenderCage
- **类型**: `bool`
- **描述**: Display the mesh corresponding to Subdivision Level 0

### bAddExtraCorners
- **类型**: `bool`
- **描述**: When using the group topology for subdivision, whether to add extra corners at sharp group edge bends on mesh boundaries. Note: We cannot add extra corners on non-boundary group edges, as this would create non-manifold geometry on subdivision.

### ExtraCornerAngleThresholdDegrees
- **类型**: `float`
- **描述**: How acute an angle between two edges needs to be to add an extra corner there when Add Extra Corners is true.


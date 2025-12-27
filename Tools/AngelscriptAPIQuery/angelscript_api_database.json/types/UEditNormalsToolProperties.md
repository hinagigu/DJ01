# UEditNormalsToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties

## 属性

### bRecomputeNormals
- **类型**: `bool`
- **描述**: Recompute all mesh normals

### NormalCalculationMethod
- **类型**: `ENormalCalculationMethod`
- **描述**: Choose the method for computing vertex normals

### bFixInconsistentNormals
- **类型**: `bool`
- **描述**: For meshes with inconsistent triangle orientations/normals, flip as needed to make the normals consistent

### bInvertNormals
- **类型**: `bool`
- **描述**: Invert (flip) all mesh normals and associated triangle orientations

### SplitNormalMethod
- **类型**: `ESplitNormalMethod`
- **描述**: Control whether and how the topology of the normals is recomputed, e.g. to create sharp edges where face normals change by a large amount or where face group IDs change.  Normals will always be recomputed unless SplitNormal Method is UseExistingTopology.

### SharpEdgeAngleThreshold
- **类型**: `float32`
- **描述**: Threshold on angle of change in face normals across an edge, above which we create a sharp edge if bSplitNormals is true

### bAllowSharpVertices
- **类型**: `bool`
- **描述**: Assign separate normals at 'sharp' vertices, for example, at the tip of a cone


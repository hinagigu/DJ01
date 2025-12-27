# UPolygonOnMeshToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties of the polygon-on-mesh operations

## 属性

### Operation
- **类型**: `EEmbeddedPolygonOpMethod`
- **描述**: What operation to apply using the Polygon

### Shape
- **类型**: `EPolygonType`
- **描述**: Polygon Shape to use in this Operation

### bCutWithBoolean
- **类型**: `bool`
- **描述**: Use a volumetric boolean rather than curve projection; cuts through all layers and across edges

### bTryToFixHoles
- **类型**: `bool`
- **描述**: Automatically attempt to fill any open boundaries left by CSG (e.g. due to numerical errors)

### PolygonScale
- **类型**: `float32`
- **描述**: Scale of polygon to embed

### Width
- **类型**: `float32`
- **描述**: Width of Polygon

### Height
- **类型**: `float32`
- **描述**: Height of Polygon

### CornerRatio
- **类型**: `float32`
- **描述**: Corner Ratio of RoundRect Polygon

### Subdivisions
- **类型**: `int`
- **描述**: Number of sides in Circle or RoundRect Corner

### bCanAcceptFailedResult
- **类型**: `bool`
- **描述**: Whether the tool will allow accepting a result if the operation fails, for instance due to inability to insert the
polygon when not cutting with boolean, or due to unrepaired cracks in the result.

### bShowIntermediateResultOnFailure
- **类型**: `bool`
- **描述**: If an operation fails and we do not allow accepting the result, whether to show the intermediate failed result, or to
show the original mesh.


# UPolyEditBevelEdgeProperties

**继承自**: `UInteractiveToolPropertySet`

## 属性

### BevelDistance
- **类型**: `float`
- **描述**: Distance that each beveled mesh edge is inset from its initial position

### Subdivisions
- **类型**: `int`
- **描述**: Number of edge loops added along the bevel faces

### RoundWeight
- **类型**: `float32`
- **描述**: Roundness of the bevel. Ignored if Subdivisions = 0.

### bInferMaterialID
- **类型**: `bool`
- **描述**: If true, when faces on either side of a beveled mesh edges have the same Material ID, beveled edge will be set to that Material ID. Otherwise SetMaterialID is used.

### SetMaterialID
- **类型**: `int`
- **描述**: Material ID to set on the new faces introduced by bevel operation, unless bInferMaterialID=true and non-ambiguous MaterialID can be inferred from adjacent faces


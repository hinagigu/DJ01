# UDisplaceMeshDirectionalFilterProperties

**继承自**: `UInteractiveToolPropertySet`

Properties for a directional filter. Allows for displacement to be applied only to vertices whose normals point in a given direction

## 属性

### bEnableFilter
- **类型**: `bool`
- **描述**: Whether the directional filter is active.

### FilterDirection
- **类型**: `FVector`
- **描述**: Unit vector representing the direction to filter along.

### FilterWidth
- **类型**: `float32`
- **描述**: Scalar value determining how close to the filter direction the vertex normals must be in order to be displaced.
              0: Only normals pointing exactly in the filter direction are displaced.
              0.5: Normals forming angle up to 90 from the filter direction are displaced.
              1.0: All vertices are displaced.


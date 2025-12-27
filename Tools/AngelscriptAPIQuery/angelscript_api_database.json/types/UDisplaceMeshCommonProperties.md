# UDisplaceMeshCommonProperties

**继承自**: `UInteractiveToolPropertySet`

The basic set of properties shared by (more or less) all DisplacementTypes.

## 属性

### DisplacementType
- **类型**: `EDisplaceMeshToolDisplaceType`
- **描述**: Displacement type

### DisplaceIntensity
- **类型**: `float32`
- **描述**: Displacement intensity

### RandomSeed
- **类型**: `int`
- **描述**: Seed for randomization

### SubdivisionType
- **类型**: `EDisplaceMeshToolSubdivisionType`
- **描述**: Type of the  mesh subdivision.

### Subdivisions
- **类型**: `int`
- **描述**: Number of times to subdivide the mesh before displacing it.

### WeightMap
- **类型**: `FName`
- **描述**: Select vertex weight map. If configured, the weight map value will be sampled to modulate displacement intensity.

### bInvertWeightMap
- **类型**: `bool`

### bShowWireframe
- **类型**: `bool`

### bDisableSizeWarning
- **类型**: `bool`


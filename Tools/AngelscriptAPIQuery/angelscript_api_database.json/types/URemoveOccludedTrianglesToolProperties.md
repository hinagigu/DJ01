# URemoveOccludedTrianglesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Standard properties

## 属性

### OcclusionTestMethod
- **类型**: `EOcclusionCalculationUIMode`
- **描述**: The method for deciding whether a triangle is occluded

### TriangleSampling
- **类型**: `EOcclusionTriangleSamplingUIMode`
- **描述**: Where to sample triangles to test occlusion

### WindingIsoValue
- **类型**: `float`
- **描述**: The winding isovalue for GeneralizedWindingNumber mode

### AddRandomRays
- **类型**: `int`
- **描述**: For raycast-based occlusion tests, optionally add random ray direction to increase the accuracy of the visibility sampling

### AddTriangleSamples
- **类型**: `int`
- **描述**: Optionally add random samples to each triangle (in addition to those from TriangleSampling) to increase the accuracy of the visibility sampling

### bOnlySelfOcclude
- **类型**: `bool`
- **描述**: If false, when multiple meshes are selected the meshes can occlude each other.  When true, we process each selected mesh independently and only consider self-occlusions.

### ShrinkRemoval
- **类型**: `int`
- **描述**: Shrink (erode) the boundary of the set of triangles to remove.

### MinAreaIsland
- **类型**: `float`

### MinTriCountIsland
- **类型**: `int`

### Action
- **类型**: `EOccludedAction`
- **描述**: What action to perform on occluded triangles


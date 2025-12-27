# USmoothHoleFillProperties

**继承自**: `UInteractiveToolPropertySet`

* Properties. This class reflects the parameters in FSmoothFillOptions, but is decorated to allow use in the UI system.

## 属性

### bConstrainToHoleInterior
- **类型**: `bool`
- **描述**: Allow smoothing and remeshing of triangles outside of the fill region

### RemeshingExteriorRegionWidth
- **类型**: `int`
- **描述**: Number of vertex rings outside of the fill region to allow remeshing

### SmoothingExteriorRegionWidth
- **类型**: `int`
- **描述**: Number of vertex rings outside of the fill region to perform smoothing

### SmoothingInteriorRegionWidth
- **类型**: `int`
- **描述**: Number of vertex rings away from the fill region boundary to constrain smoothing

### InteriorSmoothness
- **类型**: `float32`
- **描述**: Desired Smoothness. This is not a linear quantity, but larger numbers produce smoother results

### FillDensityScalar
- **类型**: `float`
- **描述**: Relative triangle density of fill region

### bProjectDuringRemesh
- **类型**: `bool`
- **描述**: Whether to project to the original mesh during post-smooth remeshing. This can be expensive on large meshes with
many holes.


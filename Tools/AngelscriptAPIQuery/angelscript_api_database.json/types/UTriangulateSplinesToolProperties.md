# UTriangulateSplinesToolProperties

**继承自**: `UInteractiveToolPropertySet`

Parameters for controlling the spline triangulation

## 属性

### ErrorTolerance
- **类型**: `float`
- **描述**: How far to allow the triangulation boundary can deviate from the spline curve before we add more vertices

### FlattenMethod
- **类型**: `EFlattenCurveMethod`
- **描述**: Whether and how to flatten the curves. If curves are flattened, they can also be offset and combined

### CombineMethod
- **类型**: `ECombineCurvesMethod`
- **描述**: Whether or how to combine the curves

### Thickness
- **类型**: `float`
- **描述**: If > 0, Extrude the triangulation by this amount

### bFlipResult
- **类型**: `bool`
- **描述**: Whether to flip the facing direction of the generated mesh

### OpenCurves
- **类型**: `EOffsetOpenCurvesMethod`
- **描述**: How to handle open curves: Either offset them, or treat them as closed curves

### CurveOffset
- **类型**: `float`
- **描述**: How much offset to apply to curves

### OffsetClosedCurves
- **类型**: `EOffsetClosedCurvesMethod`
- **描述**: Whether and how to apply offset to closed curves

### EndShapes
- **类型**: `EOpenCurveEndShapes`
- **描述**: The shape of the ends of offset curves

### JoinMethod
- **类型**: `EOffsetJoinMethod`
- **描述**: The shape of joins between segments of an offset curve

### MiterLimit
- **类型**: `float`
- **描述**: How far a miter join can extend before it is replaced by a square join


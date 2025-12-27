# UParticleModuleTypeDataAnimTrail

**继承自**: `UParticleModuleTypeDataBase`

## 属性

### TilingDistance
- **类型**: `float32`
- **描述**: The (estimated) covered distance to tile the 2nd UV set at.
If 0.0, a second UV set will not be passed in.

### DistanceTessellationStepSize
- **类型**: `float32`
- **描述**: The distance step size for tessellation.
# Tessellation Points = TruncToInt((Distance Between Spawned Particles) / DistanceTessellationStepSize)). If 0 then there is no distance tessellation.

### TangentTessellationStepSize
- **类型**: `float32`
- **描述**: The tangent scalar for tessellation.
This is the degree change in the tangent direction [0...180] required to warrant an additional tessellation point. If 0 then there is no tangent tessellation.

### WidthTessellationStepSize
- **类型**: `float32`
- **描述**: The width step size for tessellation.
This is the number of world units change in the width required to warrant an additional tessellation point. If 0 then there is no width tessellation.

### bDeadTrailsOnDeactivate
- **类型**: `bool`

### bEnablePreviousTangentRecalculation
- **类型**: `bool`

### bTangentRecalculationEveryFrame
- **类型**: `bool`


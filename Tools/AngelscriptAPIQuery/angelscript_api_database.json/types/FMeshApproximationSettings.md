# FMeshApproximationSettings

## 属性

### OutputType
- **类型**: `EMeshApproximationType`

### ApproximationAccuracy
- **类型**: `float32`

### ClampVoxelDimension
- **类型**: `int`

### bAttemptAutoThickening
- **类型**: `bool`

### TargetMinThicknessMultiplier
- **类型**: `float32`

### bIgnoreTinyParts
- **类型**: `bool`

### TinyPartSizeMultiplier
- **类型**: `float32`

### BaseCapping
- **类型**: `EMeshApproximationBaseCappingType`

### WindingThreshold
- **类型**: `float32`

### bFillGaps
- **类型**: `bool`

### GapDistance
- **类型**: `float32`

### OcclusionMethod
- **类型**: `EOccludedGeometryFilteringPolicy`

### bOccludeFromBottom
- **类型**: `bool`

### SimplifyMethod
- **类型**: `EMeshApproximationSimplificationPolicy`

### TargetTriCount
- **类型**: `int`

### TrianglesPerM
- **类型**: `float32`

### GeometricDeviation
- **类型**: `float32`

### GroundClipping
- **类型**: `EMeshApproximationGroundPlaneClippingPolicy`

### GroundClippingZHeight
- **类型**: `float32`

### bEstimateHardNormals
- **类型**: `bool`

### HardNormalAngle
- **类型**: `float32`

### UVGenerationMethod
- **类型**: `EMeshApproximationUVGenerationPolicy`

### InitialPatchCount
- **类型**: `int`

### CurvatureAlignment
- **类型**: `float32`

### MergingThreshold
- **类型**: `float32`

### MaxAngleDeviation
- **类型**: `float32`

### bGenerateNaniteEnabledMesh
- **类型**: `bool`

### NaniteFallbackTarget
- **类型**: `ENaniteFallbackTarget`

### NaniteFallbackPercentTriangles
- **类型**: `float32`

### NaniteFallbackRelativeError
- **类型**: `float32`

### bSupportRayTracing
- **类型**: `bool`

### bAllowDistanceField
- **类型**: `bool`

### MultiSamplingAA
- **类型**: `int`

### RenderCaptureResolution
- **类型**: `int`

### MaterialSettings
- **类型**: `FMaterialProxySettings`

### CaptureFieldOfView
- **类型**: `float32`

### NearPlaneDist
- **类型**: `float32`

### bUseRenderLODMeshes
- **类型**: `bool`

### bEnableSimplifyPrePass
- **类型**: `bool`

### bEnableParallelBaking
- **类型**: `bool`

### bPrintDebugMessages
- **类型**: `bool`

### bEmitFullDebugMesh
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMeshApproximationSettings& opAssign(FMeshApproximationSettings Other)
```


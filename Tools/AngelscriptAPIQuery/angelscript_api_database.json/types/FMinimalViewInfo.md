# FMinimalViewInfo

## 属性

### Location
- **类型**: `FVector`

### Rotation
- **类型**: `FRotator`

### FOV
- **类型**: `float32`

### OrthoWidth
- **类型**: `float32`

### bAutoCalculateOrthoPlanes
- **类型**: `bool`

### AutoPlaneShift
- **类型**: `float32`

### bUpdateOrthoPlanes
- **类型**: `bool`

### bUseCameraHeightAsViewTarget
- **类型**: `bool`

### OrthoNearClipPlane
- **类型**: `float32`

### OrthoFarClipPlane
- **类型**: `float32`

### PerspectiveNearClipPlane
- **类型**: `float32`

### AspectRatio
- **类型**: `float32`

### ProjectionMode
- **类型**: `ECameraProjectionMode`

### PostProcessBlendWeight
- **类型**: `float32`
- **描述**: Indicates if PostProcessSettings should be applied.

### PostProcessSettings
- **类型**: `FPostProcessSettings`
- **描述**: Post-process settings to use if PostProcessBlendWeight is non-zero.

### OffCenterProjectionOffset
- **类型**: `FVector2D`
- **描述**: Off-axis / off-center projection offset as proportion of screen dimensions

### bConstrainAspectRatio
- **类型**: `bool`

### bUseFieldOfViewForLOD
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FMinimalViewInfo& opAssign(FMinimalViewInfo Other)
```


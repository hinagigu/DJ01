# UCameraComponent

**继承自**: `USceneComponent`

Represents a camera viewpoint and settings, such as projection type, field of view, and post-process overrides.
The default behavior for an actor used as the camera view target is to look for an attached camera component and use its location, rotation, and settings.

## 属性

### bAutoCalculateOrthoPlanes
- **类型**: `bool`

### bUpdateOrthoPlanes
- **类型**: `bool`

### bUseCameraHeightAsViewTarget
- **类型**: `bool`

### bDrawFrustumAllowed
- **类型**: `bool`

### CameraMesh
- **类型**: `UStaticMesh`

### PostProcessSettings
- **类型**: `FPostProcessSettings`

### FieldOfView
- **类型**: `float32`

### OrthoWidth
- **类型**: `float32`

### AutoPlaneShift
- **类型**: `float32`

### OrthoNearClipPlane
- **类型**: `float32`

### OrthoFarClipPlane
- **类型**: `float32`

### AspectRatio
- **类型**: `float32`

### AspectRatioAxisConstraint
- **类型**: `EAspectRatioAxisConstraint`

### bConstrainAspectRatio
- **类型**: `bool`

### bOverrideAspectRatioAxisConstraint
- **类型**: `bool`

### bUseFieldOfViewForLOD
- **类型**: `bool`

### bCameraMeshHiddenInGame
- **类型**: `bool`

### bLockToHmd
- **类型**: `bool`

### bUsePawnControlRotation
- **类型**: `bool`

### ProjectionMode
- **类型**: `ECameraProjectionMode`

### PostProcessBlendWeight
- **类型**: `float32`

## 方法

### GetCameraView
```angelscript
void GetCameraView(float32 DeltaTime, FMinimalViewInfo& DesiredView)
```
Returns camera's Point of View.
Called by Camera class. Subclass and postprocess to add any effects.

### OnCameraMeshHiddenChanged
```angelscript
void OnCameraMeshHiddenChanged()
```
Internal function for updating the camera mesh visibility in PIE

### SetAspectRatio
```angelscript
void SetAspectRatio(float32 InAspectRatio)
```

### SetAspectRatioAxisConstraint
```angelscript
void SetAspectRatioAxisConstraint(EAspectRatioAxisConstraint InAspectRatioAxisConstraint)
```

### SetAutoCalculateOrthoPlanes
```angelscript
void SetAutoCalculateOrthoPlanes(bool bAutoCalculate)
```

### SetAutoPlaneShift
```angelscript
void SetAutoPlaneShift(float32 InAutoPlaneShift)
```

### SetConstraintAspectRatio
```angelscript
void SetConstraintAspectRatio(bool bInConstrainAspectRatio)
```

### SetFieldOfView
```angelscript
void SetFieldOfView(float32 InFieldOfView)
```

### SetOrthoFarClipPlane
```angelscript
void SetOrthoFarClipPlane(float32 InOrthoFarClipPlane)
```

### SetOrthoNearClipPlane
```angelscript
void SetOrthoNearClipPlane(float32 InOrthoNearClipPlane)
```

### SetOrthoWidth
```angelscript
void SetOrthoWidth(float32 InOrthoWidth)
```

### SetPostProcessBlendWeight
```angelscript
void SetPostProcessBlendWeight(float32 InPostProcessBlendWeight)
```

### SetProjectionMode
```angelscript
void SetProjectionMode(ECameraProjectionMode InProjectionMode)
```

### SetUpdateOrthoPlanes
```angelscript
void SetUpdateOrthoPlanes(bool bInUpdateOrthoPlanes)
```

### SetUseCameraHeightAsViewTarget
```angelscript
void SetUseCameraHeightAsViewTarget(bool bInUseCameraHeightAsViewTarget)
```

### SetUseFieldOfViewForLOD
```angelscript
void SetUseFieldOfViewForLOD(bool bInUseFieldOfViewForLOD)
```


# USceneCaptureComponent2D

**继承自**: `USceneCaptureComponent`

Used to capture a 'snapshot' of the scene from a single plane and feed it to a render target.

## 属性

### ProjectionType
- **类型**: `ECameraProjectionMode`

### FOVAngle
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

### TextureTarget
- **类型**: `UTextureRenderTarget2D`

### CompositeMode
- **类型**: `ESceneCaptureCompositeMode`

### PostProcessSettings
- **类型**: `FPostProcessSettings`

### PostProcessBlendWeight
- **类型**: `float32`

### CustomNearClippingPlane
- **类型**: `float32`

### bUseCustomProjectionMatrix
- **类型**: `bool`
- **描述**: Whether a custom projection matrix will be used during rendering. Use with caution. Does not currently affect culling

### CustomProjectionMatrix
- **类型**: `FMatrix`
- **描述**: The custom projection matrix to use

### bEnableOrthographicTiling
- **类型**: `bool`

### NumXTiles
- **类型**: `int`

### NumYTiles
- **类型**: `int`

### bEnableClipPlane
- **类型**: `bool`

### ClipPlaneBase
- **类型**: `FVector`

### ClipPlaneNormal
- **类型**: `FVector`

### bRenderInMainRenderer
- **类型**: `bool`

### bOverride_CustomNearClippingPlane
- **类型**: `bool`

### bCameraCutThisFrame
- **类型**: `bool`

### bConsiderUnrenderedOpaquePixelAsFullyTranslucent
- **类型**: `bool`

## 方法

### CaptureScene
```angelscript
void CaptureScene()
```
Render the scene to the texture target immediately.
This should not be used if bCaptureEveryFrame is enabled, or the scene capture will render redundantly.
If r.SceneCapture.CullByDetailMode is set, nothing will happen if DetailMode is higher than r.DetailMode.


# USceneCaptureComponentCube

**继承自**: `USceneCaptureComponent`

Used to capture a 'snapshot' of the scene from a 6 planes and feed it to a render target.

## 属性

### TextureTarget
- **类型**: `UTextureRenderTargetCube`

### bCaptureRotation
- **类型**: `bool`

## 方法

### CaptureScene
```angelscript
void CaptureScene()
```
Render the scene to the texture target immediately.
This should not be used if bCaptureEveryFrame is enabled, or the scene capture will render redundantly.
If r.SceneCapture.CullByDetailMode is set, nothing will happen if DetailMode is higher than r.DetailMode.


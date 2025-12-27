# UBaseDynamicMeshComponent

**继承自**: `UMeshComponent`

UBaseDynamicMeshComponent is a base interface for a UMeshComponent based on a UDynamicMesh.

## 属性

### bExplicitShowWireframe
- **类型**: `bool`

### WireframeColor
- **类型**: `FLinearColor`

### ColorMode
- **类型**: `EDynamicMeshComponentColorOverrideMode`

### ConstantColor
- **类型**: `FColor`

### ColorSpaceMode
- **类型**: `EDynamicMeshVertexColorTransformMode`

### bEnableFlatShading
- **类型**: `bool`

### bEnableViewModeOverrides
- **类型**: `bool`

### bEnableRaytracing
- **类型**: `bool`

## 方法

### ClearOverrideRenderMaterial
```angelscript
void ClearOverrideRenderMaterial()
```
Clear any active override render material

### ClearSecondaryRenderMaterial
```angelscript
void ClearSecondaryRenderMaterial()
```
Clear any active secondary render material

### GetColorOverrideMode
```angelscript
EDynamicMeshComponentColorOverrideMode GetColorOverrideMode()
```
@return active Color Override mode

### GetConstantOverrideColor
```angelscript
FColor GetConstantOverrideColor()
```
@return active Color used for Constant Color Override Mode

### GetDynamicMesh
```angelscript
UDynamicMesh GetDynamicMesh()
```
@return the child UDynamicMesh

### GetEnableRaytracing
```angelscript
bool GetEnableRaytracing()
```
@return true if raytracing support is currently enabled

### GetEnableWireframeRenderPass
```angelscript
bool GetEnableWireframeRenderPass()
```
@return true if wireframe rendering pass is enabled

### GetFlatShadingEnabled
```angelscript
bool GetFlatShadingEnabled()
```
@return active Color used for Constant Color Override Mode

### GetOverrideRenderMaterial
```angelscript
UMaterialInterface GetOverrideRenderMaterial(int MaterialIndex)
```
@return active override render material for the given MaterialIndex

### GetSecondaryBuffersVisibility
```angelscript
bool GetSecondaryBuffersVisibility()
```
@return true if secondary buffers are currently set to be visible

### GetSecondaryRenderMaterial
```angelscript
UMaterialInterface GetSecondaryRenderMaterial()
```
@return active secondary render material

### GetShadowsEnabled
```angelscript
bool GetShadowsEnabled()
```

### GetVertexColorSpaceTransformMode
```angelscript
EDynamicMeshVertexColorTransformMode GetVertexColorSpaceTransformMode()
```
@return active Color Override mode

### GetViewModeOverridesEnabled
```angelscript
bool GetViewModeOverridesEnabled()
```

### HasOverrideRenderMaterial
```angelscript
bool HasOverrideRenderMaterial(int k)
```
@return true if an override render material is currently enabled for the given MaterialIndex

### SetColorOverrideMode
```angelscript
void SetColorOverrideMode(EDynamicMeshComponentColorOverrideMode NewMode)
```
Configure the active Color Override

### SetConstantOverrideColor
```angelscript
void SetConstantOverrideColor(FColor NewColor)
```
Configure the Color used with Constant Color Override Mode

### SetEnableFlatShading
```angelscript
void SetEnableFlatShading(bool bEnable)
```
Configure the Color used with Constant Color Override Mode

### SetEnableRaytracing
```angelscript
void SetEnableRaytracing(bool bSetEnabled)
```
Enable/Disable raytracing support. This is an expensive call as it flushes
the rendering queue and forces an immediate rebuild of the SceneProxy.

### SetEnableWireframeRenderPass
```angelscript
void SetEnableWireframeRenderPass(bool bEnable)
```
Configure whether wireframe rendering is enabled or not

### SetOverrideRenderMaterial
```angelscript
void SetOverrideRenderMaterial(UMaterialInterface Material)
```
Set an active override render material. This should replace all materials during rendering.

### SetSecondaryBuffersVisibility
```angelscript
void SetSecondaryBuffersVisibility(bool bSetVisible)
```
Show/Hide the secondary triangle buffers. Does not invalidate SceneProxy.

### SetSecondaryRenderMaterial
```angelscript
void SetSecondaryRenderMaterial(UMaterialInterface Material)
```
Set an active secondary render material.

### SetShadowsEnabled
```angelscript
void SetShadowsEnabled(bool bEnabled)
```

### SetVertexColorSpaceTransformMode
```angelscript
void SetVertexColorSpaceTransformMode(EDynamicMeshVertexColorTransformMode NewMode)
```
Configure the active Color Space Transform Mode

### SetViewModeOverridesEnabled
```angelscript
void SetViewModeOverridesEnabled(bool bEnabled)
```


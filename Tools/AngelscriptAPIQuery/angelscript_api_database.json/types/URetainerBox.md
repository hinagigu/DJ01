# URetainerBox

**继承自**: `UContentWidget`

The Retainer Box renders children widgets to a render target first before
later rendering that render target to the screen.  This allows both frequency
and phase to be controlled so that the UI can actually render less often than the
frequency of the main game render.  It also has the side benefit of allow materials
to be applied to the render target after drawing the widgets to apply a simple post process.

* Single Child
* Caching / Performance

## 属性

### RenderOnInvalidation
- **类型**: `bool`

### RenderOnPhase
- **类型**: `bool`

### Phase
- **类型**: `int`

### PhaseCount
- **类型**: `int`

### bShowEffectsInDesigner
- **类型**: `bool`

### bRetainRender
- **类型**: `bool`

### TextureParameter
- **类型**: `FName`

## 方法

### GetEffectMaterial
```angelscript
UMaterialInstanceDynamic GetEffectMaterial()
```
Get the current dynamic effect material applied to the retainer box.

### RequestRender
```angelscript
void RequestRender()
```
Requests the retainer redrawn the contents it has.

### SetEffectMaterial
```angelscript
void SetEffectMaterial(UMaterialInterface EffectMaterial)
```
Set a new effect material to the retainer widget.

### SetRenderingPhase
```angelscript
void SetRenderingPhase(int RenderPhase, int TotalPhases)
```
Requests the retainer redrawn the contents it has.

### SetRetainRendering
```angelscript
void SetRetainRendering(bool bInRetainRendering)
```
Set the flag for if we retain the render or pass-through

### SetTextureParameter
```angelscript
void SetTextureParameter(FName TextureParameter)
```
Sets the name of the texture parameter to set the render target to on the material.


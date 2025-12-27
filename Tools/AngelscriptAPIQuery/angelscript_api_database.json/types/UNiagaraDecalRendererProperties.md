# UNiagaraDecalRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### Material
- **类型**: `UMaterialInterface`
- **描述**: What material to use for the decal.

### MaterialParameterBinding
- **类型**: `FNiagaraParameterBinding`
- **描述**: Binding to material.

### SourceMode
- **类型**: `ENiagaraRendererSourceDataMode`
- **描述**: Whether or not to draw a single element for the Emitter or to draw the particles.

### RendererVisibility
- **类型**: `int`
- **描述**: If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.

### DecalScreenSizeFade
- **类型**: `float32`
- **描述**: When the decal is smaller than this screen size fade out the decal, can be used to reduce the amount of small decals drawn.

### MaterialParameters
- **类型**: `FNiagaraRendererMaterialParameters`
- **描述**: If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.


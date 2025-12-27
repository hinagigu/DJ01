# UNiagaraVolumeRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### Material
- **类型**: `UMaterialInterface`
- **描述**: What material to use for the volume.

### MaterialParameterBinding
- **类型**: `FNiagaraParameterBinding`
- **描述**: Binding to material.

### RendererVisibility
- **类型**: `int`
- **描述**: If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.

### StepFactor
- **类型**: `float32`

### LightingDownsampleFactor
- **类型**: `float32`

### ShadowStepFactor
- **类型**: `float32`

### ShadowBiasFactor
- **类型**: `float32`

### MaterialParameters
- **类型**: `FNiagaraRendererMaterialParameters`
- **描述**: If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.


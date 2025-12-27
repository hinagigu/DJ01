# UNiagaraGeometryCacheRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### GeometryCaches
- **类型**: `TArray<FNiagaraGeometryCacheReference>`
- **描述**: Reference to the geometry cache assets to use. If ArrayIndexBinding is not set, a random element is used for each particle.

### SourceMode
- **类型**: `ENiagaraRendererSourceDataMode`
- **描述**: Whether or not to draw a single element for the Emitter or to draw the particles.

### bIsLooping
- **类型**: `bool`
- **描述**: If true, then the geometry cache keeps playing in a loop

### ComponentCountLimit
- **类型**: `uint`
- **描述**: The max number of components that this emitter will spawn or update each frame.

### RendererVisibility
- **类型**: `int`
- **描述**: If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.

### bAssignComponentsOnParticleID
- **类型**: `bool`
- **描述**: If true then components will not be automatically assigned to the first particle available, but try to stick to the same particle based on its unique id.
Disabling this option is faster, but a particle can get a different component each tick, which can lead to problems with for example motion blur.

### MaterialParameters
- **类型**: `FNiagaraRendererMaterialParameters`
- **描述**: If this array has entries, we will create a MaterialInstanceDynamic per Emitter instance from Material and set the Material parameters using the Niagara simulation variables listed.


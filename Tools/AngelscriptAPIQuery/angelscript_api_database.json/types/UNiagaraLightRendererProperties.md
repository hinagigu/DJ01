# UNiagaraLightRendererProperties

**继承自**: `UNiagaraRendererProperties`

## 属性

### SourceMode
- **类型**: `ENiagaraRendererSourceDataMode`
- **描述**: Whether or not to draw a single element for the Emitter or to draw the particles.

### RadiusScale
- **类型**: `float32`
- **描述**: A factor used to scale each particle light radius

### DefaultExponent
- **类型**: `float32`
- **描述**: The exponent to use for all lights if no exponent binding was found

### SpecularScale
- **类型**: `float32`
- **描述**: The specular scale to use for all lights if no binding was found

### ColorAdd
- **类型**: `FVector3f`
- **描述**: A static color shift applied to each rendered light

### InverseExposureBlend
- **类型**: `float32`

### RendererVisibility
- **类型**: `int`
- **描述**: If a render visibility tag is present, particles whose tag matches this value will be visible in this renderer.

### bUseInverseSquaredFalloff
- **类型**: `bool`

### bAffectsTranslucency
- **类型**: `bool`

### bAlphaScalesBrightness
- **类型**: `bool`

### bOverrideInverseExposureBlend
- **类型**: `bool`


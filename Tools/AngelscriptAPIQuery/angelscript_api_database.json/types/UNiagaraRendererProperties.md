# UNiagaraRendererProperties

**继承自**: `UNiagaraMergeable`

Emitter properties base class
Each EmitterRenderer derives from this with its own class, and returns it in GetProperties; a copy
of those specific properties is stored on UNiagaraEmitter (on the System) for serialization
and handed back to the System renderer on load.

## 属性

### Platforms
- **类型**: `FNiagaraPlatformSet`
- **描述**: Platforms on which this renderer is enabled.

### SortOrderHint
- **类型**: `int`
- **描述**: By default, emitters are drawn in the order that they are added to the system. This value will allow you to control the order in a more fine-grained manner.
      Materials of the same type (i.e. Transparent) will draw in order from lowest to highest within the system. The default value is 0.

### MotionVectorSetting
- **类型**: `ENiagaraRendererMotionVectorSetting`
- **描述**: Hint about how to generate motion (velocity) vectors for this renderer.

### bAllowInCullProxies
- **类型**: `bool`


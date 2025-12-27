# UParticleEmitter

**继承自**: `UObject`

## 属性

### EmitterName
- **类型**: `FName`
- **描述**: The name of the emitter.

### EmitterRenderMode
- **类型**: `EEmitterRenderMode`
- **描述**: How to render the emitter particles. Can be one of the following:
        ERM_Normal      - As the intended sprite/mesh
        ERM_Point       - As a 2x2 pixel block with no scaling and the color set in EmitterEditorColor
        ERM_Cross       - As a cross of lines, scaled to the size of the particle in EmitterEditorColor
        ERM_None        - Do not render

### SignificanceLevel
- **类型**: `EParticleSignificanceLevel`
- **描述**: The significance level required of this emitter's owner for this emitter to be active.

### EmitterEditorColor
- **类型**: `FColor`
- **描述**: The color of the emitter in the curve editor and debug rendering modes.

### InitialAllocationCount
- **类型**: `int`
- **描述**: Initial allocation count - overrides calculated peak count if > 0

### QualityLevelSpawnRateScale
- **类型**: `float32`

### DetailModeBitmask
- **类型**: `uint`
- **描述**: Detail mode: Set flags reflecting which system detail mode you want the emitter to be ticked and rendered in

### bUseLegacySpawningBehavior
- **类型**: `bool`

### bDisabledLODsKeepEmitterAlive
- **类型**: `bool`

### bDisableWhenInsignficant
- **类型**: `bool`

### bCollapsed
- **类型**: `bool`


# UNiagaraValidationRule_RibbonRenderer

**继承自**: `UNiagaraValidationRule`

This validation rule is for ribbon renderers to ensure they are not used in situations that can cause compatability or performance issues.
i.e. Don't use a ribbon renderer with a GPU emitter / enable GPU ribbon init on lower end devices.

## 属性

### Severity
- **类型**: `ENiagaraValidationSeverity`

### bFailIfUsedByGPUSimulation
- **类型**: `bool`
- **描述**: When enable validation will fail if used by a GPU emitter.

### bFailIfUsedByGPUInit
- **类型**: `bool`
- **描述**: When enable validation will fail if used by a CPU emitter and GPU init is enabled on the renderer.

### Platforms
- **类型**: `FNiagaraPlatformSet`


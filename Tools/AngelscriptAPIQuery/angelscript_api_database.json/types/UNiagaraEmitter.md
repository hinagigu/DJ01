# UNiagaraEmitter

**继承自**: `UObject`

Niagara Emitters are particle spawners that can be reused for different effects by putting them into Niagara Systems.
Emitters render their particles using different renderers, such as Sprite Renderers or Mesh Renderers to produce different effects.

## 属性

### bIsInheritable
- **类型**: `bool`
- **描述**: If an emitter is inheritable, new emitters based on an inheritable emitter, or Niagara Systems using an inheritable emitter, will automatically inherit changes made to the original emitter.

### TemplateAssetDescription
- **类型**: `FText`


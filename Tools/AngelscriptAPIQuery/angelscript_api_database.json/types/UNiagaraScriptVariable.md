# UNiagaraScriptVariable

**继承自**: `UObject`

* Used to store variable data and metadata per graph.

## 属性

### DefaultMode
- **类型**: `ENiagaraDefaultMode`
- **描述**: The default mode. Can be Value, Binding or Custom.

### DefaultBinding
- **类型**: `FNiagaraScriptVariableBinding`
- **描述**: The default binding. Only used if DefaultMode == ENiagaraDefaultMode::Binding.

### Metadata
- **类型**: `FNiagaraVariableMetaData`
- **描述**: The metadata associated with this script variable.

### DefaultValueVariant
- **类型**: `FNiagaraVariant`


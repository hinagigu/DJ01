# UNiagaraDataInterfaceSimCacheReader

**继承自**: `UNiagaraDataInterface`

Data interface to read properties from a Niagara Simulation Cache

## 属性

### SimCacheBinding
- **类型**: `FNiagaraUserParameterBinding`
- **描述**: User parameter Object binding if this is not a valid sim cache the default one will be used instead.

### SimCache
- **类型**: `UNiagaraSimCache`
- **描述**: Optional source SimCache to use, if the user parameter binding is valid this will be ignored.

### EmitterBinding
- **类型**: `FName`
- **描述**: Which Emitter we should read from within the SimCache.


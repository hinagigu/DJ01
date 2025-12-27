# FNiagaraOutlinerFilterSettings

View settings used in the Niagara Outliner.

## 属性

### SystemExecutionState
- **类型**: `ENiagaraExecutionState`
- **描述**: Only show systems with the following execution state.

### EmitterExecutionState
- **类型**: `ENiagaraExecutionState`
- **描述**: Only show emitters with the following execution state.

### EmitterSimTarget
- **类型**: `ENiagaraSimTarget`
- **描述**: Only show emitters with this SimTarget.

### bSystemCullState
- **类型**: `bool`
- **描述**: Only show system instances with this cull state.

### bFilterBySystemExecutionState
- **类型**: `bool`

### bFilterByEmitterExecutionState
- **类型**: `bool`

### bFilterByEmitterSimTarget
- **类型**: `bool`

### bFilterBySystemCullState
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraOutlinerFilterSettings& opAssign(FNiagaraOutlinerFilterSettings Other)
```


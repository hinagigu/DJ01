# FNiagaraDebuggerRequestConnection

Messaged broadcast from debugger to request a connection to a particular session.
If any matching client is found and it accepts, it will return a FNiagaraDebuggerAcceptConnection message to the sender.

## 属性

### SessionId
- **类型**: `FGuid`

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FNiagaraDebuggerRequestConnection& opAssign(FNiagaraDebuggerRequestConnection Other)
```


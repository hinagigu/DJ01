# UNiagaraDataInterfaceSimpleCounter

**继承自**: `UNiagaraDataInterfaceRWBase`

Thread safe counter starts at the initial value on start / reset.
When operating between CPU & GPU ensure you set the appropriate sync mode.

## 属性

### GpuSyncMode
- **类型**: `ENiagaraGpuSyncMode`
- **描述**: Select how we should synchronize the counter between Cpu & Gpu

### InitialValue
- **类型**: `int`
- **描述**: This is the value the counter will have when the instance is reset / created.


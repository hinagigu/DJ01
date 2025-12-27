# UNiagaraDataInterfaceMemoryBuffer

**继承自**: `UNiagaraDataInterface`

Data interface used to access a memory buffer.
The user is responsible for how data is read / wrote.
The DI will ensure no out of bounds access but not that the elements are of the correct type (i.e. float or int)
Elements are considered to be 4 bytes in size.

## 属性

### DefaultNumElements
- **类型**: `int`
- **描述**: Default space we will allocate for the memory buffer.

### GpuSyncMode
- **类型**: `ENiagaraGpuSyncMode`
- **描述**: How should we synhronize the data between CPU and GPU memory.


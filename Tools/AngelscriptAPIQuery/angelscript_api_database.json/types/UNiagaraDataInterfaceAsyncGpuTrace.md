# UNiagaraDataInterfaceAsyncGpuTrace

**继承自**: `UNiagaraDataInterface`

Data interface for handling latent (delayed 1 frame) traces against the scene for GPU simulations.

## 属性

### MaxTracesPerParticle
- **类型**: `int`
- **描述**: The maximum number of traces (per particle) that can be created per frame.  Defines the size of the preallocated
              buffer that is used to contain the traces.

### MaxRetraces
- **类型**: `int`
- **描述**: If a collision is rejected, how many times do we attempt to retrace from that collision point forward to find a new, valid collision.

### TraceProvider
- **类型**: `ENDICollisionQuery_AsyncGpuTraceProvider`
- **描述**: Defines which technique is used to resolve the trace - see 'AsyncGpuTraceDI/Provider Priority' in the Niagara project settings.


# __NiagaraSimCache

## 方法

### CaptureNiagaraSimCacheImmediate
```angelscript
bool CaptureNiagaraSimCacheImmediate(UNiagaraSimCache SimCache, FNiagaraSimCacheCreateParameters CreateParameters, UNiagaraComponent NiagaraComponent, UNiagaraSimCache& OutSimCache, bool bAdvanceSimulation, float32 AdvanceDeltaTime)
```
Captures the simulations current frame data into the SimCache.
This happens immediately so you may need to be careful with tick order of the component you are capturing from.
The return can be invalid if the component can not be captured for some reason (i.e. not active).
When AdvanceSimulation is true we will manually advance the simulation one frame using the provided AdvanceDeltaTime before capturing.

### CreateNiagaraSimCache
```angelscript
UNiagaraSimCache CreateNiagaraSimCache()
```
Captures the simulation cache object that can be captured into using the various API calls.


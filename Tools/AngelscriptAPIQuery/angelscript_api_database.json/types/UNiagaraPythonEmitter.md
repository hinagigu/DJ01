# UNiagaraPythonEmitter

**继承自**: `UObject`

Wrapper for an emitter stack.

## 方法

### GetModule
```angelscript
UNiagaraPythonModule GetModule(FString ModuleName)
```
returns a module by name

### GetModules
```angelscript
TArray<UNiagaraPythonModule> GetModules()
```
returns a list of all modules contained in this emitter

### GetObject
```angelscript
UNiagaraEmitter GetObject()
```
Returns the raw underlying object

### GetProperties
```angelscript
FVersionedNiagaraEmitterData GetProperties()
```
returns the emitter properties, such as determinism or interpolated spawning

### HasModule
```angelscript
bool HasModule(FString ModuleName)
```
returns true if the emitter contains a certain module

### SetProperties
```angelscript
void SetProperties(FVersionedNiagaraEmitterData Data)
```
sets the new emitter properties


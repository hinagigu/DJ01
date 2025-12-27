# UNiagaraBaselineController

**继承自**: `UObject`

Base class for baseline controllers. These can are responsible for spawning and manipulating the FX needed for the baseline perf tests.

## 属性

### TestDuration
- **类型**: `float32`

### EffectType
- **类型**: `UNiagaraEffectType`
- **描述**: The effect type this controller is in use by.

### Owner
- **类型**: `ANiagaraPerfBaselineActor`
- **描述**: The owning actor for this baseline controller.

### System
- **类型**: `TSoftObjectPtr<UNiagaraSystem>`

## 方法

### GetSystem
```angelscript
UNiagaraSystem GetSystem()
```
Returns the System for this baseline. Will synchronously load the system if needed.

### OnBeginTest
```angelscript
void OnBeginTest()
```
Called from the stats system when we begin gathering stats for the given System asset.

### OnEndTest
```angelscript
void OnEndTest(FNiagaraPerfBaselineStats Stats)
```
Called from the stats system on completion of the test with the final stats for the given system asset.

### OnOwnerTick
```angelscript
void OnOwnerTick(float DeltaTime)
```
Called when the owning actor is ticked.

### OnTickTest
```angelscript
bool OnTickTest()
```
Returns whether the baseline test is complete.


# UNiagaraParticleCallbackHandler

**继承自**: `UInterface`

## 方法

### ParticleData
```angelscript
void ParticleData(TArray<FBasicParticleData> Data, UNiagaraSystem NiagaraSystem, FVector SimulationPositionOffset)
```
This function is called once per tick with the gathered particle data. It will not be called if there is no particle data to call it with.


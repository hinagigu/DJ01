# UAnimNotifyState_TimedNiagaraEffect

**继承自**: `UAnimNotifyState`

Timed Niagara Effect Notify
Allows a looping Niagara effect to be played in an animation that will activate
at the beginning of the notify and deactivate at the end.

## 属性

### Template
- **类型**: `UNiagaraSystem`

### SocketName
- **类型**: `FName`

### LocationOffset
- **类型**: `FVector`

### RotationOffset
- **类型**: `FRotator`

### bApplyRateScaleAsTimeDilation
- **类型**: `bool`

### bDestroyAtEnd
- **类型**: `bool`

## 方法

### GetSpawnedEffect
```angelscript
UFXSystemComponent GetSpawnedEffect(UMeshComponent MeshComp)
```
Return FXSystemComponent created from SpawnEffect


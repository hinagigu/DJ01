# ULODSyncComponent

**继承自**: `UActorComponent`

Implement an Actor component for LOD Sync of different components

This is a component that allows multiple different components to sync together of their LOD

This allows to find the highest LOD of all the parts, and sync to that LOD

## 属性

### NumLODs
- **类型**: `int`

### ForcedLOD
- **类型**: `int`

### MinLOD
- **类型**: `int`

### ComponentsToSync
- **类型**: `TArray<FComponentSync>`

### CustomLODMapping
- **类型**: `TMap<FName,FLODMappingData>`

## 方法

### GetLODSyncDebugText
```angelscript
FString GetLODSyncDebugText()
```
Returns a string detailing


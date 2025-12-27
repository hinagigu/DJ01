# FRuntimePartitionHLODSetup

Holds an HLOD setup for a particular partition class.

## 属性

### Name
- **类型**: `FName`
- **描述**: Name for this HLOD layer setup

### HLODLayers
- **类型**: `TArray<TObjectPtr<UHLODLayer>>`
- **描述**: Associated HLOD Layer objects

### bIsSpatiallyLoaded
- **类型**: `bool`
- **描述**: whether this HLOD setup is spatially loaded or not

### PartitionLayer
- **类型**: `URuntimePartition`

## 方法

### opAssign
```angelscript
FRuntimePartitionHLODSetup& opAssign(FRuntimePartitionHLODSetup Other)
```


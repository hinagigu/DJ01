# FRuntimePartitionDesc

Holds settings for a runtime partition instance.

## 属性

### Class
- **类型**: `TSubclassOf<URuntimePartition>`
- **描述**: Partition class

### Name
- **类型**: `FName`
- **描述**: Name for this partition, used to map actors to it through the Actor.RuntimeGrid property

### MainLayer
- **类型**: `URuntimePartition`
- **描述**: Main partition object

### HLODSetups
- **类型**: `TArray<FRuntimePartitionHLODSetup>`
- **描述**: HLOD setups used by this partition, one for each layers in the hierarchy

## 方法

### opAssign
```angelscript
FRuntimePartitionDesc& opAssign(FRuntimePartitionDesc Other)
```


# UHLODLayer

**继承自**: `UObject`

## 属性

### LayerType
- **类型**: `EHLODLayerType`
- **描述**: Type of HLOD generation to use

### HLODBuilderClass
- **类型**: `TSubclassOf<UHLODBuilder>`
- **描述**: HLOD Builder class

### CellSize
- **类型**: `int`
- **描述**: Cell size of the runtime grid created to encompass HLOD actors generated for this HLOD Layer

### LoadingRange
- **类型**: `float`
- **描述**: Loading range of the runtime grid created to encompass HLOD actors generated for this HLOD Layer

### ParentLayer
- **类型**: `UHLODLayer`
- **描述**: HLOD Layer to assign to the generated HLOD actors

### HLODActorClass
- **类型**: `TSubclassOf<AWorldPartitionHLOD>`
- **描述**: Specify a custom HLOD Actor class, the default is AWorldPartitionHLOD

### HLODModifierClass
- **类型**: `TSubclassOf<UWorldPartitionHLODModifier>`
- **描述**: HLOD Modifier class, to allow changes to the HLOD at runtime

### bIsSpatiallyLoaded
- **类型**: `bool`


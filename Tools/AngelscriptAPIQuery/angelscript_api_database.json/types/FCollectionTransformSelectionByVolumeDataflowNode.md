# FCollectionTransformSelectionByVolumeDataflowNode

Selects pieces based on their volume

## 属性

### VolumeMin
- **类型**: `float32`
- **描述**: Minimum volume for the selection

### VolumeMax
- **类型**: `float32`
- **描述**: Maximum volume for the selection

### RangeSetting
- **类型**: `ERangeSettingEnum`
- **描述**: Values for the selection has to be inside or outside [Min, Max] range

### bInclusive
- **类型**: `bool`
- **描述**: If true then range includes Min and Max values

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCollectionTransformSelectionByVolumeDataflowNode& opAssign(FCollectionTransformSelectionByVolumeDataflowNode Other)
```


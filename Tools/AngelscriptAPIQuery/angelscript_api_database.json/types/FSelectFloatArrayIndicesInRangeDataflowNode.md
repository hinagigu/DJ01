# FSelectFloatArrayIndicesInRangeDataflowNode

Selects indices of a float array by range

## 属性

### Min
- **类型**: `float32`
- **描述**: Minimum value for the selection

### Max
- **类型**: `float32`
- **描述**: Maximum value for the selection

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
FSelectFloatArrayIndicesInRangeDataflowNode& opAssign(FSelectFloatArrayIndicesInRangeDataflowNode Other)
```


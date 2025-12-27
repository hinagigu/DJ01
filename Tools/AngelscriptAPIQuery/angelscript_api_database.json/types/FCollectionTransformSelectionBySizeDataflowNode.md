# FCollectionTransformSelectionBySizeDataflowNode

Selects pieces based on their size

## 属性

### SizeMin
- **类型**: `float32`
- **描述**: Minimum size for the selection

### SizeMax
- **类型**: `float32`
- **描述**: Maximum size for the selection

### RangeSetting
- **类型**: `ERangeSettingEnum`
- **描述**: Values for the selection has to be inside or outside [Min, Max] range

### bInclusive
- **类型**: `bool`
- **描述**: If true then range includes Min and Max values

### bUseRelativeSize
- **类型**: `bool`
- **描述**: Whether to use the 'Relative Size' -- i.e., the Size / Largest Bone Size. Otherwise, Size is the cube root of Volume.

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FCollectionTransformSelectionBySizeDataflowNode& opAssign(FCollectionTransformSelectionBySizeDataflowNode Other)
```


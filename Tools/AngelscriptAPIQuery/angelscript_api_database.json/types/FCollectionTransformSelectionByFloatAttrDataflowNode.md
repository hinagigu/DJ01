# FCollectionTransformSelectionByFloatAttrDataflowNode

Selects bones by a float attribute

## 属性

### AttrName
- **类型**: `FString`
- **描述**: Attribute name

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
FCollectionTransformSelectionByFloatAttrDataflowNode& opAssign(FCollectionTransformSelectionByFloatAttrDataflowNode Other)
```


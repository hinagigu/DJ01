# FFieldMakeDenseFloatArrayDataflowNode

Converts a sparse FloatArray (a selected subset of the whole incoming array) into a dense FloatArray
(same number of elements as the incoming array using NumSamplePositions) using the Remap input
NumSamplePositions controls the size of the output array, only indices smaller than l to than NumSamplePositions
will be processed

## 属性

### NumSamplePositions
- **类型**: `int`

### Default
- **类型**: `float32`

### bActive
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FFieldMakeDenseFloatArrayDataflowNode& opAssign(FFieldMakeDenseFloatArrayDataflowNode Other)
```


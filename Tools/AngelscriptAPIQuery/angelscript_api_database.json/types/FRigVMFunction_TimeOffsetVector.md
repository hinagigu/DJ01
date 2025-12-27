# FRigVMFunction_TimeOffsetVector

Records a value over time and can access the value from the past

## 属性

### Value
- **类型**: `FVector`

### SecondsAgo
- **类型**: `float32`

### BufferSize
- **类型**: `int`
- **描述**: The sampling precision of the buffer. The higher the more precise - the more memory usage.

### TimeRange
- **类型**: `float32`
- **描述**: The maximum time required for offsetting in seconds.

### Result
- **类型**: `FVector`

## 方法

### opAssign
```angelscript
FRigVMFunction_TimeOffsetVector& opAssign(FRigVMFunction_TimeOffsetVector Other)
```


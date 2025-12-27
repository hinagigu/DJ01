# FRigVMFunction_TimeLoop

Simulates a time value - and outputs loop information

## 属性

### Speed
- **类型**: `float32`

### Duration
- **类型**: `float32`

### Normalize
- **类型**: `bool`

### Absolute
- **类型**: `float32`
- **描述**: the overall time in seconds

### Relative
- **类型**: `float32`
- **描述**: the relative time in seconds (within the loop)

### FlipFlop
- **类型**: `float32`
- **描述**: the relative time in seconds (within the loop),
going from 0 to duration and then back from duration to 0,
or 0 to 1 and 1 to 0 if Normalize is turned on

### Even
- **类型**: `bool`
- **描述**: true if the iteration of the loop is even

## 方法

### opAssign
```angelscript
FRigVMFunction_TimeLoop& opAssign(FRigVMFunction_TimeLoop Other)
```


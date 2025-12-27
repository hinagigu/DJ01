# FModulatorContinuousParams

## 属性

### ParameterName
- **类型**: `FName`

### Default
- **类型**: `float32`
- **描述**: The default value to be used if the parameter is not found.

### MinInput
- **类型**: `float32`
- **描述**: The minimum input value. Values will be clamped to the [MinInput, MaxInput] range.

### MaxInput
- **类型**: `float32`
- **描述**: The maximum input value. Values will be clamped to the [MinInput, MaxInput] range.

### MinOutput
- **类型**: `float32`
- **描述**: The minimum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput]

### MaxOutput
- **类型**: `float32`
- **描述**: The maximum output value. The input value will be scaled from the range [MinInput, MaxInput] to [MinOut, MaxOutput]

### ParamMode
- **类型**: `ModulationParamMode`
- **描述**: The mode with which to treat the input value

## 方法

### opAssign
```angelscript
FModulatorContinuousParams& opAssign(FModulatorContinuousParams Other)
```


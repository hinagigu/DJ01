# FInputAxisProperties

Configurable properties for control axes, used to transform raw input into game ready values.

## 属性

### DeadZone
- **类型**: `float32`
- **描述**: What the dead zone of the axis is.  For control axes such as analog sticks.

### Sensitivity
- **类型**: `float32`
- **描述**: Scaling factor to multiply raw value by.

### Exponent
- **类型**: `float32`
- **描述**: For applying curves to [0..1] axes, e.g. analog sticks

### bInvert
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FInputAxisProperties& opAssign(FInputAxisProperties Other)
```


# FNiagaraPlatformSetCVarCondition

Imposes a condition that a CVar must contain a set value or range of values for a platform set to be enabled.

## 属性

### CVarName
- **类型**: `FName`
- **描述**: The name of the CVar we're testing the value of.

### PassResponse
- **类型**: `ENiagaraCVarConditionResponse`
- **描述**: If this CVar condition passes, how should this affect the state of the Platform Set?

### FailResponse
- **类型**: `ENiagaraCVarConditionResponse`
- **描述**: If this CVar condition fails, how should this affect the state of the Platform Set?

### Value
- **类型**: `bool`
- **描述**: The value this CVar must contain for this platform set to be enabled.

### MinInt
- **类型**: `int`
- **描述**: If the value of the CVar is less than this minimum then the PlatformSet will not be enabled.

### MaxInt
- **类型**: `int`
- **描述**: If the value of the CVar is greater than this maximum then the PlatformSet will not be enabled.

### MinFloat
- **类型**: `float32`
- **描述**: If the value of the CVar is less than this minimum then the PlatformSet will not be enabled.

### MaxFloat
- **类型**: `float32`
- **描述**: If the value of the CVar is greater than this maximum then the PlatformSet will not be enabled.

### bUseMinInt
- **类型**: `bool`

### bUseMaxInt
- **类型**: `bool`

### bUseMinFloat
- **类型**: `bool`

### bUseMaxFloat
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraPlatformSetCVarCondition& opAssign(FNiagaraPlatformSetCVarCondition Other)
```


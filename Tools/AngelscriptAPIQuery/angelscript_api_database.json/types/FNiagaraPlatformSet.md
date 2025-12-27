# FNiagaraPlatformSet

## 属性

### DeviceProfileStates
- **类型**: `TArray<FNiagaraDeviceProfileStateEntry>`
- **描述**: States of specific device profiles we've set.

### CVarConditions
- **类型**: `TArray<FNiagaraPlatformSetCVarCondition>`
- **描述**: Set of CVars values we require for this platform set to be enabled. If any of the linked CVars don't have the required values then this platform set will not be enabled.

### QualityLevelMask
- **类型**: `int`
- **描述**: Mask defining which effects qualities this set matches.

## 方法

### opAssign
```angelscript
FNiagaraPlatformSet& opAssign(FNiagaraPlatformSet Other)
```


# FNiagaraPlatformSetRedirect

Allows us to replace a specific device profile usage condition in all NiagaraPlatformSets.
Helpful when dealing with changes to device profile structure.

## 属性

### ProfileNames
- **类型**: `TArray<FName>`
- **描述**: The names of any device profile entry that will apply this redirect.

### Mode
- **类型**: `ENiagaraDeviceProfileRedirectMode`

### RedirectProfileName
- **类型**: `FName`
- **描述**: When in Device Profile mode, the name of the device profile to redirect to.

### CVarConditionEnabled
- **类型**: `FNiagaraPlatformSetCVarCondition`
- **描述**: When in CVar mode, the CVar condition to replace this device profile entry with when the profile entry is in the Enabled state.

### CVarConditionDisabled
- **类型**: `FNiagaraPlatformSetCVarCondition`
- **描述**: When in CVar mode, the CVar condition to replace this device profile entry with when the profile entry is in the Disabled state.

## 方法

### opAssign
```angelscript
FNiagaraPlatformSetRedirect& opAssign(FNiagaraPlatformSetRedirect Other)
```


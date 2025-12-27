# FNiagaraSystemScalabilityOverride

## 属性

### Platforms
- **类型**: `FNiagaraPlatformSet`
- **描述**: The platforms on which these settings are active (unless overridden).

### MaxDistance
- **类型**: `float32`
- **描述**: Effects of this type are culled beyond this distance.

### MaxInstances
- **类型**: `int`
- **描述**: Effects of this type will be culled when total active instances using this same EffectType exceeds this number.
If the effect type has a significance handler, instances are sorted by their significance and only the N most significant will be kept. The rest are culled.
If it does not have a significance handler, instance count culling will be applied at spawn time only. New FX that would exceed the counts are not spawned/activated.

### MaxSystemInstances
- **类型**: `int`
- **描述**: Effects of this type will be culled when total active instances of the same NiagaraSystem exceeds this number.
If the effect type has a significance handler, instances are sorted by their significance and only the N most significant will be kept. The rest are culled.
If it does not have a significance handler, instance count culling will be applied at spawn time only. New FX that would exceed the counts are not spawned/activated.

### CullProxyMode
- **类型**: `ENiagaraCullProxyMode`
- **描述**: Controls what, if any, proxy will be used in place of culled systems.

### MaxSystemProxies
- **类型**: `int`
- **描述**: Limit on the number of proxies that can be used at once per system.
While much cheaper than full FX instances, proxies still incur some cost so must have a limit.
When significance information is available using a significance handler, the most significance proxies will be kept up to this limit.

### VisibilityCulling
- **类型**: `FNiagaraSystemVisibilityCullingSettings`
- **描述**: Settings controlling how systems are culled by visibility.

### BudgetScaling
- **类型**: `FNiagaraGlobalBudgetScaling`
- **描述**: Settings related to scaling down FX based on the current budget usage.

### bOverrideDistanceSettings
- **类型**: `bool`

### bOverrideInstanceCountSettings
- **类型**: `bool`

### bOverridePerSystemInstanceCountSettings
- **类型**: `bool`

### bOverrideVisibilitySettings
- **类型**: `bool`

### bOverrideGlobalBudgetScalingSettings
- **类型**: `bool`

### bOverrideCullProxySettings
- **类型**: `bool`

### bCullByDistance
- **类型**: `bool`

### bCullMaxInstanceCount
- **类型**: `bool`

### bCullPerSystemMaxInstanceCount
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraSystemScalabilityOverride& opAssign(FNiagaraSystemScalabilityOverride Other)
```


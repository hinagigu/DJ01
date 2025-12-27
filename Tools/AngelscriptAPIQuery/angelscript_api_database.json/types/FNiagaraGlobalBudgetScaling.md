# FNiagaraGlobalBudgetScaling

## 属性

### MaxGlobalBudgetUsage
- **类型**: `float32`
- **描述**: Effects will be culled if the global budget usage exceeds this fraction. A global budget usage of 1.0 means current global FX workload has reached it's max budget. Budgets are set by CVars under FX.Budget...

### MaxDistanceScaleByGlobalBudgetUse
- **类型**: `FNiagaraLinearRamp`
- **描述**: When enabled, MaxDistance is scaled down by the global budget use based on this curve. Allows us to cull more aggressively when performance is poor.

### MaxInstanceCountScaleByGlobalBudgetUse
- **类型**: `FNiagaraLinearRamp`
- **描述**: When enabled, Max Effect Type Instances is scaled down by the global budget use based on this curve. Allows us to cull more aggressively when performance is poor.

### MaxSystemInstanceCountScaleByGlobalBudgetUse
- **类型**: `FNiagaraLinearRamp`
- **描述**: When enabled, Max System Instances is scaled down by the global budget use based on this curve. Allows us to cull more aggressively when performance is poor.

### bCullByGlobalBudget
- **类型**: `bool`

### bScaleMaxDistanceByGlobalBudgetUse
- **类型**: `bool`

### bScaleMaxInstanceCountByGlobalBudgetUse
- **类型**: `bool`

### bScaleSystemInstanceCountByGlobalBudgetUse
- **类型**: `bool`

## 方法

### opAssign
```angelscript
FNiagaraGlobalBudgetScaling& opAssign(FNiagaraGlobalBudgetScaling Other)
```


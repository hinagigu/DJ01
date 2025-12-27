# FNiagaraInputConditionMetadata

Defines options for conditionally editing and showing script inputs in the UI.

## 属性

### InputName
- **类型**: `FName`
- **描述**: The name of the input to use for matching the target values.

### TargetValues
- **类型**: `TArray<FString>`
- **描述**: The list of target values which will satisfy the input condition.  If this is empty it's assumed to be a single value of "true" for matching bool inputs.

## 方法

### opAssign
```angelscript
FNiagaraInputConditionMetadata& opAssign(FNiagaraInputConditionMetadata Other)
```


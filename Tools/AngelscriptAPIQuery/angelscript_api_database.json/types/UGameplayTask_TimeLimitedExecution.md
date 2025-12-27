# UGameplayTask_TimeLimitedExecution

**继承自**: `UGameplayTask`

Adds time limit for running a child task
- child task needs to be created with UGameplayTask_TimeLimitedExecution passed as TaskOwner
- activations are tied together and when either UGameplayTask_TimeLimitedExecution or child task is activated, other one starts as well
- OnFinished and OnTimeExpired are mutually exclusive

## 属性

### OnFinished
- **类型**: `FTaskFinishDelegate__GameplayTask_TimeLimitedExecution`

### OnTimeExpired
- **类型**: `FTaskFinishDelegate__GameplayTask_TimeLimitedExecution`


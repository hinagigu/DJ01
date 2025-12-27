# UNiagaraValidationRule_SimulationStageBudget

**继承自**: `UNiagaraValidationRule`

This validation rule can be used to enforce a budget on the number of simulation stages and the iterations that may execute.

## 属性

### bMaxSimulationStagesEnabled
- **类型**: `bool`

### bMaxIterationsPerStageEnabled
- **类型**: `bool`

### bMaxTotalIterationsEnabled
- **类型**: `bool`

### Severity
- **类型**: `ENiagaraValidationSeverity`
- **描述**: How do we want to repro the error in the stack

### MaxSimulationStages
- **类型**: `int`
- **描述**: Maximum number of simulation stages allowed, where 0 means no simulation stages.

### MaxIterationsPerStage
- **类型**: `int`
- **描述**: Maximum number of iterations a single stage is allowed to execute.
Note: Can only check across explicit counts, dynamic bindings will be ignored.

### MaxTotalIterations
- **类型**: `int`
- **描述**: Maximum total iterations across all the enabled simulation stages.
Note: Can only check across explicit counts, dynamic bindings will be ignored.


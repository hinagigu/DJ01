# UNiagaraValidationRule_SingletonModule

**继承自**: `UNiagaraValidationRule`

This validation rule checks that a module is only used once per emitter/system stack.

## 属性

### Severity
- **类型**: `ENiagaraValidationSeverity`
- **描述**: How do we want to repro the error in the stack

### bCheckDetailedUsageContext
- **类型**: `bool`
- **描述**: If true then the check is not emitter-wide, but only within the same context (e.g. particle update).


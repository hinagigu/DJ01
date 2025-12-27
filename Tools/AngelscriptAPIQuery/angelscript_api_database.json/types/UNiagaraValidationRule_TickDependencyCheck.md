# UNiagaraValidationRule_TickDependencyCheck

**继承自**: `UNiagaraValidationRule`

Validation rule to check for unwanted tick dependencies.

## 属性

### Severity
- **类型**: `ENiagaraValidationSeverity`
- **描述**: How do we want to repro the error in the stack

### bCheckActorComponentInterface
- **类型**: `bool`
- **描述**: Check that the actor component interface isn't adding a tick dependency on the CPU.

### bCheckCameraDataInterface
- **类型**: `bool`
- **描述**: Check that the camera data interface isn't adding a tick dependency on the CPU.

### bCheckSkeletalMeshInterface
- **类型**: `bool`
- **描述**: Check that the skeletal mesh interface isn't adding a tick dependency on the CPU.

### EffectTypesToExclude
- **类型**: `TArray<TSoftObjectPtr<UNiagaraEffectType>>`
- **描述**: If the system uses one of these effect types the rule will not be run.


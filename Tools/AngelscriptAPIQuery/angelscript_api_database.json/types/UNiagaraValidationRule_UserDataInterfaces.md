# UNiagaraValidationRule_UserDataInterfaces

**继承自**: `UNiagaraValidationRule`

This validation rule checks to see if you have exposed user data interfaces.

## 属性

### bOnlyIncludeExposedUObjects
- **类型**: `bool`
- **描述**: Only include data interfaces that contain exposed UObject properties in them.

### BannedDataInterfaces
- **类型**: `TArray<TSubclassOf<UNiagaraDataInterface>>`
- **描述**: List data interfaces to validate against, if this list is empty all data interfaces will be included.

### AllowDataInterfaces
- **类型**: `TArray<TSubclassOf<UNiagaraDataInterface>>`
- **描述**: List data interfaces that we always allow.

### Severity
- **类型**: `ENiagaraValidationSeverity`
- **描述**: How do we want to repro the error in the stack


# UNiagaraValidationRule_BannedDataInterfaces

**继承自**: `UNiagaraValidationRule`

This validation rule can ban the use of certain data interfaces on all or a subset of platforms.

## 属性

### Severity
- **类型**: `ENiagaraValidationSeverity`

### bBanOnGpu
- **类型**: `bool`

### bBanOnCpu
- **类型**: `bool`

### Platforms
- **类型**: `FNiagaraPlatformSet`

### BannedDataInterfaces
- **类型**: `TArray<TSubclassOf<UNiagaraDataInterface>>`


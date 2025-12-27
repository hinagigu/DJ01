# FInputMappingContextAndPriority

## 属性

### InputMapping
- **类型**: `TSoftObjectPtr<UInputMappingContext>`

### Priority
- **类型**: `int`
- **描述**: Higher priority input mappings will be prioritized over mappings with a lower priority.

### bRegisterWithSettings
- **类型**: `bool`
- **描述**: If true, then this mapping context will be registered with the settings when this game feature action is registered.

## 方法

### opAssign
```angelscript
FInputMappingContextAndPriority& opAssign(FInputMappingContextAndPriority Other)
```


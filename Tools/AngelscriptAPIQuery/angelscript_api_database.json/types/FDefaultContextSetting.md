# FDefaultContextSetting

Represents a single input mapping context and the priority that it should be applied with

## 属性

### InputMappingContext
- **类型**: `TSoftObjectPtr<UInputMappingContext>`
- **描述**: Input Mapping Context that should be Added to the EnhancedInputEditorSubsystem when it starts listening for input

### Priority
- **类型**: `int`
- **描述**: The prioirty that should be given to this mapping context when it is added

### bAddImmediately
- **类型**: `bool`
- **描述**: If true, then this IMC will be applied immediately when the EI subsystem is ready

### bRegisterWithUserSettings
- **类型**: `bool`
- **描述**: If true, then this IMC will be registered with the User Input Settings (if one is available) immediately when the Enhanced Input subsystem starts.

## 方法

### opAssign
```angelscript
FDefaultContextSetting& opAssign(FDefaultContextSetting Other)
```


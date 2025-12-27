# FAutomationTestExcludeOptions

## 属性

### Reason
- **类型**: `FName`
- **描述**: Reason to why the test is excluded

### RHIs
- **类型**: `TSet<FName>`
- **描述**: Options to target specific RHI. No option means it should be applied to all RHIs

### Platforms
- **类型**: `TSet<FName>`
- **描述**: Options to target specific platform. No option means it should be applied to all platforms

### Warn
- **类型**: `bool`
- **描述**: Should the Reason be reported as a warning in the log

## 方法

### opAssign
```angelscript
FAutomationTestExcludeOptions& opAssign(FAutomationTestExcludeOptions Other)
```


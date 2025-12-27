# FSwarmTaskStateMessage

## 属性

### Guid
- **类型**: `FGuid`
- **描述**: The Task GUID used for identifying the Task

### State
- **类型**: `uint8`
- **描述**: The current state and arbitrary message

### Message
- **类型**: `FString`

### ExitCode
- **类型**: `int`
- **描述**: Various stats, including run time, exit codes, etc.

### RunningTime
- **类型**: `float`

## 方法

### opAssign
```angelscript
FSwarmTaskStateMessage& opAssign(FSwarmTaskStateMessage Other)
```


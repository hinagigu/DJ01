# FAutomationWorkerFindWorkers

Implements a message that is published to find automation workers.

## 属性

### Changelist
- **类型**: `int`
- **描述**: Holds the change list number to find workers for.

### GameName
- **类型**: `FString`
- **描述**: The name of the game.

### ProcessName
- **类型**: `FString`
- **描述**: The name of the process.

### SessionId
- **类型**: `FGuid`
- **描述**: Holds the session identifier to find workers for.

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerFindWorkers& opAssign(FAutomationWorkerFindWorkers Other)
```


# FAutomationWorkerRunTests

Implements a message to request the running of automation tests on a worker.

## 属性

### ExecutionCount
- **类型**: `uint`

### RoleIndex
- **类型**: `int`

### TestName
- **类型**: `FString`
- **描述**: Holds the name of the test to run.

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerRunTests& opAssign(FAutomationWorkerRunTests Other)
```


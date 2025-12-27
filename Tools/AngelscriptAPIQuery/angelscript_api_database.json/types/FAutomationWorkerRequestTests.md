# FAutomationWorkerRequestTests

Implements a message for requesting available automation tests from a worker.

## 属性

### DeveloperDirectoryIncluded
- **类型**: `bool`
- **描述**: Holds a flag indicating whether the developer directory should be included.

### RequestedTestFlags
- **类型**: `uint`
- **描述**: Holds a flag indicating which tests we'd like to request.

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerRequestTests& opAssign(FAutomationWorkerRequestTests Other)
```


# FAutomationWorkerFindWorkersResponse

Implements a message that is sent in response to FAutomationWorkerFindWorkers.

## 属性

### DeviceName
- **类型**: `FString`
- **描述**: Holds the name of the device that the worker is running on.

### InstanceName
- **类型**: `FString`
- **描述**: Holds the name of the worker's application instance.

### Platform
- **类型**: `FString`
- **描述**: Holds the name of the platform that the worker is running on.

### OSVersionName
- **类型**: `FString`
- **描述**: Holds the name of the operating system version.

### ModelName
- **类型**: `FString`
- **描述**: Holds the name of the device model.

### GPUName
- **类型**: `FString`
- **描述**: Holds the name of the GPU.

### CPUModelName
- **类型**: `FString`
- **描述**: Holds the name of the CPU model.

### RAMInGB
- **类型**: `uint`
- **描述**: Holds the amount of RAM this device has in gigabytes.

### RenderModeName
- **类型**: `FString`
- **描述**: Holds the name of the current render mode.

### SessionId
- **类型**: `FGuid`
- **描述**: Holds the worker's application session identifier.

### RHIName
- **类型**: `FString`
- **描述**: Holds the name of the current RHI.

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerFindWorkersResponse& opAssign(FAutomationWorkerFindWorkersResponse Other)
```


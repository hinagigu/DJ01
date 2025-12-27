# FAutomationWorkerTestDataRequest

Implements a message that handles both storing and requesting ground truth data.
for the first time this test is run, it might need to store things, or get things.

## 属性

### DataType
- **类型**: `FString`
- **描述**: The category of the data, this is purely to bucket and separate the ground truth data we store into different directories.

### DataPlatform
- **类型**: `FString`

### DataTestName
- **类型**: `FString`

### DataName
- **类型**: `FString`

### JsonData
- **类型**: `FString`

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerTestDataRequest& opAssign(FAutomationWorkerTestDataRequest Other)
```


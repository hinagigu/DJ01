# FAutomationWorkerScreenImage

Implements a message that is sent in containing a screen shot run during performance test.

## 属性

### ScreenImage
- **类型**: `TArray<uint8>`
- **描述**: The screen shot data.

### FrameTrace
- **类型**: `TArray<uint8>`
- **描述**: The frame trace data.

### ScreenShotName
- **类型**: `FString`
- **描述**: The screen shot name.

### Metadata
- **类型**: `FAutomationScreenshotMetadata`

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerScreenImage& opAssign(FAutomationWorkerScreenImage Other)
```


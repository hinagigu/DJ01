# FAutomationWorkerImageComparisonResults

Implements a message that is sent in containing a screen shot run during performance test.

## 属性

### UniqueId
- **类型**: `FGuid`
- **描述**: The unique id for the comparison.

### ScreenshotPath
- **类型**: `FString`
- **描述**: The path of the screenshot.

### bNew
- **类型**: `bool`
- **描述**: Was this a new image we've never seen before and have no ground truth for?

### bSimilar
- **类型**: `bool`
- **描述**: Were the images similar?  If they're not you should log an error.

### MaxLocalDifference
- **类型**: `float`

### GlobalDifference
- **类型**: `float`

### ErrorMessage
- **类型**: `FString`

### IncomingFilePath
- **类型**: `FString`

### ReportComparisonFilePath
- **类型**: `FString`

### ReportApprovedFilePath
- **类型**: `FString`

### ReportIncomingFilePath
- **类型**: `FString`

### InstanceId
- **类型**: `FGuid`

## 方法

### opAssign
```angelscript
FAutomationWorkerImageComparisonResults& opAssign(FAutomationWorkerImageComparisonResults Other)
```


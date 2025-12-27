# UControlRigTestData

**继承自**: `UObject`

## 属性

### ControlRigObjectPath
- **类型**: `FSoftObjectPath`

### Initial
- **类型**: `FControlRigTestDataFrame`

### InputFrames
- **类型**: `TArray<FControlRigTestDataFrame>`

### OutputFrames
- **类型**: `TArray<FControlRigTestDataFrame>`

### FramesToSkip
- **类型**: `TArray<int>`

### Tolerance
- **类型**: `float`

## 方法

### GetFrameIndexForTime
```angelscript
int GetFrameIndexForTime(float InSeconds, bool bInput)
```

### GetPlaybackMode
```angelscript
EControlRigTestDataPlaybackMode GetPlaybackMode()
```

### GetTimeRange
```angelscript
FVector2D GetTimeRange(bool bInput)
```

### IsRecording
```angelscript
bool IsRecording()
```

### IsReplaying
```angelscript
bool IsReplaying()
```

### Record
```angelscript
bool Record(UControlRig InControlRig, float InRecordingDuration)
```

### ReleaseReplay
```angelscript
void ReleaseReplay()
```

### SetupReplay
```angelscript
bool SetupReplay(UControlRig InControlRig, bool bGroundTruth)
```


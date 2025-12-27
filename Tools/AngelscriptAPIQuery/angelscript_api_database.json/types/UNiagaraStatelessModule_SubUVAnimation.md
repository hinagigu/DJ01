# UNiagaraStatelessModule_SubUVAnimation

**继承自**: `UNiagaraStatelessModule`

## 属性

### NumFrames
- **类型**: `int`

### bStartFrameRangeOverride_Enabled
- **类型**: `bool`

### bEndFrameRangeOverride_Enabled
- **类型**: `bool`

### StartFrameRangeOverride
- **类型**: `int`

### EndFrameRangeOverride
- **类型**: `int`

### AnimationMode
- **类型**: `ENSMSubUVAnimation_Mode`

### LoopsPerSecond
- **类型**: `float32`
- **描述**: -Note: Main module has PlaybackMode (Loops / FPS) to choose between loops or frames per second

### RandomChangeInterval
- **类型**: `float32`
- **描述**: -Note: Main module has a few more options
UPROPERTY(EditAnywhere, Category = "Parameters", meta = (EditConditionHides, EditCondition = "AnimationMode == ENSMSubUVAnimation_Mode::Linear"))
bool bRandomStartFrame = false;
int32 StartFrameOffset = 0;
float LoopupIndexScale = 0.0f;


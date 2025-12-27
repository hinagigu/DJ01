# USystemTimeTimecodeProvider

**继承自**: `UTimecodeProvider`

Converts the current system time to timecode, relative to a provided frame rate.

## 属性

### bGenerateFullFrame
- **类型**: `bool`
- **描述**: When generating frame time, should we generate full frame without subframe value.

### bUseHighPerformanceClock
- **类型**: `bool`
- **描述**: Use the high performance clock instead of the system time to generate the timecode value.
Using the high performance clock is faster but will make the value drift over time.

### FrameRate
- **类型**: `FFrameRate`


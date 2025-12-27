# UTimeSynchronizableMediaSource

**继承自**: `UBaseMediaSource`

Base class for media sources that can be synchronized with the engine's timecode.

## 属性

### bUseTimeSynchronization
- **类型**: `bool`

### FrameDelay
- **类型**: `int`
- **描述**: When using Time Synchronization, how many frame back should it read.

### TimeDelay
- **类型**: `float`
- **描述**: When not using Time Synchronization, how far back it time should it read.


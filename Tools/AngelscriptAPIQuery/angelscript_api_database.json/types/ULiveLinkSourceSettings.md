# ULiveLinkSourceSettings

**继承自**: `UObject`

Base class for live link source settings (can be replaced by sources themselves)

## 属性

### Mode
- **类型**: `ELiveLinkSourceMode`
- **描述**: The the subject how to create the frame snapshot.
@note A client may evaluate manually the subject in a different mode by using EvaluateFrameAtWorldTime or EvaluateFrameAtSceneTime.

### BufferSettings
- **类型**: `FLiveLinkSourceBufferManagementSettings`
- **描述**: How the frame buffers are managed.

### ConnectionString
- **类型**: `FString`
- **描述**: Connection information that is needed by the factory to recreate the source from a preset.


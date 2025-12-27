# URenderDocPluginSettings

**继承自**: `UDeveloperSettings`

## 属性

### CaptureDelay
- **类型**: `int`
- **描述**: If > 0, RenderDoc will trigger the capture only after this amount of frames/seconds has passed.

### CaptureFrameCount
- **类型**: `int`
- **描述**: If > 1, the RenderDoc capture will encompass more than a single frame. Note: this implies that all activity in all viewports and editor windows will be captured (i.e. same as CaptureAllActivity)

### RenderDocBinaryPath
- **类型**: `FString`
- **描述**: Path to the main RenderDoc executable to use.

### bCaptureAllActivity
- **类型**: `bool`

### bCaptureAllCallstacks
- **类型**: `bool`

### bReferenceAllResources
- **类型**: `bool`

### bSaveAllInitials
- **类型**: `bool`

### bCaptureDelayInSeconds
- **类型**: `bool`

### bAutoAttach
- **类型**: `bool`

### bShowHelpOnStartup
- **类型**: `bool`

### bEnableRenderDocCrashHandler
- **类型**: `bool`


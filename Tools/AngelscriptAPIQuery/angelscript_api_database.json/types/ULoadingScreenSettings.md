# ULoadingScreenSettings

**继承自**: `UDeveloperSettings`

Settings for the Loading Screen system

## 属性

### LoadingScreenWidget
- **类型**: `FSoftClassPath`
- **描述**: The widget to display for the loading screen

### LoadingScreenZOrder
- **类型**: `int`
- **描述**: The Z-order to use when adding the loading screen widget to the viewport

### HoldLoadingScreenAdditionalSecs
- **类型**: `float32`
- **描述**: How long to hold the loading screen up after other loading finishes (to allow texture streaming)

### HoldLoadingScreenAdditionalSecsEvenInEditor
- **类型**: `bool`
- **描述**: Should we hold the loading screen for texture streaming even in the editor?

### ForceTickLoadingScreenEvenInEditor
- **类型**: `bool`
- **描述**: Should we force tick the loading screen even in the editor?

### LogLoadingScreenHeartbeatInterval
- **类型**: `float32`
- **描述**: How often to log why the loading screen is still up (0 = never)

### LoadingScreenHeartbeatHangDuration
- **类型**: `float32`
- **描述**: How long before we consider the loading screen hung and trigger the hang detector


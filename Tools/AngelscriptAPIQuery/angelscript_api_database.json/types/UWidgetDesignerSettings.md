# UWidgetDesignerSettings

**继承自**: `UDeveloperSettings`

Implements the settings for the Widget Blueprint Designer.

## 属性

### bLockToPanelOnDragByDefault
- **类型**: `bool`

### DefaultPreviewResolution
- **类型**: `FUintVector2`
- **描述**: The default preview resolution in the designer.

### bShowOutlines
- **类型**: `bool`
- **描述**: Should the designer show outlines by default?

### bExecutePreConstructEvent
- **类型**: `bool`
- **描述**: Should the designer run the design event?  Disable this if you're seeing crashes in the designer,
you may have some unsafe code running in the designer.

### bRespectLocks
- **类型**: `bool`
- **描述**: Should the designer respect locked widgets?  If true, the designer by default
will not allow you to select locked widgets in the designer view.

### CreateOnCompile
- **类型**: `EDisplayOnCompile`
- **描述**: Setting to automatically create compile tab based on compile results

### DismissOnCompile
- **类型**: `EDisplayOnCompile`
- **描述**: Setting to automatically dismiss compile tab based on compile results

### GridSnapEnabled
- **类型**: `bool`


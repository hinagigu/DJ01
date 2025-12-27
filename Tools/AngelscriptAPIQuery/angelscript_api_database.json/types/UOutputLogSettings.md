# UOutputLogSettings

**继承自**: `UObject`

Implements the Editor style settings.

## 属性

### LogFontSize
- **类型**: `int`
- **描述**: The font size used in the output log

### LogTimestampMode
- **类型**: `ELogTimes`
- **描述**: The display mode for timestamps in the output log window

### CategoryColorizationMode
- **类型**: `ELogCategoryColorizationMode`
- **描述**: How should categories be colorized in the output log?

### bCycleToOutputLogDrawer
- **类型**: `bool`
- **描述**: If checked pressing the console command shortcut will cycle between focusing the status bar console, opening the output log drawer, and back to the previous focus target.
If unchecked, the console command shortcut will only focus the status bar console

### bEnableOutputLogWordWrap
- **类型**: `bool`


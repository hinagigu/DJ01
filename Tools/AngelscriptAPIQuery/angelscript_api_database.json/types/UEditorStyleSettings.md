# UEditorStyleSettings

**继承自**: `UObject`

Implements the Editor style settings.

## 属性

### bEnableHighDPIAwareness
- **类型**: `bool`
- **描述**: Enables high dpi support in the editor which will adjust the scale of elements in the UI to account for high DPI monitors
The editor must be restarted for changes to take effect.

### ApplicationScale
- **类型**: `float32`
- **描述**: Scales the entire editor interface up or down.

### bEnableUserEditorLayoutManagement
- **类型**: `bool`
- **描述**: Whether to enable the Editor UI Layout configuration tools for the user.
If disabled, the "Save Layout As" and "Remove Layout" menus will be removed, as well as the "Import Layout..." sub-menu.

### ColorVisionDeficiencyPreviewType
- **类型**: `EColorVisionDeficiency`
- **描述**: Applies a color vision deficiency filter to the entire editor

### ColorVisionDeficiencySeverity
- **类型**: `int`

### bColorVisionDeficiencyCorrection
- **类型**: `bool`
- **描述**: Shifts the color spectrum to the visible range based on the current ColorVisionDeficiencyPreviewType

### bColorVisionDeficiencyCorrectionPreviewWithDeficiency
- **类型**: `bool`
- **描述**: If you're correcting the color deficiency, you can use this to visualize what the correction looks like with the deficiency.

### SelectionColor
- **类型**: `FLinearColor`
- **描述**: The color used to represent selection

### AdditionalSelectionColors
- **类型**: `FLinearColor`
- **描述**: Additional colors used for selections with extra meaning

### ViewportToolOverlayColor
- **类型**: `FLinearColor`
- **描述**: The color used for overlay tools inside of the viewport, like the measure tool

### EditorWindowBackgroundColor
- **类型**: `FLinearColor`
- **描述**: The color used to tint the editor window backgrounds

### MenuSearchFieldVisibilityThreshold
- **类型**: `uint`
- **描述**: Menus longer than this threshold show their search field by default. Use 0 to always show, or a high number to always hide. When a searchable menu is open but the field is hidden, you can still start a search by typing.

### RegularColor
- **类型**: `FLinearColor`
- **描述**: The color used to represent regular grid lines

### RuleColor
- **类型**: `FLinearColor`
- **描述**: The color used to represent ruler lines in the grid

### CenterColor
- **类型**: `FLinearColor`
- **描述**: The color used to represent the center lines in the grid

### GridSnapSize
- **类型**: `uint`
- **描述**: The custom grid snap size to use

### GraphBackgroundBrush
- **类型**: `FSlateBrush`
- **描述**: Optional brush used for graph backgrounds

### AssetEditorOpenLocation
- **类型**: `EAssetEditorOpenLocation`
- **描述**: New asset editor tabs will open at the specified location.

### bUseSmallToolBarIcons
- **类型**: `bool`

### bUseGrid
- **类型**: `bool`

### bShowFriendlyNames
- **类型**: `bool`

### bShowNativeComponentNames
- **类型**: `bool`

### bExpandConfigurationMenus
- **类型**: `bool`

### bEnableColorizedEditorTabs
- **类型**: `bool`


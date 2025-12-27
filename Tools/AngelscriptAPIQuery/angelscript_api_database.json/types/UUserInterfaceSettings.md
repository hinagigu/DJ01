# UUserInterfaceSettings

**继承自**: `UDeveloperSettings`

User Interface settings that control Slate and UMG.

## 属性

### RenderFocusRule
- **类型**: `ERenderFocusRule`
- **描述**: Rule to determine if we should render the Focus Brush for widgets that have user focus.

### HardwareCursors
- **类型**: `TMap<EMouseCursor,FHardwareCursorReference>`

### SoftwareCursors
- **类型**: `TMap<EMouseCursor,FSoftClassPath>`

### ApplicationScale
- **类型**: `float32`
- **描述**: An optional application scale to apply on top of the custom scaling rules.  So if you want to expose a
property in your game title, you can modify this underlying value to scale the entire UI.

### UIScaleRule
- **类型**: `EUIScalingRule`
- **描述**: The rule used when trying to decide what scale to apply.

### CustomScalingRuleClass
- **类型**: `FSoftClassPath`
- **描述**: Set DPI Scale Rule to Custom, and this class will be used instead of any of the built-in rules.

### UIScaleCurve
- **类型**: `FRuntimeFloatCurve`
- **描述**: Controls how the UI is scaled at different resolutions based on the DPI Scale Rule

### bAllowHighDPIInGameMode
- **类型**: `bool`
- **描述**: If true, game window on desktop platforms will be created with high-DPI awareness enabled.
Recommended to be enabled only if the game's UI allows users to modify 3D resolution scaling.

### DesignScreenSize
- **类型**: `FIntPoint`
- **描述**: Used only with ScaleToFit scaling rule. Defines native resolution for which were source UI textures created. DPI scaling will be 1.0 at this screen resolution.

### bLoadWidgetsOnDedicatedServer
- **类型**: `bool`
- **描述**: If false, widget references will be stripped during cook for server builds and not loaded at runtime.

### bAuthorizeAutomaticWidgetVariableCreation
- **类型**: `bool`
- **描述**: Setting to authorize or not automatic variable creation.
If true, variables will be created automatically, if the type created allows it. Drawback: it's easier to have a bad data architecture because various blueprint graph will have access to many variables.
If false, variables are never created automatically, and you have to create them manually on a case by case basis.

### CustomFontDPI
- **类型**: `uint`
- **描述**: Controls the relationship between UMG font size and pixel height.

### FontDPIPreset
- **类型**: `EFontDPI`
- **描述**: Controls the relationship between UMG font size and pixel height.

### bUseCustomFontDPI
- **类型**: `bool`
- **描述**: To set your own custom value, check this box, then enter the value in the text box.


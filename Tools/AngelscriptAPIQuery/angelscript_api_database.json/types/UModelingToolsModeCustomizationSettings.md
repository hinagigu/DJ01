# UModelingToolsModeCustomizationSettings

**继承自**: `UDeveloperSettings`

## 属性

### bUseLegacyModelingPalette
- **类型**: `bool`
- **描述**: Toggle between the Legacy Modeling Mode Palette and the new UI (requires exiting and re-entering the Mode)

### ToolSectionOrder
- **类型**: `TArray<FString>`
- **描述**: Add the names of Modeling Mode Tool Palette Sections to have them appear at the top of the Tool Palette, in the order listed below.

### SectionColors
- **类型**: `TArray<FModelingModeCustomSectionColor>`
- **描述**: Custom Section Header Colors for listed Sections in the Modeling Mode Tool Palette

### ToolColors
- **类型**: `TArray<FModelingModeCustomToolColor>`
- **描述**: Custom Tool Colors for listed Tools in the Modeling Mode Tool Palette.

Format:
SectionName        (Specifies a default color for all tools in the section.)
SectionName.ToolName        (Specifies an override color for a specific tool in the given section.)

### BrushAlphaSets
- **类型**: `TArray<FModelingModeAssetCollectionSet>`
- **描述**: A Brush Alpha Set is a named list of Content Browser Collections, which will be shown as a separate tab in
the Texture Asset Picker used in various Modeling Mode Tools when selecting a Brush Alpha (eg in Sculpting)

### bShowCategoryButtonLabels
- **类型**: `bool`
- **描述**: If true, the category labels will be shown on the toolbar buttons, else they will be hidden

### bAlwaysShowToolButtons
- **类型**: `bool`
- **描述**: If true, Tool buttons will always be shown when in a Tool. By default they will be hidden.


# UFractureModeCustomizationSettings

**继承自**: `UDeveloperSettings`

## 属性

### ToolSectionOrder
- **类型**: `TArray<FString>`
- **描述**: Add the names of Fracture Mode Tool Palette Sections to have them appear at the top of the Tool Palette, in the order listed below.

### ToolFavorites
- **类型**: `TArray<FString>`
- **描述**: Tool Names listed in the array below will appear in a Favorites section at the top of the Fracture Mode Tool Palette

### SectionColors
- **类型**: `TArray<FFractureModeCustomSectionColor>`
- **描述**: Custom Section Header Colors for listed Sections in the Fracture Mode Tool Palette

### ToolColors
- **类型**: `TArray<FFractureModeCustomToolColor>`
- **描述**: Custom Tool Colors for listed Tools in the Fracture Mode Tool Palette.

Format:
SectionName        (Specifies a default color for all tools in the section.)
SectionName.ToolName        (Specifies an override color for a specific tool in the given section.)

